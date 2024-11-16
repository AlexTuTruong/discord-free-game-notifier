import os
import requests
import json
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

webhook_url = os.getenv("WEBHOOK_URL")


def send_embed(title, subtext, timestamp, game_url, image_url):
    """
    Sends a free game article information to a given discord webhook
    formatted as an embedded message.
    """
    embed = {
        "description": f"[{title}]({game_url})\n{subtext}",
        "color": 2741919,
        "footer": {
            "text": "Sourced from deals.gg",
            "icon_url": "https://yt3.googleusercontent.com/ytc/AIdro_mibAaXbvzkMXJz1-MiT6kXrG3l86k_dLkaWtWDWLTIZw",
        },
        "timestamp": timestamp,
        "image": {"url": image_url},
    }

    message = {
        "username": "Free Games",
        "embeds": [embed],
    }

    headers = {"Content-Type": "application/json"}

    payload = json.dumps(message)

    try:
        post = requests.post(webhook_url, headers=headers, data=payload)
        print(
            f"[{datetime.now().replace(microsecond=0)}]",
            title,
            f"| Status: {post.status_code}",
        )
    except Exception:
        print(
            f"[{datetime.now().replace(microsecond=0)}]",
            f"{title}: webhook failed to send",
        )


def ping_users():
    """Pings all the users in the text channel"""
    message = {
        "username": "Free Games",
        "content": "@everyone \n# Free game alert!",
    }

    headers = {"Content-Type": "application/json"}

    payload = json.dumps(message)

    try:
        post = requests.post(webhook_url, headers=headers, data=payload)
        print(
            f"[{datetime.now().replace(microsecond=0)}]",
            "Pinging users",
            f"| Status: {post.status_code}",
        )
    except Exception:
        print(
            f"[{datetime.now().replace(microsecond=0)}]",
            "Cannot ping users: webhook failed to send",
        )


if __name__ == "__main__":
    """Send message with sample test data."""
    title = "Placeholder title"
    time = "2024-08-02T23:00:00.000Z"
    game_link = "https://gg.deals/freebie/free-disney-epic-mickey-rebrushed-demo-is-now-available/"
    sub_text = "Placeholder Subtext"
    image = (
        "https://img.gg.deals/b0/1d/347ca876b7e8169662ce02a8a4c6f5fb019e_259cr135.jpg"
    )

    ping_users()
    send_embed(title, sub_text, time, game_link, image)
