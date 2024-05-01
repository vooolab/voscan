from urllib.parse import urlparse, urljoin, urlencode
import requests
import argparse
try:
    import elements
    import scanner_utils
except:
    print("   Hata | Tool Dosyaları Eksik yada Bozuk! Toolu Güncelleyiniz...")

print(elements.banner)

def parse_url(url):
    parsed_url = urlparse(url)
    return parsed_url

def join_urls(base, relative):
    joined_url = urljoin(base, relative)
    return joined_url

def encode_query_params(params):
    encoded_params = urlencode(params)
    return encoded_params

control_urls = {}
def url_splitter(url):
    lurl = url
    if "https://" in url or "http://" in url:
        pass
    else:
        try:
            response_check_protocol_https = requests.get(f"https://{url}", timeout=3)
            response_check_protocol_https.raise_for_status()
            lurl = f"https://{url}"
        except requests.exceptions.RequestException as e:
            try:
                response_check_protocol_http = requests.get(f"http://{url}", timeout=3)
                response_check_protocol_http.raise_for_status()
                lurl = f"http://{url}"
            except requests.exceptions.RequestException as e:
                control_urls['request'] = {"connection": False, "error_code": "", "p_error": "url-not-found"}



    parsed_url = parse_url(lurl)
    control_urls['scheme'] = parsed_url.scheme
    control_urls['netloc'] = parsed_url.netloc
    control_urls['path'] = parsed_url.path
    control_urls['params'] = parsed_url.params
    control_urls['query'] = parsed_url.query
    control_urls['fragment'] = parsed_url.fragment
    control_urls['encoded_params'] = encode_query_params
    try:
        response_check = requests.get(lurl, timeout=3)
        response_check.raise_for_status()
        if response_check.history:
            control_urls['request'] = {"connection": True, "status_code": response_check.status_code, "orientation": False, "orientation_url": response_check.url}
        else:
            control_urls['request'] = {"connection": True, "status_code": response_check.status_code, "orientation": False, "orientation_url": ""}
    except requests.exceptions.RequestException as e:
        control_urls['request'] = {"connection": False, "error_code": str(e), "p_error": ""}

    return control_urls

parser = argparse.ArgumentParser(description='Web Sitelerinin Gizli Dizinlerini Tarayın!')
parser.add_argument('-u', metavar='<URL>', required=True, help='URL Adresini Girin.')
parser.add_argument('-d', metavar='<WORDLIST>', required=False, help='Dizin Taraması Başlatır. İsteğe bağlı "-d df" ile manual wordlisti tanımlayabilirsin.')
parser.add_argument('-s', metavar='<WORDLIST>', nargs='?', required=False, help='Yakında!')
parser.add_argument('-o', metavar='<FILE_NAME>', nargs='?', required=False, help='Yakında!')
args = parser.parse_args()
if args.u:
    dataRl = url_splitter(args.u)
    if dataRl['request']['connection'] == True:
        if args.d:
            scanner_utils.scan_dir_conf(dataRl['scheme'], dataRl['netloc'], args.d)
    else:
        elements.error("Siteye bağlanırken bir problem oluştu!")
else:
    elements.error("URL Adresi Belirtilmedi")
    exit()

