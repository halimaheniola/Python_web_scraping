!pip install beautifulsoup4
import urllib.parse
import urllib.request 
from urllib.request import Request, urlopen
from urllib.parse import urljoin
import urllib.error
from urllib.error import URLError, HTTPError
import os
import sys
from bs4 import BeautifulSoup
# the url of the site I want to download pdf files from e.g. of url for testing which contains about 22 pdfs https://mepb.lagosstate.gov.ng/y2015-budget/
url = input("[+] Enter the url: ")
# the path of where I want the downloaded files to be saved on my local machine
download_path = input("[+] Enter the download path in full: ")
try:
#     to make it look legit for the url
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11)'
    values = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    i = 0
    headers = {'User-Agent': user_agent}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html.read().decode('utf-8'))
#     find <a> tags with href in it so you know it is for urls, so that if it doesn't contain the the full url, it can find the url 
#     itself to it for the download 
    for tag in soup.findAll('a', href=True): 
        tag['href'] = urljoin(url, tag['href'])
    #         this is pretty easy that we are getting th eextension (splitext) from the last name of the full url(basename)
    #         the splitext splits it into the filename and the extension so the [1] is for the second part(the extension)
        if os.path.splitext(os.path.basename(tag['href']))[1] =='.pdf':
            current = urllib.request.urlopen(tag['href'])
            print("\n[*] Downloading: %s" %(os.path.basename(tag['href'])))
            f = open(download_path + "\\" +os.path.basename(tag['href']))
            f.write(current.read())
            f.close()
            i+=1
print ("\n[*] Downloaded %d files" %(i+1))
input("[+] Press any key to exit...")
#except KeyboardInterrupt:
#   print ("[*] Exiting...")
    sys.exit(0)
# except urllib.error.URLError as e:
#    print("[*] Could not get information from server!!")
#    sys.exit(1)
except Exception as ex:
#    print("I don't know what the problem is but sorry!!")
#    sys.exit(2)
    
   print (%(ex))
    raise
