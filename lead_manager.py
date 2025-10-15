import sys
from utils.io import load_leads, save_leads, export_formatted, export_to_csv, export_to_excel
from utils.formatter import format_lead
from utils.table import display_table
from datetime import date

LEAD_SOURCES = [
    "LinkedIn", "Crunchbase", "Referral", "Website Form", "Event", "Sales Outreach", "Other"
]

def get_valid_input(prompt, validator, multiline=False):
    if not multiline:
        while True:
            try:
                value = input(prompt).strip()
                return validator(value)
            except ValueError as e:
                print(f"❌ {e} Please try again.\n")
    else:
        while True:
            print(f"{prompt} (Type 'END' on a new line to finish):")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                lines.append(line)
            value = "\n".join(lines).strip()
            try:
                return validator(value)
            except ValueError as e:
                print(f"❌ {e} Please try again.\n")

def add_lead(leads):
    print("\n🔹 Enter New Lead Info:")

    company_name = get_valid_input("Company Name: ", lambda v: v if v else (_ for _ in ()).throw(ValueError("Company name cannot be empty.")))
    company_website = get_valid_input("Company Website: ", lambda v: v if v.startswith("http") else (_ for _ in ()).throw(ValueError("Must start with http or https.")))
    company_linkedin = get_valid_input("Company LinkedIn: ", lambda v: v if v.startswith("http") else (_ for _ in ()).throw(ValueError("Must start with http or https.")))
    industry = get_valid_input("Industry: ", lambda v: v if v else (_ for _ in ()).throw(ValueError("Industry cannot be empty.")))
    product_services = get_valid_input("Product/Services: ", lambda v: v if v else (_ for _ in ()).throw(ValueError("Product/Services cannot be empty.")))
    hq_state = get_valid_input("HQ State: ", lambda v: v if v else (_ for _ in ()).throw(ValueError("HQ State cannot be empty.")))
    hq_city = get_valid_input("HQ City: ", lambda v: v if v else (_ for _ in ()).throw(ValueError("HQ City cannot be empty.")))
    year_founded = get_valid_input("Year Founded (after 2000): ", lambda v: int(v) if v.isdigit() and int(v) > 2000 else (_ for _ in ()).throw(ValueError("Must be a year after 2000.")))
    ceo_name = get_valid_input("CEO Name: ", lambda v: v if v else (_ for _ in ()).throw(ValueError("CEO name cannot be empty.")))
    source = get_valid_input("Lead Source (Choose or type): " + ", ".join(LEAD_SOURCES) + ": ", lambda v: v if v else (_ for _ in ()).throw(ValueError("Source cannot be empty.")))
    operational_fit = get_valid_input("Operational Fit", lambda v: v if v else (_ for _ in ()).throw(ValueError("Operational Fit cannot be empty.")), multiline=True)
    ethical_alignment = get_valid_input("Ethical Alignment", lambda v: v if v else (_ for _ in ()).throw(ValueError("Ethical Alignment cannot be empty.")), multiline=True)
    growth_signals = get_valid_input("Growth Signals", lambda v: v if v else (_ for _ in ()).throw(ValueError("Growth Signals cannot be empty.")), multiline=True)

    # Research notes with a suggested template
    research_template = (
        "Sources consulted: \n"
        "Confidence level: \n"
        "Conflicting info or gaps: \n"
        f"Date of research: {date.today()}"
    )
    research_notes = get_valid_input(
        f"Research Notes/Context (suggested template below, type END to finish):\n{research_template}\n",
        lambda v: v,
        multiline=True
    )

    new_lead = {
        "company_name": company_name,
        "company_website": company_website,
        "company_linkedin": company_linkedin,
        "industry": industry,
        "product_services": product_services,
        "hq_state": hq_state,
        "hq_city": hq_city,
        "year_founded": year_founded,
        "ceo_name": ceo_name,
        "source": source,
        "operational_fit": operational_fit,
        "ethical_alignment": ethical_alignment,
        "growth_signals": growth_signals,
        "research_notes": research_notes
    }

    leads.append(new_lead)
    save_leads(leads)
    print("\n✅ Lead added successfully.")
    next_action = input("🔁 Return to Lead Manager menu? (Y/N): ").strip().lower()
    if next_action != "y":
        print("👋 Exiting. Good luck with your submission!")
        sys.exit()

def edit_lead(leads):
    name = input("Enter company name to edit: ").strip().lower()
    for lead in leads:
        if lead["company_name"].lower() == name:
            print(f"\n✏️ Editing lead: {lead['company_name']}")
            print("Press Enter to keep current value.\n")

            def edit_field(field, label, validator=str, multiline=False):
                current = lead.get(field, "")
                prompt = f"{label} [{current}]: "
                if not multiline:
                    value = input(prompt).strip()
                    if value:
                        try:
                            lead[field] = validator(value)
                        except ValueError as e:
                            print(f"❌ {e} Keeping old value.\n")
                else:
                    print(f"{label} [{current}] (Type 'END' to finish):")
                    lines = []
                    while True:
                        line = input()
                        if line.strip().upper() == "END":
                            break
                        lines.append(line)
                    value = "\n".join(lines).strip()
                    if value:
                        lead[field] = value

            for var, label in [
                ("company_website", "Company Website"), ("company_linkedin", "Company LinkedIn"),
                ("industry", "Industry"), ("product_services", "Product/Services"),
                ("hq_state", "HQ State"), ("hq_city", "HQ City"), ("year_founded", "Year Founded"),
                ("ceo_name", "CEO Name"), ("source", "Lead Source"),
                ("operational_fit", "Operational Fit"), ("ethical_alignment", "Ethical Alignment"),
                ("growth_signals", "Growth Signals"), ("research_notes", "Research Notes/Context")
            ]:
                multiline = var in ["operational_fit", "ethical_alignment", "growth_signals", "research_notes"]
                edit_field(var, label, multiline=multiline)

            save_leads(leads)
            print("✅ Lead updated.\n")
            return

    print(f"⚠️ Lead '{name}' not found.\n")

def delete_lead(leads):
    name = input("Enter company name to delete: ")
    updated = [lead for lead in leads if lead['company_name'].lower() != name.lower()]
    if len(updated) < len(leads):
        save_leads(updated)
        print(f"✅ Lead '{name}' deleted.\n")
    else:
        print(f"⚠️ Lead '{name}' not found.\n")
    return updated

def menu():
    leads = load_leads()
    while True:
        print("\n📋 Lead Manager Menu:")
        print("1. View All Leads")
        print("2. Add New Lead")
        print("3. Edit Lead")
        print("4. Delete Lead")
        print("5. Format First Lead")
        print("6. Export All Formatted Leads")
        print("7. Export to CSV")
        print("8. Export to Excel")
        print("9. Exit")
        choice = input("Choose an option (1–9): ")

        if choice == "1":
            display_table(leads)
        elif choice == "2":
            add_lead(leads)
        elif choice == "3":
            edit_lead(leads)
        elif choice == "4":
            leads = delete_lead(leads)
        elif choice == "5":
            if leads:
                print(format_lead(leads[0]))
            else:
                print("⚠️ No leads to format.\n")
        elif choice == "6":
            export_formatted(leads)
        elif choice == "7":
            export_to_csv(leads)
        elif choice == "8":
            export_to_excel(leads)
        elif choice == "9":
            print("👋 Exiting. Good luck with your submission!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
