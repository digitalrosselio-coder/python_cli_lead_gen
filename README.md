<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# READme.md

Here’s a **README.md** for your Lead Manager CLI with all the setup, usage, and workflow details:

***

# Lead Manager CLI

A Python-based command-line lead management system for high-quality research-driven company profiling, ideal for lead generation specialists and B2B outreach.

## Features

- Add, edit, delete, and view leads with structured company data
- Collect and manage fields including company name, website, LinkedIn, industry, products, location, year founded, CEO name, operational fit, ethical alignment, growth signals, and research notes
- Multiple view modes: full table, summary (essential fields), and detailed markdown profile
- CSV, Excel, and Markdown export for reporting or CRM import
- Clean, readable terminal output optimized for long and multiline fields
- Suggested template for research notes, ensuring standardized audit trail for every lead


## Getting Started

### Prerequisites

- Python 3.8+
- pip install packages:
    - pandas
    - openpyxl
    - tabulate


### Installation

Clone the repository and place all files (`lead_manager.py`, `io.py`, `table.py`, `formatter.py`) in the same directory.

```bash
git clone [your-repo-url]
cd lead-manager
pip install pandas openpyxl tabulate
```


### Usage

Run the main manager from terminal:

```bash
python lead_manager.py
```

You'll see an interactive menu:

```
📋 Lead Manager Menu:
1. View All Leads (Full Table)
2. View Lead Summary (Essential Fields)
3. View Lead Details (Individual)
4. Add New Lead
5. Edit Lead
6. Delete Lead
7. Export All Formatted Leads
8. Export to CSV
9. Export to Excel
10. Exit
```

**Tip:**

- Add new leads by entering data as prompted. Use the suggested template for research notes.
- View tables and details for high-level or granular review.
- Export data for reporting, CRM import, or sharing.


## File Structure

- `lead_manager.py` – orchestrates user interaction and workflow
- `io.py` – handles data IO, storage, and export (JSON, CSV, Excel, Markdown)
- `table.py` – outputs tables for all and summary views
- `formatter.py` – pretty-prints each lead in markdown format


## Data Fields

Each lead profile records:

- company_name
- company_website
- company_linkedin
- industry
- product_services
- hq_city
- hq_state
- year_founded
- ceo_name
- source
- operational_fit
- ethical_alignment
- growth_signals
- research_notes


## Example Lead Entry

```json
{
  "company_name": "Acme Tech",
  "company_website": "https://acmetech.com",
  "company_linkedin": "https://linkedin.com/company/acmetech",
  "industry": "Software",
  "product_services": "Cloud Hosting, AI Tools",
  "hq_state": "California",
  "hq_city": "San Diego",
  "year_founded": 2012,
  "ceo_name": "John Smith",
  "source": "LinkedIn",
  "operational_fit": "Strong fit for cloud integration needs.",
  "ethical_alignment": "B-Corp certified, eco-friendly datacenter.",
  "growth_signals": "Recently closed $10M funding.",
  "research_notes": "Sources consulted: LinkedIn, company website\nConfidence level: High\nConflicting info or gaps: None found\nDate of research: 2025-10-15"
}
```


## FAQ

- **Data not showing well in table view?**
Try summary mode, or review Markdown exports for full detail.
- **Want more fields?**
Extend the schema in all .py files as needed.
- **Exported files not opening?**
Ensure `pandas` and `openpyxl` are installed.


## License

MIT License

***

*Feel free to adapt this README for your specific repo or workflow!*

