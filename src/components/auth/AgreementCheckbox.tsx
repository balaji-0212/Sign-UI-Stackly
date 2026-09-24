import React, { type ReactNode } from 'react';

interface AgreementCheckboxProps {
  checked: boolean;
  onChange: (checked: boolean) => void;
  optional?: boolean;
  children: ReactNode;
  className?: string;
  id?: string;
}

/**
 * Agreement Checkbox Component.
 * Matches the custom checkbox design in Sign In Page-4.png:
 * - Unchecked: subtle border, white bg
 * - Checked: dark navy background (#0f1330) with white checkmark
 * - Optional badge tag in uppercase
 */
export const AgreementCheckbox: React.FC<AgreementCheckboxProps> = ({
  checked,
  onChange,
  optional = false,
  children,
  className = '',
  id,
}) => {
  const handleToggle = () => {
    onChange(!checked);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
      handleToggle();
    }
  };

  return (
    <div
      className={`flex items-start gap-3 select-none cursor-pointer group ${className}`}
      onClick={handleToggle}
      onKeyDown={handleKeyDown}
      tabIndex={0}
      role="checkbox"
      aria-checked={checked}
      id={id}
    >
      {/* Custom Checkbox Box */}
      <div
        className={`w-[18px] h-[18px] rounded-[4px] flex items-center justify-center shrink-0 mt-[2px] transition-all duration-150 ${
          checked
            ? 'bg-[#0f1330] border border-[#0f1330] text-white shadow-sm'
            : 'bg-white border border-[#cbd5e1] group-hover:border-[#94a3b8]'
        }`}
      >
        {checked && (
          <svg
            className="w-3 h-3 text-white"
            viewBox="0 0 12 12"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="M2.5 6L5 8.5L9.5 3.5" />
          </svg>
        )}
      </div>

      {/* Label Content */}
      <div className="text-[13.5px] text-[#334155] leading-[20px] flex-1">
        {children}
        {optional && (
          <span className="text-[10px] font-mono font-medium text-[#9aa3b2] tracking-[0.1em] uppercase ml-1.5 select-none">
            OPTIONAL
          </span>
        )}
      </div>
    </div>
  );
};

export default AgreementCheckbox;
