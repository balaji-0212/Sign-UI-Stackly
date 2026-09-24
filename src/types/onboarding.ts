export interface OrganizationDetails {
  organizationName: string;
  organizationCode: string;
  organizationType: string;
  industry: string;
  companySize: string;
  country: string;
  state: string;
  city: string;
  timeZone: string;
  organizationLogo?: File | null;
  logoPreviewUrl?: string | null;
}

export interface AdminAccount {
  firstName: string;
  lastName: string;
  officialEmail: string;
  mobileNumber: string;
  username: string;
  password: string;
  confirmPassword: string;
}

export interface OnboardingState {
  organization: OrganizationDetails;
  admin: AdminAccount;
}
