from urllib.request import urlopen
from urllib.parse import urlencode
import contextlib
 
def make_url_short(url):
    req_url = "http://tinyurl.com/api-create.php?" + urlencode({'url':url})
    with contextlib.closing(urlopen(req_url)) as response:
        return response.read().decode('utf-8')

if __name__ == "__main__":
    # sample
    k = make_url_short("https://www.linkedin.com/in/nivethitha-soundarrajan-7a5866189/")
    print(k)
