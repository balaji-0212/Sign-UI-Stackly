import React from 'react';
import { StepProgress } from './auth/StepProgress';

interface ProgressStepsProps {
  currentStep: number;
  totalSteps?: number;
  className?: string;
}

export const ProgressSteps: React.FC<ProgressStepsProps> = ({
  currentStep,
  totalSteps = 3,
  className = '',
}) => {
  return <StepProgress currentStep={currentStep} totalSteps={totalSteps} className={className} />;
};

export default ProgressSteps;
