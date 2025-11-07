import requests
post={
    "ownerName":"123",
    "phoneNumber":"312123321",
    "carModel":"Toyota",

    "date":"2025-12-12",
    "time":"00-12",
}
res = requests.post("http://127.0.0.1:8080/api/repair_requests",json=post)
