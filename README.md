# Insta Follower Bot

Day 52 of my 100 Days of Python challenge. This is a little Selenium bot that logs into [Share-a-Naan](https://app.100daysofpython.dev/services/share-a-naan) (the course's Instagram-style practice site), searches for a similar account, opens their followers list, scrolls through it, and follows everyone it hasn't already followed.

Heads up: this targets the practice site, not real Instagram. Automating actions on actual Instagram would break their Terms of Service and get an account banned, so don't point this at anything real.

## What it does

1. Logs in with your credentials
2. Searches for an account similar to yours
3. Opens their followers list
4. Scrolls to the bottom, waiting for new followers to load each time, until the list stops growing
5. Clicks "Follow" on everyone still unfollowed

## Setup

You'll need Python 3 and these packages:

```bash
pip install selenium python-dotenv
```

Chrome needs to be installed — Selenium will handle the driver itself (no need to download chromedriver manually).

Create a `.env` file in this folder with:

```
URL=
EMAIL=
PASSWORD=
SIMILAR_ACCOUNT=
```

- `URL` — the login page for Share-a-Naan
- `EMAIL` / `PASSWORD` — your login credentials
- `SIMILAR_ACCOUNT` — the username whose followers you want to follow

## Running it

```bash
python3 main.py
```

A Chrome window will open and do its thing. It stays open after the script finishes (so you can see what happened) rather than closing itself.

## Notes to self

- The followers modal isn't virtualized, so scrolling has to genuinely wait for the network to fetch more rows — there's no way to just "scroll to the end" in one shot.
- If Instagram-style selectors ever break, it's almost always because the site's XPath/class structure changed rather than a logic bug.
