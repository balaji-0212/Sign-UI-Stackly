import React, { useState, useEffect } from 'react';
import { useNavigate, Navigate } from 'react-router-dom';
import { useOnboarding } from '../context/useOnboarding';

export interface WelcomeProps {
  onSignIn?: () => void;
}

/**
 * Screen 6: Welcome to One Enterprise (/welcome)
 * Matches exact UI specification from Sign In Page-5.png.
 */
export const Welcome: React.FC<WelcomeProps> = ({ onSignIn }) => {
  const navigate = useNavigate();
  const { organization, admin } = useOnboarding();
  const [resent, setResent] = useState(false);

  // If user completed flow and transitioned to sign in, do not allow returning to /welcome
  if (typeof window !== 'undefined' && sessionStorage.getItem('flow_status') === 'completed_to_signin') {
    return <Navigate to="/signin" replace />;
  }

  useEffect(() => {
    const mainEl = document.querySelector('main');
    if (mainEl) {
      mainEl.scrollTop = 0;
    }
    window.scrollTo(0, 0);

    // Ensure onboarding is marked completed while on welcome page
    sessionStorage.setItem('onboarding_completed', 'true');

    const handlePopState = () => {
      // Keep the user on /welcome when Back/Forward is clicked while on /welcome
      window.history.pushState(null, '', window.location.href);
    };

    window.addEventListener('popstate', handlePopState);

    return () => {
      window.removeEventListener('popstate', handlePopState);
    };
  }, []);

  const handleSignIn = () => {
    // Establish /signin as the new boundary and replace /welcome from history
    sessionStorage.removeItem('onboarding_completed');
    sessionStorage.setItem('flow_status', 'completed_to_signin');
    if (onSignIn) {
      onSignIn();
    } else {
      navigate('/signin', { replace: true });
    }
  };

  const handleResend = () => {
    setResent(true);
    setTimeout(() => setResent(false), 4000);
  };

  const organizationName = organization.organizationName?.trim() || '';
  const rawCode = organization.organizationCode?.trim() || '';
  const workspaceDomain = rawCode
    ? rawCode.toLowerCase().replace(/[^a-z0-9-]/g, '') + '.oneenterprise.io'
    : 'your-workspace.oneenterprise.io';

  return (
    <div className="w-full min-w-0 flex-1 flex flex-col items-center justify-center pt-8 sm:pt-[40px] lg:pt-[100px] pb-[80px] px-4 sm:px-6">
      <div className="w-full min-w-0 max-w-[520px] flex flex-col items-center text-center">
        {/* Success Check Icon Badge */}
        <div className="flex h-[60px] w-[60px] items-center justify-center rounded-full bg-[#e9f8ef] mb-[28px]">
          <svg
            className="w-7 h-7 text-[#2ca35c]"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            aria-hidden="true"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M5 13l4 4L19 7" />
          </svg>
        </div>

        {/* Heading */}
        <h1 className="text-[26px] font-bold tracking-[-0.02em] text-[#14171f] mb-[12px]">
          Welcome to One Enterprise
        </h1>

        {/* Description */}
        <p className="text-[14.5px] leading-[22px] text-[#6b7280] max-w-[480px] mb-[36px]">
          {organizationName ? (
            <span className="font-medium text-[#4b5563]">{organizationName}</span>
          ) : (
            'Your organization'
          )}{' '}
          is ready. Your Super Admin account has been created — verify your email to activate full access.
        </p>

        {/* Verification Info Card */}
        <div className="w-full flex items-center gap-3.5 rounded-[10px] border border-[#d7e1ff] bg-[#f0f4ff] px-4 py-3.5 text-left mb-[24px]">
          <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-[8px] bg-white shadow-[0_1px_2px_rgba(0,0,0,0.04)]">
            <span className="text-[18px] text-[#2563eb]" aria-hidden="true">
              ✉
            </span>
          </div>

          <p className="text-[13px] leading-[1.5] text-[#3b4a6b]">
            We&apos;ve sent a verification link to your official email. Your
            <br />
            workspace:{' '}
            <span className="font-mono font-medium text-[#3b4a6b]">{workspaceDomain}</span>
          </p>
        </div>

        {/* Go to Sign In Button */}
        <button
          type="button"
          onClick={handleSignIn}
          className="w-full h-[48px] rounded-[8px] bg-[#0f1330] hover:bg-[#18204a] text-white text-[14px] font-medium transition-colors cursor-pointer shadow-[0_1px_2px_rgba(0,0,0,0.05)]"
        >
          Go to sign in
        </button>

        {/* Bottom Divider Line */}
        <div className="w-full border-t border-[#ecedf0] mt-[24px]" />

        {/* Resend Link */}
        <p className="text-[13px] text-[#6b7280] mt-[20px] leading-none">
          Didn&apos;t get the email?{' '}
          <button
            type="button"
            onClick={handleResend}
            className="text-[#2563eb] font-semibold hover:underline cursor-pointer focus:outline-none"
          >
            Resend verification
          </button>
        </p>

        {resent && (
          <p className="text-[12.5px] text-emerald-600 font-medium mt-3" role="status">
            ✓ Verification email resent to {admin.officialEmail || 'your email'}!
          </p>
        )}
      </div>
    </div>
  );
};

export default Welcome;
