# Google Sheets API – Entreprenörspipeline

Denna demo visar hur du kopplar Python till Google Sheets med `gspread` och `oauth2client` och hur du kan bygga ett enkelt arbetsflöde:

**Leads → Offers → Invoices**

## 1) Skapa Google-projekt + Service Account
1. Gå till **Google Cloud Console** och skapa ett projekt.
2. Aktivera **Google Sheets API** och **Google Drive API** för projektet.
3. Skapa ett **Service Account** under *APIs & Services → Credentials*.
4. Generera en **JSON-nyckel** (Add Key → Create new key → JSON) och ladda ner filen.
5. Notera servicekontots e‑postadress.

## 2) Dela ditt kalkylblad
Skapa eller öppna ett Google Sheet och **dela** det med servicekontots e‑postadress (Editor-rättigheter).

## 3) Lägg in JSON-nyckeln i projektet
Spara filen som `credentials.json` i projektmappen (byt ut innehållet i den befintliga placeholdern).

## 4) Installera beroenden
```bash
pip install -r requirements.txt
```

## 5) Kör pipeline-demo
```bash
python pipeline_demo.py --sheet "DittSheetNamn"
```
Skriptet lägger till ett lead, konverterar det till ett offer och därefter en invoice. Därefter skrivs alla steg ut i terminalen.

## Filer
- `sheets_client.py` – enkel wrapper runt gspread.
- `pipeline.py` – hanterar logiken för Leads → Offers → Invoices.
- `pipeline_demo.py` – exempel på hur du använder pipelinen.
- `credentials.json` – placeholder, ersätt med din riktiga nyckel.

## Vanliga fel
- **403/404**: Kalkylbladet är inte delat med servicekontot.
- **Invalid grant**: felaktigt `credentials.json`.
- **Worksheet not found**: fliken du angav finns inte.

Lycka till!
