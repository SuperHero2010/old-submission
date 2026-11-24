import wikidot

client = wikidot.Client()
site = client.site.get("outrooms-wiki")

all_pages = site.pages.search()

keyword = "Colossal Machine"
matches = []

for page in all_pages:
    try:
        source_text = page.source.wiki_text
        if keyword.lower() in source_text.lower():
            matches.append(page.fullname)
            print(f"Found in: {page.fullname} ({page.url})")
    except Exception as e:
        print(f"Error on {page.fullname}: {e}")

print(f"\nTotal pages referencing '{keyword}': {len(matches)}")
