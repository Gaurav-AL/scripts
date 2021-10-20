import urllib.request
import re
def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename, 'wb')
    file.write(response.read())
    
    name  = re.search("[0-9].pdf",str(file))
    #camelot is Unable to read to _io.BufferedWriter 
#     tables = camelot.read_pdf(str(file))
    
#     tables[0].to_json(f'{filename}.json')
    file.close()
    return file
 
url = "http://covid19.ap.gov.in/assets/information_guidelines/bulletin"
date = 26
month = 4
year = 2020
files = []

while(True):
    if(date < 10):
        f_url = f'{url}/0{date}-0{month}-{year}_10AM_Telugu.pdf'
    else:
        f_url = f'{url}/{date}-0{month}-{year}_10AM_Telugu.pdf'git 