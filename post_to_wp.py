import requests
from requests.auth import HTTPBasicAuth

# 🔧 CHANGE THESE THREE VALUES
WP_URL = "https://drsubhajitmaji.com"
WP_USERNAME = "YOUR_WORDPRESS_USERNAME"
WP_APP_PASSWORD = "YOUR_APPLICATION_PASSWORD"

# WordPress REST API endpoint
endpoint = f"{WP_URL}/wp-json/wp/v2/posts"

# Test post data
data = {
    "title": "API Test Post",
    "content": "<p>This post was published using Python via WordPress REST API.</p>",
    "status": "publish"
}

# Send POST request
response = requests.post(
    endpoint,
    json=data,
    auth=HTTPBasicAuth(WP_USERNAME, WP_APP_PASSWORD)
)

# Print result
print("Status Code:", response.status_code)
print("Response:", response.text)
