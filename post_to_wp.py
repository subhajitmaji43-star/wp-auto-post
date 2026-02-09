import os
import requests
from requests.auth import HTTPBasicAuth

WP_URL = os.environ["WP_URL"]
WP_USERNAME = os.environ["WP_USERNAME"]
WP_APP_PASSWORD = os.environ["WP_APP_PASSWORD"]

endpoint = f"{WP_URL}/wp-json/wp/v2/posts"

data = {
    "title": "API Test Post",
    "content": "<p>This post was published using GitHub Actions via WordPress REST API.</p>",
    "status": "publish"
}

response = requests.post(
    endpoint,
    json=data,
    auth=HTTPBasicAuth(WP_USERNAME, WP_APP_PASSWORD)
)

print(response.status_code)
print(response.text)
