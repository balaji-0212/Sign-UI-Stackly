import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import ArrowBackIosNewIcon from "@mui/icons-material/ArrowBackIosNew";

import ProgressSteps from "../components/ProgressSteps";
import AgreementCheckbox from "../components/AgreementCheckbox";
import { useOnboarding } from "../context/useOnboarding";

type ReviewConfirmProps = {
  onCreateAccount?: () => void;
};

function ReviewConfirm({ onCreateAccount }: ReviewConfirmProps) {
  const navigate = useNavigate();
  const { organization } = useOnboarding();
  const orgName = organization.organizationName || "ABC Technologies Pvt Ltd";

  const [termsAccepted, setTermsAccepted] = useState(false);
  const [authorizationAccepted, setAuthorizationAccepted] = useState(false);
  const [dataProcessingAccepted, setDataProcessingAccepted] = useState(false);
  const [updatesAccepted, setUpdatesAccepted] = useState(true);

  useEffect(() => {
    const mainEl = document.querySelector("main");
    if (mainEl) {
      mainEl.scrollTop = 0;
    }
    window.scrollTo(0, 0);
  }, []);

  const canCreateAccount =
    termsAccepted &&
    authorizationAccepted &&
    dataProcessingAccepted;

  const handleCreateAccount = () => {
    if (!canCreateAccount) return;
    if (onCreateAccount) {
      onCreateAccount();
    } else {
      navigate("/welcome");
    }
  };

  return (
    <section className="min-h-screen w-full bg-white">
      <div className="mx-auto w-full max-w-[560px] pt-12 sm:pt-20 lg:pt-[174px] pb-16 px-4 sm:px-0">
        {/* Back */}
        <button
          type="button"
          onClick={() => navigate("/admin")}
          className="flex items-center gap-2 text-sm text-[#7c8aa8] transition hover:text-[#11152f] cursor-pointer"
        >
          <ArrowBackIosNewIcon sx={{ fontSize: 12 }} />
          Back
        </button>

        {/* Progress */}
        <div className="mt-20">
          <ProgressSteps currentStep={3} />
        </div>

        {/* Step label */}
        <p className="mt-7 text-[11px] font-medium tracking-[0.25em] text-[#9aa5ba]">
          STEP 3 OF 3 · TERMS &amp; AUTHORIZATION
        </p>

        {/* Heading */}
        <h1 className="mt-4 text-[24px] font-semibold leading-tight tracking-[-0.02em] text-[#11152f]">
          Review and confirm
        </h1>

        {/* Description */}
        <p className="mt-4 text-[15px] leading-6 text-[#68758d]">
          One last step before we create{" "}
          <strong className="font-semibold text-[#59657b]">
            {orgName}&apos;s
          </strong>{" "}
          workspace.
        </p>

        {/* Agreement card */}
        <div className="mt-11 rounded-[10px] border border-[#e1e5ec] bg-[#fbfcfe] px-5 py-4">
          <div className="space-y-4">
            {/* Terms + Privacy */}
            <AgreementCheckbox
              checked={termsAccepted}
              onChange={setTermsAccepted}
            >
              I have read and agree to the{" "}
              <span className="font-semibold text-[#4161ef]">
                Terms of Service
              </span>{" "}
              and{" "}
              <span className="font-semibold text-[#4161ef]">
                Privacy Policy
              </span>
              .
            </AgreementCheckbox>

            {/* Authorization */}
            <AgreementCheckbox
              checked={authorizationAccepted}
              onChange={setAuthorizationAccepted}
            >
              I confirm that I am authorized to register{" "}
              <strong className="font-semibold text-[#59657b]">
                {orgName}
              </strong>{" "}
              on One Enterprise, and I accept responsibility as its Super
              Administrator.
            </AgreementCheckbox>

            {/* Data Processing */}
            <AgreementCheckbox
              checked={dataProcessingAccepted}
              onChange={setDataProcessingAccepted}
            >
              I agree to the{" "}
              <span className="font-semibold text-[#4161ef]">
                Data Processing Agreement
              </span>{" "}
              governing how organization data is stored and processed.
            </AgreementCheckbox>

            {/* Optional */}
            <AgreementCheckbox
              checked={updatesAccepted}
              onChange={setUpdatesAccepted}
              optional
            >
              Send me product updates and security notices by email
            </AgreementCheckbox>
          </div>
        </div>

        {/* Create account */}
        <button
          type="button"
          disabled={!canCreateAccount}
          onClick={handleCreateAccount}
          className={`mt-3 w-full rounded-[10px] px-5 py-3.5 text-sm font-semibold transition ${
            canCreateAccount
              ? "bg-[#11152f] text-white hover:bg-[#0b0e27] cursor-pointer"
              : "cursor-not-allowed bg-[#e9edf5] text-[#98a2b3]"
          }`}
        >
          Create account
        </button>

        {/* Divider */}
        <div className="mt-6 border-t border-[#e5e8ee]" />

        {/* Sign in */}
        <p className="mt-6 text-center text-sm text-[#778197]">
          Already have an organization?{" "}
          <button
            type="button"
            onClick={() => navigate("/signin")}
            className="font-semibold text-[#4161ef] hover:underline cursor-pointer"
          >
            Sign in
          </button>
        </p>
      </div>
    </section>
  );
}

export default ReviewConfirm;
