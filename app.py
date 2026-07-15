from datetime import datetime
import json
import socket
from urllib.error import URLError
from urllib.request import urlopen

from flask import Flask, render_template

app = Flask(__name__)


def fetch_today_event(now: datetime) -> str:
    """Fetch one notable historical event for the given date."""
    url = f"https://byabbe.se/on-this-day/{now.month}/{now.day}/events.json"

    try:
        with urlopen(url, timeout=10) as response:
            payload = json.load(response)
    except (URLError, socket.timeout, json.JSONDecodeError):
        return "Unable to fetch today's event right now."

    events = payload.get("events", []) if isinstance(payload, dict) else []
    if not events:
        return "No event found for today."

    event = events[0] if isinstance(events[0], dict) else {}
    year = event.get("year")
    description = event.get("description")
    if not year or not description:
        return "No complete event details available for today."

    return f"{year}: {description}"


@app.route("/")
def index():
    now = datetime.now()
    event = fetch_today_event(now)

    return render_template(
        "index.html",
        current_datetime=now.strftime("%Y-%m-%d %H:%M:%S"),
        event=event,
    )
