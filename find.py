import os
import wikidot

USERNAME = os.environ.get("WIKIDOT_USERNAME")
PASSWORD = os.environ.get("WIKIDOT_PASSWORD")

if not USERNAME or not PASSWORD:
    raise Exception("Missing Wikidot credentials in environment variables.")

with wikidot.Client(username=USERNAME, password=PASSWORD) as client:
    site = client.site.get("outrooms-wiki")

    all_pages = site.pages.search()

    keyword = "Colossal Machine"
    matches = []

    for page in all_pages:
        try:
            source_text = page.source.wiki_text
            if keyword.lower() in source_text.lower():
                matches.append(page.fullname)
                print(f"FOUND: {page.fullname} ({page.url})")
        except Exception as e:
            print(f"Error on {page.fullname}: {e}")

    print(f"\nTotal pages referencing '{keyword}': {len(matches)}")
