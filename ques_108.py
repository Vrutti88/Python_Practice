# Q108) Write a program (assuming you have internet access) that fetches data from a public API using the requests module and prints part of the JSON response.
import requests
def fetch_data_from_api():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Sample Data from the API:")
            for post in data[:3]: 
                print(f"ID: {post['id']}, Title: {post['title']}\n")
        else:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
fetch_data_from_api()
