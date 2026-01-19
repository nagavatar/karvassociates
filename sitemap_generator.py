#!/usr/bin/env python3
"""
Google-Compliant Sitemap Generator for K A R V & Associates LLP
Generates 15,000+ SEO-optimized URLs for CA services across India
"""

import os
import glob
from datetime import datetime
from urllib.parse import quote

# ================= CONFIGURATION =================
# Update this to your actual domain when you have one
BASE_URL = "https://nagavatar.github.io/karvassociates"
SITEMAP_DIR = "sitemaps"
MAX_URLS_PER_SITEMAP = 50000  # Google limit is 50,000 URLs per sitemap
TARGET_URLS = 15000
TODAY = datetime.now().strftime("%Y-%m-%d")

# Create sitemaps directory
os.makedirs(SITEMAP_DIR, exist_ok=True)

# ================= ACTUAL EXISTING PAGES =================
def get_existing_pages():
    """Scan workspace for actual HTML files"""
    pages = []
    
    # Main page
    pages.append({"loc": f"{BASE_URL}/", "priority": "1.0", "changefreq": "weekly"})
    pages.append({"loc": f"{BASE_URL}/index.html", "priority": "1.0", "changefreq": "weekly"})
    
    # Service pages
    service_pages = glob.glob("pages/*.html")
    for page in service_pages:
        filename = os.path.basename(page)
        pages.append({
            "loc": f"{BASE_URL}/pages/{filename}",
            "priority": "0.9",
            "changefreq": "monthly"
        })
    
    # Blog/SEO pages
    blog_pages = glob.glob("blogs/*.html")
    for page in blog_pages:
        filename = os.path.basename(page)
        pages.append({
            "loc": f"{BASE_URL}/blogs/{filename}",
            "priority": "0.8",
            "changefreq": "monthly"
        })
    
    return pages

# ================= CA SERVICES - Comprehensive List =================
CA_SERVICES = [
    # GST Services
    "gst-registration",
    "gst-return-filing",
    "gstr-1-filing",
    "gstr-3b-filing",
    "gst-annual-return",
    "gst-audit",
    "gst-refund",
    "gst-cancellation",
    "gst-modification",
    "gst-e-way-bill",
    "gst-input-tax-credit",
    "gst-compliance",
    "gst-consultant",
    "gst-advisory",
    "gst-litigation",
    
    # Income Tax Services
    "income-tax-filing",
    "itr-filing",
    "itr-1-filing",
    "itr-2-filing",
    "itr-3-filing",
    "itr-4-filing",
    "itr-5-filing",
    "itr-6-filing",
    "itr-7-filing",
    "tax-planning",
    "tax-consultant",
    "tax-audit",
    "tax-assessment",
    "tax-refund",
    "advance-tax",
    "tds-return-filing",
    "tds-compliance",
    "form-26as-verification",
    "capital-gains-tax",
    "nri-tax-filing",
    "salary-tax-planning",
    "business-tax-planning",
    
    # Company Registration
    "company-registration",
    "private-limited-company-registration",
    "public-limited-company-registration",
    "one-person-company-registration",
    "llp-registration",
    "partnership-firm-registration",
    "sole-proprietorship-registration",
    "nidhi-company-registration",
    "section-8-company-registration",
    "producer-company-registration",
    "startup-registration",
    "startup-india-registration",
    
    # Business Registrations
    "msme-registration",
    "udyam-registration",
    "shop-act-registration",
    "trade-license",
    "fssai-registration",
    "fssai-license",
    "import-export-code",
    "iec-registration",
    "trademark-registration",
    "patent-registration",
    "copyright-registration",
    "iso-certification",
    "drug-license",
    "epf-registration",
    "esi-registration",
    "professional-tax-registration",
    
    # Audit Services
    "statutory-audit",
    "internal-audit",
    "tax-audit",
    "stock-audit",
    "forensic-audit",
    "compliance-audit",
    "concurrent-audit",
    "management-audit",
    "cost-audit",
    "information-systems-audit",
    "bank-audit",
    "cooperative-society-audit",
    "trust-audit",
    "ngo-audit",
    
    # Accounting Services
    "bookkeeping-services",
    "accounting-services",
    "payroll-services",
    "accounts-outsourcing",
    "virtual-cfo-services",
    "financial-reporting",
    "cash-flow-management",
    "budgeting-services",
    "accounts-receivable-management",
    "accounts-payable-management",
    "bank-reconciliation",
    "inventory-management",
    
    # Compliance Services
    "annual-compliance",
    "roc-compliance",
    "company-annual-filing",
    "llp-annual-filing",
    "director-kyc",
    "din-registration",
    "dsc-registration",
    "company-name-change",
    "registered-office-change",
    "director-appointment",
    "director-resignation",
    "share-transfer",
    "increase-authorized-capital",
    "company-closure",
    "llp-closure",
    "strike-off-company",
    
    # Advisory Services
    "business-advisory",
    "financial-advisory",
    "investment-advisory",
    "merger-acquisition-advisory",
    "due-diligence",
    "valuation-services",
    "business-valuation",
    "project-finance",
    "loan-syndication",
    "working-capital-management",
    "corporate-restructuring",
    "succession-planning",
    
    # Special Services
    "chartered-accountant",
    "ca-firm",
    "ca-services",
    "ca-consultant",
    "accounting-firm",
    "tax-firm",
    "audit-firm",
    "financial-consultant",
    "business-consultant",
    "legal-compliance",
    "secretarial-services",
    "company-secretary-services"
]

# ================= INDIAN CITIES - Comprehensive List =================
INDIAN_CITIES = [
    # Delhi NCR (Primary Focus)
    "noida", "delhi", "new-delhi", "ghaziabad", "gurugram", "gurgaon",
    "faridabad", "greater-noida", "noida-extension", "indirapuram",
    "vaishali", "vasundhara", "raj-nagar-extension", "crossing-republik",
    "sector-62-noida", "sector-63-noida", "sector-18-noida",
    
    # Major Metros
    "mumbai", "bangalore", "bengaluru", "chennai", "kolkata", "hyderabad",
    "pune", "ahmedabad",
    
    # North India
    "lucknow", "kanpur", "agra", "varanasi", "allahabad", "prayagraj",
    "meerut", "aligarh", "bareilly", "moradabad", "gorakhpur", "mathura",
    "jhansi", "dehradun", "haridwar", "rishikesh", "mussoorie", "nainital",
    "haldwani", "roorkee", "saharanpur", "muzaffarnagar", "firozabad",
    
    # Rajasthan
    "jaipur", "jodhpur", "udaipur", "kota", "ajmer", "bikaner",
    "alwar", "bharatpur", "sikar", "bhilwara",
    
    # Punjab & Haryana
    "chandigarh", "ludhiana", "amritsar", "jalandhar", "patiala",
    "bathinda", "mohali", "panipat", "karnal", "rohtak", "hisar",
    "sonipat", "ambala", "yamunanagar",
    
    # Gujarat
    "surat", "vadodara", "rajkot", "bhavnagar", "jamnagar",
    "junagadh", "gandhinagar", "anand", "nadiad", "bharuch",
    
    # Maharashtra
    "nagpur", "nashik", "thane", "navi-mumbai", "aurangabad",
    "solapur", "kolhapur", "sangli", "satara", "ratnagiri",
    
    # South India
    "coimbatore", "madurai", "tiruchirappalli", "salem", "tirunelveli",
    "erode", "vellore", "thoothukudi", "visakhapatnam", "vijayawada",
    "guntur", "nellore", "kurnool", "tirupati", "rajahmundry",
    "kakinada", "warangal", "nizamabad", "karimnagar", "khammam",
    "mysore", "mangalore", "hubli", "belgaum", "gulbarga", "davangere",
    "bellary", "shimoga", "tumkur", "kochi", "thiruvananthapuram",
    "kozhikode", "thrissur", "kollam", "palakkad",
    
    # East India
    "patna", "gaya", "bhagalpur", "muzaffarpur", "darbhanga",
    "ranchi", "jamshedpur", "dhanbad", "bokaro", "hazaribagh",
    "bhubaneswar", "cuttack", "rourkela", "berhampur", "sambalpur",
    "guwahati", "silchar", "dibrugarh", "jorhat", "tezpur",
    "imphal", "shillong", "agartala", "aizawl", "itanagar", "kohima",
    "gangtok",
    
    # Central India
    "bhopal", "indore", "jabalpur", "gwalior", "ujjain", "sagar",
    "raipur", "bhilai", "bilaspur", "korba", "durg",
    
    # West India
    "goa", "panaji", "margao", "vasco-da-gama"
]

# ================= SERVICE MODIFIERS =================
SERVICE_MODIFIERS = [
    "best", "top", "expert", "professional", "affordable",
    "trusted", "reliable", "experienced", "certified",
    "online", "near-me", "local"
]

# ================= YEAR-SPECIFIC KEYWORDS =================
YEAR_KEYWORDS = [
    "2024", "2025", "2026", "fy-2024-25", "fy-2025-26",
    "ay-2025-26", "ay-2026-27"
]

# ================= URL GENERATION =================
def generate_seo_urls():
    """Generate SEO-optimized URLs for CA services"""
    urls = []
    
    # Pattern 1: service-in-city (e.g., gst-registration-in-noida)
    for service in CA_SERVICES:
        for city in INDIAN_CITIES:
            urls.append({
                "loc": f"{BASE_URL}/services/{service}-in-{city}",
                "priority": "0.7",
                "changefreq": "monthly"
            })
            if len(urls) >= TARGET_URLS:
                return urls
    
    # Pattern 2: modifier-service-city (e.g., best-chartered-accountant-noida)
    for modifier in SERVICE_MODIFIERS:
        for service in CA_SERVICES[:30]:  # Top services only
            for city in INDIAN_CITIES[:50]:  # Top cities only
                urls.append({
                    "loc": f"{BASE_URL}/services/{modifier}-{service}-{city}",
                    "priority": "0.6",
                    "changefreq": "monthly"
                })
                if len(urls) >= TARGET_URLS:
                    return urls
    
    # Pattern 3: service-year (e.g., itr-filing-2025-26)
    for service in CA_SERVICES[:50]:
        for year in YEAR_KEYWORDS:
            for city in INDIAN_CITIES[:30]:
                urls.append({
                    "loc": f"{BASE_URL}/services/{service}-{year}-{city}",
                    "priority": "0.6",
                    "changefreq": "yearly"
                })
                if len(urls) >= TARGET_URLS:
                    return urls
    
    return urls

# ================= XML GENERATION HELPERS =================
def escape_xml(text):
    """Escape special XML characters"""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def write_sitemap(filename, urls):
    """Write a Google-compliant sitemap XML file"""
    filepath = os.path.join(SITEMAP_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n')
        f.write('        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n')
        f.write('        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\n')
        f.write('              http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n')
        
        for url_data in urls:
            loc = escape_xml(url_data["loc"])
            priority = url_data.get("priority", "0.5")
            changefreq = url_data.get("changefreq", "monthly")
            
            f.write("  <url>\n")
            f.write(f"    <loc>{loc}</loc>\n")
            f.write(f"    <lastmod>{TODAY}</lastmod>\n")
            f.write(f"    <changefreq>{changefreq}</changefreq>\n")
            f.write(f"    <priority>{priority}</priority>\n")
            f.write("  </url>\n")
        
        f.write("</urlset>\n")
    
    return filepath

def write_sitemap_index(sitemap_files):
    """Write Google-compliant sitemap index file"""
    index_path = "sitemap.xml"
    
    with open(index_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        f.write(f'<!-- K A R V & Associates LLP - Sitemap Index -->\n')
        f.write(f'<!-- Generated: {TODAY} -->\n')
        f.write(f'<!-- Total Sitemaps: {len(sitemap_files)} -->\n\n')
        
        for sitemap in sitemap_files:
            f.write("  <sitemap>\n")
            f.write(f"    <loc>{BASE_URL}/{SITEMAP_DIR}/{sitemap}</loc>\n")
            f.write(f"    <lastmod>{TODAY}</lastmod>\n")
            f.write("  </sitemap>\n")
        
        f.write("</sitemapindex>\n")
    
    return index_path

# ================= MAIN EXECUTION =================
def main():
    print("=" * 60)
    print("K A R V & Associates LLP - Sitemap Generator")
    print("=" * 60)
    
    # Step 1: Get existing pages
    print("\n📁 Scanning existing pages...")
    existing_pages = get_existing_pages()
    print(f"   Found {len(existing_pages)} existing pages")
    
    # Step 2: Generate SEO URLs
    print("\n🔗 Generating SEO-optimized URLs...")
    seo_urls = generate_seo_urls()
    print(f"   Generated {len(seo_urls)} SEO URLs")
    
    # Step 3: Combine all URLs
    all_urls = existing_pages + seo_urls
    total_urls = len(all_urls)
    print(f"\n📊 Total URLs: {total_urls}")
    
    # Step 4: Split into multiple sitemaps (max 50,000 per sitemap)
    sitemap_files = []
    sitemap_count = 0
    
    # First sitemap: Existing pages (high priority)
    if existing_pages:
        sitemap_count += 1
        filename = f"sitemap-main.xml"
        write_sitemap(filename, existing_pages)
        sitemap_files.append(filename)
        print(f"\n✅ Created {filename} ({len(existing_pages)} URLs)")
    
    # Subsequent sitemaps: SEO URLs in chunks
    chunk_size = MAX_URLS_PER_SITEMAP
    for i in range(0, len(seo_urls), chunk_size):
        sitemap_count += 1
        chunk = seo_urls[i:i + chunk_size]
        filename = f"sitemap-seo-{sitemap_count}.xml"
        write_sitemap(filename, chunk)
        sitemap_files.append(filename)
        print(f"✅ Created {filename} ({len(chunk)} URLs)")
    
    # Step 5: Create sitemap index
    print("\n📋 Creating sitemap index...")
    index_path = write_sitemap_index(sitemap_files)
    print(f"✅ Created {index_path}")
    
    # Summary
    print("\n" + "=" * 60)
    print("✅ SITEMAP GENERATION COMPLETE!")
    print("=" * 60)
    print(f"   Total Sitemaps: {len(sitemap_files)}")
    print(f"   Total URLs: {total_urls}")
    print(f"   Output Directory: {SITEMAP_DIR}/")
    print(f"   Sitemap Index: {index_path}")
    print("\n📌 Next Steps:")
    print("   1. Submit sitemap.xml to Google Search Console")
    print("   2. Add to robots.txt: Sitemap: {BASE_URL}/sitemap.xml")
    print("=" * 60)

if __name__ == "__main__":
    main()
