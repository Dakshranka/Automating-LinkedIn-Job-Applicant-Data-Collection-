import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from io import BytesIO
from PIL import Image  # ✅ For displaying images

# ✅ Set Page Configurations (Title & Icon)
st.set_page_config(page_title="Job Applicant Dashboard", page_icon="📄", layout="wide")

# ✅ Load and Display Logo at the Top Center
LOGO_PATH = "credentials/logo.jpg"  # Ensure this file exists

col1, col2, col3 = st.columns([0.5,0.2,0.5])  # Create columns for centering
with col2:  # Place logo in the center column
    logo = Image.open(LOGO_PATH)
    st.image(logo, width=130)

# ✅ Apply Custom CSS for Styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .css-18e3th9 {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #4CAF50 !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            font-size: 16px !important;
        }
        .stButton>button:hover {
            background-color: #45a049 !important;
        }
        .stTextInput>div>div>input {
            border-radius: 8px !important;
            border: 1px solid #ccc !important;
            padding: 10px !important;
            font-size: 16px !important;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        tr:hover {
            background-color: #f5f5f5;
        }
        a {
            color: #007BFF;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Authenticate and Fetch Data from Google Sheets
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = r"credentials/gen-lang-client-0033592652-b9ba5445c848.json"  # Ensure this file exists

@st.cache_data
def authenticate_google_sheets():
    try:
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        client = gspread.authorize(creds)
        return client
    except Exception as e:
        st.error(f"❌ Authentication failed: {e}")
        return None

client = authenticate_google_sheets()

# ✅ Fetch Data from Google Sheets
@st.cache_data
def fetch_data():
    if client:
        try:
            SHEET_ID = "1paE3-iuEfZ_4Gtzc4fbktjXMedOqZjTm2m_mw91r1AY"  # Replace with actual Sheet ID
            sheet = client.open_by_key(SHEET_ID).sheet1  # Select first sheet
            data = sheet.get_all_records()  # Fetch data
            df = pd.DataFrame(data)

            # ✅ Convert 'resume_link' column to Clickable Hyperlinks
            if "resume_link" in df.columns:
                df["Resume"] = df["resume_link"].apply(
                    lambda url: f'<a href="{url}" target="_blank">📄 View Resume</a>' if url else "N/A"
                )
                df.drop(columns=["resume_link"], inplace=True)  # Remove original link column
            
            return df
        except Exception as e:
            st.error(f"❌ Failed to fetch data: {e}")
            return pd.DataFrame()
    return pd.DataFrame()

df = fetch_data()

# ✅ Job Applicant Dashboard Title
st.title("📄 Job Applicant Dashboard")
st.markdown("### View and Manage Job Applications")

# ✅ Search & Filter Options
search_query = st.text_input("🔍 Search Applicants (Name, Email, Phone):").strip().lower()

if not df.empty and search_query:
    df = df[df.astype(str).apply(lambda row: row.str.lower().str.contains(search_query, na=False).any(), axis=1)]

# ✅ Display Data in a Table with Resume Links
if not df.empty:
    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)  # Render HTML for clickable links
else:
    st.warning("⚠️ No matching records found.")

# ✅ Download Data as Excel/CSV
st.markdown("### 📥 Download Data")
file_format = st.selectbox("Choose Format", ["CSV", "Excel"])

if st.button("Download"):
    if not df.empty:
        output = BytesIO()
        if file_format == "CSV":
            df.to_csv(output, index=False)
            st.download_button("📥 Download CSV", output.getvalue(), file_name="applicants.csv", mime="text/csv")
        else:
            with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                df.to_excel(writer, index=False)
            st.download_button("📥 Download Excel", output.getvalue(), file_name="applicants.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        st.error("❌ No data available to download.")

st.markdown("---")
st.markdown("⚡ *Built By Daksh Ranka*")
