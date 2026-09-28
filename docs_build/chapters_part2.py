# -*- coding: utf-8 -*-
"""
Part 2 of the Guide:
- Chapter 7: Page-by-Page Deep Dive (All 11 Pages in Full Detail)
- Chapter 8: Complete Component Architecture & Hierarchy
- Chapter 9: Props Flow & Project Prop Catalog
- Chapter 10: State Management (Context + Local)
- Chapter 11: Form Architecture & Controlled Inputs
- Chapter 12: Form Validation Engine (validation.ts line-by-line)
"""

def get_part2_html():
    return """
<!-- ========================================== -->
<!-- CHAPTER 7: PAGE-BY-PAGE DEEP DIVE          -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">07</span> Page-by-Page Deep Dive (All 11 Pages)</h1>
  <p>
    <code>SignIn-UI-Frontend</code> implements two complete workflows: the <strong>Primary Onboarding Flow</strong> (a 5-step wizard) and the <strong>Secondary Authentication Flow</strong> (a 6-step login & recovery suite).
  </p>

  <h2>7.1 Primary Page 1: Sign In Page (<code>src/pages/SignInPage.tsx</code>)</h2>
  <div class="card" style="margin-bottom: 14px;">
    <div class="card-header">Page Metadata & Routing</div>
    <div class="card-body">
      <strong>Route:</strong> <code>/signin</code> (also redirected from root <code>/</code> and fallback <code>*</code>)<br>
      <strong>Visual Milestone:</strong> <code>STEP 1 OF 3 · IDENTIFY</code><br>
      <strong>Primary Layout Container:</strong> <code>max-w-[456px]</code> with desktop top-padding <code>lg:pt-[146px]</code>
    </div>
  </div>
  <ul>
    <li><strong>Purpose:</strong> Identifies returning enterprise tenants and routes new users into organization registration.</li>
    <li><strong>Components Used:</strong> <code>PrimaryButton</code>, <code>DividerText</code>, <code>SocialLoginButton</code>, <code>FormField</code>.</li>
    <li><strong>State:</strong>
      <ul>
        <li><code>workspace</code> (string, default: <code>'acmecorp'</code>) — Company workspace slug.</li>
        <li><code>email</code> (string, default: <code>''</code>) — Corporate email address.</li>
        <li><code>errors</code> (object: <code>{ workspace?: string; email?: string }</code>) — Validation error strings.</li>
        <li><code>touched</code> (object: <code>{ workspace?: boolean; email?: boolean }</code>) — Dirty tracking flags.</li>
        <li><code>showFindModal</code> (boolean, default: <code>false</code>) — Toggles the inline helper card explaining how to find a workspace.</li>
      </ul>
    </li>
    <li><strong>Special UI Pattern: Split Workspace Input:</strong> The workspace input field joins an editable text input with a fixed right suffix box displaying <code>.oneenterprise.io</code> in a muted mono font. This enforces subdomain mental mapping.</li>
    <li><strong>What Happens on Submit:</strong>
      <ol style="margin-left: 20px;">
        <li>Validates <code>workspace</code> against alphanumeric + hyphen regex.</li>
        <li>Validates <code>email</code> against standard email format.</li>
        <li>If valid, calls <code>updateOrganization({ organizationCode: workspace.toUpperCase() })</code> in Context so the user's workspace choice auto-seeds Step 1!</li>
        <li>Executes <code>navigate('/organization')</code>.</li>
      </ol>
    </li>
  </ul>

  <h2>7.2 Primary Page 2: Organization Details (<code>OrganizationDetailsPage.tsx</code> & <code>OrganizationForm.tsx</code>)</h2>
  <div class="card" style="margin-bottom: 14px;">
    <div class="card-header">Page Metadata & Routing</div>
    <div class="card-body">
      <strong>Route:</strong> <code>/organization</code> and <code>/organization/details</code><br>
      <strong>Visual Milestone:</strong> <code>STEP 1 OF 3 · ORGANIZATION DETAILS</code><br>
      <strong>Primary Layout Container:</strong> <code>max-w-[560px]</code> with top padding <code>lg:pt-[104px]</code>
    </div>
  </div>
  <ul>
    <li><strong>Purpose:</strong> Captures all enterprise organization profile attributes: name, code/slug, type, industry, employee size, country, state, city, time zone, and company logo.</li>
    <li><strong>Components Used:</strong> <code>StepProgress</code> (step 1 active), <code>FormField</code> (text and select variants), <code>FileUpload</code>, <code>PrimaryButton</code>.</li>
    <li><strong>Dependent Dropdowns:</strong> The State/Province dropdown dynamically binds to the selected Country using the internal lookup dictionary <code>statesByCountry</code> (supports India, United States, United Kingdom, Singapore, Germany, Australia). Changing country immediately re-seeds the available state options!</li>
    <li><strong>Slug Auto-Generation:</strong> When typing in "Organization Name" (e.g., "Acme International Systems"), the helper function <code>generateOrgCode()</code> automatically computes "ACME-INTE" in uppercase. Users can click "edit manually" to override it.</li>
    <li><strong>What Happens on Continue:</strong> All form values are submitted to <code>updateOrganization(...)</code> in <code>OnboardingContext</code>, and the browser navigates to <code>/admin</code>.</li>
  </ul>

  <h2>7.3 Primary Page 3: Super Admin Account (<code>src/pages/AdminAccountPage.tsx</code>)</h2>
  <div class="card" style="margin-bottom: 14px;">
    <div class="card-header">Page Metadata & Routing</div>
    <div class="card-body">
      <strong>Route:</strong> <code>/admin</code> and <code>/create-admin</code><br>
      <strong>Visual Milestone:</strong> <code>STEP 2 OF 3 · SUPER ADMIN ACCOUNT</code><br>
      <strong>Notice Banner:</strong> Blue badge explaining automatic assignment of the <code>SUPER_ADMIN</code> role.
    </div>
  </div>
  <ul>
    <li><strong>Purpose:</strong> Configures the initial root administrator credentials: First Name, Last Name, Official Email, Mobile Number, Username, Password, and Confirm Password.</li>
    <li><strong>Dynamic Headline:</strong> "This is the account you'll use to manage <strong>{organizationName}</strong>." (organizationName is reactively retrieved from <code>OnboardingContext</code>).</li>
    <li><strong>Password Visibility Toggles:</strong> Independent boolean states (<code>showPassword</code>, <code>showConfirmPassword</code>) toggle input types between <code>"password"</code> and <code>"text"</code> with MUI icons (<code>VisibilityOutlined</code> / <code>VisibilityOffOutlined</code>).</li>
    <li><strong>Strict Password Validation:</strong> Enforces minimum 8 characters, at least one digit (<code>/[0-9]/</code>), and at least one special symbol. Confirms that password and confirmPassword match.</li>
    <li><strong>What Happens on Continue:</strong> Calls <code>updateAdmin(values)</code> in Context and navigates to <code>/review</code>.</li>
  </ul>

  <h2>7.4 Primary Page 4: Review & Confirm (<code>src/pages/ReviewConfirm.tsx</code>)</h2>
  <div class="card" style="margin-bottom: 14px;">
    <div class="card-header">Page Metadata & Routing</div>
    <div class="card-body">
      <strong>Route:</strong> <code>/review</code> and <code>/review-confirm</code><br>
      <strong>Visual Milestone:</strong> <code>STEP 3 OF 3 · TERMS & AUTHORIZATION</code><br>
      <strong>Action Guard:</strong> 'Create account' button is strictly disabled until 3 mandatory checkboxes are accepted.
    </div>
  </div>
  <ul>
    <li><strong>Purpose:</strong> Legal compliance gateway. Users must review and explicitly accept legal agreements before the tenant workspace is created.</li>
    <li><strong>Agreements Card:</strong> Uses custom <code>AgreementCheckbox</code> components:
      <ol style="margin-left: 20px;">
        <li>Terms of Service & Privacy Policy (Mandatory)</li>
        <li>Confirmation of Authority to bind <code>{organizationName}</code> and accept Super Admin liability (Mandatory)</li>
        <li>Data Processing Agreement (DPA) regarding GDPR/enterprise storage (Mandatory)</li>
        <li>Product updates & security email notices (Optional — marked with uppercase OPTIONAL badge)</li>
      </ol>
    </li>
    <li><strong>Button Enabling Gate:</strong> <code>const canCreateAccount = termsAccepted &amp;&amp; authorizationAccepted &amp;&amp; dataProcessingAccepted;</code></li>
    <li><strong>What Happens on Create Account:</strong> Navigates to <code>/welcome</code>.</li>
  </ul>

  <h2>7.5 Primary Page 5: Welcome / Success (<code>src/pages/Welcome.tsx</code>)</h2>
  <div class="card" style="margin-bottom: 14px;">
    <div class="card-header">Page Metadata & Routing</div>
    <div class="card-body">
      <strong>Route:</strong> <code>/welcome</code><br>
      <strong>Status Indicator:</strong> Circular green badge with emerald checkmark (<code>bg-[#e9f8ef] text-[#2ca35c]</code>).
    </div>
  </div>
  <ul>
    <li><strong>Purpose:</strong> Confirms successful workspace provisioning and notifies the administrator that an activation link has been dispatched to their official email.</li>
    <li><strong>Computed Workspace Domain:</strong> Computes the live tenant URL:
      <pre><code><span class="kw">const</span> rawCode = organization.organizationCode?.trim() || <span class="str">'ABC-TECH'</span>;
<span class="kw">const</span> workspaceDomain = rawCode.toLowerCase().replace(/[^a-z0-9-]/g, <span class="str">''</span>) + <span class="str">'.oneenterprise.io'</span>;</code></pre>
    </li>
    <li><strong>Resend Verification Simulation:</strong> Clicking 'Resend verification' sets <code>resent = true</code>, rendering an emerald status badge: <code>"✓ Verification email resent to {admin.officialEmail}!"</code>, which auto-resets after 4 seconds via <code>setTimeout</code>.</li>
    <li><strong>Return to Sign In:</strong> Clicking 'Go to sign in' navigates to <code>/signin</code>.</li>
  </ul>

  <h2>7.6 Secondary Authentication Flow Pages</h2>
  <table>
    <thead>
      <tr>
        <th>Page File</th>
        <th>Route</th>
        <th>Step Indicator</th>
        <th>Special Technical Features</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>EnterPassword.tsx</code></td>
        <td><code>/login</code></td>
        <td><code>STEP 2 OF 3 · PASSWORD</code></td>
        <td>Demo password check (<code>'password123'</code>), failed attempt counter, triggers automatic lockout navigation to <code>/locked</code> upon 5 failed attempts. Includes remember device checkbox and user switcher card.</td>
      </tr>
      <tr>
        <td><code>TwoFactor.tsx</code></td>
        <td><code>/2fa</code></td>
        <td><code>STEP 3 OF 3 · VERIFY</code></td>
        <td>6 individual input boxes with auto-focus forward advancing via <code>useRef</code> array and backspace backward jump. Expiration timer display. Navigates to <code>/success</code>.</td>
      </tr>
      <tr>
        <td><code>ForgotPassword.tsx</code></td>
        <td><code>/forgot-password</code></td>
        <td><code>PASSWORD RECOVERY</code></td>
        <td>Work email input field with Material UI <code>TextField</code>. Navigates to <code>/check-email</code> upon clicking 'Send reset link'.</td>
      </tr>
      <tr>
        <td><code>CheckEmail.tsx</code></td>
        <td><code>/check-email</code></td>
        <td>Notification View</td>
        <td>Shows mail icon badge, expiration notice (30 minutes), 'Resend email' secondary button, and 'Back to sign in' button.</td>
      </tr>
      <tr>
        <td><code>AccountLocked.tsx</code></td>
        <td><code>/locked</code></td>
        <td>Security Warning</td>
        <td>Red lockout badge, 15-minute countdown card (<code>Try again in 15:00</code>), quick reset password link, audit log notice.</td>
      </tr>
      <tr>
        <td><code>Success.tsx</code></td>
        <td><code>/success</code></td>
        <td>Auth Complete</td>
        <td>Emerald circular checkmark icon with subtitle: "Redirecting to your dashboard...".</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ========================================== -->
<!-- CHAPTER 8: COMPONENT ARCHITECTURE          -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">08</span> Component Architecture & Hierarchy</h1>

  <h2>8.1 Master Component Hierarchy Tree</h2>
  <p>
    The following diagram illustrates how components are nested at runtime:
  </p>

  <div class="diagram-box">
App (App.tsx)
 │
 ├── Router (BrowserRouter)
 │    │
 │    └── OnboardingProvider (OnboardingContext.tsx)
 │         │
 │         └── Routes
 │              │
 │              ├── Route: "/" -> <Navigate to="/signin" />
 │              │
 │              ├── Parent Route: element={<AuthLayout />}
 │              │    │
 │              │    ├── Left: <VisualBrandingPanel /> (Sticky desktop branding stage)
 │              │    │          ├── Stackly Logo
 │              │    │          ├── Headline & Typography
 │              │    │          ├── Orbital Diagram (SVG Curves + 1E Core + People/Process/Progress)
 │              │    │          ├── Interactive Tabs (Secure, Scalable, Future-Ready)
 │              │    │          └── Security Assurances (SOC 2, ISO 27001, 99.95% SLA)
 │              │    │
 │              │    └── Right: <main><Outlet /></main>
 │              │         ├── Route: "/signin"           -> <SignInPage />
 │              │         ├── Route: "/organization"     -> <OrganizationDetailsPage />
 │              │         │                                   └── <OrganizationForm />
 │              │         ├── Route: "/admin"            -> <AdminAccountPage />
 │              │         ├── Route: "/review"           -> <ReviewConfirm />
 │              │         ├── Route: "/welcome"          -> <Welcome />
 │              │         │
 │              │         └── Secondary Routed Views (wrapped in CenteredAuthWrapper):
 │              │              ├── Route: "/login"           -> <EnterPassword />
 │              │              ├── Route: "/2fa"             -> <TwoFactor />
 │              │              ├── Route: "/forgot-password" -> <ForgotPassword />
 │              │              ├── Route: "/check-email"     -> <CheckEmail />
 │              │              ├── Route: "/locked"          -> <AccountLocked />
 │              │              └── Route: "/success"         -> <Success />
 │              │
 │              └── Fallback Route: "*" -> <Navigate to="/signin" />
  </div>

  <h2>8.2 Reusable Atomic Components Breakdown</h2>
  <table>
    <thead>
      <tr>
        <th>Component</th>
        <th>File Path</th>
        <th>Key Props</th>
        <th>Architectural Functionality</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>StepProgress</code></td>
        <td><code>components/auth/StepProgress.tsx</code></td>
        <td><code>currentStep</code>, <code>totalSteps</code>, <code>className</code></td>
        <td>Renders the horizontal 3-segment progress indicator with active navy fill, completed blue gradients, and upcoming gray bars.</td>
      </tr>
      <tr>
        <td><code>FormField</code></td>
        <td><code>components/auth/FormField.tsx</code></td>
        <td><code>id</code>, <code>label</code>, <code>required</code>, <code>error</code>, <code>isSelect</code>, <code>options</code>, <code>value</code>, <code>onChange</code></td>
        <td>Dual-mode form control. If <code>isSelect=true</code>, renders a styled dropdown with custom <code>ChevronDown</code> icon. Otherwise, renders an HTML5 text/email/password input with red validation labels.</td>
      </tr>
      <tr>
        <td><code>FileUpload</code></td>
        <td><code>components/auth/FileUpload.tsx</code></td>
        <td><code>value</code>, <code>previewUrl</code>, <code>onChange</code>, <code>optional</code></td>
        <td>Full drag-and-drop file upload zone with HTML5 file validation (PNG/JPG only, 5MB limit), image preview thumbnail, and remove action.</td>
      </tr>
      <tr>
        <td><code>PrimaryButton</code></td>
        <td><code>components/auth/PrimaryButton.tsx</code></td>
        <td><code>children</code>, <code>heightClass</code>, <code>disabled</code>, <code>type</code></td>
        <td>Standardized dark navy (<code>#0f1330</code>) primary action button with focus rings and disabled styling.</td>
      </tr>
      <tr>
        <td><code>AgreementCheckbox</code></td>
        <td><code>components/auth/AgreementCheckbox.tsx</code></td>
        <td><code>checked</code>, <code>onChange</code>, <code>optional</code>, <code>children</code></td>
        <td>Custom accessible checkbox with keyboard navigation (Space/Enter toggle) and optional metadata tag badge.</td>
      </tr>
      <tr>
        <td><code>SocialLoginButton</code></td>
        <td><code>components/auth/SocialLoginButton.tsx</code></td>
        <td><code>provider</code> ('google'|'microsoft'|'sso'), <code>onClick</code></td>
        <td>Branded SSO button with authentic Google 4-color SVG, Microsoft 4-box SVG, or SAML SSO icon.</td>
      </tr>
      <tr>
        <td><code>DividerText</code></td>
        <td><code>components/auth/DividerText.tsx</code></td>
        <td><code>text</code>, <code>className</code></td>
        <td>Subtle gray divider line with centered background-matched badge text ("or continue with").</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ========================================== -->
<!-- CHAPTER 9: PROPS FLOW                      -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">09</span> Props Flow & Real Project Props Catalog</h1>

  <h2>9.1 Real Component Props in Action</h2>
  <p>
    In React, <strong>props</strong> (short for properties) represent read-only inputs passed from a parent component down to a child component. Props make components reusable and predictable.
  </p>

  <h3>Example 1: StepProgress Props in <code>AdminAccountPage.tsx</code></h3>
  <pre><code><span class="cmt">// In AdminAccountPage.tsx (Line 73):</span>
&lt;<span class="typ">StepProgress</span> <span class="prop">currentStep</span>={2} <span class="prop">totalSteps</span>={3} /&gt;</code></pre>
  <ul>
    <li><strong>Origin:</strong> Hardcoded integer literal <code>2</code> supplied by <code>AdminAccountPage</code> because it represents Step 2 of the onboarding flow.</li>
    <li><strong>Consumer:</strong> <code>StepProgress.tsx</code>.</li>
    <li><strong>Runtime Effect:</strong> <code>StepProgress</code> loops from 1 to 3. Segment 1 (index 0) gets the completed gradient <code>bg-gradient-to-r from-[#76a4f0] to-[#8781f0]</code>; segment 2 (index 1) gets the active solid navy <code>bg-[#0e1333]</code>; segment 3 (index 2) gets the inactive gray <code>bg-[#e7eaee]</code>.</li>
  </ul>

  <h3>Example 2: FormField Polymorphic Props in <code>OrganizationForm.tsx</code></h3>
  <pre><code><span class="cmt">// In OrganizationForm.tsx (Lines 267-283):</span>
&lt;<span class="typ">FormField</span>
  <span class="prop">id</span>=<span class="str">"org-type"</span>
  <span class="prop">label</span>=<span class="str">"Organization Type"</span>
  <span class="prop">required</span>
  <span class="prop">isSelect</span>
  <span class="prop">value</span>={orgType}
  <span class="prop">onChange</span>={(e) =&gt; setOrgType(e.target.value)}
  <span class="prop">options</span>={[
    { value: <span class="str">'Enterprise'</span>, label: <span class="str">'Enterprise'</span> },
    { value: <span class="str">'Mid-Market'</span>, label: <span class="str">'Mid-Market'</span> },
    { value: <span class="str">'Small Business'</span>, label: <span class="str">'Small Business'</span> }
  ]}
/&gt;</code></pre>
  <ul>
    <li><strong>Origin:</strong> State variable <code>orgType</code> and state setter <code>setOrgType</code> owned by <code>OrganizationForm</code>.</li>
    <li><strong>Consumer:</strong> <code>FormField.tsx</code>.</li>
    <li><strong>Runtime Effect:</strong> Because <code>isSelect={true}</code>, <code>FormField</code> renders an HTML <code>&lt;select&gt;</code> rather than an <code>&lt;input&gt;</code>, maps through <code>options</code> to render <code>&lt;option&gt;</code> children, and positions a <code>ChevronDown</code> icon in the right margin.</li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 10: STATE MANAGEMENT               -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">10</span> State Management (Context + Local State)</h1>

  <h2>10.1 Two-Tier State Architecture</h2>
  <p>
    <code>SignIn-UI-Frontend</code> avoids bulky external state libraries (like Redux or Zustand) by using a clean, native <strong>Two-Tier State Architecture</strong>:
  </p>

  <div class="diagram-box">
+-----------------------------------------------------------------------------------------+
| TIER 1: GLOBAL STATE (React Context: OnboardingContext.tsx)                             |
| Scope: Persists across the entire multi-step route lifecycle                            |
|                                                                                         |
| Data Objects:                                                                           |
|   1. organization: OrganizationDetails                                                 |
|      (organizationName, organizationCode, organizationType, industry,                   |
|       companySize, country, state, city, timeZone, organizationLogo)                    |
|   2. admin: AdminAccount                                                                |
|      (firstName, lastName, officialEmail, mobileNumber, username, password)             |
|                                                                                         |
| Updater Methods:                                                                        |
|   - updateOrganization(Partial<OrganizationDetails>)                                    |
|   - updateAdmin(Partial<AdminAccount>)                                                  |
|   - resetOnboarding()                                                                   |
+-----------------------------------------------------------------------------------------+
                                      ▲                      │
                   dispatches updates │                      │ seeds initial values
                                      │                      ▼
+-----------------------------------------------------------------------------------------+
| TIER 2: LOCAL FORM STATE (useState within individual page components)                  |
| Scope: Ephemeral, isolated to active screen                                             |
|                                                                                         |
| Examples:                                                                               |
|   - OrganizationForm: [orgName, setOrgName], [orgCode, setOrgCode], [errors, setErrors] |
|   - AdminAccountPage: [values, setValues], [showPassword, setShowPassword]              |
|   - ReviewConfirm:    [termsAccepted, setTermsAccepted], [canCreateAccount]             |
|   - EnterPassword:    [password, setPassword], [attempts, setAttempts]                  |
|   - TwoFactor:        [otp, setOtp] (6-item array)                                      |
+-----------------------------------------------------------------------------------------+
  </div>

  <h2>10.2 Why This State Pattern is Superior</h2>
  <ul>
    <li><strong>Form Draft Isolation:</strong> When a user types in <code>AdminAccountPage</code>, local keystrokes update local state (<code>values</code>). This prevents unnecessary top-level context re-renders on every single keystroke. Only when the user passes validation and clicks 'Continue' is <code>updateAdmin(values)</code> dispatched to the global context!</li>
    <li><strong>Seamless Back-Navigation:</strong> If a user navigates from Step 2 back to Step 1 (via the 'Back' button), <code>OrganizationForm</code> mounts and reads its initial field values from <code>organization.*</code> in Context. The user never loses previously typed data!</li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 11: FORM ARCHITECTURE              -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">11</span> Form Architecture & Controlled Inputs</h1>

  <h2>11.1 Controlled Inputs Explained</h2>
  <p>
    Every input field in this project is a <strong>Controlled Component</strong>. In React, a controlled component is an input element whose value is driven by React state, not internal DOM state:
  </p>
  <pre><code>&lt;<span class="typ">input</span>
  <span class="prop">id</span>=<span class="str">"org-name"</span>
  <span class="prop">type</span>=<span class="str">"text"</span>
  <span class="prop">value</span>={orgName}                          <span class="cmt">// 1. Single Source of Truth</span>
  <span class="prop">onChange</span>={handleOrgNameChange}           <span class="cmt">// 2. Intercepts Keystrokes</span>
/&gt;</code></pre>
  <p>
    <strong>How it works at runtime:</strong>
    <ol style="margin-left: 20px;">
      <li>User presses key 'A'.</li>
      <li>Browser fires <code>onChange</code> event.</li>
      <li><code>handleOrgNameChange</code> extracts <code>e.target.value</code>.</li>
      <li>Handler calls <code>setOrgName(val)</code>.</li>
      <li>React schedules a re-render.</li>
      <li>React passes the new <code>orgName</code> string to the input's <code>value</code> prop.</li>
      <li>The letter 'A' renders on screen.</li>
    </ol>
  </p>

  <h2>11.2 File Upload & Drag-and-Drop Architecture</h2>
  <p>
    <code>src/components/auth/FileUpload.tsx</code> provides a production-grade file upload pipeline:
  </p>
  <ul>
    <li><strong>Hidden File Input:</strong> A real HTML <code>&lt;input type="file" className="hidden"&gt;</code> is referenced via <code>const inputRef = useRef&lt;HTMLInputElement&gt;(null)</code>.</li>
    <li><strong>Click Delegation:</strong> Clicking the styled dashed container executes <code>inputRef.current?.click()</code>.</li>
    <li><strong>HTML5 Drag Events:</strong> Handles <code>onDragOver</code>, <code>onDragLeave</code>, and <code>onDrop</code> with <code>e.preventDefault()</code> to prevent the browser from opening the image in a new tab.</li>
    <li><strong>Object URL Previews:</strong> When a file is selected, it generates an in-memory blob preview via <code>URL.createObjectURL(file)</code> for immediate thumbnail display.</li>
  </ul>
</div>

<!-- ========================================== -->
<!-- CHAPTER 12: FORM VALIDATION ENGINE         -->
<!-- ========================================== -->
<div class="page-break">
  <h1><span class="chapter-num">12</span> Form Validation Engine (<code>validation.ts</code>)</h1>

  <h2>12.1 The Validation Functions in <code>src/utils/validation.ts</code></h2>
  <p>
    All business validation rules are encapsulated in pure, unit-testable TypeScript functions:
  </p>

  <table>
    <thead>
      <tr>
        <th>Function</th>
        <th>Validation Criteria</th>
        <th>Error Message Returned</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>validateRequired(val, name)</code></td>
        <td>Checks if string is empty or only whitespace (<code>!value || !value.trim()</code>).</td>
        <td><code>"{fieldName} is required"</code></td>
      </tr>
      <tr>
        <td><code>validateEmail(email, name)</code></td>
        <td>1. Checks required.<br>2. Evaluates regex: <code>/^[^\s@]+@[^\s@]+\.[^\s@]+$/</code>.</td>
        <td><code>"Please enter a valid email address"</code></td>
      </tr>
      <tr>
        <td><code>validateWorkspace(slug)</code></td>
        <td>1. Checks required.<br>2. Evaluates regex: <code>/^[a-zA-Z0-9-]+$/</code> (letters, digits, hyphens only).</td>
        <td><code>"Workspace can only contain letters, numbers, and hyphens"</code></td>
      </tr>
      <tr>
        <td><code>validatePassword(pwd)</code></td>
        <td>1. Checks required.<br>2. Length &gt;= 8.<br>3. At least one digit: <code>/[0-9]/</code>.<br>4. At least one symbol: <code>/[!@#$%^&amp;*(),.?":{}|&lt;&gt;]/</code>.</td>
        <td><code>"Password must be at least 8 characters"</code> / <code>"...must include at least one number"</code> / <code>"...one symbol"</code></td>
      </tr>
      <tr>
        <td><code>validateConfirmPassword(p1, p2)</code></td>
        <td>1. Checks confirm required.<br>2. Compares <code>p1 !== p2</code>.</td>
        <td><code>"Passwords do not match"</code></td>
      </tr>
      <tr>
        <td><code>generateOrgCode(name)</code></td>
        <td>Sanitizes special characters, splits into words, takes the first 4 letters of word 1 and first 4 of word 2 with a hyphen. E.g., "Google Cloud" -&gt; "GOOG-CLOU".</td>
        <td>Returns generated slug string.</td>
      </tr>
    </tbody>
  </table>

  <h2>12.2 Real-time "Touched" Dirty Tracking</h2>
  <p>
    To ensure an exceptional user experience, error messages do NOT flash when a user first lands on an empty form. Each field tracks a <code>touched[fieldName]</code> boolean flag. Errors only display after the user leaves the field (<code>onBlur</code>) or attempts to submit the form!
  </p>
</div>
"""
