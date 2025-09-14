import requests

def run(ip):
    print(f"\n📍 Fetching IP location for: {ip}\n")

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()

        if data["status"] == "success":
            print(f"🌍 Country: {data['country']}")
            print(f"🏙️ Region: {data['regionName']}")
            print(f"📍 City: {data['city']}")
            print(f"📡 ISP: {data['isp']}")
            print(f"🌐 Org: {data['org']}")
            print(f"🛰️ Latitude: {data['lat']}")
            print(f"🛰️ Longitude: {data['lon']}")
            print(f"📅 Timezone: {data['timezone']}")
        else:
            print("❌ Could not fetch location. Invalid IP or domain.")

    except Exception as e:
        print(f"🚨 Error: {str(e)}")
