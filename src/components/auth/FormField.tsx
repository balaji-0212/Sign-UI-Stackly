import React, { type InputHTMLAttributes, type ReactNode } from 'react';
import { ChevronDown } from 'lucide-react';

export interface SelectOption {
  value: string;
  label: string;
}

interface FormFieldProps extends InputHTMLAttributes<HTMLInputElement | HTMLSelectElement> {
  id: string;
  label: string;
  required?: boolean;
  error?: string;
  helperText?: ReactNode;
  isSelect?: boolean;
  options?: SelectOption[];
  maxLength?: number;
  className?: string;
  inputClassName?: string;
  labelClassName?: string;
}

export const FormField: React.FC<FormFieldProps> = ({
  id,
  label,
  required = false,
  error,
  helperText,
  isSelect = false,
  options = [],
  className = '',
  inputClassName = 'h-[46px]',
  labelClassName = 'mb-[7px]',
  placeholder,
  value,
  onChange,
  disabled = false,
  type = 'text',
  maxLength,
  ...rest
}) => {
  const baseInputClass = `w-full min-w-0 ${inputClassName} px-[14px] rounded-[8px] border text-[14px] text-[#14171f] placeholder-[#a6abbb] bg-white transition-colors duration-150 focus:outline-none ${
    error
      ? 'border-red-400 focus:border-red-500 focus:ring-1 focus:ring-red-500/20'
      : 'border-[#e5e7eb] focus:border-[#6378ff] focus:ring-1 focus:ring-[#6378ff]/20'
  } ${disabled ? 'bg-slate-50 text-slate-400 cursor-not-allowed' : ''}`;

  return (
    <div className={`w-full min-w-0 flex flex-col ${className}`}>
      {/* Label */}
      <label
        htmlFor={id}
        className={`text-[13px] font-medium text-[#14171f] select-none flex items-center gap-[3px] ${labelClassName}`}
      >
        <span>{label}</span>
        {required && (
          <span className="text-[#e11d48] font-semibold" aria-hidden="true">
            *
          </span>
        )}
      </label>

      {/* Input or Select */}
      {isSelect ? (
        <div className="relative w-full min-w-0">
          <select
            id={id}
            value={value as string}
            onChange={onChange as React.ChangeEventHandler<HTMLSelectElement>}
            disabled={disabled}
            aria-invalid={!!error}
            aria-describedby={error ? `${id}-error` : helperText ? `${id}-helper` : undefined}
            className={`${baseInputClass} pr-[38px] appearance-none cursor-pointer`}
            {...(rest as any)}
          >
            {placeholder && (
              <option value="" disabled>
                {placeholder}
              </option>
            )}
            {options.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label}
              </option>
            ))}
          </select>
          <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-[14px] text-[#9aa3b2]">
            <ChevronDown size={14} strokeWidth={2} />
          </div>
        </div>
      ) : (
        <input
          id={id}
          type={type}
          value={value}
          onChange={onChange as React.ChangeEventHandler<HTMLInputElement>}
          placeholder={placeholder}
          disabled={disabled}
          maxLength={maxLength}
          aria-invalid={!!error}
          aria-describedby={error ? `${id}-error` : helperText ? `${id}-helper` : undefined}
          className={baseInputClass}
          {...(rest as any)}
        />
      )}

      {/* Error or Helper Message */}
      {error ? (
        <p id={`${id}-error`} className="text-[12px] text-red-500 mt-[5px] pl-[1px]" role="alert">
          {error}
        </p>
      ) : helperText ? (
        <div id={`${id}-helper`} className="text-[12px] text-[#64748b] mt-[5px] pl-[1px]">
          {helperText}
        </div>
      ) : null}
    </div>
  );
};
