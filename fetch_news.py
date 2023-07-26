import requests

url = "https://yfinance-stock-market-data.p.rapidapi.com/stock-info"

payload = { "symbol": "AAPL, MSFT, NVDA, GOOG, META" }
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "2cc7cd160fmsh1a3b8247c7a0a8cp1630aejsn3eda2dca1de7",
    "X-RapidAPI-Host": "yfinance-stock-market-data.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

# Check if the request was successful and the response contains data
if response.status_code == 200 and response.json():
    api_response = response.json()

    # Save the API response to a file
    with open("api_response.json", "w") as file:
        file.write(str(api_response))

    print("API response has been written to 'api_response.json' file.")
else:
    print("Failed to retrieve data from the API.")
