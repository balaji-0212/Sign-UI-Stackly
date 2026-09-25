import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { OnboardingProvider } from './context/OnboardingContext';
import { AuthLayout } from './components/AuthLayout';
import { SignInPage } from './pages/SignInPage';
import { OrganizationDetailsPage } from './pages/OrganizationDetailsPage';
import { AdminAccountPage } from './pages/AdminAccountPage';
import { ReviewConfirm } from './pages/ReviewConfirm';
import { Welcome } from './pages/Welcome';
import { EnterPassword } from './pages/EnterPassword';
import { TwoFactor } from './pages/TwoFactor';
import { ForgotPassword } from './pages/ForgotPassword';
import { CheckEmail } from './pages/CheckEmail';
import { AccountLocked } from './pages/AccountLocked';
import { Success } from './pages/Success';

/**
 * Centered container for secondary authentication screens to preserve
 * the friend's original max-w-md centered layout.
 */
const CenteredAuthWrapper: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div className="w-full min-w-0 flex-1 flex flex-col justify-center items-center p-8 lg:p-16">
    <div className="w-full max-w-md">
      {children}
    </div>
  </div>
);

/**
 * Route guard for completed onboarding pages (/organization, /admin, /review)
 * - If onboarding is completed and user is on /welcome, keeps them from going back to onboarding.
 * - If user clicked 'Go to sign in' (flow_status === 'completed_to_signin'), prevents going back
 *   into the completed onboarding flow and redirects to /signin.
 */
const OnboardingFlowGuard: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const isCompleted = typeof window !== 'undefined' && sessionStorage.getItem('onboarding_completed') === 'true';
  const isCompletedToSignIn = typeof window !== 'undefined' && sessionStorage.getItem('flow_status') === 'completed_to_signin';
  if (isCompleted) {
    return <Navigate to="/welcome" replace />;
  }
  if (isCompletedToSignIn) {
    return <Navigate to="/signin" replace />;
  }
  return <>{children}</>;
};

/**
 * Route guard for /signin
 * - If onboarding is completed and user hasn't yet clicked 'Go to sign in', redirects to /welcome.
 */
const SignInGuard: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const isCompleted = typeof window !== 'undefined' && sessionStorage.getItem('onboarding_completed') === 'true';
  if (isCompleted) {
    return <Navigate to="/welcome" replace />;
  }
  return <>{children}</>;
};

function App() {
  return (
    <Router>
      <OnboardingProvider>
        <Routes>
          {/* Root redirects to /signin */}
          <Route path="/" element={<Navigate to="/signin" replace />} />

          {/* All auth and onboarding pages share the 50/50 AuthLayout */}
          <Route element={<AuthLayout />}>
            {/* Step 1: Sign In route from working project */}
            <Route path="/signin" element={<SignInGuard><SignInPage /></SignInGuard>} />

            {/* Steps 2 & 3: Organization onboarding routes */}
            <Route path="/organization" element={<OnboardingFlowGuard><OrganizationDetailsPage /></OnboardingFlowGuard>} />
            <Route path="/organization/details" element={<OnboardingFlowGuard><OrganizationDetailsPage /></OnboardingFlowGuard>} />

            {/* Step 4: Create Admin Account route from teammate project */}
            <Route path="/admin" element={<OnboardingFlowGuard><AdminAccountPage /></OnboardingFlowGuard>} />
            <Route path="/create-admin" element={<OnboardingFlowGuard><AdminAccountPage /></OnboardingFlowGuard>} />

            {/* Step 5: Review and Confirm route */}
            <Route path="/review" element={<OnboardingFlowGuard><ReviewConfirm /></OnboardingFlowGuard>} />
            <Route path="/review-confirm" element={<OnboardingFlowGuard><ReviewConfirm /></OnboardingFlowGuard>} />

            {/* Step 6: Welcome to One Enterprise route */}
            <Route path="/welcome" element={<Welcome />} />

            {/* Preserved secondary auth routes from base project */}
            <Route path="/login" element={<CenteredAuthWrapper><EnterPassword /></CenteredAuthWrapper>} />
            <Route path="/2fa" element={<CenteredAuthWrapper><TwoFactor /></CenteredAuthWrapper>} />
            <Route path="/forgot-password" element={<CenteredAuthWrapper><ForgotPassword /></CenteredAuthWrapper>} />
            <Route path="/check-email" element={<CenteredAuthWrapper><CheckEmail /></CenteredAuthWrapper>} />
            <Route path="/locked" element={<CenteredAuthWrapper><AccountLocked /></CenteredAuthWrapper>} />
            <Route path="/success" element={<CenteredAuthWrapper><Success /></CenteredAuthWrapper>} />
          </Route>

          {/* Fallback route */}
          <Route path="*" element={<Navigate to="/signin" replace />} />
        </Routes>
      </OnboardingProvider>
    </Router>
  );
}

export default App;