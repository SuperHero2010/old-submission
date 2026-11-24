import os
import wikidot

USERNAME = os.environ.get("WIKIDOT_USERNAME")
PASSWORD = os.environ.get("WIKIDOT_PASSWORD")

if not USERNAME or not PASSWORD:
    raise Exception("Missing Wikidot credentials in environment variables.")

with wikidot.Client(username=USERNAME, password=PASSWORD) as client:
    site = client.site.get("outrooms-wiki")

    pages = site.pages.search(category="_default")

    for page in pages:
        if not page.fullname.startswith("level-"):
            continue

        try:
            current_source = page.source.wiki_text

            if "[[module Comments]]" in current_source:
                print(f"Skipping {page.fullname} (already has Comments)")
                continue

            updated_source = current_source + "\n\n[[module Comments]]"

            page.edit(title=page.title, source=updated_source, comment="Appended Comments module via script")
            print(f"Appended to {page.fullname}")
        except Exception as e:
            print(f"Error on {page.fullname}: {e}")
