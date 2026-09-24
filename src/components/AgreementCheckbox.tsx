import React from 'react';
import CheckIcon from '@mui/icons-material/Check';

interface AgreementCheckboxProps {
  checked: boolean;
  onChange: (checked: boolean) => void;
  children: React.ReactNode;
  optional?: boolean;
}

export const AgreementCheckbox: React.FC<AgreementCheckboxProps> = ({
  checked,
  onChange,
  children,
  optional = false,
}) => {
  return (
    <label className="flex items-start gap-3 cursor-pointer select-none group">
      <div className="relative flex items-center justify-center mt-0.5 shrink-0">
        <input
          type="checkbox"
          checked={checked}
          onChange={(e) => onChange(e.target.checked)}
          className="sr-only"
        />
        <div
          className={`w-[18px] h-[18px] rounded-[4px] border flex items-center justify-center transition-colors ${
            checked
              ? 'bg-[#11152f] border-[#11152f] text-white'
              : 'bg-white border-[#cfd5e2] group-hover:border-[#98a2b3]'
          }`}
        >
          {checked && (
            <CheckIcon sx={{ fontSize: 13, color: '#ffffff', strokeWidth: 2 }} />
          )}
        </div>
      </div>

      <div className="text-[13.5px] leading-[1.45] text-[#52617f]">
        {children}
        {optional && (
          <span className="ml-1 text-[12px] text-[#9aa5ba] font-normal">(optional)</span>
        )}
      </div>
    </label>
  );
};

export default AgreementCheckbox;
