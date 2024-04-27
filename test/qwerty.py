import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMWU5OTIyYTctYmJjOS00NzU5LTg3NWYtMjc0Nzg2YTVmNjJmIiwidHlwZSI6ImFwaV90b2tlbiJ9.8eJQEjmcjaHCjpJFKEsxBzD48CDaUTKez_IR3HzXHWM"}

url = "https://api.edenai.run/v2/audio/text_to_speech"
payload = {
    "providers": "openai", "language": "ru",
    "option": "MALE",
    "text": "я научу вас смея",
    "fallback_providers": ""
}

response = requests.post(url, json=payload, headers=headers)

result = json.loads(response.text)
print(result)