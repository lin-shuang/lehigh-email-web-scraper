import json, csv, requests, time
import bs4 as bs

# file_all_emails_spreadsheet = open("deans_list_scrape_spreadsheet_2019.csv","w+")
file_cached_emails = open("cached_emails.json", "r")
cached_emails = json.loads(file_cached_emails.read())
file_cached_emails.close()
# file_cached_emails_update = open("cached_emails.json", "w")
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Referrer": "https://webapps.lehigh.edu/",
    "Origin": "https://webapps.lehigh.edu",
    "Host": "www.lehigh.edu"
}

def get_lehigh_email(first, last, cache):
    key = first+'_'+last
    email = None
    add_to_cache = False
    if cache.get(key) is not None:
        return cache.get(key)
    else:
        add_to_cache = True
    time.sleep(2)
    full_name = first.lower()+" "+last.lower()
    lehigh_lookup_url = "https://www.lehigh.edu/cgi-bin/ldapsearch/ldapsearch.pl"
    payload = {'cn': full_name}
    headers['Content-Length'] = str(len(payload))
    response = requests.post(lehigh_lookup_url, data = payload, headers = headers).text
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
    if email is None:
        add_to_cache = False
        # print(str(soup))
        print(full_name)
        print(f"Failed to get email for {first} {last}")
    if add_to_cache:
        cache[key] = email
    
    return email

new = []
with open("./DCPNM.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row['Directory']
        name = name.replace(".", "").replace(",", "").strip()
        splits = name.split(" ")
        first, last = splits[0], " ".join(splits[1:])
        email = get_lehigh_email(first, last, cached_emails)
        print("got email")
        print(email)
        new.append({"first": first, "last": last, "email": email})

with open("file_for_nationals.csv", "w") as n:
    writer = csv.DictWriter(n, fieldnames=new[0].keys())
    writer.writeheader()
    for r in new:
        writer.writerow(r)

with open("new_cache.json", "w") as j:
    json.dump(cached_emails, j)
