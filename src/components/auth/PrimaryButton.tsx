import React, { type ButtonHTMLAttributes, type ReactNode } from 'react';

interface PrimaryButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode;
  className?: string;
  heightClass?: string;
}

export const PrimaryButton: React.FC<PrimaryButtonProps> = ({
  children,
  className = '',
  heightClass = 'h-[44px]',
  disabled = false,
  type = 'submit',
  ...rest
}) => {
  return (
    <button
      type={type}
      disabled={disabled}
      className={`w-full ${heightClass} rounded-[8px] bg-[#0f1330] hover:bg-[#18204a] active:bg-[#0a0d24] text-white text-[14px] font-medium flex items-center justify-center transition-colors duration-150 cursor-pointer shadow-[0_1px_2px_rgba(0,0,0,0.05)] focus:outline-none focus:ring-2 focus:ring-[#0f1330]/30 disabled:opacity-60 disabled:cursor-not-allowed ${className}`}
      {...rest}
    >
      {children}
    </button>
  );
};
