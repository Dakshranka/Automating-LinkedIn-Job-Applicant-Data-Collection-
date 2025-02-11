## Automating LinkedIn Job Applicant Data Collection
# 📌 Overview
This project automates the process of fetching resumes from Gmail, extracting details, and uploading them to Google Sheets & Google Drive.
# ✨ Features

- ✅ Fetches emails labeled as "Job Application" from Gmail.
- ✅ Extracts PDF attachments (resumes) from emails.
- ✅ Parses name, email, and phone number from the resume.
- ✅ Checks for duplicate resumes in Google Drive before uploading.
- ✅ Uploads resumes to Google Drive and stores the link.
- ✅ Saves resume details (name, email, phone, resume link) in Google Sheets.
- ✅ Ensures duplicate email handling, preventing multiple processing.
- ✅ HR Dashboard displays data from Google Sheets for easy retrieval.

# 🔧 1. Prerequisites

* 📌 1.1 Google Account Setup

- ✔️ A Google Account with access to Google Drive & Google Sheets.
- ✔️ Enable Google Drive API & Google Sheets API.

* 📌 1.2 Python & Virtual Environment

- ✔️ Install Python (>= 3.8).
- ✔️ Create a virtual environment (recommended):
```md
```sh
python -m venv venv  
source venv/bin/activate   # Mac/Linux  
venv\Scripts\activate      # Windows
````
# 🔑 2. API Setup & Authentication

#  📌 2.1 Enable Google Drive & Sheets API

- 1️⃣ Go to Google Cloud Console.
- 2️⃣ Create a new project (or select an existing one).
- 3️⃣ Enable the following APIs:

  1. Google Drive API
  2. Google Sheets API
  3. Gmail API

# 📌 2.2 Create Service Account Credentials

- 1️⃣ Go to APIs & Services > Credentials.
- 2️⃣ Click + Create Credentials > Service Account.
- 3️⃣ Download the JSON credentials file and store it in the project directory.

# 📩 3. Gmail Setup - Label & Filters

# 📌 3.1 Create a Gmail Label

- 1️⃣ Open Gmail and go to Settings ⚙️.
- 2️⃣ Click "See all settings" > "Labels".
- 3️⃣ Scroll down and click "Create New Label".
- 4️⃣ Name it "Job Application" and save.

# 📌 3.2 Create a Gmail Filter

- 1️⃣ Click the Search bar > Show search options.
- 2️⃣ Set the filters:

  1. Subject contains: "Job Application"
  2. Has attachment: ✅ checked
  3. File type: .pdf
- 3️⃣ Click Create filter, then:
   - Apply label "Job Application"
   - Click Create filter again.

# ⚙️ 4. Installation of Dependencies
* 📌 4.1 Install Required Libraries
```md
  pip install -r requirements.txt
````
# 🖥️ 5. Code Explanation & Execution

# 📌 5.1 gmail_fetch.py - Fetch & Download Resumes

- ✔️ Connects to Gmail using IMAP.
- ✔️ Fetches emails under the label "Job Application".
- ✔️ Extracts PDF resumes and saves them locally.
- ✔️ Prevents duplicate processing using processed_emails.txt.

# 📌 5.2 google_sheets.py - Upload to Google Sheets & Drive

- ✔️ Extracts text from resumes using pdfplumber.
- ✔️ Extracts name, email, and phone.
- ✔️ Uploads resume to Google Drive (avoiding duplicates).
- ✔️ Adds details to Google Sheets (avoiding duplicates).

# 📌 5.3 dashboard.py - Streamlit Dashboard

- ✔️ Google Sheets Integration – Fetches and updates applicant data seamlessly.
- ✔️ Resume Links – Displays resumes as clickable hyperlinks for quick access.
- ✔️ Search & Filter – Allows searching by name, email, or phone number.
- ✔️ Downloadable Data – Exports applicant data in CSV or Excel format.
- ✔️ Custom UI – Uses a logo, custom styling, and enhanced UI elements.

# 📌 5.4 app.py - Main File to Run the Setup

- ✔️ Streamlit Dashboard Integration – Automatically starts the dashboard and opens it in a browser.
- ✔️ Email Fetching & Resume Processing – Fetches emails, extracts resumes, and processes data.
- ✔️ Google Drive & Sheets Sync – Uploads resumes to Google Drive and updates Google Sheets, avoiding duplicates.
- ✔️ Automated Scheduling – Runs Gmail fetching and resume processing every 5 minutes using schedule.
- ✔️ Flask API Endpoints – Provides API routes to manually trigger email fetching and resume processing.

# 🚀 6. How to Run the Script

- 📌 6.1 Start the Automation
```md
python app.py
```
- 📌 6.2 Access the API
Open http://localhost:5000/ for API status.
Use the following endpoints:
```md
POST /process_resumes  # Manually process resumes
POST /fetch_gmail      # Manually fetch emails
```
- 📌 6.3 Streamlit Dashboard
The dashboard automatically starts at:
http://localhost:8501/




