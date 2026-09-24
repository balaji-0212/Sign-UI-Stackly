import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import CheckIcon from "@mui/icons-material/Check";
import { useOnboarding } from "../context/useOnboarding";

type WelcomeProps = {
  onSignIn?: () => void;
};

function Welcome({ onSignIn }: WelcomeProps) {
  const navigate = useNavigate();
  const { organization } = useOnboarding();
  const [resendStatus, setResendStatus] = useState<string | null>(null);

  useEffect(() => {
    const mainEl = document.querySelector("main");
    if (mainEl) {
      mainEl.scrollTop = 0;
    }
    window.scrollTo(0, 0);
  }, []);

  const handleSignIn = () => {
    if (onSignIn) {
      onSignIn();
    } else {
      navigate("/signin");
    }
  };

  const handleResend = () => {
    setResendStatus("Verification email resent!");
    setTimeout(() => setResendStatus(null), 3000);
  };

  const orgName = organization.organizationName || "ABC Technologies Pvt Ltd";
  const orgSlug = (organization.organizationCode || "abc-tech").toLowerCase();
  const workspaceDomain = `${orgSlug}.oneenterprise.io`;

  return (
    <section className="min-h-screen w-full bg-white">
      <div className="mx-auto flex min-h-screen w-full max-w-[560px] flex-col items-center pt-16 sm:pt-24 lg:pt-[243px] pb-16 px-4 sm:px-0 text-center">
        {/* Success icon */}
        <div className="flex h-[60px] w-[60px] items-center justify-center rounded-full bg-[#e9f8ef]">
          <CheckIcon
            sx={{
              fontSize: 30,
              color: "#2ca35c",
              strokeWidth: 2,
            }}
          />
        </div>

        {/* Heading */}
        <h1 className="mt-7 text-[24px] font-semibold tracking-[-0.02em] text-[#11152f]">
          Welcome to One Enterprise
        </h1>

        {/* Description */}
        <p className="mt-3 max-w-[520px] text-[15px] leading-6 text-[#727d91]">
          <strong className="font-semibold text-[#667085]">
            {orgName}
          </strong>{" "}
          is ready. Your Super Admin account
          <br />
          has been created - verify your email to activate full access.
        </p>

        {/* Verification card */}
        <div className="mt-12 flex w-full items-center gap-4 rounded-[10px] border border-[#d7e1ff] bg-[#f0f4ff] px-4 py-3.5 text-left">
          <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-[9px] bg-white">
            <span className="text-[18px] text-[#4161ef]">
              ✉
            </span>
          </div>

          <p className="text-[13px] leading-[1.45] text-[#52617f]">
            We&apos;ve sent a verification link to your official email. Your
            <br />
            workspace:{" "}
            <span className="font-mono font-semibold text-[#435273]">
              {workspaceDomain}
            </span>
          </p>
        </div>

        {/* Sign in */}
        <button
          type="button"
          onClick={handleSignIn}
          className="mt-6 w-full rounded-[10px] bg-[#11152f] px-5 py-3.5 text-sm font-semibold text-white transition hover:bg-[#0b0e27] cursor-pointer"
        >
          Go to sign in
        </button>

        {/* Divider */}
        <div className="mt-6 w-full border-t border-[#e5e8ee]" />

        {/* Resend */}
        <p className="mt-6 text-sm text-[#7a8497]">
          Didn&apos;t get the email?{" "}
          <button
            type="button"
            onClick={handleResend}
            className="font-semibold text-[#4161ef] hover:underline cursor-pointer"
          >
            Resend verification
          </button>
        </p>
        {resendStatus && (
          <p className="mt-2 text-xs text-emerald-600 font-medium">
            {resendStatus}
          </p>
        )}
      </div>
    </section>
  );
}

export default Welcome;
