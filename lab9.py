import requests
import time
from bs4 import BeautifulSoup #Import BeautifulSoup for HTML parsing 

#Fetch data from the given URL
def fetch_data(url) :
try:
    response = requests.get(url)
    response.raise_for_status()

    # Return raw HTML content
    return response.text
except requests.RequestException as e:
    print(f"Error fetching data: {e}")
    return None
# Process and extract meaninmgful data using BeautifulSoup
def process_data(data):
    if data:
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(data, "html.parser")

        # Extract relevant information
        name = soup.find("h2") # Name is in an <h2> tag
        favorite_color = soup.find("h3") #Favorite color is in an <h3> tag

        # Extract the last modification date (if present)
        creation_date = soup.find("meta", attrs={"name":"date"})

        # Display extracted information
        print("\n --- Extracted Information ---")
        print(f"Name: {name.text.strip() if name else 'Not Found'}")
        print(f"Creation Date: {creation_date['content'] if creation_date else 'Not Provided'}")
        print("-------------------------------\n")

        print(data)
    else:
        print("No data to process")

        def main():

            url = input("Enter the URL to fetch data from: ").strip()
            #url = "http://olymus.realpython.org/profiles/dionysus"

            iterations = 3 # Fetch data 3 times
            interval = 10 # in 10 second intervals

            print("Staring data fetching process...\n")

            for i in range(iterations):
                print(f"Iteration {i + 1}:")

                # Fetch and process the data
                data = fetch_data(url)
                process_data(data)

                # Wait for the next iteration
                if i < iterations - 1:
                    print(f"waiting for {interval} seconds...\n")
                    time.sleep(interval)

                    print("\nData fetching process completed")

                    if __name__ == "__main__":
                        main()