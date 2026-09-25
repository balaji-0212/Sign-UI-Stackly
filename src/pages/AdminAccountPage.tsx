import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import ShieldOutlinedIcon from '@mui/icons-material/ShieldOutlined';
import VisibilityOutlinedIcon from '@mui/icons-material/VisibilityOutlined';
import VisibilityOffOutlinedIcon from '@mui/icons-material/VisibilityOffOutlined';
import { FormField } from '../components/auth/FormField';
import { PrimaryButton } from '../components/auth/PrimaryButton';
import { StepProgress } from '../components/auth/StepProgress';
import { useOnboarding } from '../context/useOnboarding';
import { validateConfirmPassword, validateEmail, validatePassword, validateRequired } from '../utils/validation';

/**
 * Screen 4: Create Your Admin Account (/admin or /create-admin)
 * Matches exact UI specification from "Sign In Page-2.png".
 * Integrates teammate's exact right-side form functionality while
 * inheriting the locked, pixel-perfect left branding panel from AuthLayout.
 */
export const AdminAccountPage: React.FC = () => {
  const navigate = useNavigate();
  const { admin, organization, updateAdmin } = useOnboarding();
  const [values, setValues] = useState(admin);
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  useEffect(() => {
    const mainEl = document.querySelector('main');
    if (mainEl) {
      mainEl.scrollTop = 0;
    }
    window.scrollTo(0, 0);
  }, []);

  const setField = (field: keyof typeof values, value: string) => {
    setValues((current) => ({ ...current, [field]: value }));
    if (errors[field]) setErrors((current) => ({ ...current, [field]: '' }));
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    const nextErrors = {
      firstName: validateRequired(values.firstName, 'First Name'),
      lastName: validateRequired(values.lastName, 'Last Name'),
      officialEmail: validateEmail(values.officialEmail, 'Official Email'),
      mobileNumber: validateRequired(values.mobileNumber, 'Mobile Number'),
      username: validateRequired(values.username, 'Username'),
      password: validatePassword(values.password),
      confirmPassword: validateConfirmPassword(values.password, values.confirmPassword),
    };
    setErrors(nextErrors);
    if (Object.values(nextErrors).every((message) => !message)) {
      updateAdmin(values);
      navigate('/review');
    }
  };

  const organizationName = organization.organizationName?.trim() || '';

  return (
    <div className="w-full min-w-0 flex-1 flex flex-col items-center justify-start pt-8 sm:pt-[60px] lg:pt-[107px] pb-[80px] px-4 sm:px-6">
      <div className="w-full min-w-0 max-w-[560px] flex flex-col">
        {/* Back Button */}
        <button
          type="button"
          onClick={() => navigate('/organization')}
          className="inline-flex items-center gap-1 text-[13px] font-medium text-[#6b7280] hover:text-[#374151] transition-colors cursor-pointer group mb-[16px] w-fit"
        >
          <span className="text-[15px] leading-none">‹</span>
          <span>Back</span>
        </button>

        {/* Step Progress (Ref Y=142, Step 2 active) */}
        <StepProgress currentStep={2} totalSteps={3} />

        {/* Step Indicator */}
        <div className="text-[10.5px] font-mono font-medium tracking-[0.14em] text-[#7c828e] uppercase mt-[20px] mb-[10px] leading-none select-none">
          STEP 2 OF 3 · SUPER ADMIN ACCOUNT
        </div>

        {/* Headline */}
        <h1 className="text-[24px] font-bold tracking-[-0.02em] leading-[28px] text-[#14171f] mb-[15px]">
          Create your admin account
        </h1>

        {/* Subtitle */}
        <p className="text-[13.5px] text-[#64748b] leading-[18px] mb-[36px]">
          This is the account you&apos;ll use to manage{' '}
          {organizationName ? (
            <strong className="font-semibold text-[#14171f]">{organizationName}</strong>
          ) : (
            'your organization'
          )}
          .
        </p>

        {/* Notice Banner */}
        <div className="flex items-center gap-3 rounded-[10px] border border-[#d8e2ff] bg-[#eef3ff] px-4 py-[14px] text-[13px] leading-[17px] text-[#3c4f77] mb-[26px]">
          <span className="w-8 h-8 shrink-0 flex items-center justify-center rounded-[8px] bg-white text-[#315eea]">
            <ShieldOutlinedIcon sx={{ fontSize: 18 }} />
          </span>
          <span>
            This account will automatically be assigned the <span className="font-mono text-[12px] font-bold">SUPER_ADMIN</span> role, with full access to your organization's workspace.
          </span>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} noValidate className="flex flex-col gap-[20px]">
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-[16px]">
            <FormField
              id="first-name"
              label="First Name"
              required
              value={values.firstName}
              onChange={(event) => setField('firstName', event.target.value)}
              error={errors.firstName}
              placeholder="Enter Your First Name"
              autoComplete="given-name"
            />
            <FormField
              id="last-name"
              label="Last Name"
              required
              value={values.lastName}
              onChange={(event) => setField('lastName', event.target.value)}
              error={errors.lastName}
              placeholder="Enter Your Last Name"
              autoComplete="family-name"
            />
          </div>

          <FormField
            id="official-email"
            label="Official Email"
            required
            type="email"
            value={values.officialEmail}
            onChange={(event) => setField('officialEmail', event.target.value)}
            error={errors.officialEmail}
            placeholder="Enter Your Official Email"
            autoComplete="email"
          />

          <FormField
            id="mobile-number"
            label="Mobile Number"
            required
            value={values.mobileNumber}
            onChange={(event) => setField('mobileNumber', event.target.value)}
            error={errors.mobileNumber}
            placeholder="Enter Your Mobile Number"
            autoComplete="tel"
          />

          <FormField
            id="username"
            label="Username"
            required
            value={values.username}
            onChange={(event) => setField('username', event.target.value)}
            error={errors.username}
            placeholder="Enter Your Username"
            autoComplete="username"
          />

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-[16px]">
            <div className="relative">
              <FormField
                id="password"
                label="Password"
                required
                type={showPassword ? 'text' : 'password'}
                value={values.password}
                onChange={(event) => setField('password', event.target.value)}
                error={errors.password}
                placeholder="Enter Your Password"
                inputClassName="h-[46px] pr-11"
                autoComplete="new-password"
              />
              <button
                aria-label="Show password"
                type="button"
                onClick={() => setShowPassword((current) => !current)}
                className="absolute right-3 top-[38px] text-[#94a3b8] hover:text-[#475569] cursor-pointer"
              >
                {showPassword ? (
                  <VisibilityOffOutlinedIcon sx={{ fontSize: 19 }} />
                ) : (
                  <VisibilityOutlinedIcon sx={{ fontSize: 19 }} />
                )}
              </button>
            </div>

            <div className="relative">
              <FormField
                id="confirm-password"
                label="Confirm Password"
                required
                type={showConfirmPassword ? 'text' : 'password'}
                value={values.confirmPassword}
                onChange={(event) => setField('confirmPassword', event.target.value)}
                error={errors.confirmPassword}
                placeholder="Enter Your Confirm Password"
                inputClassName="h-[46px] pr-11"
                autoComplete="new-password"
              />
              <button
                aria-label="Show confirm password"
                type="button"
                onClick={() => setShowConfirmPassword((current) => !current)}
                className="absolute right-3 top-[38px] text-[#94a3b8] hover:text-[#475569] cursor-pointer"
              >
                {showConfirmPassword ? (
                  <VisibilityOffOutlinedIcon sx={{ fontSize: 19 }} />
                ) : (
                  <VisibilityOutlinedIcon sx={{ fontSize: 19 }} />
                )}
              </button>
            </div>
          </div>

          <p className="-mt-[11px] text-[12.5px] text-[#94a3b8]">
            Minimum 8 characters, with at least one number and one symbol.
          </p>

          <PrimaryButton type="submit" heightClass="h-[48px]">
            Continue
          </PrimaryButton>
        </form>
      </div>
    </div>
  );
};

export default AdminAccountPage;
