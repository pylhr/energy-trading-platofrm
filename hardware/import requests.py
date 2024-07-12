import requests
import json

# ThingSpeak parameters
read_api_key = "94TL0V0SC17LX8VS"
channel_id = "2157555"
field_number = "1"

# Prepare the request URL
url = f"https://api.thingspeak.com/channels/{channel_id}/fields/{field_number}.json?api_key={read_api_key}"

# Send the HTTP GET request
response = requests.get(url)

# Parse the JSON response
data = json.loads(response.text)

# Get the latest entry
latest_entry = data["feeds"][-1]

# Extract the field value
field_value = latest_entry["field" + field_number]

# Print the field value
print("Latest Field Value:", field_value)
