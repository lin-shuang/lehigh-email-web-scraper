# lehigh-email-web-scraper
Get student's emails by their names using Lehigh People Directory (LDAP) Search

### Instructions 
1. Download Python and Lehigh's Cisco AnyConnect VPN if you don't have it

2. See required packages to install in requirements.txt (in cmd use: pip install INSERT_PACKAGE_NAME_HERE)

    - pip install bs4
    - pip install requests

    - I used python 3 and it worked having installed the packages.

3. Copy and Paste all the names from the most recent Dean's List into DCPNM.csv

    - The Deans_list_web_scaper.py is not functioning as the webpage is no longer the list and instead it just lists the pdf lists.
    - Personally I used a list like [[DCPNM.csv]] and the [[emails_from_spreadsheet.py]]. (DCPNM is Delta Chi Potential new members).

4. Add "Directory" as the first line

5. Delete "Dean’s List (Semester)" line

6. Run [[emails_from_spreadsheet.py]]

    - RUN THIS WHILE IN VPN AS IT REQUIRES LOGIN OTHERWISE (or just be on the campus wifi).
    - This will take a while to run as it sleeps as to not get spam blocked by the email query.

Made by Cody B.

This text and uploading done by Cole K.

Updated by Shuang L.
