import json
import requests
headers = {f"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMWU5OTIyYTctYmJjOS00NzU5LTg3NWYtMjc0Nzg2YTVmNjJmIiwidHlwZSI6ImFwaV90b2tlbiJ9.8eJQEjmcjaHCjpJFKEsxBzD48CDaUTKez_IR3HzXHWM"}
url = "https://api.edenai.run/v2/image/generation"

payload = {
    "response_as_dict": True,
    "attributes_as_list": False,
    "show_original_response": False,
    "num_images": 1,
    "providers": "stabilityai,deepai,openai,replicate,amazon",
    "text": "",
    "resolution": "512x512"
}

response = requests.post(url, json=payload, headers=headers)
result = json.loads(response.text)
print(result)