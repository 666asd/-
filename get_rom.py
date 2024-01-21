import requests
import datetime
import base64
import hashlib
import sys

# Dummy values, countryCode required if querying EU servers
# Most important here are the hardware and channel
# channel如:stable(开发版)、current(测试版)、release（稳定版）
params = {
    #"countryCode": "EU",
    "deviceID": "",
    "rom": "0.0.1",
    "hardware": "X08A",
    "cfe": "",
    "linux": "0.0.1",
    "ramfs": "0.0.1",
    "sqafs": "0.0.1",
    "rootfs": "0.0.1",
    "channel": sys.argv[1],
    "serialNumber": "",
}

# Default server: http://api.miwifi.com, EU servers: http://eu.api.miwifi.com
server = "http://api.miwifi.com"
recoveryURL = "/rs/grayupgrade"
normalUpgradeUrl = "/rs/grayupgrade"
default_token = "8007236f-a2d6-4847-ac83-c49395ad6d65"

def main():

    # Constuct initial sub url based on params
    sub_url = recoveryURL + "?"
    for key, value in params.items():
        sub_url += key + "=" + value + "&"

    # Add time to params formatted as %Y-%m-%d--%X
    timestr = datetime.datetime.now().strftime("%Y-%m-%d--%X")
    params["time"] = timestr
    
    # Get sorted params list
    sortedParams = sorted(params.items(), key=lambda x: x[0])

    # Loop through sorted params to create params string
    paramsString = ""
    for item in sortedParams:
        paramsString += item[0] + "=" + item[1] + "&"

    # Append default token to paramsString
    paramsString += default_token

    # Create signature of paramsString (md5 with base64 contents)
    signature = hashlib.md5(base64.b64encode(paramsString.encode('utf-8'))).hexdigest()

    # Construct url
    url = server + sub_url + "s=" + signature + "&time=" + timestr + "&token=" + default_token

    print("URL: " + url)

    # Set user agent to "miwifi-", similar to their recovery process
    headers = {'User-Agent': 'miwifi-'}

    # Make request with url and headers
    response = requests.get(url, headers=headers)
    
    # Print response details
    print("Status code: " + str(response.status_code))
    print("Response: " + response.text)

if __name__ == "__main__":
    main()
