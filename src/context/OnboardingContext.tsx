import React, { useState, useCallback, type ReactNode } from 'react';
import type { OrganizationDetails, AdminAccount } from '../types/onboarding';
import { OnboardingContext } from './OnboardingContextValue';

const initialOrganization: OrganizationDetails = {
  organizationName: '',
  organizationCode: '',
  organizationType: 'Enterprise',
  industry: 'Information Technology',
  companySize: '501-1000',
  country: 'India',
  state: 'Telangana',
  city: '',
  timeZone: 'Asia/Kolkata (UTC +05:30)',
  organizationLogo: null,
  logoPreviewUrl: null,
};

const initialAdmin: AdminAccount = {
  firstName: 'Ananya',
  lastName: 'Rao',
  officialEmail: 'ananya.rao@abctech.com',
  mobileNumber: '+91 98765 43210',
  username: 'ananya.rao',
  password: '',
  confirmPassword: '',
};

export const OnboardingProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [organization, setOrganization] = useState<OrganizationDetails>(initialOrganization);
  const [admin, setAdmin] = useState<AdminAccount>(initialAdmin);

  const updateOrganization = useCallback((data: Partial<OrganizationDetails>) => {
    setOrganization((prev) => ({ ...prev, ...data }));
  }, []);

  const updateAdmin = useCallback((data: Partial<AdminAccount>) => {
    setAdmin((prev) => ({ ...prev, ...data }));
  }, []);

  const resetOnboarding = useCallback(() => {
    setOrganization(initialOrganization);
    setAdmin(initialAdmin);
  }, []);

  return (
    <OnboardingContext.Provider
      value={{
        organization,
        admin,
        updateOrganization,
        updateAdmin,
        resetOnboarding,
      }}
    >
      {children}
    </OnboardingContext.Provider>
  );
};
