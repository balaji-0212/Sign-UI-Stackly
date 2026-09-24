import React, { useRef, useState } from 'react';
import { Upload, X } from 'lucide-react';

interface FileUploadProps {
  id?: string;
  label?: string;
  optional?: boolean;
  value?: File | null;
  previewUrl?: string | null;
  onChange?: (file: File | null) => void;
  className?: string;
}

export const FileUpload: React.FC<FileUploadProps> = ({
  id = 'file-upload',
  label = 'Organization Logo',
  optional = true,
  value,
  previewUrl,
  onChange,
  className = '',
}) => {
  const inputRef = useRef<HTMLInputElement>(null);
  const [isDragOver, setIsDragOver] = useState(false);
  const [localPreview, setLocalPreview] = useState<string | null>(previewUrl || null);
  const [fileError, setFileError] = useState<string | null>(null);

  const validateFile = (file: File): string | null => {
    const validTypes = ['image/png', 'image/jpeg', 'image/jpg'];
    if (!validTypes.includes(file.type)) {
      return 'Please upload a PNG or JPG image file';
    }
    const maxSize = 5 * 1024 * 1024; // 5MB
    if (file.size > maxSize) {
      return 'File size exceeds the 5MB limit';
    }
    return null;
  };

  const handleFileChange = (file: File | null) => {
    setFileError(null);
    if (file) {
      const error = validateFile(file);
      if (error) {
        setFileError(error);
        if (inputRef.current) inputRef.current.value = '';
        return;
      }
      const url = URL.createObjectURL(file);
      setLocalPreview(url);
      onChange?.(file);
    } else {
      setLocalPreview(null);
      onChange?.(null);
      if (inputRef.current) inputRef.current.value = '';
    }
  };

  const onDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFileChange(e.dataTransfer.files[0]);
    }
  };

  const onDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(true);
  };

  const onDragLeave = () => {
    setIsDragOver(false);
  };

  return (
    <div className={`w-full min-w-0 flex flex-col ${className}`}>
      {/* Label */}
      <div className="flex items-center gap-[4px] mb-[7px]">
        <label htmlFor={id} className="text-[13px] font-medium text-[#14171f] select-none">
          {label}
        </label>
        {optional && (
          <span className="text-[10px] font-mono font-medium text-[#9aa3b2] tracking-[0.1em] uppercase select-none">
            OPTIONAL
          </span>
        )}
      </div>

      {/* Upload Zone */}
      <div
        onDrop={onDrop}
        onDragOver={onDragOver}
        onDragLeave={onDragLeave}
        onClick={() => inputRef.current?.click()}
        className={`relative w-full h-[116px] rounded-[8px] border border-dashed transition-all duration-150 flex flex-col items-center justify-center cursor-pointer select-none px-4 ${
          isDragOver
            ? 'border-[#6378ff] bg-[#f5f7ff]'
            : 'border-[#d6dbe3] hover:border-[#a3adb8] bg-white'
        }`}
      >
        <input
          ref={inputRef}
          id={id}
          type="file"
          accept="image/png,image/jpeg,image/jpg"
          onChange={(e) => {
            if (e.target.files && e.target.files[0]) {
              handleFileChange(e.target.files[0]);
            }
          }}
          className="hidden"
        />

        {localPreview || value ? (
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 rounded-[6px] border border-[#e5e7eb] overflow-hidden flex items-center justify-center bg-slate-50">
              <img
                src={localPreview || ''}
                alt="Logo preview"
                className="w-full h-full object-contain"
              />
            </div>
            <div className="flex flex-col text-left">
              <span className="text-[13px] font-medium text-[#14171f] truncate max-w-[200px]">
                {value ? value.name : 'Selected logo'}
              </span>
              <span className="text-[11px] text-[#717684]">Click or drop to replace</span>
            </div>
            <button
              type="button"
              onClick={(e) => {
                e.stopPropagation();
                handleFileChange(null);
              }}
              className="ml-2 p-1 rounded-full text-slate-400 hover:text-slate-600 hover:bg-slate-100"
              aria-label="Remove uploaded image"
            >
              <X size={16} />
            </button>
          </div>
        ) : (
          <>
            <div className="w-[32px] h-[32px] flex items-center justify-center text-[#717684] mb-[8px]">
              <Upload size={18} strokeWidth={1.5} />
            </div>
            <div className="text-[13px] text-[#14171f] font-normal leading-tight text-center">
              <span className="text-[#2563eb] font-medium">Upload logo</span> or drag and drop — PNG, JPG up to 5MB
            </div>
          </>
        )}
      </div>

      {fileError && (
        <p className="text-[12px] text-red-500 mt-[5px] pl-[1px]" role="alert">
          {fileError}
        </p>
      )}
    </div>
  );
};
