def format_lead(lead):
    return f"""### 🏢 Lead: {lead.get('company_name', '')}
- **Source**: {lead.get('source', '')}
- **Founded**: {lead.get('year_founded', '')}
- **Location**: {lead.get('hq_city', '')}, {lead.get('hq_state', '')}
- **CEO**: {lead.get('ceo_name', '')}
- **Website**: {lead.get('company_website', '')}
- **LinkedIn**: {lead.get('company_linkedin', '')}
- **Industry**: {lead.get('industry', '')}
- **Product/Services**: {lead.get('product_services', '')}

**Operational Fit**  
{lead.get('operational_fit', '')}

**Ethical Alignment**  
{lead.get('ethical_alignment', '')}

**Growth Signals**  
{lead.get('growth_signals', '')}

**Research Notes/Context**  
{lead.get('research_notes', '')}
"""
