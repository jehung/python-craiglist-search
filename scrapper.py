import requests
#import bs4
from bs4 import BeautifulSoup
import sys


def fetch_search_results(query="beige fabric sofa", minAsk=300, maxAsk=1000):
    search_params = {
        key: val for key, val in locals().items() if val is not None
    }
    if not search_params:
        raise ValueError("No valid keywords")

    base = 'http://vancouver.craigslist.ca/search/fua'
    resp = requests.get(base, params=search_params, timeout=3)
    resp.raise_for_status()  # <- no-op if status==200
    return resp.content, resp.encoding

# then add this function lower down
def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, from_encoding=encoding)
    return parsed

def extract_listings(parsed):
    listings = parsed.find_all('p', class_='row')
    return listings

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html, encoding = read_search_results()
    else:
        html, encoding = fetch_search_results(minAsk=300, maxAsk=1000)
    doc = parse_source(html, encoding)
    listings = extract_listings(doc) # add this line
    print len(listings)              # and this one
    for i in range(0, 1):
        print listings[i].prettify()    
    #print listings[3].prettify()     # and this one too
    