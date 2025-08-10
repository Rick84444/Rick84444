import argparse
from pipeline import EntrepreneurPipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Demo för Entreprenör-pipeline")
    parser.add_argument("--credentials", default="credentials.json")
    parser.add_argument("--sheet", required=True, help="Namn på Google Sheet")
    args = parser.parse_args()

    pipeline = EntrepreneurPipeline(args.credentials, args.sheet)
    pipeline.add_lead("L1", "Första Lead", "lead@example.com", "0700000000")
    pipeline.convert_lead_to_offer("L1", "O1", "Webbdesign", "5000")
    pipeline.convert_offer_to_invoice("O1", "I1", "5000")

    print("Leads:", pipeline.list_leads())
    print("Offers:", pipeline.list_offers())
    print("Invoices:", pipeline.list_invoices())


if __name__ == "__main__":
    main()
