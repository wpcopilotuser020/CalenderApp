from datetime import datetime
import json
from urllib.error import URLError
from urllib.request import urlopen

from flask import Flask, render_template_string

app = Flask(__name__)


def fetch_today_event(now: datetime) -> str:
    """Fetch one notable historical event for the given date."""
    url = f"https://byabbe.se/on-this-day/{now.month}/{now.day}/events.json"

    try:
        with urlopen(url, timeout=10) as response:
            payload = json.load(response)
    except (URLError, TimeoutError, json.JSONDecodeError):
        return "Unable to fetch today's event right now."

    events = payload.get("events", []) if isinstance(payload, dict) else []
    if not events:
        return "No event found for today."

    event = events[0]
    year = event.get("year", "Unknown year")
    description = event.get("description", "No description available.")
    return f"{year}: {description}"


@app.route("/")
def index():
    now = datetime.now()
    event = fetch_today_event(now)

    return render_template_string(
        """
        <html>
            <head><title>Today's Event</title></head>
            <body>
                <h1>Current Date and Time</h1>
                <p>{{ current_datetime }}</p>
                <h2>Event for Today</h2>
                <p>{{ event }}</p>
            </body>
        </html>
        """,
        current_datetime=now.strftime("%Y-%m-%d %H:%M:%S"),
        event=event,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
