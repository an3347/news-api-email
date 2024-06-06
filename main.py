import requests

api_key = "87e7e1831b1e443c9f07453ace6e5cca"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&sortBy=publishedAt&apiKey=" \
      "87e7e1831b1e443c9f07453ace6e5cca"

request = requests.get(url)
content = request.text
print(content)
