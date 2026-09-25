
import { spawn } from 'node:child_process';
import fs from 'node:fs';

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const port = 9557;
const chrome = spawn(chromePath, [
  '--headless=new',
  '--remote-debugging-port=' + port,
  '--hide-scrollbars',
  '--disable-gpu',
  '--window-size=1920,1080',
  'about:blank'
]);

await new Promise(r => setTimeout(r, 2000));
const res = await fetch('http://127.0.0.1:' + port + '/json/list');
const targets = await res.json();
const target = targets.find(t => t.type === 'page');
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise(r => { ws.onopen = r; });

let id = 0;
function send(method, params = {}) {
  return new Promise((resolve, reject) => {
    const msgId = ++id;
    const h = (msg) => {
      const d = JSON.parse(msg.data);
      if (d.id === msgId) {
        ws.removeEventListener('message', h);
        if (d.error) reject(d.error); else resolve(d.result);
      }
    };
    ws.addEventListener('message', h);
    ws.send(JSON.stringify({ id: msgId, method, params }));
  });
}

await send('Page.enable');
await send('Emulation.setDeviceMetricsOverride', {
  width: 1920,
  height: 1080,
  deviceScaleFactor: 1,
  mobile: false
});

await send('Page.navigate', { url: 'http://localhost:5173/signin' });
await new Promise(r => setTimeout(r, 3500));

const shot = await send('Page.captureScreenshot', { format: 'png' });
fs.writeFileSync('d:/Java Enterprise Stackly Project/SignIn-UI-Frontend/qa-verify/signin_1920x1080_now.png', Buffer.from(shot.data, 'base64'));
console.log('Saved 1920x1080 screenshot');

ws.close();
chrome.kill();
