import React from 'react';

interface StepProgressProps {
  currentStep: number;
  totalSteps?: number;
  className?: string;
}

/**
 * Reusable 3-step progress bar component.
 * Reproduces the exact 3-segment progress indicator:
 * - Completed steps: soft blue-to-indigo gradient (from-[#76a4f0] to-[#8781f0])
 * - Active step: solid dark navy (#0e1333)
 * - Future steps: subtle light gray (#e7eaee)
 */
export const StepProgress: React.FC<StepProgressProps> = ({
  currentStep,
  totalSteps = 3,
  className = '',
}) => {
  return (
    <div
      className={`w-full max-w-[560px] h-[4px] flex items-center gap-[6px] ${className}`}
      role="progressbar"
      aria-valuenow={currentStep}
      aria-valuemin={1}
      aria-valuemax={totalSteps}
      aria-label={`Step ${currentStep} of ${totalSteps}`}
    >
      {Array.from({ length: totalSteps }, (_, index) => {
        const stepNumber = index + 1;
        let segmentClass = 'bg-[#e7eaee]';

        if (stepNumber < currentStep) {
          // Completed step
          segmentClass = 'bg-gradient-to-r from-[#76a4f0] to-[#8781f0]';
        } else if (stepNumber === currentStep) {
          // Current active step
          segmentClass = 'bg-[#0e1333]';
        }

        return (
          <div
            key={stepNumber}
            className={`flex-1 h-full rounded-[2px] transition-all duration-300 ${segmentClass}`}
          />
        );
      })}
    </div>
  );
};
