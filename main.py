import requests
from send_email import send_email

api_key = "87e7e1831b1e443c9f07453ace6e5cca"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&sortBy=publishedAt&apiKey=" \
      "87e7e1831b1e443c9f07453ace6e5cca"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = """\
Subject: News of the day

"""
# Access the article titles and description
for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
