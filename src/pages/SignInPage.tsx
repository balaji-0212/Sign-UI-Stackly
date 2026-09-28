import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { PrimaryButton } from '../components/auth/PrimaryButton';
import { DividerText } from '../components/auth/DividerText';
import { SocialLoginButton } from '../components/auth/SocialLoginButton';
import { FormField } from '../components/auth/FormField';
import { validateEmail, validateWorkspace } from '../utils/validation';
import { useOnboarding } from '../context/useOnboarding';

/**
 * Sign In Page (/signin)
 * Matches exact visual UI specification from Sigin UI project.
 */
export const SignInPage: React.FC = () => {
  const navigate = useNavigate();
  const { updateOrganization } = useOnboarding();

  const [workspace, setWorkspace] = useState('');
  const [email, setEmail] = useState('');
  const [errors, setErrors] = useState<{ workspace?: string; email?: string }>({});
  const [touched, setTouched] = useState<{ workspace?: boolean; email?: boolean }>({});
  const [showFindModal, setShowFindModal] = useState(false);

  useEffect(() => {
    if (typeof window === 'undefined') return;

    const isCompletedToSignIn = sessionStorage.getItem('flow_status') === 'completed_to_signin';
    if (!isCompletedToSignIn) return;

    // Establish /signin as boundary: push an entry so popstate can intercept browser Back
    window.history.pushState({ boundary: 'signin' }, '', window.location.href);

    const handlePopState = () => {
      if (sessionStorage.getItem('flow_status') === 'completed_to_signin') {
        window.history.pushState({ boundary: 'signin' }, '', window.location.href);
      }
    };

    window.addEventListener('popstate', handlePopState);
    return () => {
      window.removeEventListener('popstate', handlePopState);
    };
  }, []);

  const handleWorkspaceChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value.slice(0, 50);
    setWorkspace(val);
    if (touched.workspace) {
      setErrors((prev) => ({ ...prev, workspace: validateWorkspace(val) }));
    }
  };

  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value.slice(0, 100);
    setEmail(val);
    if (touched.email) {
      setErrors((prev) => ({ ...prev, email: validateEmail(val, 'Work email') }));
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setTouched({ workspace: true, email: true });

    const wsError = validateWorkspace(workspace);
    const emailError = validateEmail(email, 'Work email');

    setErrors({
      workspace: wsError,
      email: emailError,
    });

    if (!wsError && !emailError) {
      sessionStorage.removeItem('flow_status');
      sessionStorage.removeItem('onboarding_completed');
      updateOrganization({ organizationCode: workspace.toUpperCase() });
      navigate('/organization');
    }
  };

  return (
    <div className="w-full min-w-0 flex-1 flex flex-col items-center justify-start pt-10 sm:pt-[90px] lg:pt-[146px] [@media(max-height:850px)]:lg:pt-[70px] pb-6 lg:pb-0 px-4 sm:px-6">
      <div className="w-full min-w-0 max-w-[456px] flex flex-col">
        {/* Top Identifier */}
        <div className="text-[10.5px] font-mono font-medium tracking-[0.14em] text-[#7c828e] uppercase mb-[15px] leading-none select-none">
          STEP 1 OF 3 · IDENTIFY
        </div>

        {/* Heading */}
        <h1 className="text-[24px] font-bold text-[#14171f] tracking-[-0.02em] leading-none mb-[12px]">
          Sign in
        </h1>

        {/* Description */}
        <p className="text-[14px] text-[#6b7280] leading-[18px] mb-[33px]">
          Enter your workspace and work email to continue.
        </p>

        {/* Form */}
        <form onSubmit={handleSubmit} noValidate className="w-full min-w-0 flex flex-col">
          {/* Split Workspace Input */}
          <div className="flex flex-col w-full min-w-0">
            <label
              htmlFor="workspace-input"
              className="text-[13px] font-medium text-[#14171f] mb-[5px] select-none flex items-center gap-[3px]"
            >
              <span>Workspace</span>
              <span className="text-[#e11d48] font-semibold" aria-hidden="true">
                *
              </span>
            </label>
            <div
              className={`flex items-center w-full min-w-0 h-[44px] rounded-[8px] border bg-white overflow-hidden transition-colors duration-150 ${
                errors.workspace && touched.workspace
                  ? 'border-red-400 focus-within:border-red-500 focus-within:ring-1 focus-within:ring-red-500/20'
                  : 'border-[#e5e7eb] focus-within:border-[#6378ff] focus-within:ring-1 focus-within:ring-[#6378ff]/20'
              }`}
            >
              <input
                id="workspace-input"
                type="text"
                value={workspace}
                maxLength={50}
                onChange={handleWorkspaceChange}
                onBlur={() => {
                  setTouched((prev) => ({ ...prev, workspace: true }));
                  setErrors((prev) => ({ ...prev, workspace: validateWorkspace(workspace) }));
                }}
                placeholder="Enter Your Workspace"
                className="flex-1 min-w-0 h-full pl-[14px] pr-2 text-[14px] text-[#14171f] placeholder-[#a6abbb] bg-white focus:outline-none"
                autoComplete="organization"
              />
              <div className="h-full px-2.5 sm:px-0 sm:w-[157px] shrink-0 bg-[#f4f5f7] border-l border-[#e5e7eb] flex items-center justify-center text-[13px] text-[#64748b] select-none font-mono">
                .oneenterprise.io
              </div>
            </div>
            {errors.workspace && touched.workspace ? (
              <p className="text-[12px] text-red-500 mt-[4px] pl-[1px]" role="alert">
                {errors.workspace}
              </p>
            ) : null}

            {/* Find workspace helper link */}
            <div className="text-[12.5px] text-[#6b7280] mt-[5px]">
              Don't know your workspace?{' '}
              <button
                type="button"
                onClick={() => setShowFindModal(!showFindModal)}
                className="text-[#232a5c] font-medium hover:underline cursor-pointer focus:outline-none"
              >
                Find it here
              </button>
            </div>

            {/* Find workspace info modal / banner */}
            {showFindModal && (
              <div className="mt-2 p-3 bg-blue-50 border border-blue-200 rounded-lg text-[12px] text-blue-900 flex justify-between items-start">
                <span>
                  Your workspace is usually your company domain name (e.g. <strong>acmecorp</strong> from acmecorp.com). Check your team invitation email for details.
                </span>
                <button
                  type="button"
                  onClick={() => setShowFindModal(false)}
                  className="ml-2 font-bold text-blue-600 hover:text-blue-800"
                >
                  ✕
                </button>
              </div>
            )}
          </div>

          {/* Work Email */}
          <div className="mt-[13px] w-full min-w-0">
            <FormField
              id="work-email"
              label="Work email"
              required
              type="email"
              inputClassName="h-[44px]"
              labelClassName="mb-[5px]"
              maxLength={100}
              value={email}
              onChange={handleEmailChange}
              onBlur={() => {
                setTouched((prev) => ({ ...prev, email: true }));
                setErrors((prev) => ({
                  ...prev,
                  email: validateEmail(email, 'Work email'),
                }));
              }}
              placeholder="Enter Your Work Email"
              error={touched.email ? errors.email : ''}
              autoComplete="email"
            />
          </div>

          {/* Continue Button */}
          <div className="mt-[16px] w-full min-w-0">
            <PrimaryButton type="submit" heightClass="h-[44px]">
              Continue
            </PrimaryButton>
          </div>
        </form>

        {/* Social Divider */}
        <DividerText text="or continue with" className="mt-[21px] mb-[17px]" />

        {/* Social SSO Buttons */}
        <div className="flex flex-col gap-[6px] w-full min-w-0">
          <SocialLoginButton
            provider="google"
            onClick={() => {}}
          />
          <SocialLoginButton
            provider="microsoft"
            onClick={() => {}}
          />
          <SocialLoginButton
            provider="sso"
            onClick={() => {}}
          />
        </div>

        {/* Bottom Divider Line */}
        <div id="signin-bottom-divider" className="w-full border-t border-[#e5e7eb] mt-[26px]" />

        {/* Bottom Switch Link */}
        <div className="text-center text-[13px] text-[#6b7280] mt-[22px] leading-none">
          <span>New to One Enterprise? </span>
          <button
            type="button"
            onClick={() => {
              sessionStorage.removeItem('flow_status');
              sessionStorage.removeItem('onboarding_completed');
              navigate('/organization');
            }}
            className="text-[#232a5c] font-semibold hover:underline cursor-pointer focus:outline-none"
          >
            Create an account
          </button>
        </div>
      </div>
    </div>
  );
};
