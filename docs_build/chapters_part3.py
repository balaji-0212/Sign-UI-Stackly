# -*- coding: utf-8 -*-
"""
Part 3 of the Guide:
- Chapter 13: Event Handling & Interaction Patterns
- Chapter 14: TypeScript Implementation (Interfaces, Types & Safety)
- Chapter 15: Styling Architecture: Tailwind CSS v4 in Depth
- Chapter 16: Material UI (MUI v9) Integration & Synergy
- Chapter 17: CSS Architecture & Custom Directives
- Chapter 18: Left Panel: Visual Branding Architecture (VisualBrandingPanel.tsx)
- Chapter 19: Right Panel: Dynamic Form Container
- Chapter 20: Asset Catalog & Media Pipeline
- Chapter 21: End-to-End Cross-Page Data Flow
- Chapter 22: Module Interconnection & Dependency Graph
- Chapter 23: End-to-End User Flow & Screen Transitions
"""

def get_part3_html():
    return """
<!-- ========================================== -->
<!-- CHAPTER 13: EVENT HANDLING                 -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">13</span> Event Handling & Interactive Handlers</h1>

  <h2>13.1 Key Event Handlers in the Project</h2>
  <p>
    React employs a Synthetic Event system that wraps native browser events for cross-browser consistency. The project implements five key event patterns:
  </p>

  <table>
    <thead>
      <tr>
        <th>Event Name</th>
        <th>Where Implemented</th>
        <th>Handler Function</th>
        <th>Runtime Execution Sequence</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>onSubmit</code></td>
        <td><code>OrganizationForm.tsx</code>, <code>SignInPage.tsx</code>, <code>AdminAccountPage.tsx</code></td>
        <td><code>handleSubmit(e)</code></td>
        <td>1. Calls <code>e.preventDefault()</code> to halt browser reload.<br>2. Executes <code>validateAll()</code>.<br>3. If valid, dispatches context updates.<br>4. Navigates to next route.</td>
      </tr>
      <tr>
        <td><code>onChange</code></td>
        <td><code>FormField.tsx</code>, <code>OrganizationForm.tsx</code></td>
        <td><code>handleOrgNameChange(e)</code></td>
        <td>1. Extracts <code>e.target.value</code>.<br>2. Updates local form state.<br>3. Computes <code>generateOrgCode()</code> if slug is in auto-mode.<br>4. Clears active error if touched.</td>
      </tr>
      <tr>
        <td><code>onBlur</code></td>
        <td>All Input Fields</td>
        <td>Inline arrow functions</td>
        <td>Fires when input loses focus. Sets <code>touched[field] = true</code> and immediately checks validation to give instant feedback.</td>
      </tr>
      <tr>
        <td><code>onKeyDown</code></td>
        <td><code>AgreementCheckbox.tsx</code>, <code>TwoFactor.tsx</code></td>
        <td><code>handleKeyDown(e)</code></td>
        <td>In <code>AgreementCheckbox</code>: intercepts Space/Enter to toggle check state for accessibility.<br>In <code>TwoFactor</code>: intercepts Backspace to shift focus to previous OTP box.</td>
      </tr>
      <tr>
        <td><code>onDrop</code> &amp; <code>onDragOver</code></td>
        <td><code>FileUpload.tsx</code></td>
        <td><code>onDrop(e)</code>, <code>onDragOver(e)</code></td>
        <td>1. <code>e.preventDefault()</code> prevents browser file opening.<br>2. Extracts <code>e.dataTransfer.files[0]</code>.<br>3. Validates file type and &lt;= 5MB size.<br>4. Creates blob URL preview.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ========================================== -->
<!-- CHAPTER 14: TYPESCRIPT IMPLEMENTATION      -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">14</span> TypeScript Implementation & Type Safety</h1>

  <h2>14.1 Core Type Interfaces in <code>src/types/onboarding.ts</code></h2>
  <p>
    TypeScript guarantees complete contract enforcement across the application. The central models are defined cleanly:
  </p>

  <pre><code><span class="kw">export interface</span> <span class="typ">OrganizationDetails</span> {
  organizationName: <span class="typ">string</span>;
  organizationCode: <span class="typ">string</span>;
  organizationType: <span class="typ">string</span>;
  industry: <span class="typ">string</span>;
  companySize: <span class="typ">string</span>;
  country: <span class="typ">string</span>;
  state: <span class="typ">string</span>;
  city: <span class="typ">string</span>;
  timeZone: <span class="typ">string</span>;
  organizationLogo?: <span class="typ">File</span> | <span class="typ">null</span>;
  logoPreviewUrl?: <span class="typ">string</span> | <span class="typ">null</span>;
}

<span class="kw">export interface</span> <span class="typ">AdminAccount</span> {
  firstName: <span class="typ">string</span>;
  lastName: <span class="typ">string</span>;
  officialEmail: <span class="typ">string</span>;
  mobileNumber: <span class="typ">string</span>;
  username: <span class="typ">string</span>;
  password: <span class="typ">string</span>;
  confirmPassword: <span class="typ">string</span>;
}

<span class="kw">export interface</span> <span class="typ">OnboardingState</span> {
  organization: <span class="typ">OrganizationDetails</span>;
  admin: <span class="typ">AdminAccount</span>;
}</code></pre>

  <h2>14.2 Partial Updates via Generic Types</h2>
  <p>
    In <code>src/context/OnboardingContextValue.ts</code>, updater functions utilize TypeScript's built-in utility type <code>Partial&lt;T&gt;</code>:
  </p>
  <pre><code><span class="kw">export interface</span> <span class="typ">OnboardingContextType</span> {
  organization: <span class="typ">OrganizationDetails</span>;
  admin: <span class="typ">AdminAccount</span>;
  updateOrganization: (data: <span class="typ">Partial</span>&lt;<span class="typ">OrganizationDetails</span>&gt;) =&gt; <span class="typ">void</span>;
  updateAdmin: (data: <span class="typ">Partial</span>&lt;<span class="typ">AdminAccount</span>&gt;) =&gt; <span class="typ">void</span>;
  resetOnboarding: () =&gt; <span class="typ">void</span>;
}</code></pre>
  <p>
    <strong>Why this matters:</strong> <code>Partial&lt;OrganizationDetails&gt;</code> allows callers to submit only the fields they want to change (for instance, when <code>SignInPage</code> updates only <code>{ organizationCode: workspace.toUpperCase() }</code>), without having to pass the other 10 properties.
  </p>
</div>

<!-- ========================================== -->
<!-- CHAPTER 15: TAILWIND CSS V4 IN DEPTH       -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">15</span> Styling Architecture: Tailwind CSS v4 in Depth</h1>

  <h2>15.1 The Modern Tailwind v4 Engine</h2>
  <p>
    This project is built on the brand new <strong>Tailwind CSS v4</strong> (<code>@tailwindcss/vite ^4.3.3</code>). Unlike Tailwind v3, Tailwind v4:
  </p>
  <ul>
    <li>Does NOT require a <code>tailwind.config.js</code> or <code>postcss.config.js</code> file!</li>
    <li>Uses the native Vite plugin <code>@tailwindcss/vite</code> configured in <code>vite.config.ts</code>.</li>
    <li>Directly imports into CSS via <code>@import "tailwindcss";</code> in <code>src/index.css</code>.</li>
    <li>Configures custom theme tokens directly inside CSS using the official <code>@theme</code> directive!</li>
  </ul>

  <h2>15.2 Breakdown of Real Tailwind Classes Used in the Project</h2>
  <table>
    <thead>
      <tr>
        <th>Tailwind Class Snippet</th>
        <th>Where Used</th>
        <th>CSS Property & Design Purpose</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>hidden lg:block lg:w-1/2</code></td>
        <td><code>AuthLayout.tsx</code></td>
        <td>Hides the left panel on screens under 1024px. Displays it at 50% width on desktop.</td>
      </tr>
      <tr>
        <td><code>h-screen overflow-hidden</code></td>
        <td><code>AuthLayout.tsx</code></td>
        <td>Locks total viewport height to 100vh and prevents outer browser scrollbars from appearing.</td>
      </tr>
      <tr>
        <td><code>overflow-y-auto no-scrollbar</code></td>
        <td><code>AuthLayout.tsx</code> &lt;main&gt;</td>
        <td>Enables smooth vertical scrolling on the right form container while hiding ugly browser scrollbars.</td>
      </tr>
      <tr>
        <td><code>rounded-[28px] bg-white/90 backdrop-blur-xl</code></td>
        <td><code>VisualBrandingPanel.tsx</code> (1E Card)</td>
        <td>Creates the ultra-modern glassmorphic frosted-glass card with 28px border-radius and blur filter.</td>
      </tr>
      <tr>
        <td><code>bg-gradient-to-r from-[#76a4f0] to-[#8781f0]</code></td>
        <td><code>StepProgress.tsx</code></td>
        <td>Creates the polished blue-to-indigo linear gradient fill for completed steps in the progress indicator.</td>
      </tr>
      <tr>
        <td><code>bg-[#0f1330] hover:bg-[#18204a] text-white</code></td>
        <td><code>PrimaryButton.tsx</code></td>
        <td>The primary brand color: deep midnight navy with smooth hover shift to indigo navy.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ========================================== -->
<!-- CHAPTER 16: MATERIAL UI (MUI V9) SYNERGY   -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">16</span> Material UI (MUI v9) Integration & Synergy</h1>

  <h2>16.1 How MUI and Tailwind Coexist</h2>
  <p>
    A common question in enterprise interviews: <em>"Why does your project use both Tailwind CSS and Material UI?"</em>
  </p>
  <div class="callout callout-note">
    <div class="callout-title">The Engineering Separation of Concerns</div>
    <strong>Tailwind CSS v4</strong> governs all macro-layouts, page containers, responsive grids, orbital diagrams, and custom branding cards.<br>
    <strong>Material UI v9</strong> (<code>@mui/material</code> & <code>@mui/icons-material</code>) provides specialized accessible enterprise controls and battle-tested icon vectors.
  </div>

  <h2>16.2 Real Project Examples of MUI Usage</h2>
  <ul>
    <li><strong>Custom Styled Components (<code>src/components/ui/Button.tsx</code>):</strong>
      <pre><code><span class="kw">import</span> { Button <span class="kw">as</span> MuiButton } <span class="kw">from</span> <span class="str">'@mui/material'</span>;
<span class="kw">import</span> { styled } <span class="kw">from</span> <span class="str">'@mui/material/styles'</span>;

<span class="kw">export const</span> <span class="typ">PrimaryButton</span> = styled(MuiButton)({
  backgroundColor: <span class="str">'#0F172A'</span>,
  color: <span class="str">'#ffffff'</span>,
  textTransform: <span class="str">'none'</span>,
  fontWeight: 600,
  fontSize: <span class="str">'14px'</span>,
  padding: <span class="str">'12px 24px'</span>,
  borderRadius: <span class="str">'8px'</span>,
  <span class="str">'&:hover'</span>: { backgroundColor: <span class="str">'#1E293B'</span> }
});</code></pre>
    </li>
    <li><strong>Material UI Icons:</strong> Used in <code>VisualBrandingPanel.tsx</code> (<code>SecurityOutlinedIcon</code>, <code>LockOutlinedIcon</code>, <code>AccessTimeOutlinedIcon</code>) and <code>AdminAccountPage.tsx</code> (<code>ShieldOutlinedIcon</code>, <code>VisibilityOutlinedIcon</code>, <code>VisibilityOffOutlinedIcon</code>).</li>
    <li><strong>Enterprise Password Field:</strong> In <code>EnterPassword.tsx</code>, MUI's <code>TextField</code> with <code>InputAdornment</code> and <code>IconButton</code> hosts the password reveal toggle with clean accessible focus rings.</li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 17: CSS ARCHITECTURE               -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">17</span> CSS Architecture & Custom Directives</h1>

  <h2>17.1 Analysis of <code>src/index.css</code></h2>
  <p>
    <code>src/index.css</code> is concise, modern, and acts as the central styling manifest:
  </p>
  <pre><code>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
@import "tailwindcss";

@theme {
  --color-brand-dark: #0F172A;
  --color-brand-blue: #4F46E5;
  --color-brand-lightblue: #F0F4F8;
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

body {
  font-family: 'Inter', sans-serif;
  -webkit-font-smoothing: antialiased;
}

/* Hide scrollbar while preserving natural scroll behavior */
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}</code></pre>
  <ul>
    <li><strong>Google Fonts:</strong> Loads <em>Inter</em> for standard clean body typography and <em>JetBrains Mono</em> for technical labels, code, and step indicators.</li>
    <li><strong><code>@theme</code> Directive:</strong> Exposes CSS custom properties that integrate with Tailwind v4's class generator (e.g. <code>text-brand-dark</code>, <code>font-mono</code>).</li>
    <li><strong><code>.no-scrollbar</code> Utility:</strong> Strips scrollbar visual elements across WebKit (Chrome, Edge, Safari), Firefox (<code>scrollbar-width: none</code>), and IE/legacy Edge (<code>-ms-overflow-style: none</code>) while maintaining scrollability.</li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 18: LEFT-SIDE BRANDING PANEL       -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">18</span> Left Panel: Visual Branding Architecture</h1>

  <h2>18.1 Deep Inspection of <code>VisualBrandingPanel.tsx</code></h2>
  <p>
    The left branding panel is a showcase of sophisticated CSS positioning, SVG vector geometry, and glassmorphism. It contains four vertical layers:
  </p>

  <div class="diagram-box">
+-----------------------------------------------------------------------------------+
| 1. BACKGROUND LAYERS (Z-0)                                                        |
|   - Full coverage background image: url('/mountains.png') (bg-cover bg-center)     |
|   - Soft white tint overlay: bg-white/25 (ensures high contrast text readability) |
+-----------------------------------------------------------------------------------+
| 2. TOP HEADER (Z-20)                                                              |
|   - Brand Logo: <img src="/stackly-logo.png" alt="STACKLY" className="h-[36px]" />|
+-----------------------------------------------------------------------------------+
| 3. HERO & ORBITAL SYSTEM (Z-10)                                                   |
|   Left Side Text:                                                                 |
|     - Category tracker: "CLOUD PLATFORM · HRMS · CRM · ERP · FINANCE · AI"        |
|     - Bold H1: "One identity. Infinite Potential." (with blue highlight)          |
|     - Subtitle: "A unified platform to connect your people, data and operations"  |
|                                                                                   |
|   Right Side Orbital System (290px x 330px SVG canvas):                           |
|     - SVG Curved Paths (Cubic Bezier curve vectors stroke="#60a5fa")              |
|     - Center Core: Frosted Glass 1E Card (108px x 108px, cyan/sky glow, 1E text)  |
|     - Node 1: "People / Together" card with user group icon (top-right)           |
|     - Node 2: "Process / Simpler" card with stacked layers icon (bottom-left)     |
|     - Node 3: "Progress / Faster" card with bar chart icon (bottom-right)         |
+-----------------------------------------------------------------------------------+
| 4. BOTTOM TABS & COMPLIANCE FOOTER (Z-20)                                         |
|   - Interactive tab triggers: [Secure] [Scalable] [Future-Ready]                  |
|     (Active tab gets 2.5px blue indicator pill bar)                               |
|   - Slogan: "BUILT FOR A BRIGHTER TOMORROW"                                       |
|   - Security Badges: SOC 2 Type II · ISO 27001 · 99.95% uptime SLA                |
+-----------------------------------------------------------------------------------+
  </div>
</div>

<!-- ========================================== -->
<!-- CHAPTER 19: RIGHT-SIDE FORM CONTAINER      -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">19</span> Right Panel: Dynamic Form Container</h1>

  <h2>19.1 Layout & Sizing Standards</h2>
  <p>
    The right panel inside <code>src/components/AuthLayout.tsx</code> is configured with:
  </p>
  <pre><code>&lt;<span class="typ">main</span> <span class="prop">className</span>=<span class="str">"w-full lg:w-1/2 h-full overflow-y-auto overflow-x-hidden no-scrollbar flex flex-col items-center justify-start bg-white"</span>&gt;
  &lt;<span class="typ">Outlet</span> /&gt;
&lt;/<span class="typ">main</span>&gt;</code></pre>

  <h2>19.2 The StepProgress Indicator Standard</h2>
  <p>
    Every onboarding screen renders the <code>&lt;StepProgress /&gt;</code> bar at the top of the form. The bar has a fixed maximum width of <code>560px</code> and height of <code>4px</code>, split into 3 segments separated by <code>6px</code> gaps.
  </p>
  <ul>
    <li><strong>Completed Segments:</strong> Render with <code>bg-gradient-to-r from-[#76a4f0] to-[#8781f0]</code>.</li>
    <li><strong>Active Current Segment:</strong> Renders with solid midnight navy <code>bg-[#0e1333]</code>.</li>
    <li><strong>Upcoming Inactive Segments:</strong> Render with soft light gray <code>bg-[#e7eaee]</code>.</li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 20: ASSET PIPELINE                 -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">20</span> Asset Catalog & Media Pipeline</h1>

  <h2>20.1 Media Catalog Table</h2>
  <table>
    <thead>
      <tr>
        <th>Asset Filename</th>
        <th>Location</th>
        <th>Format</th>
        <th>How it is Used</th>
        <th>Visual Role</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>mountains.png</code></td>
        <td><code>public/</code></td>
        <td>PNG Image</td>
        <td>CSS background in <code>VisualBrandingPanel.tsx</code> via <code>url('/mountains.png')</code></td>
        <td>Full-bleed cinematic mountain range backdrop for the entire left panel.</td>
      </tr>
      <tr>
        <td><code>stackly-logo.png</code></td>
        <td><code>public/</code></td>
        <td>PNG Image</td>
        <td>HTML <code>&lt;img&gt;</code> tag in <code>VisualBrandingPanel.tsx</code></td>
        <td>Primary corporate header logo.</td>
      </tr>
      <tr>
        <td><code>stackly-logoo.png</code></td>
        <td><code>public/</code></td>
        <td>PNG Image</td>
        <td>Public static asset</td>
        <td>High-resolution brand logo asset variant.</td>
      </tr>
      <tr>
        <td><code>hero.png</code></td>
        <td><code>src/assets/</code></td>
        <td>PNG Image</td>
        <td>Vite bundled asset</td>
        <td>Alternative graphic illustration asset.</td>
      </tr>
      <tr>
        <td><code>favicon.svg</code></td>
        <td><code>public/</code></td>
        <td>SVG Vector</td>
        <td>Linked in <code>index.html</code> (<code>&lt;link rel="icon"&gt;</code>)</td>
        <td>Browser tab identity icon.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ========================================== -->
<!-- CHAPTER 21: CROSS-PAGE DATA FLOW           -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">21</span> End-to-End Cross-Page Data Flow</h1>

  <h2>21.1 Tracing Data Movement Through the Pipeline</h2>
  <p>
    A critical concept to explain to an engineering manager is how data moves between distinct page routes without getting wiped out:
  </p>

  <div class="diagram-box">
[Screen 1: /signin]
  User enters workspace: "acmecorp" and email: "you@acmecorp.com"
  Click "Continue"
  Calls: updateOrganization({ organizationCode: "ACMECORP" })
    │
    ▼ React Context (OnboardingContext) stores organizationCode = "ACMECORP"
[Screen 2: /organization]
  Component mounts. Reads organizationCode from Context.
  User fills Organization Name: "Acme Corporation"
  Auto-slug generates code, or user keeps "ACMECORP".
  User fills Industry, Country ("United States"), State ("California"), City ("San Francisco").
  User uploads Logo ("acme-logo.png").
  Click "Continue"
  Calls: updateOrganization({ organizationName, organizationCode, industry, country, state, city, ... })
    │
    ▼ React Context updates entire organization object in memory
[Screen 3: /admin]
  Component mounts.
  Reads organizationName: "Acme Corporation" -> dynamically injects into headline!
  User enters First Name ("Ananya"), Last Name ("Rao"), Email ("ananya@acmecorp.com"), Password.
  Click "Continue"
  Calls: updateAdmin({ firstName, lastName, officialEmail, mobileNumber, username, password })
    │
    ▼ React Context updates admin object in memory
[Screen 4: /review]
  Component mounts.
  Reads organization.organizationName -> displays in confirmation authorization text!
  User checks 3 mandatory legal agreements.
  Click "Create account"
    │
    ▼ Final step reached
[Screen 5: /welcome]
  Component mounts.
  Reads organization.organizationCode ("ACMECORP") -> computes "acmecorp.oneenterprise.io".
  Reads admin.officialEmail ("ananya@acmecorp.com") -> displays verification notice!
  User clicks "Go to sign in" -> Returns to /signin.
  </div>
</div>

<!-- ========================================== -->
<!-- CHAPTER 22: MODULE INTERCONNECTION         -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">22</span> Module Interconnection & Dependency Graph</h1>

  <h2>22.1 How Modules Connect Across the Codebase</h2>
  <div class="diagram-box">
                                     [main.tsx]
                                          │
                                          ▼
                                      [App.tsx]
                     ┌────────────────────┴────────────────────┐
                     ▼                                         ▼
            [OnboardingContext]                          [AuthLayout]
                     │                                         │
                     │ provides data via useOnboarding()       ├─────────────────────────┐
                     │                                         ▼                         ▼
                     │                             [VisualBrandingPanel]              [Outlet]
                     │                                                                   │
                     ├───────────────────┬───────────────────┬───────────────────────────┤
                     ▼                   ▼                   ▼                           ▼
               [SignInPage]     [OrganizationForm]    [AdminAccountPage]          [ReviewConfirm]
                     │                   │                   │                           │
                     │                   ├── [FormField] ────┤                           │
                     │                   ├── [FileUpload]    └── [MUI Icons]             └── [AgreementCheckbox]
                     └── [SocialButtons] └── [StepProgress]
  </div>
</div>

<!-- ========================================== -->
<!-- CHAPTER 23: COMPLETE USER JOURNEY          -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">23</span> End-to-End User Flow & Screen Transitions</h1>

  <h2>23.1 The 6-Stage User Journey</h2>
  <ol style="margin-left: 20px; line-height: 1.8;">
    <li><strong>Stage 1: Tenant Discovery (<code>/signin</code>)</strong> — User opens the app. Enters workspace name and work email. If new, clicks 'Create an account'.</li>
    <li><strong>Stage 2: Workspace Setup (<code>/organization</code>)</strong> — User completes the company profile. Slug is auto-generated in real time. Regional states populate dynamically based on country selection.</li>
    <li><strong>Stage 3: Privilege Elevation (<code>/admin</code>)</strong> — User establishes the root Super Administrator. Strict password complexity rules (length, number, symbol) are enforced before proceeding.</li>
    <li><strong>Stage 4: Compliance Attestation (<code>/review</code>)</strong> — User reviews all obligations, binds their organization, and accepts terms of service and DPA.</li>
    <li><strong>Stage 5: Activation & Provisioning (<code>/welcome</code>)</strong> — User views their assigned workspace subdomain and receives instructions to verify their email.</li>
    <li><strong>Stage 6: Day-One Sign-In (<code>/login</code> & <code>/2fa</code>)</strong> — Returning administrator signs in with password, passes two-factor authenticator verification, and lands on <code>/success</code>.</li>
  </ol>
</div>
"""
