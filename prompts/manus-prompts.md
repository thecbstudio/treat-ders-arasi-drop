# Prompts given to Manus

## 1. Research and scoring

```
You are the growth team for "treat" (treat-app.serverpod.space): a mobile app where local cafés post free "drops" (e.g. a free coffee), students claim them with a QR code, visit, and post a tagged, gift-disclosed Instagram story. Cafés get honest local marketing; students get treated.

Goal: build the go-to-market for Bahçeşehir University Beşiktaş South Campus, Istanbul.

Step 1 (Apify): Use the Google Maps scraper to collect cafés within 1.5 km of the campus: name, rating, review count, address, website, Instagram handle, and 20 most recent reviews each. Target 40+ places.
Step 2: From the reviews, extract what students say (price, crowding, study-friendliness). Score each café 0-100 for fit with treat (independent, mid review count, active Instagram, quiet hours). Output a ranked table as CSV plus the top 10 with one-line reasons.
Step 3: Summarize 5 insights with direct evidence (quote + source café) and propose one campaign concept with a tagline in Turkish and English.

Show your sources. Do not invent data; mark anything you could not verify.
```

## 2. Launch kit

```
Continue with the same data. Campaign: "Ders Arası Drop". Build the launch kit. Log minutes and credits spent per step.

1. Outreach: for the top 5 cafés, write a personal Instagram DM in Turkish (max 70 words each). Each must cite one real insight from that café's own reviews and propose a specific drop for its quiet hours. Add a short follow-up message. Output as a table.
2. Visuals (fal.ai via MCP): generate one key visual for the campaign in two sizes, warm, student, café setting, no text in the image; add the tagline as an overlay. Then a version for each of the top 5 cafés. Then one 5-8 second vertical video ad.
3. Landing page for café owners, in Turkish, deployed to a public URL: hero with the tagline, how it works in 3 steps, "why now" with real numbers from this research, the key visual, and a call to action. Mobile-first.
4. Content calendar: 14 days, Instagram + TikTok, one post per day with hook, format, caption in Turkish, and which visual to use. CSV.

Rules: do not invent users, partners or results. treat has no paying cafés yet; say "pilot". Mark anything unverified.
```

## 3. Proof layer

```
Add a proof layer and do not fabricate any result.
(1) Control vs personalised: for Hygge Coffee Shop show side by side (a) a generic offer any tool could write without data and (b) your data-driven offer; under (b) list each decision you made and the exact review quote or data field behind it.
(2) Per-café pages: make the landing page accept ?cafe=<slug> and personalise the headline, proposed drop and insight quote for each of the top 5.
(3) Pipeline tracker: a public page with one row per top-5 café and columns Found, Scored, Offer ready, Sent, Replied, Agreed, Drop live; fill only the stages that are true now.
(4) Publish the site to a public URL.
(5) One paragraph: which steps ran fully autonomously, which needed a human, total minutes and credits.
```
