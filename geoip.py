import re
import csv
import time
import urllib.request
import json

## open file required as input for program
in_file = open("IP_input.log")
## Set output file
out_file = "GeoIP.csv"

## Open a file to write to and set column headers
def set_header():
    write_file = open(out_file,'a+',encoding="utf-8")
    write_file.write("Number Count")
    write_file.write(",")
    write_file.write("IP Address")
    write_file.write(",")
    write_file.write("Hostname")
    write_file.write(",")
    write_file.write("City")
    write_file.write(",")
    write_file.write("country")
    write_file.write(",")
    write_file.write("country code")
    write_file.write(",")
    write_file.write("ISP")
    write_file.write(",")
    write_file.write("Latitude")
    write_file.write(",")
    write_file.write("Longitude")
    write_file.write(",")
    write_file.write("Organisation")
    write_file.write(",")
    write_file.write("Query")
    write_file.write(",")
    write_file.write("Region")
    write_file.write(",")
    write_file.write("RegionName")
    write_file.write(",")
    write_file.write("Status")
    write_file.write(",")
    write_file.write("Timezone")
    write_file.write(",")
    write_file.write("Zip")
    write_file.write("\n")
    write_file.close()


def get_ip():
    counter = 0
    for line in in_file:
    ##regex to find ip in file
        ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
        counter+=1
        ## removes [' and '] from each string so the API can read it ok
        ip_string = str(ip)
        ip_string = ip_string.strip("[']")
        
        ## Writes to file if ip is over 5 characters in length - basic error check to avoid blanks
        if len(ip_string) > 5 :
            ## uncomment to view current IP thats being worked on
            #print (ip_string)

            ##get the JSON data from api
            json_dump = geo_ip(ip_string)

            ## open file to write to - ensure there is encoding to avoid character errors
            write_file = open(out_file,'a+',encoding="utf-8")

            ##write data to file each , starts a new comment
            write_file.write(str(counter))
            write_file.write(",")
            #time.sleep(1)
            write_file.write(ip_string)
            write_file.write(",")
            #time.sleep(1)
            as_name = format_csv_cell(json_dump['as'])
            write_file.write(str(as_name))
            write_file.write(",")
            #time.sleep(1)
            city_name = format_csv_cell(json_dump['city'])
            write_file.write(str(city_name))
            write_file.write(",")
            #time.sleep(1)
            country_name = format_csv_cell(json_dump['country'])
            write_file.write(str(country_name))
            write_file.write(",")
            #time.sleep(1)
            write_file.write(json_dump['countryCode'])
            write_file.write(",")
            #time.sleep(1)
            isp_name = format_csv_cell(json_dump['isp'])
            write_file.write(str(isp_name))
            write_file.write(",")
            #time.sleep(1)
            write_file.write(str(json_dump['lat']))
            write_file.write(",")
            #time.sleep(1)
            write_file.write(str(json_dump['lon']))
            write_file.write(",")
            #time.sleep(1)
            org_name = format_csv_cell(json_dump['org'])
            write_file.write(str(org_name))
            write_file.write(",")
            #time.sleep(1)
            write_file.write(json_dump['query'])
            write_file.write(",")
            #time.sleep(1)
            write_file.write(json_dump['region'])
            write_file.write(",")
            #time.sleep(1)
            region_name = format_csv_cell(json_dump['regionName'])
            write_file.write(str(region_name))
            write_file.write(",")
            #time.sleep(1)
            write_file.write(json_dump['status'])
            write_file.write(",")
            #time.sleep(1)
            write_file.write(json_dump['timezone'])
            write_file.write(",")
            #time.sleep(1)
            write_file.write(json_dump['zip'])
            write_file.write("\n")
            write_file.close()

            ## time delay to avoid ban
            time.sleep(2)
            

## This is the API call 
def geo_ip(ip):
    url = 'http://ip-api.com/json/'+ip
    url = url+"?lang=en"
    req = urllib.request.Request(url)

    ##parsing response
    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    
    ##parse json and return
    for item in cont:
        return cont
        
##Set csv cell format - takes out comma to avoid creating new columns
def format_csv_cell(item):
    item_formatter = str(item)
    item_formatter = item_formatter.replace(",", "")
    return item_formatter
    
##run the functions
set_header()

##delay after setting header to avoid the header being missed
time.sleep(2)

get_ip()
