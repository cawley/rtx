import requests
import csv

# this script writes user data to a .csv file in addition to printing it out
# this is a basic example of a rest api workflow in how the user gets the data all teh way from the request to how the data is stored at the concluision of the request

response = requests.get("https://api.example.com/users/123")

if response.status_code == 200:
    data = response.json()
    with open("user_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Email"])
        writer.writerow([data["id"], data["name"], data["email"]])
else:
    print(f"Request failed with status code {response.status_code}")
