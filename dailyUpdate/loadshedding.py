import requests

LICENSE_KEY = os.environ.get("KEY")
eskom_url = "https://developer.sepush.co.za/business/2.0/area?id=ethekwini3-12a-cbdeast"
payload={}
headers = {
    'token': LICENSE_KEY,
}

response = requests.request("GET", eskom_url , headers=headers, data=payload)
response = response.json()



print(response)
stage = int(response["events"][0]["note"][6]) -1
affected_hours = response["schedule"]["days"][0]["stages"][stage]
# print(affected_hours)
# print(stage)

def all_affected_hours():
    all_hours = []
    for n in affected_hours:
        if 8 <= int(n[0:2]) <= 16:
            all_hours.append(n)

    return all_hours
    
