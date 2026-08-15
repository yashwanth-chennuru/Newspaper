# Project Framework

La Gazzetta Odierna is a deliberately small static newspaper. This document is the project’s evolving engineering and editorial framework: it favours clear source files, a zero-dependency published site, and only the abstractions that remove real repetition.

## Runtime boundary

- Published output is static HTML and CSS.
- Interactive behaviour stays in an inline `<script>` in the page that uses it; no external JavaScript bundles.
- Shared visual rules belong in `assets/css/style.css`.
- A browser must be able to open `index.html` directly without a build step.

## Source of truth

- Edition overview: `index.html`.
- Long-form briefings: `articles/`.
- Structured experimental topic content: `data/`.
- Topic hierarchy experiments: `data/motorsports/`.
- Release history: `changelog.html`.

When repeated article markup begins to make a change risky, introduce a small standard-library Python generator with structured data as input. Do not add a framework, package manager, or generated output unless it materially reduces repeated source.

## Implementation rules

1. Prefer semantic HTML (`header`, `nav`, `main`, `section`, `article`, `time`) over generic wrappers.
2. Keep card information compact: title, concise deck, tags, and one clear destination.
3. Reuse CSS classes before adding one-off style rules.
4. Keep editorial facts, source URLs, and display markup separate where practical.
5. Preserve the current frontend output during maintenance refactors unless a visual change is explicitly requested.
6. Do not bypass paywalls, authentication, or access controls when researching.

## Edition workflow

1. Research from the priority source set and record article dates.
2. Update only the relevant topic branch and its highlights.
3. Mark reporting, rumours, and official announcements precisely.
4. Run `python3 tools/site_check.py` before committing.
5. Add a changelog entry and increment `v0.0.x` for each user-visible release. The move to `v1.0.0` remains a user decision.

## Evolving this framework

Change this document only after a repeated pattern, an observed failure, or a new stable convention. Keep additions short, testable, and specific to this project.
