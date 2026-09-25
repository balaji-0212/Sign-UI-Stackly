import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { StepProgress } from '../components/auth/StepProgress';
import { AgreementCheckbox } from '../components/auth/AgreementCheckbox';
import { useOnboarding } from '../context/useOnboarding';

export interface ReviewConfirmProps {
  onCreateAccount?: () => void;
}

/**
 * Screen 5: Review and Confirm (/review or /review-confirm)
 * Matches exact UI specification from Sign In Page-4.png.
 */
export const ReviewConfirm: React.FC<ReviewConfirmProps> = ({ onCreateAccount }) => {
  const navigate = useNavigate();
  const { organization } = useOnboarding();

  const [termsAccepted, setTermsAccepted] = useState(false);
  const [authorizationAccepted, setAuthorizationAccepted] = useState(false);
  const [dataProcessingAccepted, setDataProcessingAccepted] = useState(false);
  const [updatesAccepted, setUpdatesAccepted] = useState(true);

  useEffect(() => {
    const mainEl = document.querySelector('main');
    if (mainEl) {
      mainEl.scrollTop = 0;
    }
    window.scrollTo(0, 0);
  }, []);

  const canCreateAccount = termsAccepted && authorizationAccepted && dataProcessingAccepted;

  const handleCreateAccount = () => {
    if (!canCreateAccount) return;
    sessionStorage.removeItem('flow_status');
    sessionStorage.setItem('onboarding_completed', 'true');
    if (onCreateAccount) {
      onCreateAccount();
    } else {
      navigate('/welcome', { replace: true });
    }
  };

  const organizationName = organization.organizationName?.trim() || '';

  return (
    <div className="w-full min-w-0 flex-1 flex flex-col items-center justify-start pt-8 sm:pt-[60px] lg:pt-[107px] pb-[80px] px-4 sm:px-6">
      <div className="w-full min-w-0 max-w-[560px] flex flex-col">
        {/* Back Button */}
        <button
          type="button"
          onClick={() => navigate('/admin')}
          className="inline-flex items-center gap-1 text-[13px] font-medium text-[#6b7280] hover:text-[#374151] transition-colors cursor-pointer group mb-[16px] w-fit"
        >
          <span className="text-[15px] leading-none">‹</span>
          <span>Back</span>
        </button>

        {/* Step Progress (Step 3 active) */}
        <StepProgress currentStep={3} totalSteps={3} />

        {/* Step Indicator */}
        <div className="text-[10.5px] font-mono font-medium tracking-[0.14em] text-[#7c828e] uppercase mt-[20px] mb-[10px] leading-none select-none">
          STEP 3 OF 3 · TERMS & AUTHORIZATION
        </div>

        {/* Headline */}
        <h1 className="text-[24px] font-bold tracking-[-0.02em] leading-tight text-[#14171f] mb-[10px]">
          Review and confirm
        </h1>

        {/* Subtitle */}
        <p className="text-[14px] text-[#64748b] leading-[20px] mb-[28px]">
          One last step before we create{' '}
          {organizationName ? (
            <>
              <strong className="font-semibold">{organizationName}&apos;s</strong>{' '}
            </>
          ) : (
            'your '
          )}
          workspace.
        </p>

        {/* Agreements Card */}
        <div className="rounded-[10px] border border-[#e1e5ec] bg-[#fbfcfe] px-5 py-4 mb-[24px]">
          <div className="space-y-4">
            <AgreementCheckbox checked={termsAccepted} onChange={setTermsAccepted}>
              I have read and agree to the{' '}
              <span className="font-semibold text-[#2563eb] hover:underline cursor-pointer">
                Terms of Service
              </span>{' '}
              and{' '}
              <span className="font-semibold text-[#2563eb] hover:underline cursor-pointer">
                Privacy Policy
              </span>
              .
            </AgreementCheckbox>

            <AgreementCheckbox
              checked={authorizationAccepted}
              onChange={setAuthorizationAccepted}
            >
              I confirm that I am authorized to register{' '}
              {organizationName ? (
                <strong className="font-semibold">{organizationName}</strong>
              ) : (
                'the organization'
              )}{' '}
              on One Enterprise, and I accept responsibility as its Super Administrator.
            </AgreementCheckbox>

            <AgreementCheckbox
              checked={dataProcessingAccepted}
              onChange={setDataProcessingAccepted}
            >
              I agree to the{' '}
              <span className="font-semibold text-[#2563eb] hover:underline cursor-pointer">
                Data Processing Agreement
              </span>{' '}
              governing how organization data is stored and processed.
            </AgreementCheckbox>

            <AgreementCheckbox
              checked={updatesAccepted}
              onChange={setUpdatesAccepted}
              optional
            >
              Send me product updates and security notices by email
            </AgreementCheckbox>
          </div>
        </div>

        {/* Create Account Button */}
        <button
          type="button"
          disabled={!canCreateAccount}
          onClick={handleCreateAccount}
          className={`w-full h-[48px] rounded-[8px] text-[14px] font-medium transition-colors shadow-[0_1px_2px_rgba(0,0,0,0.05)] ${
            canCreateAccount
              ? 'bg-[#0f1330] hover:bg-[#18204a] text-white cursor-pointer'
              : 'bg-[#e9edf5] text-[#98a2b3] cursor-not-allowed'
          }`}
        >
          Create account
        </button>

        {/* Bottom Divider Line */}
        <div className="w-full border-t border-[#ecedf0] mt-[26px]" />

        {/* Bottom Sign In Link */}
        <div className="text-center text-[13px] text-[#6b7280] mt-[20px] leading-none w-full min-w-0">
          <span>Already have an organization? </span>
          <button
            type="button"
            onClick={() => navigate('/signin')}
            className="text-[#2563eb] font-medium hover:underline cursor-pointer focus:outline-none"
          >
            Sign in
          </button>
        </div>
      </div>
    </div>
  );
};

export default ReviewConfirm;
