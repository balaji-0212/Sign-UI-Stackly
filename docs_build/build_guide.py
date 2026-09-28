# -*- coding: utf-8 -*-
"""
SignIn-UI-Frontend: Complete Project Learning & Architecture Guide Builder
Generates a comprehensive, publication-grade HTML manual and compiles it to PDF via Edge Headless.
"""

import os
import subprocess
import sys

HTML_TEMPLATE_HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>SignIn-UI-Frontend — Complete Project Learning & Architecture Guide</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Cabinet+Grotesk:wght@700;800;900&display=swap');

  @page {
    size: A4;
    margin: 18mm 16mm 18mm 16mm;
    @bottom-right {
      content: counter(page);
      font-family: 'JetBrains Mono', monospace;
      font-size: 8pt;
      color: #94a3b8;
    }
    @bottom-left {
      content: "SignIn-UI-Frontend — Architecture & Learning Guide";
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8pt;
      color: #94a3b8;
    }
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    line-height: 1.6;
    font-size: 10.5pt;
    font-feature-settings: "cv02", "cv03", "cv04", "cv11";
  }

  /* Page Break Utilities */
  .page-break {
    page-break-after: always;
    break-after: page;
  }
  .avoid-break {
    page-break-inside: avoid;
    break-inside: avoid;
  }

  /* Cover Page */
  .cover {
    min-height: 92vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 40px 20px;
    border-bottom: 3px solid #2563eb;
  }
  .cover-top {
    border-left: 6px solid #2563eb;
    padding-left: 24px;
    margin-top: 40px;
  }
  .cover-badge {
    display: inline-block;
    background: #eff6ff;
    color: #1d4ed8;
    border: 1px solid #bfdbfe;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9pt;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 9999px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 20px;
  }
  .cover-title {
    font-family: 'Cabinet Grotesk', 'Plus Jakarta Sans', sans-serif;
    font-size: 32pt;
    font-weight: 900;
    line-height: 1.15;
    color: #0f172a;
    letter-spacing: -0.03em;
    margin-bottom: 16px;
  }
  .cover-title span {
    color: #2563eb;
  }
  .cover-subtitle {
    font-size: 13pt;
    color: #475569;
    max-width: 620px;
    line-height: 1.5;
    font-weight: 400;
  }
  .cover-meta {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 24px;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    margin-top: 40px;
  }
  .meta-item {
    font-size: 9pt;
  }
  .meta-label {
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    font-weight: 600;
    color: #64748b;
    letter-spacing: 0.08em;
    margin-bottom: 2px;
  }
  .meta-val {
    font-weight: 700;
    color: #0f172a;
  }

  /* Typography */
  h1, h2, h3, h4, h5 {
    color: #0f172a;
    font-weight: 800;
    letter-spacing: -0.02em;
    line-height: 1.25;
  }
  h1 {
    font-size: 20pt;
    margin-top: 36px;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 2px solid #e2e8f0;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  h1 .chapter-num {
    background: #2563eb;
    color: #ffffff;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11pt;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 6px;
  }
  h2 {
    font-size: 14pt;
    margin-top: 24px;
    margin-bottom: 12px;
    color: #1e293b;
    border-left: 4px solid #3b82f6;
    padding-left: 10px;
  }
  h3 {
    font-size: 11.5pt;
    margin-top: 18px;
    margin-bottom: 8px;
    color: #334155;
  }
  p {
    margin-bottom: 12px;
    color: #334155;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 9pt;
  }
  th, td {
    border: 1px solid #cbd5e1;
    padding: 8px 12px;
    text-align: left;
    vertical-align: top;
  }
  th {
    background-color: #f1f5f9;
    font-weight: 700;
    color: #0f172a;
  }
  tr:nth-child(even) {
    background-color: #f8fafc;
  }

  /* Code & Syntax */
  code {
    font-family: 'JetBrains Mono', Consolas, monospace;
    background: #f1f5f9;
    color: #0f172a;
    padding: 1.5px 5px;
    border-radius: 4px;
    font-size: 8.5pt;
    border: 1px solid #e2e8f0;
  }
  pre {
    background: #0f172a;
    color: #f8fafc;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8pt;
    line-height: 1.45;
    padding: 14px 16px;
    border-radius: 8px;
    overflow-x: auto;
    margin: 14px 0;
    border: 1px solid #1e293b;
  }
  pre code {
    background: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: inherit;
  }
  .kw { color: #f43f5e; font-weight: 600; }
  .fn { color: #38bdf8; }
  .str { color: #a3e635; }
  .cmt { color: #94a3b8; font-style: italic; }
  .typ { color: #fbbf24; }
  .prop { color: #c084fc; }

  /* Callout Boxes */
  .callout {
    border-radius: 8px;
    padding: 12px 16px;
    margin: 14px 0;
    font-size: 9pt;
    border-left: 4px solid;
  }
  .callout-note {
    background: #eff6ff;
    border-left-color: #2563eb;
    color: #1e40af;
  }
  .callout-tip {
    background: #f0fdf4;
    border-left-color: #16a34a;
    color: #166534;
  }
  .callout-warning {
    background: #fffbeb;
    border-left-color: #d97706;
    color: #92400e;
  }
  .callout-interview {
    background: #faf5ff;
    border-left-color: #9333ea;
    color: #6b21a8;
  }
  .callout-title {
    font-weight: 700;
    text-transform: uppercase;
    font-size: 7.5pt;
    letter-spacing: 0.08em;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  /* Diagrams */
  .diagram-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 14px;
    margin: 16px 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    line-height: 1.4;
    white-space: pre-wrap;
    color: #0f172a;
  }
  .diagram-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 700;
    font-size: 9.5pt;
    color: #334155;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  /* Grid & Flex Layouts for visual cards */
  .card-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin: 14px 0;
  }
  .card {
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 12px;
    background: #ffffff;
  }
  .card-header {
    font-weight: 700;
    font-size: 9.5pt;
    color: #0f172a;
    margin-bottom: 4px;
  }
  .card-body {
    font-size: 8.5pt;
    color: #64748b;
  }

  /* Checklist */
  .checklist {
    list-style: none;
    margin: 12px 0;
  }
  .checklist li {
    padding: 4px 0;
    display: flex;
    align-items: flex-start;
    gap: 8px;
    font-size: 9pt;
  }
  .check-box {
    width: 14px;
    height: 14px;
    border: 1.5px solid #2563eb;
    border-radius: 3px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-top: 2px;
    color: #2563eb;
    font-weight: bold;
    font-size: 10px;
    background: #eff6ff;
  }

  /* Table of Contents */
  .toc-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px 24px;
    margin-top: 20px;
  }
  .toc-item {
    display: flex;
    justify-content: space-between;
    font-size: 8.5pt;
    border-bottom: 1px dotted #cbd5e1;
    padding: 3px 0;
  }
  .toc-title {
    font-weight: 500;
    color: #1e293b;
  }
  .toc-num {
    font-family: 'JetBrains Mono', monospace;
    color: #64748b;
  }
</style>
</head>
<body>
"""

HTML_TEMPLATE_FOOTER = """
</body>
</html>
"""

print("Writing template header & footer ready...")
