import requests
import json

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        print("Data fatch Successfully")   
        print(data)
    except requests.exceptions.RequestException as i:
        print("API request error:",i)   
        return None
    except json.JSONDecodeError:
        print("jso recive")
        return None
    
def extract_username(data): 
    username = []
    for item in data:
           username.append(item.get("username"))
    return username 

def transfrom_data_structure(data):
    
    datastructure = []
    
    for item in data:
        user_info = {
              "name" : item.get("name"),
              "city" : item.get("address",{}).get("city"),
              "company" : item.get("company",{}).get("name")
        }
    datastructure.append(user_info)
    return datastructure

def nested_file(data):
    
    location = []
    
    for item in data:
        geo = item.get("address",{}).get("geo",{})
        lat = geo.get("lat")
        lng = geo.get("lng")
        location.append((lat, lng))

    return location

if __name__ == "__main__":
    
    url = "https://jsonplaceholder.typicode.com/users"
    data = fetch_data(url)

    if data is None:
        print("Error fetching data — using mock JSON!")
        data = [
            {
            "id": 2,
            "name": "Ervin Howell",
            "username": "Antonette",
            "email": "Shanna@melissa.tv",
            "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {
            "lat": "-43.9509",
            "lng": "-34.4618"
             }
           }
         }   
        ]

    print("\nUsernames:")
    print(extract_username(data))

    
    print("\nSimplified user info:")
    print(nested_file(data))

   
    print("\nGeo-locations (lat, lng):")
    print(nested_file(data))