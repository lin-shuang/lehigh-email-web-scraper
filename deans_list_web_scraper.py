import bs4 as bs
import urllib.request
import requests
import time
import json

file_all_emails_spreadsheet = open("deans_list_scrape_spreadsheet_2019.csv","w+")
file_cached_emails = open("cached_emails.json", "r")
cached_emails = json.loads(file_cached_emails.read())
file_cached_emails.close()
file_cached_emails_update = open("cached_emails.json", "w")

def get_lehigh_email(first, last, cache):
    key = first+'_'+last
    add_to_cache = False
    if cache.get(key) is not None:
        return cache.get(key)
    else:
        add_to_cache = True
    time.sleep(2)
    full_name = first+"*"+last
    lehigh_lookup_url = "https://www.lehigh.edu/cgi-bin/ldapsearch.pl"
    payload = {'cn': full_name}
    response = requests.post(lehigh_lookup_url, data = payload).text
    soup = bs.BeautifulSoup(response,'lxml')
    #do this for multiple results
    if "returning " in soup.get_text():
        for table_data in soup.find_all("tr"):
            #print(table_data)
            row_break_down = table_data.find_all("td")
            if len(row_break_down) < 1: #header row skip
                continue
            assumed_first = row_break_down[0].get_text()
            assumed_last = row_break_down[1].get_text()

            if assumed_first == first and assumed_last == last: #grab the real email if our assumptions work
                email = row_break_down[3].get_text()
    else:
        for table_data in soup.find_all("td"):
            if "@lehigh.edu" in table_data.get_text():
                email = table_data.get_text()
    if add_to_cache:
        cache[key] = email
    return email

source = urllib.request.urlopen('https://studentaffairs.lehigh.edu/content/deans-list').read()

soup = bs.BeautifulSoup(source,'lxml')

csv_str = "first_name,last_name,lehigh_email\n"

for alpha_break in soup.find_all("div", {"class": "views-field-field-wms-answer"}):
    name_row = alpha_break.find("p")
    #remove the html line breaks, the line breaks are added via CKEditor, so we can assume its uniform
    name_row_text = str(name_row)
    name_row_text = name_row_text.replace("</p>", "")
    name_row_text = name_row_text.replace("<p>", "")
    name_row_text = name_row_text.replace("<br/>", "|")
    #make it a pipe just in case down the road we want to make a pdv
    name_arr_separated = name_row_text.split("|")
    for name in name_arr_separated:
        last_name,first_name = name.split(", ") #deconstruct the name string into a tuple
        csv_str += first_name+","+last_name+","+get_lehigh_email(first_name,last_name, cached_emails)+"\n"

#note: its a matter of preference that I write it out all at the end, I'm torn between writing it out line by line or queing it like this :|
file_all_emails_spreadsheet.write(csv_str)
file_all_emails_spreadsheet.close()
file_cached_emails_update.write(json.dumps(cached_emails))
file_cached_emails_update.close()
