import os
import wikidot
from datetime import datetime, timedelta

USERNAME = os.environ.get('WIKIDOT_USERNAME')
PASSWORD = os.environ.get('WIKIDOT_PASSWORD')

if not USERNAME or not PASSWORD:
    print("Error: Missing credentials.")
    exit(1)

with wikidot.Client(username=USERNAME, password=PASSWORD) as client:
    site = client.site.get('outrooms-wiki')

    pages = site.pages.search(category='submission')

    one_day_ago = datetime.now() - timedelta(days=1)

    for page in pages:
        try:
            if page.fullname == 'submission:_template':
                print(f"Skipping template page: {page.fullname}")
                continue

            if page.created_at < one_day_ago:
                print(f"Deleting old submission: {page.fullname} (Created: {page.created_at})")
                page.destroy()
            else:
                print(f"Skipping recent submission: {page.fullname} (Created: {page.created_at})")
        except Exception as e:
            print(f"Error processing {page.fullname}: {e}")

print("Done.")
