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
            <Route path="/signin" element={<SignInPage />} />

            {/* Steps 2 & 3: Organization onboarding routes */}
            <Route path="/organization" element={<OrganizationDetailsPage />} />
            <Route path="/organization/details" element={<OrganizationDetailsPage />} />

            {/* Step 4: Create Admin Account route from teammate project */}
            <Route path="/admin" element={<AdminAccountPage />} />
            <Route path="/create-admin" element={<AdminAccountPage />} />

            {/* Step 5: Review and Confirm route */}
            <Route path="/review" element={<ReviewConfirm />} />
            <Route path="/review-confirm" element={<ReviewConfirm />} />

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