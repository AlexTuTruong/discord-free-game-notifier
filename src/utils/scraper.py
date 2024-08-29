import requests
from datetime import datetime
from bs4 import BeautifulSoup

URL = "https://gg.deals/news/?dateRange=today&type=6"
# URL = "https://gg.deals/news/?type=6"  # Most recent freebie articles for testing


def get_articles() -> list:
    """Gets data from the "freebies" articles and returns a JSON list of their data."""
    try:
        response = requests.get(URL, timeout=30)
        print(
            f"[{datetime.now().replace(microsecond=0)}]",
            f"gg.deals response: {response.status_code}",
        )
    except Exception:
        print(
            f"[{datetime.now().replace(microsecond=0)}]",
            "Failed to get data from gg.deals",
        )

    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")

    messages = []

    for article in articles:

        title = article.find("div", class_="news-title-wrapper").text.strip()

        sub_text = article.find("div", class_="news-lead").text.strip()

        timestamp = article.find("time").get("datetime")

        game_url = "https://gg.deals" + article.find("a", class_="full-link").get(
            "href"
        )

        image_url = (
            article.find("div", class_="news-image-wrapper")
            .find()
            .get("srcset")
            .split(",")[0][:-5]
        )

        message = {
            "title": title,
            "sub_text": sub_text,
            "timestamp": timestamp,
            "game_url": game_url,
            "image_url": image_url,
        }

        messages.append(message)

    return messages


if __name__ == "__main__":
    """Gets freebie articles from today and prints them."""
    articles = get_articles()

    for article in articles:
        print(
            f"{article['title']}\n{article['sub_text']}\n{article['timestamp']}\n{article['game_url']}\n{article['image_url']}\n",
            "==========",
        )
