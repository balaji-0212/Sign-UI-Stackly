import { createContext } from 'react';
import type { OrganizationDetails, AdminAccount } from '../types/onboarding';

export interface OnboardingContextType {
  organization: OrganizationDetails;
  admin: AdminAccount;
  updateOrganization: (data: Partial<OrganizationDetails>) => void;
  updateAdmin: (data: Partial<AdminAccount>) => void;
  resetOnboarding: () => void;
}

export const OnboardingContext = createContext<OnboardingContextType | undefined>(undefined);
