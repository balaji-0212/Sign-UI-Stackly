import React, { useState, useCallback, type ReactNode } from 'react';
import type { OrganizationDetails, AdminAccount } from '../types/onboarding';
import { OnboardingContext } from './OnboardingContextValue';

const initialOrganization: OrganizationDetails = {
  organizationName: '',
  organizationCode: '',
  organizationType: '',
  industry: '',
  companySize: '',
  country: '',
  state: '',
  city: '',
  timeZone: '',
  organizationLogo: null,
  logoPreviewUrl: null,
};

const initialAdmin: AdminAccount = {
  firstName: '',
  lastName: '',
  officialEmail: '',
  mobileNumber: '',
  username: '',
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
