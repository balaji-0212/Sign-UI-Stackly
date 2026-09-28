# -*- coding: utf-8 -*-
"""
Part 1 of the Guide:
- Cover Page
- Table of Contents
- Chapter 1: Executive Overview & The "What & Why" of SignIn-UI-Frontend
- Chapter 2: High-Level Architecture & 50/50 Desktop Split Layout
- Chapter 3: Complete Project File & Folder Structure
- Chapter 4: Application Startup Flow (Browser to DOM)
- Chapter 5: Package.json & Dependency Deep Dive
- Chapter 6: Complete Routing Architecture (React Router v7)
"""

def get_part1_html():
    return """
<!-- ========================================== -->
<!-- COVER PAGE                                 -->
<!-- ========================================== -->
<div class="cover page-break">
  <div class="cover-top">
    <div class="cover-badge">Enterprise UI Architecture Series</div>
    <div class="cover-title">
      SignIn-UI-Frontend<br>
      <span>Complete Project Learning & Architecture Guide</span>
    </div>
    <div class="cover-subtitle">
      A Deep, File-by-File, Flow-by-Flow Engineering Manual for the Stackly Auth & Multi-Step Enterprise Workspace Onboarding Platform
    </div>
  </div>

  <div class="cover-meta">
    <div class="meta-item">
      <div class="meta-label">Project Codebase</div>
      <div class="meta-val">SignIn-UI-Frontend (stackly-auth)</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Core Tech Stack</div>
      <div class="meta-val">React 19.2 + TypeScript + Vite 8.3 + Tailwind v4 + MUI v9</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Architecture Style</div>
      <div class="meta-val">50/50 Split Auth Layout with React Context Multi-Step Pipeline</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Target Audience</div>
      <div class="meta-val">Engineering Leads, POC Reviewers, Frontend Developers</div>
    </div>
  </div>
</div>

<!-- ========================================== -->
<!-- TABLE OF CONTENTS                          -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">TOC</span> Table of Contents</h1>
  <p style="color: #64748b; font-size: 9pt; margin-bottom: 16px;">
    This guide is organized into 40 comprehensive chapters covering every file, prop, state, hook, and architecture decision in the project.
  </p>

  <div class="toc-grid">
    <div class="toc-item"><span class="toc-title">1. Executive Overview & Problem Solved</span><span class="toc-num">01</span></div>
    <div class="toc-item"><span class="toc-title">2. High-Level Architecture & 50/50 Layout</span><span class="toc-num">02</span></div>
    <div class="toc-item"><span class="toc-title">3. Complete Folder & File Map</span><span class="toc-num">03</span></div>
    <div class="toc-item"><span class="toc-title">4. Application Startup Flow (Browser to DOM)</span><span class="toc-num">04</span></div>
    <div class="toc-item"><span class="toc-title">5. Package.json & Dependencies Table</span><span class="toc-num">05</span></div>
    <div class="toc-item"><span class="toc-title">6. Routing Architecture (React Router v7)</span><span class="toc-num">06</span></div>
    <div class="toc-item"><span class="toc-title">7. Page-by-Page Deep Dive (All 11 Pages)</span><span class="toc-num">07</span></div>
    <div class="toc-item"><span class="toc-title">8. Component Architecture & Hierarchy</span><span class="toc-num">08</span></div>
    <div class="toc-item"><span class="toc-title">9. Props Flow & Project Prop Catalog</span><span class="toc-num">09</span></div>
    <div class="toc-item"><span class="toc-title">10. State Management (Context + Local)</span><span class="toc-num">10</span></div>
    <div class="toc-item"><span class="toc-title">11. Form Architecture & Controlled Inputs</span><span class="toc-num">11</span></div>
    <div class="toc-item"><span class="toc-title">12. Form Validation Engine (validation.ts)</span><span class="toc-num">12</span></div>
    <div class="toc-item"><span class="toc-title">13. Event Handling & Interactive Handlers</span><span class="toc-num">13</span></div>
    <div class="toc-item"><span class="toc-title">14. TypeScript Implementation & Interfaces</span><span class="toc-num">14</span></div>
    <div class="toc-item"><span class="toc-title">15. Styling Architecture: Tailwind CSS v4</span><span class="toc-num">15</span></div>
    <div class="toc-item"><span class="toc-title">16. Material UI (MUI v9) Integration & Synergy</span><span class="toc-num">16</span></div>
    <div class="toc-item"><span class="toc-title">17. CSS Architecture & Custom Directives</span><span class="toc-num">17</span></div>
    <div class="toc-item"><span class="toc-title">18. Left Panel: Visual Branding Architecture</span><span class="toc-num">18</span></div>
    <div class="toc-item"><span class="toc-title">19. Right Panel: Dynamic Form Container</span><span class="toc-num">19</span></div>
    <div class="toc-item"><span class="toc-title">20. Asset Catalog & Media Pipeline</span><span class="toc-num">20</span></div>
    <div class="toc-item"><span class="toc-title">21. End-to-End Cross-Page Data Flow</span><span class="toc-num">21</span></div>
    <div class="toc-item"><span class="toc-title">22. Module Interconnection & Dependency Graph</span><span class="toc-num">22</span></div>
    <div class="toc-item"><span class="toc-title">23. End-to-End User Flow & Screen Transitions</span><span class="toc-num">23</span></div>
    <div class="toc-item"><span class="toc-title">24. Button-by-Button Interactive Reference</span><span class="toc-num">24</span></div>
    <div class="toc-item"><span class="toc-title">25. Conditional Rendering Strategies</span><span class="toc-num">25</span></div>
    <div class="toc-item"><span class="toc-title">26. Responsive Breakpoint Behavior</span><span class="toc-num">26</span></div>
    <div class="toc-item"><span class="toc-title">27. Error Handling, Validation & Lockout Logic</span><span class="toc-num">27</span></div>
    <div class="toc-item"><span class="toc-title">28. Backend Integration Status & Mock Architecture</span><span class="toc-num">28</span></div>
    <div class="toc-item"><span class="toc-title">29. Authentication & Security Simulation</span><span class="toc-num">29</span></div>
    <div class="toc-item"><span class="toc-title">30. React Concepts Master Checklist</span><span class="toc-num">30</span></div>
    <div class="toc-item"><span class="toc-title">31. TypeScript Concepts Master Checklist</span><span class="toc-num">31</span></div>
    <div class="toc-item"><span class="toc-title">32. Line-by-Line Code Walkthroughs</span><span class="toc-num">32</span></div>
    <div class="toc-item"><span class="toc-title">33. POC & Interview Speaking Script with Q&A</span><span class="toc-num">33</span></div>
    <div class="toc-item"><span class="toc-title">34. "How I Built This" Development Narrative</span><span class="toc-num">34</span></div>
    <div class="toc-item"><span class="toc-title">35. Architecture Rationale: "Why This Way?"</span><span class="toc-num">35</span></div>
    <div class="toc-item"><span class="toc-title">36. Technical Improvement Opportunities</span><span class="toc-num">36</span></div>
    <div class="toc-item"><span class="toc-title">37. Complete System Architecture Diagrams</span><span class="toc-num">37</span></div>
    <div class="toc-item"><span class="toc-title">38. Technical Project Glossary</span><span class="toc-num">38</span></div>
    <div class="toc-item"><span class="toc-title">39. Final Project Cheat Sheet</span><span class="toc-num">39</span></div>
    <div class="toc-item"><span class="toc-title">40. Self-Assessment & Mastery Checklist</span><span class="toc-num">40</span></div>
  </div>
</div>

<!-- ========================================== -->
<!-- CHAPTER 1: OVERVIEW                        -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">01</span> Project Overview & Problem Solved</h1>

  <h2>1.1 What is SignIn-UI-Frontend?</h2>
  <p>
    <strong>SignIn-UI-Frontend</strong> (internal package name: <code>stackly-auth</code>) is an enterprise-grade, multi-stage authentication and workspace onboarding frontend application built for the <strong>One Enterprise</strong> cloud platform by <strong>Stackly</strong>.
  </p>
  <p>
    In modern B2B SaaS applications, onboarding an enterprise client is fundamentally different from a consumer sign-up. A consumer only needs an email and password. An enterprise onboarding process requires collecting organization metadata (name, slug/code, industry, employee head-count, regional compliance jurisdiction, and logo branding), configuring the initial root Super Administrator identity, confirming legal compliance and data governance policies, and provisioning a dedicated tenant workspace subdomain (e.g., <code>https://acmecorp.oneenterprise.io</code>).
  </p>

  <h2>1.2 The Core Problem it Solves</h2>
  <p>
    Enterprise software onboarding is traditionally clunky, overwhelming, and fragmented. If users face a 25-field monolithic form on a single page, bounce rates spike, and users abandon onboarding. <strong>SignIn-UI-Frontend</strong> solves this with:
  </p>
  <ul>
    <li><strong>Cognitive Load Reduction:</strong> The onboarding journey is decomposed into three clear, progressive milestones:
      <ol style="margin-left: 20px; margin-top: 4px;">
        <li><strong>Step 1: Organization Details</strong> — Establishing company identity, workspace slug, and geographic settings.</li>
        <li><strong>Step 2: Super Admin Account</strong> — Creating the privileged administrator identity with enforced enterprise password complexity.</li>
        <li><strong>Step 3: Review & Confirm</strong> — Verifying legal acceptance, authorization, and data processing agreements before tenant creation.</li>
      </ol>
    </li>
    <li><strong>High-Confidence Visual Branding:</strong> A sticky, 50% split-screen desktop panel presents enterprise trust badges (SOC 2 Type II, ISO 27001, 99.95% SLA) and an interactive visual orbital diagram illustrating how <em>People</em>, <em>Process</em>, and <em>Progress</em> interconnect through One Enterprise (1E).</li>
    <li><strong>Dual-Track Authentication Flow:</strong> It seamlessly integrates two major user journeys:
      <ul style="margin-left: 20px; margin-top: 4px;">
        <li><strong>Existing Tenant Sign-In:</strong> Workspace resolution (<code>acmecorp.oneenterprise.io</code>) with Work Email validation and SSO (Google, Microsoft, SAML).</li>
        <li><strong>New Organization Provisioning:</strong> The complete 3-step registration wizard transferring captured metadata across steps into a unified state store.</li>
      </ul>
    </li>
  </ul>

  <h2>1.3 Conversational Explanation: How the App Works</h2>
  <div class="callout callout-note">
    <div class="callout-title">Conversational Explanation Style</div>
    "When a user opens the application, it immediately directs them to <code>/signin</code>. On large screens, the screen splits cleanly down the middle: the left side displays our interactive visual branding panel with our mountain backdrop, orbital cards, and security assurances. The right side contains the interactive form.<br><br>
    If an existing employee types their workspace and email, they proceed into the authentication pipeline. If a company is registering for the first time, they click 'Create an account'. This opens our step-by-step onboarding wizard. In Step 1, they enter their company name—our code automatically suggests a clean uppercase code like 'ABC-TECH'. They select their industry, country, and state. When they click 'Continue', that data isn't lost; our React Context stores it. Step 2 asks for their Admin details. Step 3 asks them to accept legal agreements. Once accepted, they click 'Create account' and reach the Welcome screen with their assigned workspace URL!"
  </div>
</div>

<!-- ========================================== -->
<!-- CHAPTER 2: HIGH-LEVEL ARCHITECTURE         -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">02</span> High-Level Architecture & 50/50 Layout</h1>

  <h2>2.1 The 50/50 Desktop Split Layout Pattern</h2>
  <p>
    The visual and architectural foundation of <code>SignIn-UI-Frontend</code> is the <strong>50/50 Split Screen Architecture</strong> defined inside <code>src/components/AuthLayout.tsx</code>. This layout separates the viewport into two distinct horizontal partitions on screens at or above the Tailwind <code>lg</code> breakpoint (1024px):
  </p>

  <div class="diagram-box">
+---------------------------------------------------------------------------------------------------+
| Viewport: 100vw x 100vh  (h-screen w-full overflow-hidden bg-white)                               |
+-------------------------------------------------+-------------------------------------------------+
| LEFT PANEL (50% on lg:block, hidden on mobile)  | RIGHT PANEL (100% mobile, 50% on lg:w-1/2)      |
| Component: <VisualBrandingPanel />             | Component: <Outlet /> rendered inside <main>    |
|                                                 |                                                 |
| - Fixed viewport height (h-full)                | - Independent vertical scrolling (overflow-y)   |
| - Locked non-scrollable stage (overflow-hidden) | - Scrollbar hidden via custom .no-scrollbar     |
| - Full mountain background image                | - Centered form column (max-w-[456px] - [560px])|
| - Stackly Brand Logo                            | - StepProgress (3 segments indicator)           |
| - Orbital Diagram (1E Center + 3 Nodes)         | - Dynamic Page Injection via React Router       |
| - Interactive Tabs (Secure, Scalable, Future)   |   (/signin, /organization, /admin, /review,     |
| - Compliance Footer (SOC 2, ISO 27001, SLA)     |    /welcome, /login, /2fa, /locked, etc.)       |
+-------------------------------------------------+-------------------------------------------------+
  </div>

  <h2>2.2 Why This Architectural Separation Matters</h2>
  <ul>
    <li><strong>Zero Layout Shift:</strong> Because the left branding panel is mounted once by <code>AuthLayout</code> as a persistent route layout, navigating between <code>/signin</code>, <code>/organization</code>, <code>/admin</code>, and <code>/review</code> changes only the right-hand <code>&lt;Outlet /&gt;</code>. The left panel does NOT unmount, re-render, or flicker.</li>
    <li><strong>Independent Scroll State:</strong> The left panel is pinned to <code>max-h-screen overflow-hidden</code>. The right panel has <code>overflow-y-auto</code> with <code>.no-scrollbar</code>. When a user scrolls down a long form like <code>OrganizationForm</code> (which has 8 input groups and a file upload), the branding and trust assurances stay perfectly locked in the user's field of view.</li>
    <li><strong>Graceful Mobile Degradation:</strong> On viewports below 1024px (tablets and smartphones), the left panel receives <code>hidden</code>, allowing the right-side form container to take 100% of the screen width with natural mobile scrolling and comfortable touch targets.</li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 3: COMPLETE FOLDER & FILE MAP      -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">03</span> Complete Project Folder & File Structure</h1>
  <p>
    The following tree represents the exact, actual filesystem structure of <code>SignIn-UI-Frontend</code>. No imaginary files or directories are included.
  </p>

  <div class="diagram-box">
SignIn-UI-Frontend/
├── public/                               # Static public assets served directly by Vite at root
│   ├── favicon.svg                       # Browser tab favicon icon
│   ├── icons.svg                         # SVG symbol sprite sheet
│   ├── mountains.png                     # High-res scenic mountain image for left branding panel
│   ├── stackly-logo.png                  # Primary Stackly brand logo
│   └── stackly-logoo.png                 # Alternate branded logo asset
│
├── src/                                  # Application source code
│   ├── assets/                           # Bundled assets processed through Vite module graph
│   │   ├── hero.png                      # Hero illustration graphic
│   │   ├── react.svg                     # Standard React logo
│   │   └── vite.svg                      # Standard Vite logo
│   │
│   ├── components/                       # Reusable UI component library
│   │   ├── auth/                         # Domain-specific authentication & form primitives
│   │   │   ├── AgreementCheckbox.tsx     # Custom styled checkbox with optional badge
│   │   │   ├── DividerText.tsx           # Horizontal rule with centered text ("or continue with")
│   │   │   ├── FileUpload.tsx            # Drag-and-drop file upload with preview and validation
│   │   │   ├── FormField.tsx             # Universal input & dropdown wrapper with error states
│   │   │   ├── PrimaryButton.tsx         # Dark navy action button (#0f1330) with hover states
│   │   │   ├── SocialLoginButton.tsx     # Google, Microsoft, and SAML SSO authentication buttons
│   │   │   └── StepProgress.tsx          # 3-segment progress indicator with gradient states
│   │   │
│   │   ├── organization/                 # Organization domain components
│   │   │   └── OrganizationForm.tsx      # Comprehensive Step 1 onboarding form (439 lines)
│   │   │
│   │   ├── ui/                           # Material UI styled component wrappers
│   │   │   └── Button.tsx                # MUI Button styled as PrimaryButton and SecondaryButton
│   │   │
│   │   ├── AgreementCheckbox.tsx         # Re-export bridge to ./auth/AgreementCheckbox
│   │   ├── AuthLayout.tsx                # 50/50 Split Screen Master Layout wrapper with <Outlet />
│   │   ├── ProgressSteps.tsx             # Re-export wrapper around StepProgress
│   │   └── VisualBrandingPanel.tsx       # Pixel-perfect Left Branding Panel (277 lines)
│   │
│   ├── context/                          # Global React State Management
│   │   ├── OnboardingContext.tsx         # Provider component storing organization & admin state
│   │   ├── OnboardingContextValue.ts     # TypeScript interface & Context object creation
│   │   └── useOnboarding.ts              # Custom hook with guard check for accessing context
│   │
│   ├── pages/                            # Routed Page Views (11 distinct page components)
│   │   ├── AccountLocked.tsx             # Security lockout screen triggered after 5 failed logins
│   │   ├── AdminAccountPage.tsx          # Step 2: Super Admin Account creation form
│   │   ├── CheckEmail.tsx                # Password reset link dispatch notification page
│   │   ├── EnterPassword.tsx             # Password entry page with attempt counter and lockout trigger
│   │   ├── ForgotPassword.tsx            # Self-service work email password recovery form
│   │   ├── OrganizationDetailsPage.tsx   # Step 1: Organization details page container
│   │   ├── ReviewConfirm.tsx             # Step 3: Terms, authorization, and data processing review
│   │   ├── ReviewConfirmPage.tsx         # Re-export alias for ReviewConfirm
│   │   ├── SignInPage.tsx                # Step 1 Identify: Workspace & Work Email sign-in page
│   │   ├── Success.tsx                   # Post-authentication success confirmation card
│   │   ├── TwoFactor.tsx                 # 6-digit OTP authenticator verification screen
│   │   ├── Welcome.tsx                   # Final Step 6: Workspace provisioned & email verify screen
│   │   └── WelcomePage.tsx               # Re-export alias for Welcome
│   │
│   ├── types/                            # Global TypeScript Type Definitions
│   │   └── onboarding.ts                 # Interfaces for OrganizationDetails, AdminAccount, State
│   │
│   ├── utils/                            # Helper utilities & Business Logic
│   │   └── validation.ts                 # Validation functions (email, workspace, password, org-code)
│   │
│   ├── App.css                           # Legacy / starter CSS rules
│   ├── App.tsx                           # Master application component with Router and Routes
│   ├── index.css                         # Tailwind v4 import, @theme variables, and font imports
│   └── main.tsx                          # React 19 bootstrap entry point (createRoot + StrictMode)
│
├── .gitignore                            # Git file exclusions (node_modules, dist, etc.)
├── index.html                            # Single-Page Application HTML entry template
├── package.json                          # Project manifest, dependencies, and execution scripts
├── package-lock.json                     # Deterministic dependency lockfile
├── tsconfig.app.json                     # TypeScript compiler configuration for client code
├── tsconfig.json                         # TypeScript root solution configuration
├── tsconfig.node.json                    # TypeScript compiler configuration for Vite scripts
└── vite.config.ts                        # Vite bundler configuration with React and Tailwind plugins
  </div>

  <h2>3.1 File-by-File Breakdown: Purpose, Imports & Exports</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 25%;">File Path</th>
        <th style="width: 20%;">What it Imports</th>
        <th style="width: 20%;">What it Exports</th>
        <th style="width: 35%;">Purpose & What Breaks if Removed</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>src/main.tsx</code></td>
        <td><code>StrictMode</code>, <code>createRoot</code>, <code>./index.css</code>, <code>App</code></td>
        <td>None (entry file)</td>
        <td>Bootstraps React 19 into the <code>#root</code> DOM element. If removed, the entire app fails to run; blank white screen.</td>
      </tr>
      <tr>
        <td><code>src/App.tsx</code></td>
        <td><code>react-router-dom</code>, <code>OnboardingProvider</code>, <code>AuthLayout</code>, all 11 pages</td>
        <td><code>App</code> (default)</td>
        <td>Defines all URL route mappings, sets up <code>OnboardingProvider</code> context, and establishes route fallback. If removed, routing collapses.</td>
      </tr>
      <tr>
        <td><code>src/components/AuthLayout.tsx</code></td>
        <td><code>Outlet</code>, <code>VisualBrandingPanel</code></td>
        <td><code>AuthLayout</code> (named)</td>
        <td>Provides the two-column 50/50 responsive split layout. Houses the persistent left branding panel and dynamic right outlet. If removed, layout collapses.</td>
      </tr>
      <tr>
        <td><code>src/components/VisualBrandingPanel.tsx</code></td>
        <td>React, MUI Icons (<code>Security</code>, <code>Lock</code>, <code>AccessTime</code>)</td>
        <td><code>VisualBrandingPanel</code> (named)</td>
        <td>Renders the left-side branding UI with background image, orbital diagram, 1E core, interactive tabs, and compliance badges.</td>
      </tr>
      <tr>
        <td><code>src/context/OnboardingContext.tsx</code></td>
        <td>React, <code>OnboardingContextValue</code>, <code>types/onboarding</code></td>
        <td><code>OnboardingProvider</code> (named)</td>
        <td>Holds global state for <code>organization</code> and <code>admin</code> across steps. Provides <code>updateOrganization</code>, <code>updateAdmin</code>, and <code>resetOnboarding</code>.</td>
      </tr>
      <tr>
        <td><code>src/context/useOnboarding.ts</code></td>
        <td><code>useContext</code>, <code>OnboardingContextValue</code></td>
        <td><code>useOnboarding</code> (named)</td>
        <td>Custom hook providing safe access to OnboardingContext. Throws an explicit error if consumed outside the provider.</td>
      </tr>
      <tr>
        <td><code>src/utils/validation.ts</code></td>
        <td>None (pure TypeScript)</td>
        <td><code>validateRequired</code>, <code>validateEmail</code>, <code>validateWorkspace</code>, <code>validatePassword</code>, <code>validateConfirmPassword</code>, <code>generateOrgCode</code></td>
        <td>Validation engine and slug auto-generator. If removed, all form submissions break without validation logic.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ========================================== -->
<!-- CHAPTER 4: STARTUP FLOW                    -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">04</span> Application Startup Flow (Browser to DOM)</h1>

  <h2>4.1 What Happens When You Run `npm run dev`?</h2>
  <p>
    When a developer executes <code>npm run dev</code> in the terminal, the following sequence occurs under the hood:
  </p>

  <div class="diagram-box">
Step 1: Terminal executes 'npm run dev' -> maps to 'vite' binary in package.json
   │
Step 2: Vite initializes development server at http://localhost:5173
   │    - Loads vite.config.ts
   │    - Registers @vitejs/plugin-react (fast HMR transform)
   │    - Registers @tailwindcss/vite (compiles Tailwind v4 stylesheet in-memory)
   │
Step 3: Browser requests http://localhost:5173/
   │    - Server serves index.html
   │    - Browser parses <div id="root"></div>
   │    - Browser finds script: <script type="module" src="/src/main.tsx"></script>
   │
Step 4: Vite transpiles & serves src/main.tsx via native ES Modules (ESM)
   │    - main.tsx imports './index.css' (injects compiled Tailwind rules & Google Fonts)
   │    - main.tsx imports App from './App.tsx'
   │    - Calls createRoot(document.getElementById('root')!).render(...)
   │
Step 5: React 19 creates Root Fiber and mounts <StrictMode><App /></StrictMode>
   │
Step 6: App.tsx executes in memory:
   │    - Instantiates <Router> (HTML5 History API)
   │    - Instantiates <OnboardingProvider> (initializes organization & admin state)
   │    - Evaluates <Routes> against current window.location.pathname
   │
Step 7: Route matching and rendering:
   │    - If URL is "/" -> Matches <Route path="/" element={<Navigate to="/signin" replace />} />
   │      Browser URL changes to /signin without page reload
   │    - Route /signin matches nested route under <Route element={<AuthLayout />}>
   │    - <AuthLayout> renders:
   │         Left:  <VisualBrandingPanel />
   │         Right: <main><Outlet /></main> -> which resolves to <SignInPage />
   │
Step 8: Final Paint: User sees the complete 50/50 Sign In Page in ~120 milliseconds!
  </div>

  <h2>4.2 The Role of StrictMode</h2>
  <p>
    In <code>src/main.tsx</code>, <code>&lt;App /&gt;</code> is wrapped in <code>&lt;StrictMode&gt;</code>. In development mode, React intentionally invokes component render functions and state updater functions twice. This is an intentional debugging tool to help developers detect side-effects, memory leaks, and unsafe mutations before shipping to production. In production builds (<code>npm run build</code>), <code>StrictMode</code> adds zero overhead.
  </p>
</div>

<!-- ========================================== -->
<!-- CHAPTER 5: PACKAGE.JSON DEEP DIVE          -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">05</span> Package.json & Dependencies Table</h1>

  <h2>5.1 Actual Project Dependencies Breakdown</h2>
  <p>
    Inspecting the actual <code>package.json</code> reveals a modern, cutting-edge frontend toolchain utilizing React 19, Tailwind CSS v4, and Material UI v9.
  </p>

  <table>
    <thead>
      <tr>
        <th>Package Name</th>
        <th>Version</th>
        <th>Type</th>
        <th>Where Used</th>
        <th>Technical Purpose & Necessity</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>react</code></td>
        <td><code>^19.2.8</code></td>
        <td>Runtime</td>
        <td>Entire Project</td>
        <td>The core component library providing JSX syntax, component lifecycle, React Hooks (<code>useState</code>, <code>useCallback</code>, <code>useRef</code>, <code>useEffect</code>).</td>
      </tr>
      <tr>
        <td><code>react-dom</code></td>
        <td><code>^19.2.8</code></td>
        <td>Runtime</td>
        <td><code>src/main.tsx</code></td>
        <td>The browser rendering glue for React. Provides <code>createRoot</code> to mount the React virtual DOM tree into HTML5.</td>
      </tr>
      <tr>
        <td><code>react-router-dom</code></td>
        <td><code>^7.18.4</code></td>
        <td>Runtime</td>
        <td><code>App.tsx</code>, all Pages</td>
        <td>Client-side single-page routing without page reloads. Provides <code>BrowserRouter</code>, <code>Routes</code>, <code>Route</code>, <code>Navigate</code>, <code>Outlet</code>, and <code>useNavigate</code>.</td>
      </tr>
      <tr>
        <td><code>tailwindcss</code></td>
        <td><code>^4.3.3</code></td>
        <td>Runtime/Dev</td>
        <td><code>src/index.css</code></td>
        <td>Tailwind CSS version 4 engine. Delivers utility-first styling with zero-runtime CSS generation and CSS variable theming.</td>
      </tr>
      <tr>
        <td><code>@tailwindcss/vite</code></td>
        <td><code>^4.3.3</code></td>
        <td>Runtime/Plugin</td>
        <td><code>vite.config.ts</code></td>
        <td>Official Vite plugin for Tailwind v4. Compiles utility classes directly inside Vite's lightning-fast build pipeline without PostCSS.</td>
      </tr>
      <tr>
        <td><code>@mui/material</code></td>
        <td><code>^9.4.0</code></td>
        <td>Runtime</td>
        <td><code>components/ui/Button.tsx</code>, <code>EnterPassword.tsx</code></td>
        <td>Material UI v9 component library. Supplies enterprise input elements like <code>TextField</code>, <code>Checkbox</code>, <code>FormControlLabel</code>, and <code>styled</code>.</td>
      </tr>
      <tr>
        <td><code>@mui/icons-material</code></td>
        <td><code>^9.4.0</code></td>
        <td>Runtime</td>
        <td><code>VisualBrandingPanel.tsx</code>, <code>AdminAccountPage.tsx</code></td>
        <td>MUI SVG icons: <code>SecurityOutlined</code>, <code>LockOutlined</code>, <code>AccessTimeOutlined</code>, <code>ShieldOutlined</code>, <code>VisibilityOutlined</code>.</td>
      </tr>
      <tr>
        <td><code>@emotion/react</code> & <code>@emotion/styled</code></td>
        <td><code>^11.14.0</code></td>
        <td>Runtime</td>
        <td>MUI dependency</td>
        <td>Underlying CSS-in-JS styling engines required by Material UI to process dynamic component styling and <code>styled()</code> wrappers.</td>
      </tr>
      <tr>
        <td><code>lucide-react</code></td>
        <td><code>^1.47.0</code></td>
        <td>Runtime</td>
        <td><code>FormField.tsx</code>, <code>FileUpload.tsx</code>, <code>SocialLoginButton.tsx</code></td>
        <td>Feather-style modern lightweight SVG icons: <code>ChevronDown</code>, <code>Upload</code>, <code>X</code>, <code>Users</code>, <code>Eye</code>, <code>EyeOff</code>, <code>Lock</code>, <code>Check</code>.</td>
      </tr>
      <tr>
        <td><code>vite</code></td>
        <td><code>^8.3.0</code></td>
        <td>Dev</td>
        <td>Build system</td>
        <td>Next-generation frontend dev server and bundler. Provides Hot Module Replacement (HMR) and optimized Rollup production builds.</td>
      </tr>
      <tr>
        <td><code>typescript</code></td>
        <td><code>~6.0.2</code></td>
        <td>Dev</td>
        <td>Type checking</td>
        <td>Static type system providing compile-time type validation, autocompletion, and refactoring safety across all <code>.ts</code> and <code>.tsx</code> files.</td>
      </tr>
      <tr>
        <td><code>oxlint</code></td>
        <td><code>^1.81.0</code></td>
        <td>Dev</td>
        <td>Code Quality</td>
        <td>Rust-based, ultra-fast linter that analyzes JavaScript/TypeScript code 50x-100x faster than traditional ESLint.</td>
      </tr>
    </tbody>
  </table>

  <h2>5.2 Dependencies vs devDependencies</h2>
  <p>
    <strong>dependencies</strong> are packages necessary to execute the application in the user's browser runtime (React, React Router, Tailwind, MUI, Lucide). 
    <strong>devDependencies</strong> are development-only tools required to transpile, type-check, bundle, or lint code during the development lifecycle (Vite, TypeScript, oxlint, type definition files). They are not bundled into the final production payload.
  </p>
</div>

<!-- ========================================== -->
<!-- CHAPTER 6: ROUTING ARCHITECTURE            -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">06</span> Complete Routing Architecture (React Router v7)</h1>

  <h2>6.1 Route Table & Layout Mapping</h2>
  <p>
    All application routing is declared declaratively in <code>src/App.tsx</code> using <code>react-router-dom</code> (v7.18.4). Notice how <code>&lt;AuthLayout /&gt;</code> acts as a parent layout route wrapping every authenticated screen.
  </p>

  <table>
    <thead>
      <tr>
        <th>Path</th>
        <th>Rendered Component</th>
        <th>Layout Wrapper</th>
        <th>Flow Purpose</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>/</code></td>
        <td><code>&lt;Navigate to="/signin" replace /&gt;</code></td>
        <td>None</td>
        <td>Root redirect: forwards users straight to the sign-in screen.</td>
      </tr>
      <tr>
        <td><code>/signin</code></td>
        <td><code>&lt;SignInPage /&gt;</code></td>
        <td><code>AuthLayout</code></td>
        <td>Step 1 Identify: Workspace and work email entry point.</td>
      </tr>
      <tr>
        <td><code>/organization</code></td>
        <td><code>&lt;OrganizationDetailsPage /&gt;</code></td>
        <td><code>AuthLayout</code></td>
        <td>Step 1 of 3: Organization Details form.</td>
      </tr>
      <tr>
        <td><code>/organization/details</code></td>
        <td><code>&lt;OrganizationDetailsPage /&gt;</code></td>
        <td><code>AuthLayout</code></td>
        <td>Alias route for Step 1 Organization Details.</td>
      </tr>
      <tr>
        <td><code>/admin</code></td>
        <td><code>&lt;AdminAccountPage /&gt;</code></td>
        <td><code>AuthLayout</code></td>
        <td>Step 2 of 3: Super Administrator account configuration.</td>
      </tr>
      <tr>
        <td><code>/create-admin</code></td>
        <td><code>&lt;AdminAccountPage /&gt;</code></td>
        <td><code>AuthLayout</code></td>
        <td>Alias route for Step 2 Admin Account.</td>
      </tr>
      <tr>
        <td><code>/review</code></td>
        <td><code>&lt;ReviewConfirm /&gt;</code></td>
        <td><code>AuthLayout</code></td>
        <td>Step 3 of 3: Review & Confirm agreements.</td>
      </tr>
      <tr>
        <td><code>/review-confirm</code></td>
        <td><code>&lt;ReviewConfirm /&gt;</code></td>
        <td><code>AuthLayout</code></td>
        <td>Alias route for Step 3 Review & Confirm.</td>
      </tr>
      <tr>
        <td><code>/welcome</code></td>
        <td><code>&lt;Welcome /&gt;</code></td>
        <td><code>AuthLayout</code></td>
        <td>Final onboarding completion & workspace ready screen.</td>
      </tr>
      <tr>
        <td><code>/login</code></td>
        <td><code>&lt;EnterPassword /&gt;</code></td>
        <td><code>AuthLayout &gt; CenteredAuthWrapper</code></td>
        <td>Password entry screen for returning users.</td>
      </tr>
      <tr>
        <td><code>/2fa</code></td>
        <td><code>&lt;TwoFactor /&gt;</code></td>
        <td><code>AuthLayout &gt; CenteredAuthWrapper</code></td>
        <td>6-digit authenticator code verification.</td>
      </tr>
      <tr>
        <td><code>/forgot-password</code></td>
        <td><code>&lt;ForgotPassword /&gt;</code></td>
        <td><code>AuthLayout &gt; CenteredAuthWrapper</code></td>
        <td>Password recovery request screen.</td>
      </tr>
      <tr>
        <td><code>/check-email</code></td>
        <td><code>&lt;CheckEmail /&gt;</code></td>
        <td><code>AuthLayout &gt; CenteredAuthWrapper</code></td>
        <td>Password recovery email dispatch confirmation.</td>
      </tr>
      <tr>
        <td><code>/locked</code></td>
        <td><code>&lt;AccountLocked /&gt;</code></td>
        <td><code>AuthLayout &gt; CenteredAuthWrapper</code></td>
        <td>Security lockout page after 5 failed password attempts.</td>
      </tr>
      <tr>
        <td><code>/success</code></td>
        <td><code>&lt;Success /&gt;</code></td>
        <td><code>AuthLayout &gt; CenteredAuthWrapper</code></td>
        <td>Login authentication success indicator.</td>
      </tr>
      <tr>
        <td><code>*</code></td>
        <td><code>&lt;Navigate to="/signin" replace /&gt;</code></td>
        <td>None</td>
        <td>Catch-all wildcard fallback route: sends unknown URLs to <code>/signin</code>.</td>
      </tr>
    </tbody>
  </table>

  <h2>6.2 The CenteredAuthWrapper Component</h2>
  <p>
    Inside <code>src/App.tsx</code> lines 21-27, a dedicated helper component wraps secondary authentication screens:
  </p>
  <pre><code><span class="kw">const</span> <span class="fn">CenteredAuthWrapper</span>: React.FC&lt;{ children: React.ReactNode }&gt; = ({ children }) =&gt; (
  &lt;<span class="typ">div</span> <span class="prop">className</span>=<span class="str">"w-full min-w-0 flex-1 flex flex-col justify-center items-center p-8 lg:p-16"</span>&gt;
    &lt;<span class="typ">div</span> <span class="prop">className</span>=<span class="str">"w-full max-w-md"</span>&gt;
      {children}
    &lt;/<span class="typ">div</span>&gt;
  &lt;/<span class="typ">div</span>&gt;
);</code></pre>
  <p>
    <strong>Why was this written?</strong> The primary onboarding pages (<code>OrganizationForm</code>, <code>AdminAccountPage</code>, <code>ReviewConfirm</code>) require a wider container (<code>max-w-[560px]</code>) aligned to the top with precise padding (<code>pt-[104px]</code>) to accommodate step progress bars. Secondary auth pages (like entering a password, 2FA, or lockout) are shorter and look best centered vertically in the viewport inside a compact <code>max-w-md</code> (448px) column.
  </p>
</div>
"""
