from typing import List
from sheets_client import SheetsClient


class EntrepreneurPipeline:
    """Pipeline med tre steg: Leads -> Offers -> Invoices."""

    LEAD_HEADERS = ["id", "namn", "email", "telefon", "status"]
    OFFER_HEADERS = ["id", "lead_id", "beskrivning", "belopp", "status"]
    INVOICE_HEADERS = ["id", "offer_id", "belopp", "betald"]

    def __init__(self, credentials: str, spreadsheet: str):
        self.leads = SheetsClient(credentials, spreadsheet, "Leads")
        self.offers = SheetsClient(credentials, spreadsheet, "Offers")
        self.invoices = SheetsClient(credentials, spreadsheet, "Invoices")

        self.leads.ensure_headers(self.LEAD_HEADERS)
        self.offers.ensure_headers(self.OFFER_HEADERS)
        self.invoices.ensure_headers(self.INVOICE_HEADERS)

    def add_lead(self, lead_id: str, name: str, email: str = "", phone: str = "") -> None:
        self.leads.append_row([lead_id, name, email, phone, "lead"])

    def list_leads(self) -> List[List[str]]:
        return self.leads.read_all()

    def convert_lead_to_offer(self, lead_id: str, offer_id: str, description: str, amount: str) -> None:
        rows = self.leads.read_all()
        for i, row in enumerate(rows[1:], start=2):
            if row[0] == lead_id:
                self.leads.update_cell(i, self.LEAD_HEADERS.index("status") + 1, "offer")
                break
        else:
            raise ValueError(f"Lead {lead_id} hittades inte")

        self.offers.append_row([offer_id, lead_id, description, amount, "offer"])

    def list_offers(self) -> List[List[str]]:
        return self.offers.read_all()

    def convert_offer_to_invoice(self, offer_id: str, invoice_id: str, amount: str) -> None:
        rows = self.offers.read_all()
        for i, row in enumerate(rows[1:], start=2):
            if row[0] == offer_id:
                self.offers.update_cell(i, self.OFFER_HEADERS.index("status") + 1, "invoice")
                break
        else:
            raise ValueError(f"Offer {offer_id} hittades inte")

        self.invoices.append_row([invoice_id, offer_id, amount, "nej"])

    def list_invoices(self) -> List[List[str]]:
        return self.invoices.read_all()
