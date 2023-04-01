import re
import requests
import json


if __name__ == '__main__':

    url = f'http://www.columbia.edu/~fdc/sample.html'
    req = requests.get(url)
    web_text = req.text
    h3_patterns = re.compile(r'<h3.*>(.+)</h3>')
    h3_array = h3_patterns.findall(web_text)
    print(h3_array)
