from typing import List, Any, Optional
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file",
]


class SheetsClient:
    """
    Enkel wrapper runt gspread för att arbeta med en worksheet i ett Google Sheet.
    """

    def __init__(self, credentials_path: str, spreadsheet_name: str, worksheet_name: str = "Sheet1"):
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, SCOPES)
        self.gc = gspread.authorize(creds)
        self.sh = self.gc.open(spreadsheet_name)
        try:
            self.ws = self.sh.worksheet(worksheet_name)
        except gspread.WorksheetNotFound:
            self.ws = self.sh.add_worksheet(title=worksheet_name, rows=100, cols=26)

    def ensure_headers(self, headers: List[str]) -> None:
        values = self.ws.get_all_values()
        if not values:
            self.ws.append_row(headers)
        else:
            current = values[0]
            if current != headers:
                self.ws.update("A1", [headers])

    def append_row(self, row: List[Any]) -> None:
        self.ws.append_row(row, value_input_option="USER_ENTERED")

    def read_all(self) -> List[List[str]]:
        return self.ws.get_all_values()

    def update_cell(self, row: int, col: int, value: Any) -> None:
        self.ws.update_cell(row, col, value)

    def find_first(self, query: str) -> Optional[gspread.cell.Cell]:
        try:
            return self.ws.find(query)
        except gspread.exceptions.CellNotFound:
            return None
