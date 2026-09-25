import React, { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { StepProgress } from '../auth/StepProgress';
import { FormField } from '../auth/FormField';
import { FileUpload } from '../auth/FileUpload';
import { PrimaryButton } from '../auth/PrimaryButton';
import { useOnboarding } from '../../context/useOnboarding';
import { generateOrgCode, validateRequired } from '../../utils/validation';

interface OrganizationFormProps {
  onContinue?: () => void;
  className?: string;
}

const statesByCountry: Record<string, { value: string; label: string }[]> = {
  India: [
    { value: 'Telangana', label: 'Telangana' },
    { value: 'Maharashtra', label: 'Maharashtra' },
    { value: 'Karnataka', label: 'Karnataka' },
    { value: 'Delhi', label: 'Delhi' },
    { value: 'Tamil Nadu', label: 'Tamil Nadu' },
    { value: 'Gujarat', label: 'Gujarat' },
    { value: 'Uttar Pradesh', label: 'Uttar Pradesh' },
    { value: 'West Bengal', label: 'West Bengal' },
  ],
  'United States': [
    { value: 'California', label: 'California' },
    { value: 'New York', label: 'New York' },
    { value: 'Texas', label: 'Texas' },
    { value: 'Washington', label: 'Washington' },
    { value: 'Illinois', label: 'Illinois' },
    { value: 'Florida', label: 'Florida' },
  ],
  'United Kingdom': [
    { value: 'England', label: 'England' },
    { value: 'Scotland', label: 'Scotland' },
    { value: 'Wales', label: 'Wales' },
    { value: 'Northern Ireland', label: 'Northern Ireland' },
  ],
  Singapore: [
    { value: 'Central Singapore', label: 'Central Singapore' },
    { value: 'North East', label: 'North East' },
    { value: 'North West', label: 'North West' },
    { value: 'South East', label: 'South East' },
    { value: 'South West', label: 'South West' },
  ],
  Germany: [
    { value: 'Bavaria', label: 'Bavaria' },
    { value: 'Berlin', label: 'Berlin' },
    { value: 'Hamburg', label: 'Hamburg' },
    { value: 'Hesse', label: 'Hesse' },
    { value: 'North Rhine-Westphalia', label: 'North Rhine-Westphalia' },
  ],
  Australia: [
    { value: 'New South Wales', label: 'New South Wales' },
    { value: 'Victoria', label: 'Victoria' },
    { value: 'Queensland', label: 'Queensland' },
    { value: 'Western Australia', label: 'Western Australia' },
  ],
};

/**
 * Unified Organization Details Form Component.
 * Matches Sign In Page-1.png (top) and Sign In Page-3.png (lower) exactly.
 */
export const OrganizationForm: React.FC<OrganizationFormProps> = ({
  onContinue,
  className = '',
}) => {
  const navigate = useNavigate();
  const { organization, updateOrganization } = useOnboarding();
  const orgCodeInputRef = useRef<HTMLInputElement>(null);

  const [orgName, setOrgName] = useState(organization.organizationName || '');
  const [orgCode, setOrgCode] = useState(organization.organizationCode || '');
  const [isManualCode, setIsManualCode] = useState(false);
  const [orgType, setOrgType] = useState(organization.organizationType || '');
  const [industry, setIndustry] = useState(organization.industry || '');
  const [companySize, setCompanySize] = useState(organization.companySize || '');
  const [country, setCountry] = useState(organization.country || '');
  const [stateProvince, setStateProvince] = useState(organization.state || '');
  const [city, setCity] = useState(organization.city || '');
  const [timeZone, setTimeZone] = useState(organization.timeZone || '');
  const [logoFile, setLogoFile] = useState<File | null>(organization.organizationLogo || null);

  const [errors, setErrors] = useState<Record<string, string>>({});
  const [touched, setTouched] = useState<Record<string, boolean>>({});

  const handleOrgNameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value;
    setOrgName(val);
    if (!isManualCode) {
      const generated = generateOrgCode(val);
      setOrgCode(generated);
    }
    if (touched.orgName) {
      setErrors((prev) => ({ ...prev, orgName: validateRequired(val, 'Organization name') }));
    }
  };

  const handleOrgCodeChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setIsManualCode(true);
    const val = e.target.value.toUpperCase();
    setOrgCode(val);
    if (touched.orgCode) {
      setErrors((prev) => ({ ...prev, orgCode: validateRequired(val, 'Organization code') }));
    }
  };

  const handleCountryChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const newCountry = e.target.value;
    setCountry(newCountry);
    setStateProvince('');
    if (touched.country) {
      setErrors((prev) => ({ ...prev, country: validateRequired(newCountry, 'Country') }));
    }
  };

  const validateAll = () => {
    const newErrors: Record<string, string> = {};
    const nameErr = validateRequired(orgName, 'Organization name');
    if (nameErr) newErrors.orgName = nameErr;

    const codeErr = validateRequired(orgCode, 'Organization code');
    if (codeErr) newErrors.orgCode = codeErr;

    const typeErr = validateRequired(orgType, 'Organization type');
    if (typeErr) newErrors.orgType = typeErr;

    const indErr = validateRequired(industry, 'Industry');
    if (indErr) newErrors.industry = indErr;

    const sizeErr = validateRequired(companySize, 'Company size');
    if (sizeErr) newErrors.companySize = sizeErr;

    const countryErr = validateRequired(country, 'Country');
    if (countryErr) newErrors.country = countryErr;

    const stateErr = validateRequired(stateProvince, 'State / Province');
    if (stateErr) newErrors.stateProvince = stateErr;

    const cityErr = validateRequired(city, 'City');
    if (cityErr) newErrors.city = cityErr;

    const timeZoneErr = validateRequired(timeZone, 'Time Zone');
    if (timeZoneErr) newErrors.timeZone = timeZoneErr;

    setErrors(newErrors);
    setTouched({
      orgName: true,
      orgCode: true,
      orgType: true,
      industry: true,
      companySize: true,
      country: true,
      stateProvince: true,
      city: true,
      timeZone: true,
    });

    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (validateAll()) {
      updateOrganization({
        organizationName: orgName,
        organizationCode: orgCode,
        organizationType: orgType,
        industry,
        companySize,
        country,
        state: stateProvince,
        city,
        timeZone,
        organizationLogo: logoFile,
      });

      if (onContinue) {
        onContinue();
      } else {
        navigate('/admin');
      }
    }
  };

  return (
    <div className={`w-full min-w-0 max-w-[560px] flex flex-col ${className}`}>
      {/* 3-Step Progress Indicator — matches reference bar at top */}
      <div className="mb-[28px]">
        <StepProgress currentStep={1} totalSteps={3} />
      </div>

      {/* Step Subheader — matches "STEP 1 OF 3 · ORGANIZATION DETAILS" */}
      <div className="text-[10.5px] font-mono font-medium tracking-[0.14em] text-[#7c828e] uppercase mb-[10px] leading-none select-none">
        STEP 1 OF 3 · ORGANIZATION DETAILS
      </div>

      {/* Main Title — matches "Tell us about your organization" */}
      <h1 className="text-[26px] font-bold text-[#14171f] tracking-[-0.02em] leading-tight mb-[6px]">
        Tell us about your organization
      </h1>

      {/* Subtitle — matches reference */}
      <p className="text-[13.5px] text-[#64748b] leading-[20px] mb-[28px]">
        This creates your organization's workspace on One Enterprise.
      </p>

      {/* Form Fields */}
      <form onSubmit={handleSubmit} noValidate className="w-full min-w-0 flex flex-col">
        {/* Organization Name */}
        <div className="mb-[18px]">
          <FormField
            id="org-name"
            label="Organization Name"
            required
            value={orgName}
            onChange={handleOrgNameChange}
            onBlur={() => {
              setTouched((prev) => ({ ...prev, orgName: true }));
              setErrors((prev) => ({
                ...prev,
                orgName: validateRequired(orgName, 'Organization name'),
              }));
            }}
            placeholder="Enter Your Organization Name"
            error={touched.orgName ? errors.orgName : ''}
            autoComplete="organization"
          />
        </div>

        {/* Organization Code — plain input with helper text matching reference */}
        <div className="mb-[6px] flex flex-col w-full min-w-0">
          <label
            htmlFor="org-code"
            className="text-[13px] font-medium text-[#14171f] mb-[7px] select-none flex items-center gap-[3px]"
          >
            <span>Organization Code</span>
            <span className="text-[#e11d48] font-semibold" aria-hidden="true">
              *
            </span>
          </label>
          <input
            ref={orgCodeInputRef}
            id="org-code"
            type="text"
            value={orgCode}
            onChange={handleOrgCodeChange}
            onBlur={() => {
              setTouched((prev) => ({ ...prev, orgCode: true }));
              setErrors((prev) => ({
                ...prev,
                orgCode: validateRequired(orgCode, 'Organization code'),
              }));
            }}
            placeholder="Enter Your Organization Code"
            className={`w-full min-w-0 h-[46px] px-[14px] rounded-[8px] border text-[14px] text-[#14171f] font-mono uppercase placeholder-[#a6abbb] bg-white transition-colors duration-150 focus:outline-none ${
              errors.orgCode && touched.orgCode
                ? 'border-red-400 focus:border-red-500 focus:ring-1 focus:ring-red-500/20'
                : 'border-[#e5e7eb] focus:border-[#6378ff] focus:ring-1 focus:ring-[#6378ff]/20'
            }`}
          />
          {errors.orgCode && touched.orgCode ? (
            <p className="text-[12px] text-red-500 mt-[5px] pl-[1px]" role="alert">
              {errors.orgCode}
            </p>
          ) : (
            <div className="text-[12px] text-[#64748b] mt-[5px] pl-[1px]">
              Auto-generated from your organization name —{' '}
              <button
                type="button"
                onClick={() => {
                  setIsManualCode(true);
                  orgCodeInputRef.current?.focus();
                }}
                className="text-[#2563eb] font-medium hover:underline cursor-pointer focus:outline-none"
              >
                edit manually
              </button>
            </div>
          )}
        </div>

        {/* Organization Type — full width, single column (matches reference) */}
        <div className="mb-[18px] mt-[14px]">
          <FormField
            id="org-type"
            label="Organization Type"
            required
            isSelect
            value={orgType}
            onChange={(e) => {
              setOrgType(e.target.value);
              if (touched.orgType) {
                setErrors((prev) => ({ ...prev, orgType: validateRequired(e.target.value, 'Organization type') }));
              }
            }}
            placeholder="Select organization type"
            error={touched.orgType ? errors.orgType : ''}
            options={[
              { value: 'Enterprise', label: 'Enterprise' },
              { value: 'Mid-Market', label: 'Mid-Market' },
              { value: 'Small Business', label: 'Small Business' },
              { value: 'Startup', label: 'Startup' },
              { value: 'Government / Public', label: 'Government / Public' },
              { value: 'Non-Profit', label: 'Non-Profit' },
            ]}
          />
        </div>

        {/* Industry — full width, single column (matches reference) */}
        <div className="mb-[18px]">
          <FormField
            id="industry"
            label="Industry"
            required
            isSelect
            value={industry}
            onChange={(e) => {
              setIndustry(e.target.value);
              if (touched.industry) {
                setErrors((prev) => ({ ...prev, industry: validateRequired(e.target.value, 'Industry') }));
              }
            }}
            placeholder="Select industry"
            error={touched.industry ? errors.industry : ''}
            options={[
              { value: 'Information Technology', label: 'Information Technology' },
              { value: 'Financial Services', label: 'Financial Services' },
              { value: 'Healthcare & Life Sciences', label: 'Healthcare & Life Sciences' },
              { value: 'Manufacturing', label: 'Manufacturing' },
              { value: 'Retail & E-commerce', label: 'Retail & E-commerce' },
              { value: 'Telecommunications', label: 'Telecommunications' },
              { value: 'Education', label: 'Education' },
            ]}
          />
        </div>

        {/* Company Size — full width (matches reference) */}
        <div className="mb-[18px]">
          <FormField
            id="company-size"
            label="Company Size"
            required
            isSelect
            value={companySize}
            onChange={(e) => {
              setCompanySize(e.target.value);
              if (touched.companySize) {
                setErrors((prev) => ({ ...prev, companySize: validateRequired(e.target.value, 'Company size') }));
              }
            }}
            placeholder="Select company size"
            error={touched.companySize ? errors.companySize : ''}
            options={[
              { value: '1-50', label: '1-50 employees' },
              { value: '51-200', label: '51-200 employees' },
              { value: '201-500', label: '201-500 employees' },
              { value: '501-1000', label: '501-1000' },
              { value: '1001-5000', label: '1,001-5,000 employees' },
              { value: '5000+', label: '5,000+ employees' },
            ]}
          />
        </div>

        {/* 2-Column: Country & State/Province (matches reference) */}
        <div className="grid grid-cols-2 gap-4 mb-[18px]">
          <FormField
            id="country"
            label="Country"
            required
            isSelect
            value={country}
            onChange={handleCountryChange}
            placeholder="Select country"
            error={touched.country ? errors.country : ''}
            options={[
              { value: 'India', label: 'India' },
              { value: 'United States', label: 'United States' },
              { value: 'United Kingdom', label: 'United Kingdom' },
              { value: 'Singapore', label: 'Singapore' },
              { value: 'Germany', label: 'Germany' },
              { value: 'Australia', label: 'Australia' },
            ]}
          />

          <FormField
            id="state"
            label="State / Province"
            required
            isSelect
            value={stateProvince}
            onChange={(e) => {
              setStateProvince(e.target.value);
              if (touched.stateProvince) {
                setErrors((prev) => ({ ...prev, stateProvince: validateRequired(e.target.value, 'State / Province') }));
              }
            }}
            placeholder="Select state / province"
            error={touched.stateProvince ? errors.stateProvince : ''}
            options={country ? statesByCountry[country] || [] : []}
          />
        </div>

        {/* 2-Column: City & Time Zone (matches reference) */}
        <div className="grid grid-cols-2 gap-4 mb-[18px]">
          <FormField
            id="city"
            label="City"
            required
            value={city}
            onChange={(e) => {
              setCity(e.target.value);
              if (touched.city) {
                setErrors((prev) => ({ ...prev, city: validateRequired(e.target.value, 'City') }));
              }
            }}
            onBlur={() => {
              setTouched((prev) => ({ ...prev, city: true }));
              setErrors((prev) => ({
                ...prev,
                city: validateRequired(city, 'City'),
              }));
            }}
            placeholder="Enter Your City"
            error={touched.city ? errors.city : ''}
          />

          <FormField
            id="time-zone"
            label="Time Zone"
            required
            isSelect
            value={timeZone}
            onChange={(e) => {
              setTimeZone(e.target.value);
              if (touched.timeZone) {
                setErrors((prev) => ({ ...prev, timeZone: validateRequired(e.target.value, 'Time Zone') }));
              }
            }}
            placeholder="Select time zone"
            options={[
              { value: 'Asia/Kolkata (UTC +05:30)', label: 'Asia/Kolkata (UTC +05:30)' },
              { value: 'America/New_York (UTC -05:00)', label: 'America/New_York (UTC -05:00)' },
              { value: 'Europe/London (UTC +00:00)', label: 'Europe/London (UTC +00:00)' },
              { value: 'Asia/Singapore (UTC +08:00)', label: 'Asia/Singapore (UTC +08:00)' },
              { value: 'Australia/Sydney (UTC +11:00)', label: 'Australia/Sydney (UTC +11:00)' },
            ]}
            error={touched.timeZone ? errors.timeZone : ''}
          />
        </div>

        {/* Organization Logo — matches reference with "OPTIONAL" tag */}
        <div className="mb-[22px]">
          <FileUpload
            id="org-logo"
            label="Organization Logo"
            optional
            value={logoFile}
            onChange={(file) => setLogoFile(file)}
          />
        </div>

        {/* Continue Button */}
        <div className="w-full min-w-0">
          <PrimaryButton type="submit" heightClass="h-[48px]">
            Continue
          </PrimaryButton>
        </div>
      </form>

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
  );
};
