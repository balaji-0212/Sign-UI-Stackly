import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const ReviewConfirmPage: React.FC = () => {
  const navigate = useNavigate();

  const [termsAccepted, setTermsAccepted] = useState(false);
  const [authorizationAccepted, setAuthorizationAccepted] =
    useState(false);
  const [dataProcessingAccepted, setDataProcessingAccepted] =
    useState(false);
  const [updatesAccepted, setUpdatesAccepted] = useState(true);

  const canCreateAccount =
    termsAccepted &&
    authorizationAccepted &&
    dataProcessingAccepted;

  const handleCreateAccount = () => {
    if (!canCreateAccount) {
      return;
    }

    navigate("/welcome");
  };

  return (
    <div className="w-full min-w-0 flex-1 overflow-y-auto bg-white">
      <div className="mx-auto flex w-full max-w-[560px] flex-col px-6 pb-10 pt-10 lg:px-0 lg:pt-[90px]">

        {/* Back */}
        <button
          type="button"
          onClick={() => navigate("/admin")}
          className="flex w-fit items-center gap-2 text-[13px] font-medium text-[#7c8aa8] transition hover:text-[#11152f]"
        >
          <span className="text-[19px] leading-none">
            ‹
          </span>

          <span>
            Back
          </span>
        </button>

        {/* Progress */}
        <div className="mt-10 flex w-full gap-3">
          <div className="h-[5px] flex-1 rounded-full bg-[#5068ed]" />
          <div className="h-[5px] flex-1 rounded-full bg-[#5068ed]" />
          <div className="h-[5px] flex-1 rounded-full bg-[#11152f]" />
        </div>

        {/* Step Label */}
        <p className="mt-7 text-[10.5px] font-mono font-medium tracking-[0.16em] text-[#7c828e]">
          STEP 3 OF 3 · TERMS &amp; AUTHORIZATION
        </p>

        {/* Heading */}
        <h1 className="mt-4 text-[24px] font-bold leading-[29px] tracking-[-0.02em] text-[#14171f]">
          Review and confirm
        </h1>

        {/* Description */}
        <p className="mt-4 text-[14px] leading-[21px] text-[#68758d]">
          One last step before we create{" "}
          <strong className="font-semibold text-[#59657b]">
            ABC Technologies Pvt Ltd&apos;s
          </strong>{" "}
          workspace.
        </p>

        {/* Agreement Card */}
        <div className="mt-9 rounded-[10px] border border-[#e1e5ec] bg-[#fbfcfe] px-5 py-5">
          <div className="flex flex-col gap-5">

            {/* Terms and Privacy */}
            <label className="flex cursor-pointer items-start gap-3">
              <input
                type="checkbox"
                checked={termsAccepted}
                onChange={(event) =>
                  setTermsAccepted(event.target.checked)
                }
                className="mt-[3px] h-4 w-4 shrink-0 accent-[#11152f]"
              />

              <span className="text-[13px] leading-[21px] text-[#59657b]">
                I have read and agree to the{" "}
                <span className="font-semibold text-[#4161ef]">
                  Terms of Service
                </span>{" "}
                and{" "}
                <span className="font-semibold text-[#4161ef]">
                  Privacy Policy
                </span>
                .
              </span>
            </label>

            {/* Authorization */}
            <label className="flex cursor-pointer items-start gap-3">
              <input
                type="checkbox"
                checked={authorizationAccepted}
                onChange={(event) =>
                  setAuthorizationAccepted(event.target.checked)
                }
                className="mt-[3px] h-4 w-4 shrink-0 accent-[#11152f]"
              />

              <span className="text-[13px] leading-[21px] text-[#59657b]">
                I confirm that I am authorized to register{" "}
                <strong className="font-semibold text-[#59657b]">
                  ABC Technologies Pvt Ltd
                </strong>{" "}
                on One Enterprise, and I accept responsibility as its Super
                Administrator.
              </span>
            </label>

            {/* Data Processing */}
            <label className="flex cursor-pointer items-start gap-3">
              <input
                type="checkbox"
                checked={dataProcessingAccepted}
                onChange={(event) =>
                  setDataProcessingAccepted(event.target.checked)
                }
                className="mt-[3px] h-4 w-4 shrink-0 accent-[#11152f]"
              />

              <span className="text-[13px] leading-[21px] text-[#59657b]">
                I agree to the{" "}
                <span className="font-semibold text-[#4161ef]">
                  Data Processing Agreement
                </span>{" "}
                governing how organization data is stored and processed.
              </span>
            </label>

            {/* Optional Updates */}
            <label className="flex cursor-pointer items-start gap-3">
              <input
                type="checkbox"
                checked={updatesAccepted}
                onChange={(event) =>
                  setUpdatesAccepted(event.target.checked)
                }
                className="mt-[3px] h-4 w-4 shrink-0 accent-[#11152f]"
              />

              <span className="text-[13px] leading-[21px] text-[#59657b]">
                Send me product updates and security notices by email

                <span className="ml-3 text-[9px] font-medium tracking-[0.12em] text-[#9aa5ba]">
                  OPTIONAL
                </span>
              </span>
            </label>

          </div>
        </div>

        {/* Create Account Button */}
        <button
          type="button"
          disabled={!canCreateAccount}
          onClick={handleCreateAccount}
          className={`mt-3 h-[46px] w-full rounded-[9px] text-[14px] font-semibold transition ${
            canCreateAccount
              ? "bg-[#11152f] text-white hover:bg-[#0b0e27]"
              : "cursor-not-allowed bg-[#e9edf5] text-[#98a2b3]"
          }`}
        >
          Create account
        </button>

        {/* Divider */}
        <div className="mt-6 border-t border-[#e5e8ee]" />

        {/* Sign In */}
        <p className="mt-6 text-center text-[13px] text-[#778197]">
          Already have an organization?{" "}
          <button
            type="button"
            onClick={() => navigate("/signin")}
            className="font-semibold text-[#4161ef] hover:underline"
          >
            Sign in
          </button>
        </p>

      </div>
    </div>
  );
};

export default ReviewConfirmPage;