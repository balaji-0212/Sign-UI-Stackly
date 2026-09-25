import { Outlet } from 'react-router-dom';
import { VisualBrandingPanel } from './VisualBrandingPanel';

export const AuthLayout = () => {
  return (
    <div className="flex h-screen w-full overflow-hidden bg-white select-text font-sans">
      {/* LEFT: Branding panel (Friend's perfect UI - 50% on desktop) */}
      <div className="hidden lg:block lg:w-1/2 h-full shrink-0 overflow-hidden">
        <VisualBrandingPanel />
      </div>

      {/* RIGHT: Form area (Working Right UI - 50% on desktop) */}
      <main className="w-full lg:w-1/2 h-full overflow-y-auto overflow-x-hidden no-scrollbar flex flex-col items-center justify-start bg-white">
        <Outlet />
      </main>
    </div>
  );
};