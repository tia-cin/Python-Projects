import urllib.request as lib

def main(url):
    print("Checking conectivity...")

    res = lib.urlopen(url)
    print(f"Connected to {url} successfully!")
    print(f"Here is the response {res.getcode()}")

site_url = input("Please paste the url of site: ")

main(site_url)