#extract year month date from URL
import re
def extract_date(url):
    match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', url)
    return match.groups() if match else None

print(extract_date("https://www.washingtonpost.com/news/.../2016/09/02/..."))


