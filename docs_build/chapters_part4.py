# -*- coding: utf-8 -*-
"""
Part 4 of the Guide:
- Chapter 24: Button-by-Button Interactive Reference
- Chapter 25: Conditional Rendering Strategies
- Chapter 26: Responsive Breakpoint Behavior
- Chapter 27: Error Handling, Validation & Lockout Logic
- Chapter 28: Backend Integration Status & Mock Architecture
- Chapter 29: Authentication & Security Simulation
- Chapter 30: React Concepts Master Checklist
- Chapter 31: TypeScript Concepts Master Checklist
- Chapter 32: Line-by-Line Code Walkthroughs
- Chapter 33: POC & Interview Speaking Script with Q&A
- Chapter 34: "How I Built This" Development Narrative
- Chapter 35: Architecture Rationale: "Why This Way?"
- Chapter 36: Technical Improvement Opportunities
- Chapter 37: Complete System Architecture Diagrams
- Chapter 38: Technical Project Glossary
- Chapter 39: Final Project Cheat Sheet
- Chapter 40: Self-Assessment & Mastery Checklist
"""

def get_part4_html():
    return """
<!-- ========================================== -->
<!-- CHAPTER 24: BUTTON-BY-BUTTON REFERENCE     -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">24</span> Button-by-Button Interactive Reference</h1>

  <table>
    <thead>
      <tr>
        <th>Button Label</th>
        <th>Screen / Location</th>
        <th>Visual Appearance</th>
        <th>Fired Event & Function</th>
        <th>State Changes & Navigation Outcome</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Continue</strong></td>
        <td><code>SignInPage.tsx</code></td>
        <td>Navy pill (<code>h-[44px] bg-[#0f1330]</code>)</td>
        <td><code>handleSubmit(e)</code></td>
        <td>Validates inputs. Saves workspace slug to Context. Navigates to <code>/organization</code>.</td>
      </tr>
      <tr>
        <td><strong>Google / Microsoft / SSO</strong></td>
        <td><code>SignInPage.tsx</code></td>
        <td>White bordered with provider SVG icon</td>
        <td><code>onClick={() =&gt; navigate('/organization')}</code></td>
        <td>Simulates external OAuth/SSO login and routes user into workspace configuration.</td>
      </tr>
      <tr>
        <td><strong>Find it here</strong></td>
        <td><code>SignInPage.tsx</code></td>
        <td>Inline blue link (<code>text-[#232a5c]</code>)</td>
        <td><code>onClick={() =&gt; setShowFindModal(!showFindModal)}</code></td>
        <td>Toggles <code>showFindModal</code> to render inline dismissible workspace helper card.</td>
      </tr>
      <tr>
        <td><strong>Continue</strong></td>
        <td><code>OrganizationForm.tsx</code></td>
        <td>Large navy button (<code>h-[48px] bg-[#0f1330]</code>)</td>
        <td><code>handleSubmit(e)</code></td>
        <td>Validates all 4 required fields. Commits company profile to Context. Navigates to <code>/admin</code>.</td>
      </tr>
      <tr>
        <td><strong>‹ Back</strong></td>
        <td><code>AdminAccountPage.tsx</code></td>
        <td>Muted gray text with chevron</td>
        <td><code>onClick={() =&gt; navigate('/organization')}</code></td>
        <td>Navigates backward to Step 1 without losing already entered data.</td>
      </tr>
      <tr>
        <td><strong>Password Eye Icon</strong></td>
        <td><code>AdminAccountPage.tsx</code></td>
        <td>MUI Visibility SVG icon</td>
        <td><code>onClick={() =&gt; setShowPassword(!showPassword)}</code></td>
        <td>Flips <code>showPassword</code> boolean, toggling input between masked <code>password</code> and clear <code>text</code>.</td>
      </tr>
      <tr>
        <td><strong>Continue</strong></td>
        <td><code>AdminAccountPage.tsx</code></td>
        <td>Large navy button (<code>h-[48px] bg-[#0f1330]</code>)</td>
        <td><code>handleSubmit(e)</code></td>
        <td>Enforces password complexity. Commits admin profile to Context. Navigates to <code>/review</code>.</td>
      </tr>
      <tr>
        <td><strong>Create account</strong></td>
        <td><code>ReviewConfirm.tsx</code></td>
        <td>Disabled light gray (<code>bg-[#e9edf5]</code>) or Active navy</td>
        <td><code>onClick={handleCreateAccount}</code></td>
        <td>Guarded by <code>canCreateAccount</code>. When all 3 mandatory boxes are checked, navigates to <code>/welcome</code>.</td>
      </tr>
      <tr>
        <td><strong>Go to sign in</strong></td>
        <td><code>Welcome.tsx</code></td>
        <td>Large navy button (<code>h-[48px] bg-[#0f1330]</code>)</td>
        <td><code>onClick={handleSignIn}</code></td>
        <td>Navigates user back to <code>/signin</code> to begin day-one login.</td>
      </tr>
      <tr>
        <td><strong>Resend verification</strong></td>
        <td><code>Welcome.tsx</code></td>
        <td>Blue underlined text link</td>
        <td><code>onClick={handleResend}</code></td>
        <td>Sets <code>resent = true</code>, displaying emerald confirmation notice for 4000ms.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ========================================== -->
<!-- CHAPTER 25: CONDITIONAL RENDERING          -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">25</span> Conditional Rendering Strategies</h1>

  <h2>25.1 Real Conditional Patterns in the Codebase</h2>
  <ul>
    <li><strong>Short-Circuit Evaluation (<code>&amp;&amp;</code>):</strong>
      <pre><code><span class="cmt">// In ReviewConfirm.tsx: renders OPTIONAL tag only if optional is true</span>
{optional &amp;&amp; (
  &lt;<span class="typ">span</span> <span class="prop">className</span>=<span class="str">"text-[10px] font-mono font-medium text-[#9aa3b2] tracking-[0.1em] uppercase ml-1.5"</span>&gt;
    OPTIONAL
  &lt;/<span class="typ">span</span>&gt;
)}</code></pre>
    </li>
    <li><strong>Ternary Operator (<code>? :</code>):</strong>
      <pre><code><span class="cmt">// In FormField.tsx: dynamically renders HTML &lt;select&gt; vs &lt;input&gt;</span>
{isSelect ? (
  &lt;<span class="typ">select</span> ...&gt;...&lt;/<span class="typ">select</span>&gt;
) : (
  &lt;<span class="typ">input</span> ... /&gt;
)}</code></pre>
    </li>
    <li><strong>File Preview vs Dropzone Placeholder:</strong>
      <pre><code><span class="cmt">// In FileUpload.tsx: renders thumbnail if file exists, else shows Upload icon</span>
{localPreview || value ? (
  &lt;<span class="typ">div</span> <span class="prop">className</span>=<span class="str">"flex items-center gap-3"</span>&gt;
    &lt;<span class="typ">img</span> <span class="prop">src</span>={localPreview || <span class="str">''</span>} <span class="prop">alt</span>=<span class="str">"Logo preview"</span> /&gt;
  &lt;/<span class="typ">div</span>&gt;
) : (
  &lt;&gt;&lt;<span class="typ">Upload</span> <span class="prop">size</span>={18} /&gt;&lt;<span class="typ">span</span>&gt;Upload logo or drag and drop&lt;/<span class="typ">span</span>&gt;&lt;/&gt;
)}</code></pre>
    </li>
    <li><strong>Conditional Action Disabling:</strong>
      <pre><code><span class="cmt">// In ReviewConfirm.tsx:</span>
&lt;<span class="typ">button</span>
  <span class="prop">disabled</span>={!canCreateAccount}
  <span class="prop">className</span>={canCreateAccount ? <span class="str">'bg-[#0f1330] text-white'</span> : <span class="str">'bg-[#e9edf5] text-[#98a2b3]'</span>}
&gt;
  Create account
&lt;/<span class="typ">button</span>&gt;</code></pre>
    </li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 26: RESPONSIVE DESIGN              -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">26</span> Responsive Breakpoint Behavior</h1>

  <h2>26.1 Viewport Breakpoints in the Codebase</h2>
  <p>
    The application leverages Tailwind's mobile-first breakpoint system:
  </p>

  <table>
    <thead>
      <tr>
        <th>Device Class</th>
        <th>Breakpoint</th>
        <th>Left Branding Panel Behavior</th>
        <th>Right Form Panel Behavior</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Mobile Phones</strong></td>
        <td><code>&lt; 640px</code></td>
        <td>Completely hidden (<code>hidden</code>). Saves bandwidth and vertical screen space.</td>
        <td>Full-width (<code>w-full</code>). Inputs, buttons, and headers stack into a single column. Padding: <code>px-4 pt-8</code>.</td>
      </tr>
      <tr>
        <td><strong>Tablets</strong></td>
        <td><code>640px - 1023px</code> (<code>sm:</code>)</td>
        <td>Hidden. Focus remains 100% on fast, frictionless onboarding.</td>
        <td>Comfortable padded container (<code>px-6 sm:pt-[60px]</code>). 2-column fields (First/Last name, Country/State, City/Timezone) render side-by-side.</td>
      </tr>
      <tr>
        <td><strong>Desktop / Laptops</strong></td>
        <td><code>&gt;= 1024px</code> (<code>lg:</code>)</td>
        <td>Visible at 50% width (<code>lg:w-1/2</code>). Fixed height (<code>h-full overflow-hidden</code>). Interactive orbital system active.</td>
        <td>Visible at 50% width (<code>lg:w-1/2</code>). Independent scrolling via <code>overflow-y-auto .no-scrollbar</code>. Top padding aligned at <code>lg:pt-[104px]</code>.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ========================================== -->
<!-- CHAPTER 27: ERROR HANDLING & LOCKOUT       -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">27</span> Error Handling, Guardrails & Lockout Logic</h1>

  <h2>27.1 Form Error Handling Pipeline</h2>
  <p>
    When invalid data is detected, the error propagates from the validation function down to the UI:
  </p>
  <div class="diagram-box">
User types "invalid-email" in Work email
   │
   ▼ onBlur event fires
validateEmail("invalid-email") returns "Please enter a valid email address"
   │
   ▼ errors state updated: setErrors({ email: "Please enter a valid email address" })
FormField receives error prop
   │
   ├── Input border turns red: border-red-400 focus:border-red-500
   ├── Accessible aria-invalid={true} and aria-describedby="work-email-error" applied
   └── Error paragraph renders: <p id="work-email-error" role="alert" className="text-red-500">
  </div>

  <h2>27.2 The 5-Attempt Security Lockout Algorithm</h2>
  <p>
    In <code>src/pages/EnterPassword.tsx</code>, enterprise security policy is simulated:
  </p>
  <pre><code><span class="kw">const</span> MAX_ATTEMPTS = 5;
<span class="kw">const</span> DEMO_PASSWORD = <span class="str">'password123'</span>;

<span class="kw">const</span> <span class="fn">handleSignIn</span> = () =&gt; {
  <span class="kw">const</span> trimmed = password.trim();
  <span class="kw">if</span> (trimmed === DEMO_PASSWORD) {
    navigate(<span class="str">'/2fa'</span>);
    <span class="kw">return</span>;
  }
  <span class="kw">const</span> next = attempts + 1;
  setAttempts(next);
  <span class="kw">if</span> (next &gt;= MAX_ATTEMPTS) {
    navigate(<span class="str">'/locked'</span>); <span class="cmt">// &lt;-- Automatically redirects to /locked!</span>
    <span class="kw">return</span>;
  }
  setError(<span class="str">`Incorrect password. You have ${MAX_ATTEMPTS - next} attempts remaining.`</span>);
};</code></pre>
</div>

<!-- ========================================== -->
<!-- CHAPTER 28: BACKEND INTEGRATION STATUS     -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">28</span> Backend Integration Status & Mock Architecture</h1>

  <h2>28.1 Explicit Engineering Reality Check</h2>
  <div class="callout callout-warning">
    <div class="callout-title">Current Implementation Status</div>
    <strong>This project currently uses frontend-only mock and state simulation.</strong> There is currently no active Axios/fetch HTTP client, REST API endpoint, GraphQL server, or backend database actively wired to these forms.
  </div>
  <p>
    Every data transition (such as passing organization name from Step 1 to Step 2, and generating the workspace subdomain on Step 5) is managed in-memory by React's <code>OnboardingContext</code>.
  </p>

  <h2>28.2 How to Wire Up the Real Backend in the Future</h2>
  <p>
    When the backend team delivers the Java Enterprise Spring Boot microservices, the integration points are clearly isolated:
  </p>
  <ol style="margin-left: 20px;">
    <li><strong>Step 1 (Check Workspace Availability):</strong> Call <code>GET /api/v1/workspaces/verify?slug={orgCode}</code> inside <code>OrganizationForm.tsx</code> before proceeding.</li>
    <li><strong>Step 2 (Upload Logo to S3/Cloud Storage):</strong> In <code>FileUpload.tsx</code>, dispatch a <code>POST /api/v1/assets/upload</code> with <code>FormData</code>.</li>
    <li><strong>Step 3 (Create Tenant Transaction):</strong> In <code>ReviewConfirm.tsx</code>, replace <code>navigate('/welcome')</code> with:
      <pre><code><span class="kw">const</span> response = <span class="kw">await</span> fetch(<span class="str">'/api/v1/onboarding/provision'</span>, {
  method: <span class="str">'POST'</span>,
  headers: { <span class="str">'Content-Type'</span>: <span class="str">'application/json'</span> },
  body: JSON.stringify({ organization, admin })
});
<span class="kw">if</span> (response.ok) navigate(<span class="str">'/welcome'</span>);</code></pre>
    </li>
  </ol>
</div>

<!-- ========================================== -->
<!-- CHAPTER 29: AUTH & SECURITY SIMULATION     -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">29</span> Authentication & Security Simulation</h1>

  <h2>29.1 Simulated Security Capabilities</h2>
  <ul>
    <li><strong>Workspace-First Tenant Isolation:</strong> Enforces multi-tenant SaaS architecture where user identities are scoped under tenant workspaces (e.g. <code>acmecorp.oneenterprise.io</code>).</li>
    <li><strong>Super Admin Role Assignment:</strong> Displays the blue notice badge highlighting that the root account receives the privileged <code>SUPER_ADMIN</code> role.</li>
    <li><strong>Enterprise Password Complexity Policy:</strong> Validates length (8+), numbers (0-9), and symbols (!@#$%) before allowing admin creation.</li>
    <li><strong>Two-Factor Authentication (2FA) Simulation:</strong> A 6-box OTP entry component with auto-focus advancing and 5-minute countdown simulation.</li>
    <li><strong>Brute-Force Lockout Defense:</strong> Locks account for 15 minutes after 5 consecutive bad password attempts and redirects to <code>/locked</code>.</li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 30 & 31: REACT & TS CHECKLISTS     -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">30 &amp; 31</span> React &amp; TypeScript Concepts Checklists</h1>

  <h2>30.1 React Concepts Master Checklist</h2>
  <ul class="checklist">
    <li><span class="check-box">&#10003;</span> <strong>JSX Syntax:</strong> Used across all components for declarative HTML-in-JS templating.</li>
    <li><span class="check-box">&#10003;</span> <strong>Functional Components:</strong> 100% of components are modern React functional components with TypeScript typing (<code>React.FC</code>).</li>
    <li><span class="check-box">&#10003;</span> <strong>Props &amp; Prop Drilling Avoidance:</strong> Used for atomic UI controls (<code>FormField</code>, <code>StepProgress</code>), while React Context eliminates prop drilling for onboarding data.</li>
    <li><span class="check-box">&#10003;</span> <strong>useState Hook:</strong> Controls form inputs, error objects, visibility toggles, and tab switches.</li>
    <li><span class="check-box">&#10003;</span> <strong>useCallback Hook:</strong> Memoizes <code>updateOrganization</code>, <code>updateAdmin</code>, and <code>resetOnboarding</code> inside <code>OnboardingContext.tsx</code> to prevent unnecessary child re-renders.</li>
    <li><span class="check-box">&#10003;</span> <strong>useRef Hook:</strong> Manages DOM focus in <code>TwoFactor.tsx</code> (input refs array), <code>FileUpload.tsx</code> (file input ref), and <code>OrganizationForm.tsx</code> (org-code manual edit ref).</li>
    <li><span class="check-box">&#10003;</span> <strong>useEffect Hook:</strong> Resets vertical window scroll position to <code>scrollTop = 0</code> upon page transitions.</li>
    <li><span class="check-box">&#10003;</span> <strong>useContext &amp; Custom Hook:</strong> <code>useOnboarding()</code> provides centralized access to the onboarding context store.</li>
    <li><span class="check-box">&#10003;</span> <strong>Conditional Rendering:</strong> Implemented via <code>&amp;&amp;</code>, ternaries, and dynamic CSS classes.</li>
    <li><span class="check-box">&#10003;</span> <strong>Client-Side Routing:</strong> Integrated via <code>react-router-dom</code> with nested layout routes and <code>&lt;Outlet /&gt;</code>.</li>
  </ul>

  <h2>31.1 TypeScript Concepts Master Checklist</h2>
  <ul class="checklist">
    <li><span class="check-box">&#10003;</span> <strong>Interfaces:</strong> <code>OrganizationDetails</code>, <code>AdminAccount</code>, <code>OnboardingState</code>, <code>FormFieldProps</code>, <code>StepProgressProps</code>.</li>
    <li><span class="check-box">&#10003;</span> <strong>Type Aliases:</strong> <code>SocialProvider = 'google' | 'microsoft' | 'sso'</code> in <code>SocialLoginButton.tsx</code>.</li>
    <li><span class="check-box">&#10003;</span> <strong>Union Types:</strong> Tab state in <code>VisualBrandingPanel</code>: <code>activeTab: 'secure' | 'scalable' | 'future'</code>.</li>
    <li><span class="check-box">&#10003;</span> <strong>Utility Types (<code>Partial&lt;T&gt;</code>):</strong> Used in context updater methods for partial field mutations.</li>
    <li><span class="check-box">&#10003;</span> <strong>HTML Element Prop Inheritance:</strong> <code>FormFieldProps extends InputHTMLAttributes&lt;HTMLInputElement | HTMLSelectElement&gt;</code>.</li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 32: CODE WALKTHROUGHS              -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">32</span> Important Line-by-Line Code Walkthroughs</h1>

  <h2>32.1 Code Walkthrough 1: Application Bootstrap (<code>src/main.tsx</code>)</h2>
  <pre><code>1: <span class="kw">import</span> { StrictMode } <span class="kw">from</span> <span class="str">'react'</span>
2: <span class="kw">import</span> { createRoot } <span class="kw">from</span> <span class="str">'react-dom/client'</span>
3: <span class="kw">import</span> <span class="str">'./index.css'</span>
4: <span class="kw">import</span> App <span class="kw">from</span> <span class="str">'./App.tsx'</span>
5: 
6: createRoot(document.getElementById(<span class="str">'root'</span>)!).render(
7:   &lt;<span class="typ">StrictMode</span>&gt;
8:     &lt;<span class="typ">App</span> /&gt;
9:   &lt;/<span class="typ">StrictMode</span>&gt;,
10: )</code></pre>
  <ul>
    <li><strong>Line 2:</strong> Imports <code>createRoot</code>, the modern React 19 concurrent renderer entry point.</li>
    <li><strong>Line 3:</strong> Imports <code>./index.css</code>, injecting Tailwind v4 and Google Fonts globally before components render.</li>
    <li><strong>Line 6:</strong> <code>document.getElementById('root')!</code> locates the HTML root div. The TypeScript non-null assertion operator (<code>!</code>) asserts that the element definitely exists in the DOM.</li>
    <li><strong>Lines 7-9:</strong> Wraps <code>&lt;App /&gt;</code> in <code>&lt;StrictMode&gt;</code> to activate dev-mode double-rendering checks.</li>
  </ul>

  <h2>32.2 Code Walkthrough 2: Custom Hook Guard (<code>src/context/useOnboarding.ts</code>)</h2>
  <pre><code>1: <span class="kw">import</span> { useContext } <span class="kw">from</span> <span class="str">'react'</span>;
2: <span class="kw">import</span> { OnboardingContext } <span class="kw">from</span> <span class="str">'./OnboardingContextValue'</span>;
3: <span class="kw">import type</span> { OnboardingContextType } <span class="kw">from</span> <span class="str">'./OnboardingContextValue'</span>;
4: 
5: <span class="kw">export const</span> <span class="fn">useOnboarding</span> = (): <span class="typ">OnboardingContextType</span> =&gt; {
6:   <span class="kw">const</span> context = useContext(OnboardingContext);
7:   <span class="kw">if</span> (!context) {
8:     <span class="kw">throw new</span> Error(<span class="str">'useOnboarding must be used within an OnboardingProvider'</span>);
9:   }
10:   <span class="kw">return</span> context;
11: };</code></pre>
  <ul>
    <li><strong>Lines 5-6:</strong> Consumes <code>OnboardingContext</code> via native <code>useContext</code>.</li>
    <li><strong>Lines 7-9:</strong> Fail-Fast Defensive Guard. If a developer accidentally renders a component using <code>useOnboarding()</code> outside the <code>&lt;OnboardingProvider&gt;</code> tree, React immediately throws a clear, actionable runtime error rather than silently failing with <code>TypeError: Cannot read properties of undefined</code>!</li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 33: POC SPEAKING SCRIPT & Q&A      -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">33</span> How to Explain This Project in a POC or Interview</h1>

  <h2>33.1 Senior Developer Speaking Script</h2>
  <div class="callout callout-interview">
    <div class="callout-title">Deliver this explanation with confidence</div>
    "Good morning / afternoon everyone. I'm excited to walk you through <strong>SignIn-UI-Frontend</strong>, our modern enterprise authentication and workspace onboarding platform for One Enterprise.<br><br>
    Our primary business goal was to solve a major friction point in B2B SaaS: enterprise onboarding abandonment. Rather than overwhelming administrators with a single massive 25-field form, we engineered a modular 3-step progressive onboarding pipeline.<br><br>
    On screens 1024px and wider, we implement a <strong>50/50 Split Screen Architecture</strong> using our <code>AuthLayout</code>. The left side is a persistent, non-scrolling branding panel that highlights our enterprise trust certifications—SOC 2 Type II, ISO 27001, and our 99.95% uptime SLA—along with an interactive visual orbital diagram illustrating how <em>People</em>, <em>Process</em>, and <em>Progress</em> interconnect through One Enterprise.<br><br>
    The right side hosts our scrollable form views powered by React Router v7. In Step 1, the user enters their organization details. Our code auto-generates a clean workspace slug in real time and dynamically populates regional states based on country selection. When they click Continue, this data is preserved in our centralized React Context store. Step 2 collects root Super Administrator credentials with enforced password complexity. Step 3 acts as our legal compliance gateway, strictly requiring confirmation of authority and Data Processing Agreements before the tenant is provisioned.<br><br>
    Technologically, we built this on React 19, TypeScript, Vite, Tailwind CSS v4, and Material UI v9. Everything is fully typed, accessible, and responsive. I'd be glad to dive into any specific component or architectural layer!"
  </div>

  <h2>33.2 Likely Interview / POC Questions &amp; Model Answers</h2>
  <div class="card" style="margin-bottom: 12px;">
    <div class="card-header">Q1: Why did you use React Context instead of Redux or Zustand?</div>
    <div class="card-body">
      <strong>Answer:</strong> "For this specific multi-step onboarding wizard, Redux would have introduced unnecessary boilerplate and bundle weight. Our onboarding workflow has a single, cohesive state domain: <code>organization</code> and <code>admin</code> data. React's native Context API combined with <code>useCallback</code> memoization gave us 100% of the cross-step state persistence we needed with zero external dependencies and minimal bundle footprint."
    </div>
  </div>

  <div class="card" style="margin-bottom: 12px;">
    <div class="card-header">Q2: How does the application prevent losing data when a user clicks 'Back'?</div>
    <div class="card-body">
      <strong>Answer:</strong> "When a user fills Step 1 and clicks Continue, the handler dispatches <code>updateOrganization(...)</code> to our <code>OnboardingContext</code>. When the user is on Step 2 (Admin Account) and clicks '‹ Back', the router navigates back to <code>/organization</code>. When <code>OrganizationForm</code> mounts, its local <code>useState</code> hooks are initialized directly from <code>organization.*</code> in Context. As a result, all previously selected inputs, dropdowns, and uploaded files are seamlessly restored."
    </div>
  </div>

  <div class="card" style="margin-bottom: 12px;">
    <div class="card-header">Q3: How does the 50/50 split layout behave on mobile devices?</div>
    <div class="card-body">
      <strong>Answer:</strong> "In <code>AuthLayout.tsx</code>, the left branding container is styled with <code>hidden lg:block lg:w-1/2</code>. On viewports below 1024px (tablets and phones), the left branding panel is completely removed from layout calculation. The right form container automatically expands to <code>w-full</code>, delivering a clean, single-column mobile experience with touch-friendly input targets."
    </div>
  </div>
</div>

<!-- ========================================== -->
<!-- CHAPTER 34 & 35: HOW I BUILT THIS & WHY    -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">34 &amp; 35</span> "How I Built This" &amp; Architecture Decisions</h1>

  <h2>34.1 The 13-Step Development Story</h2>
  <ol style="margin-left: 20px; line-height: 1.8;">
    <li><strong>Step 1 (Scaffolding):</strong> Initialized Vite with React 19 and TypeScript template.</li>
    <li><strong>Step 2 (Tooling):</strong> Installed Tailwind CSS v4 via <code>@tailwindcss/vite</code>, Material UI v9, and Lucide icons.</li>
    <li><strong>Step 3 (Global Styles):</strong> Configured <code>index.css</code> with Google Fonts (Inter, JetBrains Mono) and custom <code>@theme</code> color tokens.</li>
    <li><strong>Step 4 (Type Contracts):</strong> Authored <code>src/types/onboarding.ts</code> to define strict TypeScript interfaces for all organization and admin data models.</li>
    <li><strong>Step 5 (Validation Engine):</strong> Built <code>src/utils/validation.ts</code> with unit-level validation functions and auto-slug generation.</li>
    <li><strong>Step 6 (Context Store):</strong> Implemented <code>OnboardingContext.tsx</code> with <code>useCallback</code> memoized updaters and the <code>useOnboarding</code> custom hook.</li>
    <li><strong>Step 7 (Atomic UI Controls):</strong> Built reusable primitives: <code>FormField</code>, <code>FileUpload</code>, <code>PrimaryButton</code>, <code>StepProgress</code>, and <code>AgreementCheckbox</code>.</li>
    <li><strong>Step 8 (Visual Branding Stage):</strong> Engineered <code>VisualBrandingPanel.tsx</code> featuring full mountain image background, SVG orbital system, glassmorphic 1E card, and interactive tabs.</li>
    <li><strong>Step 9 (AuthLayout Master):</strong> Created <code>AuthLayout.tsx</code> establishing the 50/50 split desktop layout with <code>&lt;Outlet /&gt;</code>.</li>
    <li><strong>Step 10 (Onboarding Flow Pages):</strong> Assembled <code>OrganizationForm.tsx</code>, <code>AdminAccountPage.tsx</code>, <code>ReviewConfirm.tsx</code>, and <code>Welcome.tsx</code>.</li>
    <li><strong>Step 11 (Secondary Auth Suite):</strong> Integrated login views: <code>EnterPassword.tsx</code> (with 5-attempt lockout counter), <code>TwoFactor.tsx</code> (with 6-box auto-advancing OTP), <code>ForgotPassword.tsx</code>, and <code>AccountLocked.tsx</code>.</li>
    <li><strong>Step 12 (Routing Matrix):</strong> Configured <code>src/App.tsx</code> with React Router v7 routes, redirects, and fallbacks.</li>
    <li><strong>Step 13 (Refinement &amp; Linting):</strong> Executed <code>oxlint</code> and TypeScript compilation checks (<code>tsc -b</code>) to ensure zero errors and clean bundle output.</li>
  </ol>

  <h2>35.1 Engineering Decisions: "Why Was It Written This Way?"</h2>
  <ul>
    <li><strong>Why Tailwind v4 instead of CSS Modules?</strong> Tailwind v4 provides rapid utility styling with zero CSS runtime overhead and built-in CSS variable theming.</li>
    <li><strong>Why Controlled Inputs instead of Uncontrolled refs?</strong> Controlled components enable real-time field validation, dynamic slug auto-generation on keystroke, and conditional button enabling.</li>
    <li><strong>Why Native SVG instead of Canvas for Orbital Diagram?</strong> SVG vectors scale infinitely across Retina and 4K displays without blurring, support CSS animations, and have zero impact on JavaScript main thread execution.</li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 36: TECHNICAL IMPROVEMENTS        -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">36</span> Technical Improvement Roadmap</h1>

  <p>
    In technical discussions, demonstrating awareness of future architectural enhancements proves seniority. Here is the clear division between current implementation and future roadmap:
  </p>

  <table>
    <thead>
      <tr>
        <th>Domain</th>
        <th>Current Implementation</th>
        <th>Possible Future Enhancement</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Data Persistence</strong></td>
        <td>In-memory React Context (data resets on hard browser page refresh).</td>
        <td>Persist draft onboarding state to <code>sessionStorage</code> or <code>localStorage</code> so users can refresh without losing progress.</td>
      </tr>
      <tr>
        <td><strong>Schema Validation</strong></td>
        <td>Custom imperative functions in <code>validation.ts</code>.</td>
        <td>Migrate to a declarative schema validation library like <strong>Zod</strong> or <strong>Yup</strong> integrated with React Hook Form.</td>
      </tr>
      <tr>
        <td><strong>Backend API</strong></td>
        <td>Frontend mock state simulation.</td>
        <td>Implement an Axios or TanStack Query (React Query) layer with retry logic, loading spinners, and error boundary wrappers.</td>
      </tr>
      <tr>
        <td><strong>Automated Testing</strong></td>
        <td>TypeScript static type analysis and oxlint linting.</td>
        <td>Add Vitest and React Testing Library test suites covering form validation and routing transitions.</td>
      </tr>
      <tr>
        <td><strong>Internationalization</strong></td>
        <td>Hardcoded English labels and messages.</td>
        <td>Extract UI strings into an <code>i18next</code> translation dictionary for multi-language global enterprise support.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ========================================== -->
<!-- CHAPTER 37: ARCHITECTURE DIAGRAMS          -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">37</span> Complete System Architecture Diagrams</h1>

  <h2>37.1 Multi-Step Onboarding State &amp; Navigation Sequence</h2>
  <div class="diagram-box">
[ User Action ]            [ Page Route ]               [ Context State Update ]
      │                           │                                │
      │ Lands on URL              ▼                                │
      ├──────────────────► /signin (SignInPage)                    │
      │ User enters email         │                                │
      │ Clicks "Continue"         ├───────────────────────────────► updateOrganization({ organizationCode })
      │                           ▼                                │
      ├──────────────────► /organization (OrganizationDetailsPage) │
      │ Enters Org Name/Type      │                                │
      │ Auto-generates slug       │                                │
      │ Uploads Logo              │                                │
      │ Clicks "Continue"         ├───────────────────────────────► updateOrganization({ fullOrgDetails })
      │                           ▼                                │
      ├──────────────────► /admin (AdminAccountPage)               │
      │ Enters Admin credentials  │                                │
      │ Validates password rule   │                                │
      │ Clicks "Continue"         ├───────────────────────────────► updateAdmin({ fullAdminDetails })
      │                           ▼                                │
      ├──────────────────► /review (ReviewConfirm)                 │
      │ Checks 3 mandatory DPAs   │                                │
      │ Clicks "Create account"   ├───────────────────────────────► Tenant Provisioned!
      │                           ▼                                │
      └──────────────────► /welcome (Welcome)                      │
                           Displays subdomain & verify email       ▼
  </div>
</div>

<!-- ========================================== -->
<!-- CHAPTER 38: TECHNICAL GLOSSARY             -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">38</span> Technical Project Glossary</h1>

  <table>
    <thead>
      <tr>
        <th>Term</th>
        <th>Simple Definition</th>
        <th>How it Connects to SignIn-UI-Frontend</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Single-Page App (SPA)</strong></td>
        <td>A web app that rewrites the current web page with new data from the web server, instead of the default method of a browser loading entire new pages.</td>
        <td>Our application runs as an SPA using React Router v7. Navigation between <code>/signin</code> and <code>/organization</code> happens instantly in-memory.</td>
      </tr>
      <tr>
        <td><strong>Controlled Component</strong></td>
        <td>An input element whose value is controlled by React state.</td>
        <td>All inputs in <code>OrganizationForm</code> and <code>AdminAccountPage</code> bind their <code>value</code> and <code>onChange</code> to React state.</td>
      </tr>
      <tr>
        <td><strong>React Context</strong></td>
        <td>A React feature for sharing values between components without having to explicitly pass a prop through every level of the tree.</td>
        <td><code>OnboardingContext</code> stores company profile and admin information across all onboarding screens.</td>
      </tr>
      <tr>
        <td><strong>Layout Route</strong></td>
        <td>A parent route in React Router that renders a common layout containing an <code>&lt;Outlet /&gt;</code> for child routes.</td>
        <td><code>AuthLayout.tsx</code> serves as the layout route, rendering the sticky left branding panel once for all routes.</td>
      </tr>
      <tr>
        <td><strong>Tailwind Utility Class</strong></td>
        <td>Single-purpose CSS classes that apply specific styling rules directly in JSX.</td>
        <td>Classes like <code>flex</code>, <code>h-screen</code>, <code>bg-[#0f1330]</code>, and <code>rounded-[28px]</code> compose the entire design.</td>
      </tr>
      <tr>
        <td><strong>Glassmorphism</strong></td>
        <td>A modern UI trend using translucent backgrounds with background blur filters to create a frosted glass look.</td>
        <td>Used in <code>VisualBrandingPanel.tsx</code> for the center 1E card (<code>backdrop-blur-xl bg-white/90</code>).</td>
      </tr>
      <tr>
        <td><strong>Fail-Safe Guard</strong></td>
        <td>Code designed to detect improper usage and fail early with an informative diagnostic error.</td>
        <td><code>useOnboarding.ts</code> checks <code>if (!context) throw new Error(...)</code>.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ========================================== -->
<!-- CHAPTER 39: FINAL PROJECT CHEAT SHEET      -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">39</span> Final Project Cheat Sheet</h1>

  <div class="diagram-box">
========================================================================================
                          SIGNIN-UI-FRONTEND QUICK CHEAT SHEET
========================================================================================
Project Name:         SignIn-UI-Frontend (package: stackly-auth)
Core Technologies:    React 19.2, TypeScript 6.0, Vite 8.3, Tailwind CSS v4, MUI v9
Entry Point:          src/main.tsx (mounts <App /> into #root via createRoot)
Root Router:          src/App.tsx (BrowserRouter, Routes, Route, Navigate)
Layout Container:     src/components/AuthLayout.tsx (50/50 Desktop Split Layout)
Left Branding Panel:  src/components/VisualBrandingPanel.tsx (Mountains, SVG Orbital, 1E Core)
State Management:     src/context/OnboardingContext.tsx (Context API + useOnboarding hook)
Validation Engine:    src/utils/validation.ts (validateRequired, validateEmail, validatePassword)

PRIMARY ONBOARDING ROUTES:
  1. /signin            -> SignInPage.tsx (Workspace & Work email identification)
  2. /organization      -> OrganizationDetailsPage.tsx / OrganizationForm.tsx (Company info)
  3. /admin             -> AdminAccountPage.tsx (Super Admin credentials & password rule)
  4. /review            -> ReviewConfirm.tsx (Mandatory Terms of Service, Authority, DPA)
  5. /welcome           -> Welcome.tsx (Provisioned subdomain & email verification)

SECONDARY AUTHENTICATION ROUTES:
  - /login              -> EnterPassword.tsx (Demo pass: password123, 5-attempt lockout)
  - /2fa                -> TwoFactor.tsx (6-digit auto-advancing OTP verification)
  - /forgot-password    -> ForgotPassword.tsx (Self-service recovery)
  - /check-email        -> CheckEmail.tsx (Reset link dispatch notice)
  - /locked             -> AccountLocked.tsx (15-minute brute-force lockout screen)
  - /success            -> Success.tsx (Post-login dashboard redirect screen)
========================================================================================
  </div>
</div>

<!-- ========================================== -->
<!-- CHAPTER 40: MASTERY CHECKLIST              -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">40</span> Self-Assessment &amp; Mastery Checklist</h1>

  <h2>40.1 Project Knowledge Verification Checklist</h2>
  <ul class="checklist">
    <li><span class="check-box">&#10003;</span> <strong>Architecture:</strong> I can explain the 50/50 split layout in <code>AuthLayout.tsx</code> and why it prevents layout shift.</li>
    <li><span class="check-box">&#10003;</span> <strong>Startup Sequence:</strong> I can trace execution from <code>index.html</code> to <code>main.tsx</code>, <code>createRoot</code>, <code>StrictMode</code>, and <code>App.tsx</code>.</li>
    <li><span class="check-box">&#10003;</span> <strong>Routing:</strong> I can explain how React Router v7 routes work and how parent layout routes wrap child views via <code>&lt;Outlet /&gt;</code>.</li>
    <li><span class="check-box">&#10003;</span> <strong>State Management:</strong> I can explain why React Context was chosen over Redux and how data persists across steps.</li>
    <li><span class="check-box">&#10003;</span> <strong>Form Controls:</strong> I can explain how controlled inputs work with <code>value</code> and <code>onChange</code> handlers.</li>
    <li><span class="check-box">&#10003;</span> <strong>Validation:</strong> I can explain how <code>validation.ts</code> checks emails, workspaces, password complexity, and auto-generates slugs.</li>
    <li><span class="check-box">&#10003;</span> <strong>Styling Stack:</strong> I can explain how Tailwind CSS v4's <code>@theme</code> and utility classes cooperate with Material UI v9 components.</li>
    <li><span class="check-box">&#10003;</span> <strong>Left Branding Panel:</strong> I can describe how the SVG orbital curve paths connect People, Process, and Progress to the 1E center core.</li>
    <li><span class="check-box">&#10003;</span> <strong>Backend Status:</strong> I can clearly state that this project currently utilizes frontend-only mock state simulation and explain how real APIs will be connected.</li>
    <li><span class="check-box">&#10003;</span> <strong>POC Confidence:</strong> I can deliver the Senior Developer speaking script and answer technical interview questions without hesitation!</li>
  </ul>
</div>
"""
