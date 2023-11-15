# lehigh-email-web-scraper
Get student's emails by their names using Lehigh People Directory (LDAP) Search.

### Instructions 
1. Download Python and Lehigh's Cisco AnyConnect VPN if you're not on campus Wifi

2. See required packages to install in requirements.txt (in cmd use: pip install INSERT_PACKAGE_NAME_HERE)
    - pip install bs4
    - pip install requests

    - I used Python 3 and it worked after having installed the packages.

3. Open DCPNM.csv and Copy and Paste all the names from the most recent Dean's List's .pdf into this text file
    - The Deans_list_web_scaper.py is not functioning as the webpage is no longer the list, instead, it just lists the .pdf files
    - Personally I used a list like [[DCPNM.csv]] and the [[emails_from_spreadsheet.py]]. (DCPNM = Delta Chi Potential new members)

4. Add "Directory" as the first line in DCPNM.csv

5. Find and Delete the "Dean’s List [Semester]" line in DCPNM.csv

6. Run [[emails_from_spreadsheet.py]]
    - RUN THIS WHILE IN VPN AS IT REQUIRES LOGIN OTHERWISE (or just be on the campus Wifi)
    - This program uses LDAP to get emails matching the student names
    - This will take a while to run as it sleeps to not get spam blocked by the email query
  
7. The output is file_for_nationals.csv
    - You can import this into a spreadsheet to get the emails to send out yourself
    - OR send it to nationals if you're using SURGE to send emails for you

Made by Cody B.

This text and uploading done by Cole K.

Instructions updated by Shuang L.
