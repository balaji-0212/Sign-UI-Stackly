import { useContext } from 'react';
import { OnboardingContext } from './OnboardingContextValue';
import type { OnboardingContextType } from './OnboardingContextValue';

export const useOnboarding = (): OnboardingContextType => {
  const context = useContext(OnboardingContext);
  if (!context) {
    throw new Error('useOnboarding must be used within an OnboardingProvider');
  }
  return context;
};
