import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const port = 9556;
const outputDir = 'd:\\Java Enterprise Stackly Project\\SignIn-UI-Frontend\\qa-verify';

if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

console.log('Spawning headless Chrome for visual QA...');
const chrome = spawn(chromePath, [
  '--headless=new',
  `--remote-debugging-port=${port}`,
  '--hide-scrollbars',
  '--disable-gpu',
  '--window-size=1440,900',
  'about:blank'
]);

const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
await wait(2000);

try {
  const res = await fetch(`http://127.0.0.1:${port}/json/list`);
  const targets = await res.json();
  const target = targets.find((t) => t.type === 'page');
  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((resolve) => { ws.onopen = resolve; });

  let nextId = 0;
  function send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = ++nextId;
      const handler = (msg) => {
        const data = JSON.parse(msg.data);
        if (data.id === id) {
          ws.removeEventListener('message', handler);
          if (data.error) reject(data.error);
          else resolve(data.result);
        }
      };
      ws.addEventListener('message', handler);
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  await send('Page.enable');

  async function capturePage(url, filename, scrollY = 0) {
    console.log(`Navigating to ${url}...`);
    await send('Emulation.setDeviceMetricsOverride', {
      width: 1440,
      height: 900,
      deviceScaleFactor: 1,
      mobile: false
    });
    await send('Page.navigate', { url });
    await wait(4500);

    if (scrollY > 0) {
      const scrollSel = await send('Runtime.evaluate', {
        expression: `
          const rightPanel = document.querySelector('.overflow-y-auto');
          if (rightPanel) { rightPanel.scrollTop = ${scrollY}; 'scrolled-panel'; }
          else { window.scrollTo(0, ${scrollY}); 'scrolled-window'; }
        `,
        returnByValue: true
      });
      console.log('Scroll result:', scrollSel.result.value);
      await wait(400);
    }

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    const filePath = path.join(outputDir, filename);
    fs.writeFileSync(filePath, Buffer.from(shot.data, 'base64'));
    console.log(`✓ Saved: ${filePath}`);
  }

  // Screen 1: Sign In
  await capturePage('http://localhost:5173/signin', 'screen1_signin.png');

  // Screen 2: Organization top portion
  await capturePage('http://localhost:5173/organization', 'screen2_org_top.png');

  // Screen 3: Organization lower portion (scrolled)
  await capturePage('http://localhost:5173/organization', 'screen3_org_lower.png', 700);

  // Screen 4: Admin account
  await capturePage('http://localhost:5173/admin', 'screen4_admin.png');

  console.log('\nAll 4 screenshots captured successfully.');
  ws.close();
} catch (err) {
  console.error('Error during visual QA:', err);
} finally {
  chrome.kill();
}
