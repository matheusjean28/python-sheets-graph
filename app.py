from dotenv import load_dotenv
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# You should create a .env file with yours configuration files.
# Latter i´ll put a .md step-by-step setup at this repo


# ensure that .evn is loaded automatic 
load_dotenv()

filename = os.getenv("FILENAME")
planilha_id = os.getenv("PLANILHA_ID")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    filename,
    SCOPES
)

client = gspread.authorize(creds)

planilha = client.open_by_key(planilha_id)
sheet = planilha.get_worksheet(0)
dados = sheet.get_all_records()

print(dados)
