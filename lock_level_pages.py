import os
import wikidot

USERNAME = os.environ.get('WIKIDOT_USERNAME')
PASSWORD = os.environ.get('WIKIDOT_PASSWORD')

if not USERNAME or not PASSWORD:
    print("Error: Missing credentials.")
    exit(1)

with wikidot.Client(username=USERNAME, password=PASSWORD) as client:
    site = client.site.get('outrooms-wiki')

    level_pages = site.pages.search(fullname='level-*')

    for page in level_pages:
        try:
            if not page.locked:
                print(f"Locking: {page.fullname}")
                page.set_lock(True)
            else:
                print(f"Already locked: {page.fullname}")
        except Exception as e:
            print(f"Error locking {page.fullname}: {e}")

print("Done.")
