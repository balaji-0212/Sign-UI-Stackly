import React, { useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import { OrganizationForm } from '../components/organization/OrganizationForm';

/**
 * Organization Details Page (/organization)
 * Natural vertical scrolling onboarding form.
 */
export const OrganizationDetailsPage: React.FC = () => {
  const [searchParams] = useSearchParams();

  useEffect(() => {
    const scrollParam = searchParams.get('scroll');
    if (scrollParam) {
      const scrollY = parseInt(scrollParam, 10);
      if (!isNaN(scrollY)) {
        const mainEl = document.querySelector('main');
        if (mainEl) {
          mainEl.scrollTop = scrollY;
        }
      }
    }
  }, [searchParams]);

  return (
    <div className="w-full min-w-0 flex-1 flex flex-col items-center justify-start pt-8 sm:pt-[60px] lg:pt-[104px] pb-[80px] px-4 sm:px-6">
      <OrganizationForm />
    </div>
  );
};
