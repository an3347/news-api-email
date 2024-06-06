import requests
from send_email import send_email
from datetime import datetime

today_date = datetime.today().strftime("%B %d of %Y")
topic = "tesla"

api_key = "87e7e1831b1e443c9f07453ace6e5cca"

urls = ["https://newsapi.org/v2/everything?"
        f"q={topic}"
        "&sortBy=publishedAt&apiKey="
        "87e7e1831b1e443c9f07453ace6e5cca"
        "&language=hi",
        "https://newsapi.org/v2/top-headlines"
        "?country=in"
        f"&apiKey={api_key}"]

for url in urls:

    # Make request
    request = requests.get(url)

    # Get a dictionary with data
    content = request.json()

    body = f"""\
    Subject: News on {today_date}
    
    """
    # Access the article titles and description
    for article in content["articles"][:20]:
        if article["title"] is not None and article["description"] is not None:
            body = (body + article["title"] + "\n"
                    + article["description"] + "\n"
                    + article["url"] + 2 * "\n")

    body = body.encode("utf-8")
    send_email(message=body)
