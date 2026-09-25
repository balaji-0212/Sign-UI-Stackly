/**
 * Form validation utilities for authentication and onboarding flows.
 */

export const validateRequired = (value: string, fieldName: string): string => {
  if (!value || !value.trim()) {
    return `${fieldName} is required`;
  }

  return '';
};

export const validateEmail = (
  email: string,
  fieldName: string = 'Work email'
): string => {
  if (!email || !email.trim()) {
    return `${fieldName} is required`;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!emailRegex.test(email.trim())) {
    return 'Please enter a valid email address';
  }

  return '';
};

export const validateWorkspace = (workspace: string): string => {
  if (!workspace || !workspace.trim()) {
    return 'Workspace is required';
  }

  const workspaceRegex = /^[a-zA-Z0-9-]+$/;

  if (!workspaceRegex.test(workspace.trim())) {
    return 'Workspace can only contain letters, numbers, and hyphens';
  }

  return '';
};

export const validatePassword = (password: string): string => {
  if (!password) {
    return 'Password is required';
  }

  if (password.length < 8) {
    return 'Password must be at least 8 characters';
  }

  if (!/[0-9]/.test(password)) {
    return 'Password must include at least one number';
  }

  if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
    return 'Password must include at least one symbol';
  }

  return '';
};

export const validateConfirmPassword = (
  password: string,
  confirmPassword: string
): string => {
  if (!confirmPassword) {
    return 'Confirm password is required';
  }

  if (password !== confirmPassword) {
    return 'Passwords do not match';
  }

  return '';
};

/**
 * Utility to generate an organization code from an organization name.
 * E.g., "ABC Technologies Pvt Ltd" -> "ABC-TECH"
 */
export const generateOrgCode = (name: string): string => {
  if (!name || !name.trim()) {
    return '';
  }

  const words = name
    .toUpperCase()
    .replace(/[^A-Z0-9\s]/g, '')
    .split(/\s+/)
    .filter(Boolean);

  if (words.length === 0) {
    return '';
  }

  if (words.length === 1) {
    return words[0].slice(0, 8);
  }

  const first = words[0].slice(0, 4);
  const second = words[1].slice(0, 4);

  return `${first}-${second}`;
};