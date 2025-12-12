import os
import re
import requests

def download_pdf_from_drive(drive_url: str, save_path: str):
    """
    Download a PDF from a Google Drive sharing link and save it locally.
    """
    # Try pattern: /d/<FILE_ID>/
    match = re.search(r"/d/([A-Za-z0-9_-]+)", drive_url)
    if match:
        file_id = match.group(1)
    else:
        # Try pattern: ?id=<FILE_ID>
        match = re.search(r"id=([A-Za-z0-9_-]+)", drive_url)
        if match:
            file_id = match.group(1)
        else:
            raise ValueError("❌ Could not extract file ID from the link.")

    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    print(f"📥 Downloading PDF (file ID {file_id})...")

    resp = requests.get(download_url)
    resp.raise_for_status()

    with open(save_path, "wb") as f:
        f.write(resp.content)

    print(f"✅ PDF downloaded → {save_path}")

# Ask for the Drive link
drive_link = input("📌 Paste your Google Drive PDF link here: ").strip()

# Make sure the data folder exists
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# Local path for the PDF
pdf_path = os.path.join(DATA_DIR, "source.pdf")

# Download the PDF
download_pdf_from_drive(drive_link, pdf_path)