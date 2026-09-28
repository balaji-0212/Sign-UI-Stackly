# -*- coding: utf-8 -*-
"""
SignIn-UI-Frontend Guide Compiler
Assembles all chapter parts into an HTML manual and compiles to PDF via Edge Headless.
"""

import os
import subprocess
import sys
import time

from build_guide import HTML_TEMPLATE_HEADER, HTML_TEMPLATE_FOOTER
from chapters_part1 import get_part1_html
from chapters_part2 import get_part2_html
from chapters_part3 import get_part3_html
from chapters_part4 import get_part4_html

def compile_manual():
    base_dir = r"D:\Java Enterprise Stackly Project\SignIn-UI-Frontend"
    docs_dir = os.path.join(base_dir, "docs_build")
    html_file = os.path.join(docs_dir, "guide.html")
    pdf_file = os.path.join(base_dir, "SignIn-UI-Frontend_Complete_Learning_Guide.pdf")

    print("[1/3] Assembling HTML Document...")
    full_html = (
        HTML_TEMPLATE_HEADER +
        get_part1_html() +
        get_part2_html() +
        get_part3_html() +
        get_part4_html() +
        HTML_TEMPLATE_FOOTER
    )

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"      HTML manual written: {html_file} ({len(full_html):,} bytes)")

    print("[2/3] Compiling to PDF via Edge Headless...")
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    edge_exe = None
    for p in edge_paths:
        if os.path.exists(p):
            edge_exe = p
            break

    if not edge_exe:
        print("ERROR: Microsoft Edge not found in standard paths.")
        sys.exit(1)

    print(f"      Using browser engine: {edge_exe}")
    
    # Chromium file URI requires forward slashes
    file_uri = "file:///" + html_file.replace("\\", "/")

    cmd = [
        edge_exe,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_file}",
        file_uri
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    print(f"      Browser exit code: {result.returncode}")

    print("[3/3] Verifying Generated PDF...")
    time.sleep(2)
    if os.path.exists(pdf_file):
        size_bytes = os.path.getsize(pdf_file)
        size_kb = size_bytes / 1024
        size_mb = size_kb / 1024
        print(f"SUCCESS: PDF generated successfully!")
        print(f"Destination: {pdf_file}")
        print(f"File Size:   {size_mb:.2f} MB ({size_bytes:,} bytes)")
    else:
        print(f"ERROR: PDF file not found at {pdf_file}")
        sys.exit(1)

if __name__ == "__main__":
    compile_manual()
