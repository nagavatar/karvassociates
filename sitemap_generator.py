#!/usr/bin/env python3
"""
Sitemap Generator for K A R V & Associates LLP
Generates SEO URLs for CA services across India
"""

import os
import glob
from datetime import datetime

# ================= CONFIGURATION =================
BASE_URL = "https://nagavatar.github.io/karvassociates"
SITEMAP_DIR = "sitemaps"
TODAY = datetime.now().strftime("%Y-%m-%d")

os.makedirs(SITEMAP_DIR, exist_ok=True)

# ================= EXISTING PAGES =================
def get_existing_pages():
    pages = []
    pages.append({"loc": f"{BASE_URL}/", "priority": "1.0", "changefreq": "weekly"})
    if os.path.exists("index.html"):
        pages.append({"loc": f"{BASE_URL}/index.html", "priority": "1.0", "changefreq": "weekly"})
    for page in sorted(glob.glob("pages/*.html")):
        pages.append({"loc": f"{BASE_URL}/pages/{os.path.basename(page)}", "priority": "0.9", "changefreq": "monthly"})
    for page in sorted(glob.glob("blogs/*.html")):
        pages.append({"loc": f"{BASE_URL}/blogs/{os.path.basename(page)}", "priority": "0.8", "changefreq": "monthly"})
    if os.path.exists("links.html"):
        pages.append({"loc": f"{BASE_URL}/links.html", "priority": "0.6", "changefreq": "monthly"})
    return pages

# ================= CA SERVICES =================
CA_SERVICES = [
    # GST Services
    "gst-registration", "gst-return-filing", "gstr-1-filing", "gstr-3b-filing",
    "gst-annual-return", "gst-audit", "gst-refund", "gst-consultant", "gst-compliance",
    "gst-e-way-bill", "gst-input-tax-credit", "gst-advisory", "gst-litigation",
    # Income Tax
    "income-tax-filing", "itr-filing", "itr-1-filing", "itr-2-filing", "itr-3-filing",
    "itr-4-filing", "itr-5-filing", "itr-6-filing", "tax-planning", "tax-consultant",
    "tax-audit", "tds-return-filing", "tds-compliance", "advance-tax-payment",
    "capital-gains-tax", "nri-tax-filing", "salary-tax-planning",
    # Company Registration
    "company-registration", "private-limited-company-registration", "llp-registration",
    "opc-registration", "partnership-firm-registration", "startup-registration",
    "public-limited-company", "section-8-company", "nidhi-company-registration",
    # Business Registrations
    "msme-registration", "udyam-registration", "fssai-registration", "fssai-license",
    "trademark-registration", "import-export-code", "iec-registration",
    "epf-registration", "esi-registration", "professional-tax-registration",
    "shop-act-license", "trade-license", "drug-license", "iso-certification",
    # Audit Services
    "statutory-audit", "internal-audit", "stock-audit", "forensic-audit",
    "compliance-audit", "concurrent-audit", "management-audit", "bank-audit",
    "trust-audit", "ngo-audit", "cooperative-society-audit",
    # Accounting
    "bookkeeping-services", "accounting-services", "payroll-services", "virtual-cfo",
    "accounts-outsourcing", "financial-reporting", "cash-flow-management",
    "bank-reconciliation", "inventory-accounting",
    # Compliance
    "roc-compliance", "annual-compliance", "director-kyc", "company-closure",
    "llp-closure", "strike-off-company", "din-registration", "dsc-registration",
    "share-transfer", "director-appointment", "registered-office-change",
    # General CA
    "chartered-accountant", "ca-firm", "ca-services", "best-ca", "top-ca",
    "ca-consultant", "accounting-firm", "tax-firm", "audit-firm"
]

# ================= INDIAN CITIES =================
CITIES = [
    # Delhi NCR - Primary Focus
    "noida", "delhi", "new-delhi", "ghaziabad", "gurugram", "gurgaon", "faridabad",
    "greater-noida", "indirapuram", "vaishali", "vasundhara", "crossing-republik",
    "noida-extension", "sector-62-noida", "sector-63-noida", "sector-18-noida",
    "raj-nagar-extension", "kaushambi", "sahibabad",
    # UP Cities
    "lucknow", "kanpur", "agra", "varanasi", "prayagraj", "allahabad", "meerut",
    "aligarh", "bareilly", "moradabad", "gorakhpur", "mathura", "firozabad",
    "muzaffarnagar", "saharanpur", "jhansi", "etawah", "rampur",
    # Uttarakhand
    "dehradun", "haridwar", "rishikesh", "roorkee", "haldwani", "nainital",
    # Haryana
    "panipat", "karnal", "rohtak", "hisar", "sonipat", "ambala", "yamunanagar",
    "bhiwani", "sirsa", "jind", "rewari", "palwal",
    # Punjab
    "chandigarh", "ludhiana", "amritsar", "jalandhar", "patiala", "bathinda", "mohali",
    "pathankot", "hoshiarpur", "batala", "moga", "abohar",
    # Rajasthan
    "jaipur", "jodhpur", "udaipur", "kota", "ajmer", "bikaner", "alwar",
    "bharatpur", "sikar", "bhilwara", "pali", "tonk",
    # Major Metros
    "mumbai", "bangalore", "bengaluru", "chennai", "kolkata", "hyderabad", "pune", "ahmedabad",
    # Maharashtra
    "nagpur", "nashik", "thane", "navi-mumbai", "aurangabad", "solapur", "kolhapur",
    "sangli", "satara", "ratnagiri", "ahmednagar",
    # Gujarat
    "surat", "vadodara", "rajkot", "bhavnagar", "jamnagar", "junagadh", "gandhinagar",
    "anand", "nadiad", "bharuch", "vapi", "navsari",
    # South India
    "coimbatore", "madurai", "tiruchirappalli", "salem", "tirunelveli", "erode", "vellore",
    "kochi", "thiruvananthapuram", "kozhikode", "thrissur", "kollam",
    "visakhapatnam", "vijayawada", "guntur", "nellore", "tirupati", "kakinada",
    "mysore", "mangalore", "hubli", "belgaum", "gulbarga", "davangere",
    # East India
    "patna", "gaya", "bhagalpur", "muzaffarpur", "ranchi", "jamshedpur", "dhanbad",
    "bokaro", "bhubaneswar", "cuttack", "rourkela", "guwahati", "silchar",
    # Central India
    "bhopal", "indore", "jabalpur", "gwalior", "ujjain", "raipur", "bhilai", "bilaspur"
]

# ================= GENERATE SEO URLS =================
def generate_seo_urls(limit=15000):
    urls = []
    
    # Pattern 1: service-in-city
    for service in CA_SERVICES:
        for city in CITIES:
            urls.append({"loc": f"{BASE_URL}/services/{service}-in-{city}", "priority": "0.6", "changefreq": "monthly"})
            if len(urls) >= limit: return urls
    
    # Pattern 2: best-service-city
    for service in CA_SERVICES[:25]:
        for city in CITIES[:30]:
            urls.append({"loc": f"{BASE_URL}/services/best-{service}-{city}", "priority": "0.5", "changefreq": "monthly"})
            if len(urls) >= limit: return urls
    
    # Pattern 3: service-near-me-city
    for service in CA_SERVICES[:20]:
        for city in CITIES[:25]:
            urls.append({"loc": f"{BASE_URL}/services/{service}-near-me-{city}", "priority": "0.5", "changefreq": "monthly"})
            if len(urls) >= limit: return urls
    
    # Pattern 4: top-service-city
    for service in CA_SERVICES[:20]:
        for city in CITIES[:25]:
            urls.append({"loc": f"{BASE_URL}/services/top-{service}-{city}", "priority": "0.5", "changefreq": "monthly"})
            if len(urls) >= limit: return urls
    
    # Pattern 5: affordable-service-city
    for service in CA_SERVICES[:15]:
        for city in CITIES[:20]:
            urls.append({"loc": f"{BASE_URL}/services/affordable-{service}-{city}", "priority": "0.4", "changefreq": "monthly"})
            if len(urls) >= limit: return urls
    
    return urls

# ================= XML WRITER =================
def write_sitemap(filepath, urls):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            f.write(f'  <url>\n    <loc>{u["loc"]}</loc>\n    <lastmod>{TODAY}</lastmod>\n')
            f.write(f'    <changefreq>{u["changefreq"]}</changefreq>\n    <priority>{u["priority"]}</priority>\n  </url>\n')
        f.write('</urlset>\n')

def write_sitemap_index(sitemaps):
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        f.write(f'<!-- K A R V & Associates LLP - {len(sitemaps)} sitemaps -->\n')
        for sm in sitemaps:
            f.write(f'  <sitemap>\n    <loc>{BASE_URL}/sitemaps/{sm}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </sitemap>\n')
        f.write('</sitemapindex>\n')

# ================= MAIN =================
def main():
    print("=" * 60)
    print("K A R V & Associates - Sitemap Generator")
    print("=" * 60)
    
    # Get real pages
    existing = get_existing_pages()
    print(f"\n✓ Found {len(existing)} real pages")
    
    # Generate SEO URLs
    seo_urls = generate_seo_urls(15000)
    print(f"✓ Generated {len(seo_urls)} SEO URLs")
    
    # Write sitemaps
    sitemaps = []
    
    # Sitemap 1: Real pages
    write_sitemap(f"{SITEMAP_DIR}/sitemap-main.xml", existing)
    sitemaps.append("sitemap-main.xml")
    print(f"✅ sitemap-main.xml ({len(existing)} URLs)")
    
    # Split SEO URLs into chunks of 10,000
    chunk_size = 10000
    for i, start in enumerate(range(0, len(seo_urls), chunk_size)):
        chunk = seo_urls[start:start + chunk_size]
        filename = f"sitemap-seo-{i+1}.xml"
        write_sitemap(f"{SITEMAP_DIR}/{filename}", chunk)
        sitemaps.append(filename)
        print(f"✅ {filename} ({len(chunk)} URLs)")
    
    # Write index
    write_sitemap_index(sitemaps)
    print(f"\n✅ sitemap.xml (index with {len(sitemaps)} sitemaps)")
    
    total = len(existing) + len(seo_urls)
    print(f"\n{'='*60}\n📊 TOTAL: {total} URLs across {len(sitemaps)} sitemaps\n{'='*60}")

if __name__ == "__main__":
    main()
