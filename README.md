# la gazzetta odierna

A static personal daily brief for AI and motorsports.

## Run
Open `index.html` in a browser. There is no build step or runtime dependency.

## Structure
- `index.html` — edition overview, Highlights, AI and Motorsports cards
- `articles/` — one self-contained long-form briefing per story
- `style.css` — shared responsive presentation

Tabs and tag filters use the small inline script inside `index.html`; no external JavaScript is used. Highlights repeat the same card content as their corresponding desk entries and link to the full briefing.

## Project framework

`PROJECT.md` records the project’s static-site and editorial conventions. Before a release, run:

```sh
python3 tools/site_check.py
```

The checker uses only the standard library and verifies local links, duplicate HTML IDs, and the no-external-JavaScript rule.
