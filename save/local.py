import requests
res = requests.get("http://77.232.139.226:8080/api/repair_requests")
print(res.json())
