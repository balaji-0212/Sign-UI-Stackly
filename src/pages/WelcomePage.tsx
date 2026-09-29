import React from "react";
import { useNavigate } from "react-router-dom";
import { useOnboarding } from "../context/useOnboarding";

const WelcomePage: React.FC = () => {
  const navigate = useNavigate();

  const { organization, admin } = useOnboarding();

  const organizationName =
    organization.organizationName || "ABC Technologies Pvt Ltd";

  const email =
    admin.officialEmail || "admin@abctech.com";

  return (
    <div className="w-full min-w-0 flex-1 overflow-y-auto bg-white">
      <div className="mx-auto flex w-full max-w-[560px] flex-col items-center px-6 pb-12 pt-10 text-center lg:pt-[100px]">

        {/* Success Icon */}
        <div className="flex h-[64px] w-[64px] items-center justify-center rounded-full bg-[#eaf8ef]">
          <div className="flex h-[40px] w-[40px] items-center justify-center rounded-full bg-[#22a05a]">
            <svg
              width="22"
              height="22"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M5 12.5L9.5 17L19 7.5"
                stroke="white"
                strokeWidth="2.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </div>
        </div>

        {/* Success Label */}
        <p className="mt-7 text-[10.5px] font-mono font-medium tracking-[0.17em] text-[#7c828e]">
          ACCOUNT CREATED SUCCESSFULLY
        </p>

        {/* Heading */}
        <h1 className="mt-4 text-[27px] font-bold leading-[34px] tracking-[-0.025em] text-[#14171f]">
          Welcome to One Enterprise
        </h1>

        {/* Organization */}
        <p className="mt-3 text-[14px] leading-[22px] text-[#64748b]">
          Your workspace for{" "}
          <strong className="font-semibold text-[#30384a]">
            {organizationName}
          </strong>{" "}
          has been created.
        </p>

        {/* Verification Card */}
        <div className="mt-9 w-full rounded-[12px] border border-[#d6e3ff] bg-[#f3f6ff] p-5 text-left">

          <div className="flex items-start gap-3">

            {/* Email Icon */}
            <div className="flex h-[40px] w-[40px] shrink-0 items-center justify-center rounded-[9px] bg-white">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <rect
                  x="3"
                  y="5"
                  width="18"
                  height="14"
                  rx="2"
                  stroke="#4161ef"
                  strokeWidth="1.8"
                />

                <path
                  d="M4 7L12 13L20 7"
                  stroke="#4161ef"
                  strokeWidth="1.8"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </div>

            {/* Verification Information */}
            <div className="min-w-0">

              <h2 className="text-[14px] font-semibold text-[#263252]">
                Verify your work email
              </h2>

              <p className="mt-1 text-[13px] leading-[19px] text-[#61708e]">
                We&apos;ve sent a verification link to:
              </p>

              <p className="mt-1 break-all text-[13px] font-semibold text-[#263252]">
                {email}
              </p>

            </div>

          </div>

          {/* Expiry */}
          <div className="mt-4 border-t border-[#dbe4fa] pt-4">
            <p className="text-[12px] leading-[18px] text-[#68758d]">
              This verification link expires in{" "}
              <strong className="font-semibold text-[#3f4d6b]">
                24 hours
              </strong>
              .
            </p>
          </div>

        </div>

        {/* Go To Sign In */}
        <button
          type="button"
          onClick={() => navigate("/signin")}
          className="mt-6 h-[46px] w-full rounded-[9px] bg-[#11152f] text-[14px] font-semibold text-white transition hover:bg-[#0b0e27]"
        >
          Go to sign in
        </button>

        {/* Resend Verification */}
        <button
          type="button"
          onClick={() => {
            window.alert("Verification email resent.");
          }}
          className="mt-5 text-[13px] font-semibold text-[#4161ef] hover:underline"
        >
          Resend verification email
        </button>

      </div>
    </div>
  );
};

export default WelcomePage;