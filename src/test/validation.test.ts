import { describe, expect, it } from 'vitest';

import {
  validateRequired,
  validateEmail,
  validateWorkspace,
  validatePassword,
  validateConfirmPassword,
  generateOrgCode,
} from '../utils/validation';

describe('validateRequired', () => {
  it('should return an error when the value is empty', () => {
    expect(validateRequired('', 'Name')).toBe('Name is required');
  });

  it('should return an error when the value contains only spaces', () => {
    expect(validateRequired('   ', 'Name')).toBe('Name is required');
  });

  it('should return no error for a valid value', () => {
    expect(validateRequired('John', 'Name')).toBe('');
  });
});

describe('validateEmail', () => {
  it('should return an error when email is empty', () => {
    expect(validateEmail('')).toBe('Work email is required');
  });

  it('should return an error for an invalid email', () => {
    expect(validateEmail('invalid-email')).toBe(
      'Please enter a valid email address'
    );
  });

  it('should return no error for a valid email', () => {
    expect(validateEmail('test@example.com')).toBe('');
  });

  it('should accept a custom field name', () => {
    expect(validateEmail('', 'Email')).toBe('Email is required');
  });

  it('should accept an email with spaces around it', () => {
    expect(validateEmail('  test@example.com  ')).toBe('');
  });
});

describe('validateWorkspace', () => {
  it('should return an error when workspace is empty', () => {
    expect(validateWorkspace('')).toBe('Workspace is required');
  });

  it('should return an error when workspace contains spaces', () => {
    expect(validateWorkspace('my workspace')).toBe(
      'Workspace can only contain letters, numbers, and hyphens'
    );
  });

  it('should return an error when workspace contains special characters', () => {
    expect(validateWorkspace('my_workspace!')).toBe(
      'Workspace can only contain letters, numbers, and hyphens'
    );
  });

  it('should accept letters, numbers, and hyphens', () => {
    expect(validateWorkspace('my-workspace-123')).toBe('');
  });

  it('should accept uppercase letters', () => {
    expect(validateWorkspace('MY-WORKSPACE')).toBe('');
  });
});

describe('validatePassword', () => {
  it('should return an error when password is empty', () => {
    expect(validatePassword('')).toBe('Password is required');
  });

  it('should return an error when password is less than 8 characters', () => {
    expect(validatePassword('Pass1!')).toBe(
      'Password must be at least 8 characters'
    );
  });

  it('should return an error when password has no number', () => {
    expect(validatePassword('Password!')).toBe(
      'Password must include at least one number'
    );
  });

  it('should return an error when password has no symbol', () => {
    expect(validatePassword('Password123')).toBe(
      'Password must include at least one symbol'
    );
  });

  it('should accept a valid password', () => {
    expect(validatePassword('Password123!')).toBe('');
  });
});

describe('validateConfirmPassword', () => {
  it('should return an error when confirm password is empty', () => {
    expect(validateConfirmPassword('Password123!', '')).toBe(
      'Confirm password is required'
    );
  });

  it('should return an error when passwords do not match', () => {
    expect(
      validateConfirmPassword('Password123!', 'Different123!')
    ).toBe('Passwords do not match');
  });

  it('should return no error when passwords match', () => {
    expect(
      validateConfirmPassword('Password123!', 'Password123!')
    ).toBe('');
  });
});

describe('generateOrgCode', () => {
  it('should return an empty string for an empty organization name', () => {
    expect(generateOrgCode('')).toBe('');
  });

  it('should generate a code from two words', () => {
    expect(generateOrgCode('ABC Technologies')).toBe('ABC-TECH');
  });

  it('should use the first two words for a longer organization name', () => {
    expect(
      generateOrgCode('ABC Technologies Private Limited')
    ).toBe('ABC-TECH');
  });

  it('should limit a single-word organization code to 8 characters', () => {
    expect(generateOrgCode('Technology')).toBe('TECHNOLO');
  });

  it('should convert lowercase names to uppercase', () => {
    expect(generateOrgCode('abc technologies')).toBe('ABC-TECH');
  });

  it('should remove special characters', () => {
    expect(generateOrgCode('ABC & Technologies')).toBe('ABC-TECH');
  });
});