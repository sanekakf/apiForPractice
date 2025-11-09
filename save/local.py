import requests
post={
    "id":44
}
res = requests.post("http://127.0.0.1:8080/api/repair_requests/done", json=post)
# print(res.json())
