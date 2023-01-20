import json
import csv

file_input_csv = open("deans_list_scrape_spreadsheet_2019.csv", "r")

file_output_cache = open("cached_emails.json", "w+")

reader = csv.DictReader(file_input_csv)

output_cache = {}

for row in reader:
    first_name = row['first_name']
    last_name = row['last_name']
    email = row['lehigh_email']
    key = first_name+"_"+last_name
    output_cache[key] = email

file_input_csv.close()

file_output_cache.write(json.dumps(output_cache))
file_output_cache.close()
