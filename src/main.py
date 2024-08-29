import time
from utils import scraper
from utils.webhook import send_embed
from utils.webhook import ping_users


def check_and_notify():
    """Checks for free games articles and sends the webhook if any are found."""
    data = scraper.get_articles()
    if data:
        ping_users()

        for item in data:
            send_embed(
                item["title"],
                item["sub_text"],
                item["timestamp"],
                item["game_url"],
                item["image_url"],
            )
            time.sleep(0.5)
    else:
        print("No articles found")


check_and_notify()
