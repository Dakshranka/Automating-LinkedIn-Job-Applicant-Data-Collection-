####Automating LinkedIn Job Applicant Data Collection
##Documentation:
##Overview:
This project automates the process of fetching resumes from Gmail, extracting details, and uploading them to Google Sheets & Google Drive.
##✨ Features
✔️ Fetches emails labelled as "Job Application" from Gmail.
✔️ Extracts PDF attachments (resumes) from emails.
✔️ Parses name, email, and phone number from the resume.
✔️ Checks for duplicate resumes in Google Drive before uploading
✔️ Uploads the resume to Google Drive and stores the link.
✔️ Saves resume details (name, email, phone, resume link) in Google Sheets.
✔️ Ensures duplicate email handling so resumes are not processed twice.
✔️ All the details from the google sheets has been seen on the dashboard making it easier retrieval for HR. 
##1️. Prerequisites
Make sure you have the following before starting:
#1.1 Google Account Setup
•	A Google Account with access to Google Drive & Google Sheets
•	Enable Google Drive API & Google Sheets API
#1.2 Python & Virtual Environment
•	Install Python (>= 3.8)
•	Create a virtual environment (recommended):


#Command to Create Virtual Environment:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

##2. API Setup & Authentication
#2.1 Enable Google Drive & Sheets API
•	Go to Google Cloud Console: https://console.cloud.google.com/
•	Create a new project (or select an existing one).
#1.	Enable the following APIs:
o	Google Drive API
o	Google Sheets API
o	Gmail API
#2.	Create Service Account Credentials:
o	Go to APIs & Services > Credentials
o	Click + Create Credentials > Service Account
o	Download the JSON credentials file and store it in the project directory.
##3️. Gmail Setup - Label & Filters
#3.1 Create a Gmail Label
1.	Open Gmail and go to Settings ⚙️.
2.	Click "See all settings" > "Labels".
3.	Scroll down and click "Create New Label".
4.	Name it "Job Application" and save.
#3.2 Create a Gmail Filter
1.	In Gmail, click Search bar > Show search options.
2.	Set filters:
o	Subject contains: "Job Application"
o	Has attachment: ✅ checked
o	File type: .pdf
3.	Click Create filter, then:
o	Apply label "Job Application"
o	Click Create filter again.
4. Installation Of Dependencies:
4.1 Install Required Libraries

##Command:
pip install -r requirements.txt
##5. Code Explanation & Execution
#5.1 gmail_fetch.py - Fetch & Download Resumes
•	Connects to Gmail using IMAP.
•	Fetches emails under the label "Job Application".
•	Extracts PDF resumes and saves them locally.
•	Prevents duplicate processing using processed_emails.txt.
#5.2) google_sheets.py - Upload to Google Sheets & Drive
•	Extracts text from resumes using pdfplumber.
•	Extracts name, email, and phone.
•	Uploads resume to Google Drive (avoiding duplicates).
•	Adds details to Google Sheets (avoiding duplicates).
#5.3) dashborad.py- Using streamlit :
•	Google Sheets Integration – Fetches and updates applicant data seamlessly.
•	Resume Links – Displays resumes as clickable hyperlinks for quick access.
•	Search & Filter – Allows searching by name, email, or phone number.
•	Downloadable Data – Exports applicant data in CSV or Excel format.
•	Custom UI – Uses a logo, custom styling, and enhanced UI elements.
#5.4) app.py- It is the main file for running the whole set up
•	Streamlit Dashboard Integration – Automatically starts the dashboard and opens it in a browser.
•	Email Fetching & Resume Processing – Fetches emails, extracts resumes, and processes data.
•	Google Drive & Sheets Sync – Uploads resumes to Google Drive and updates Google Sheets, avoiding duplicates.
•	Automated Scheduling – Runs Gmail fetching and resume processing every 5 minutes using schedule.
•	Flask API Endpoints – Provides API routes to manually trigger email fetching and resume processing.
##How to Run the Script:
#Start the Automation:
python main.py
#Access the API:
•	Open http://localhost:5000/ for API status.
•	Use POST /process_resumes to manually process resumes.
•	Use POST /fetch_gmail to manually fetch emails.
#Streamlit Dashboard:
•	The dashboard automatically starts and opens at http://localhost:8501.

##6) Conclusion
This automation streamlines the process of fetching resumes, extracting key details, and organizing them efficiently in Google Drive and Sheets. By integrating Flask, Streamlit, and scheduling, it ensures a seamless, hands-free operation. With automated email processing and a user-friendly dashboard, managing resumes has never been easier.
🚀 Now, run the script and let automation handle the rest! 🚀






