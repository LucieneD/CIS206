#7 Remove leading zeros from IP address
import re
def clean_ip(ip):
    return re.sub(r'\b0+(\d)', r'\1', ip)

print(clean_ip("216.08.094.196"))  # "216.8.94.196"

