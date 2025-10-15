from tabulate import tabulate

def brief(text, max_len=40):
    """Truncate text to max_len characters, taking only the first line."""
    if not text:
        return ""
    s = str(text).strip().splitlines()[0]  # First line only
    if len(s) > max_len:
        return s[:max_len - 1] + "…"
    return s

def display_table(leads):
    if not leads:
        print("\n⚠️ No leads found.\n")
        return

    table = []
    for i, lead in enumerate(leads, 1):
        table.append([
            i,  # Add row number for reference
            lead.get("company_name", ""),
            brief(lead.get("company_website", ""), 25),
            lead.get("industry", ""),
            brief(lead.get("product_services", ""), 30),
            f"{lead.get('hq_city', '')}, {lead.get('hq_state', '')}",
            lead.get("year_founded", ""),
            lead.get("ceo_name", ""),
            # lead.get("source", ""),
            # brief(lead.get("operational_fit", ""), 25),
            # brief(lead.get("ethical_alignment", ""), 25),
            # brief(lead.get("growth_signals", ""), 25),
            # brief(lead.get("research_notes", ""), 30)
        ])

    headers = [
        "#", "Company", "Website", "Industry", "Product/Services",
        "Location", "Founded", "CEO", 
        # "Source",
        # "Operational Fit", "Ethical Alignment", "Growth Signals",
        # "Research Notes"
    ]

    print("\n📊 Lead Overview:\n")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    print(f"\n💡 Showing {len(leads)} leads. Use 'Format First Lead' or export options for full details.\n")

def display_lead_summary(leads):
    """Alternative: Show only essential fields for quick overview"""
    if not leads:
        print("\n⚠️ No leads found.\n")
        return

    table = []
    for i, lead in enumerate(leads, 1):
        table.append([
            i,
            lead.get("company_name", ""),
            lead.get("industry", ""),
            f"{lead.get('hq_city', '')}, {lead.get('hq_state', '')}",
            lead.get("year_founded", ""),
            # lead.get("source", ""),
            # brief(lead.get("operational_fit", ""), 40)
        ])

    headers = [
        "#", "Company", "Industry", "Location", "Founded", "Source", 
        # "Operational Fit"
    ]

    print("\n📊 Lead Summary:\n")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    print(f"\n💡 Showing {len(leads)} leads. Use menu options for detailed view or exports.\n")
