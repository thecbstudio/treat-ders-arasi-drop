# treat — Ders Arası Drop

**Go-to-market for a student app, run by an AI agent in one morning.**
Istanbul Ignited by Slush’D · Manus AI Hackathon · 12 October 2026
Team: Çınar Özkan · Ece Azra Odabaşı

Live site: https://treat-ders-arasi-drop.netlify.app
Pilot pipeline: https://treat-ders-arasi-drop.netlify.app/tracker/

## The problem

[treat](https://treat-app.serverpod.space) is a working app: a café posts a free "drop", a student claims it with a QR code, visits, and shares a tagged, gift-disclosed Instagram story. The product existed before the hackathon. What it did not have was a single café, a marketing team, or a budget.

So we did not build a product today. We built its go-to-market.

## What we did

| Step | Tool | Result |
|---|---|---|
| Find real customers | **Apify** (Google Maps scraper) | 184 open cafés within 1.5 km of BAU Beşiktaş South Campus, 3,290 reviews, 53 Instagram profiles, 73 websites |
| Choose and understand them | **Manus** | Every café scored 0–100 for fit (independent, review volume, Instagram, "quiet / good for studying" in reviews); top 5 with reasons and sources |
| Write to each of them | **Manus** | 5 personal offers, each built on a quote from that café's own reviews; 5 outreach messages; a 14-day content plan |
| Give each café its own page | **Manus** | Landing page with one personalised view per café, plus a generic-vs-data-driven offer comparison and a pipeline tracker |
| Make the campaign visuals | **fal.ai** | Campaign photos (FLUX 1.1 Pro Ultra) and a video ad (Kling image-to-video), used on the site, in the pitch video and on Instagram |
| Go live | us | Instagram account opened with the first posts and a reel |
| Test it in the real world | us | Walked into 3 cafés the same day with their pages. **2 said yes.** 1 said no (already has enough customers) |

Before: about one hour per café by hand. After: the whole kit in 29.5 minutes of agent time, then real conversations the same day.

## What is in this repository

- `site/` — the deployed site (English at `/`, Turkish café pages at `/tr/?cafe=<slug>`, tracker at `/tracker/`).
- `data/` — Manus outputs: ranked cafés, outreach messages, content calendar, time log.
- `prompts/` — the prompts given to Manus.
- `social/` — Instagram posts and captions.
- `video/` — source of the pitch video (HyperFrames composition).

## Honest notes

- Scores are a prioritisation derived from Google Maps data and review text, not a verified judgement of any business.
- "Said yes" means the owner agreed to try a pilot drop. No paid partnership or performance result is claimed.
- The Manus-published URL (`*.manus.space`) was not reachable from our network in Istanbul, so the same site is served from Netlify.
- The fal.ai connector inside Manus could not complete authorisation during the event, so the visuals were generated directly on fal.ai.
- Raw review exports are not included in this repository.
