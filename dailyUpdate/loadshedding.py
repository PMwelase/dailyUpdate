import requests

LICENSE_KEY = "05F040E5-4A394118-BE194A3D-7192DB78"
eskom_url = "https://developer.sepush.co.za/business/2.0/area?id=ethekwini3-12a-cbdeast&test=current"
payload={}
headers = {
    'token': LICENSE_KEY,
}

response = requests.request("GET", eskom_url , headers=headers, data=payload)
response = response.json()

# print(response)
stage = int(response["events"][0]["note"][6]) -1
affected_hours = response["schedule"]["days"][0]["stages"][stage]
print(stage)
affected_hours = []
# print(affected_hours)

def all_affected_hours():
    all_hours = []
    for n in affected_hours:
        if 8 <= int(n[0:2]) <= 16:
            n = n.replace('30', '00')
            all_hours.append(n)

    return all_hours
