import React from 'react';

interface DividerTextProps {
  text?: string;
  className?: string;
}

export const DividerText: React.FC<DividerTextProps> = ({
  text = 'or continue with',
  className = '',
}) => {
  return (
    <div className={`relative w-full flex items-center justify-center ${className}`}>
      <div className="absolute inset-0 flex items-center">
        <div className="w-full border-t border-[#e5e7eb]" />
      </div>
      <span className="relative bg-white px-[12px] text-[11.5px] text-[#747a88] select-none">
        {text}
      </span>
    </div>
  );
};
