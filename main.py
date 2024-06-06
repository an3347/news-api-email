import requests

api_key = "87e7e1831b1e443c9f07453ace6e5cca"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&sortBy=publishedAt&apiKey=" \
      "87e7e1831b1e443c9f07453ace6e5cca"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
