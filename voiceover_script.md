# Poster Presentation — Voiceover Script (3:00)

**How to record your video:**
1. Open `presentation/presentation.html` in Chrome (double-click or `open presentation.html`)
2. Press **F11** for fullscreen (or Cmd+Shift+F on Mac)
3. Start **QuickTime screen recording** (File → New Screen Recording) with mic enabled
4. Click the **Auto (3:00)** button — smooth continuous zoom/pan plays automatically
5. Narrate along using this script below
6. Stop recording when it finishes (~3:00)

**Controls:**
- **Auto** — auto-play with smooth continuous pan/zoom (~3:00 total)
- **→ / ←** — jump between sections manually
- **Space** — pause/resume
- **R** — reset to start

---

## Step 1: Title (0:00 – 0:08)
*Camera starts zoomed into poster header, pans across title*

> "Hi, I'm Fabio Choi from Team 096. Our project is the US Accident Severity Dashboard — an interactive what-if risk simulator built on 7.7 million US traffic accident records."

---

## Step 2: Motivation (0:08 – 0:25)
*Camera pans into Motivation card*

> "Road traffic accidents kill over 1.3 million people annually. Current road safety tools are reactive — they only analyze crashes after they happen. Transportation planners lack a way to ask 'what would happen if conditions changed?' Our dashboard fills that gap with proactive what-if simulation, letting stakeholders identify high-risk areas and test interventions before deploying resources."

---

## Step 3: Data (0:25 – 0:39)
*Camera drifts to Data card, then Tech Stack*

> "We use the US Accidents dataset by Moosavi et al. — 7.7 million records across 49 states spanning 2016 to 2023, about 1.5 gigabytes of raw CSV. Key features include severity on a 1-to-4 scale, weather condition, time of day, visibility, and infrastructure booleans: traffic signal, junction, crossing, stop sign, and station."

---

## Step 4: Approaches (0:39 – 1:00)
*Camera zooms out to show full Approaches card, drifts across*

> "Our approach has three core components. First, H3 hexagonal spatial binning — we partition the US into uniform hexagonal cells using Uber's H3 index at resolution 3 nationally and resolution 5 for state-level detail. Second, a LightGBM gradient-boosted model trained on the full dataset to predict severity, capturing non-linear interactions between features. Third, empirical severity multipliers — per-feature ratios of mean severity that power real-time what-if simulation without re-running the model. The Delta View uses a diverging green-grey-red color scale to show exactly where conditions improve or worsen."

---

## Step 5: Dashboard (1:00 – 1:35)
*Camera zooms into Dashboard hero screenshots, pans across, then down to detail strip*

> "Here are the three dashboard modes in action. On the left, the Historical View — a US map with H3 hexagons colored by mean severity, green for low, red for high. In the center, What-If Mode — here we're simulating rain on Georgia. The rain multiplier of 1.03 pushes average severity from about 2.51 to 2.58, shown by red delta indicators on the metrics. On the right, Delta View — a diverging map showing pervasive red across Georgia under rain-plus-night conditions, meaning severity worsens everywhere. Below, zoomed-in views: state-level filtering, severity distribution, hourly trends, and simulation impact charts."

---

## Step 6: Results (1:35 – 1:55)
*Camera pans to Experiments & Results, drifts across tables*

> "LightGBM achieves approximately 73% accuracy on the held-out 20% test set with balanced F1 and strong AUC scores. The top predictive features are distance and H3 spatial location, followed by hour of day. Traffic signals decrease severity — supporting infrastructure investment — while junctions increase it. Our sensitivity analysis confirms that nighttime, rain, and severe storms all worsen severity, while adding traffic signals and stop signs improve it."

---

## Step 7: Comparison (1:55 – 2:20)
*Camera pans into Comparison card*

> "Compared to traditional logit models from Savolainen et al., our LightGBM captures non-linear interactions they miss. Compared to neural networks like Abdelwahab and Abdel-Aty, we maintain full interpretability with built-in feature importances — no need for expensive post-hoc SHAP analysis. And compared to existing traffic dashboards, which are descriptive and typically limited to one region, our tool is prescriptive — it lets you simulate scenarios — and covers all 49 states simultaneously."

---

## Step 8: Conclusions (2:20 – 2:45)
*Camera flows to Conclusions, then pulls back to header*

> "To summarize: we built an end-to-end pipeline from 7.7 million raw accident records to an interactive geospatial dashboard with real-time what-if simulation. H3 binning plus empirical multipliers enable instant scenario exploration without re-running the model. The Delta View uniquely visualizes where interventions help most. And our analysis confirms that infrastructure features like traffic signals measurably reduce accident severity, supporting evidence-based investment decisions. Thank you."

---

## Timing Summary

| Step | Section | Duration | Cumulative |
|------|---------|----------|------------|
| 1 | Title | 8s | 0:08 |
| 2 | Motivation | 17s | 0:25 |
| 3 | Data | 14s | 0:39 |
| 4 | Approaches | 21s | 1:00 |
| 5 | Dashboard | 35s | 1:35 |
| 6 | Results | 20s | 1:55 |
| 7 | Comparison | 25s | 2:20 |
| 8 | Conclusions | 25s | 2:45 |

**Total: ~2:45** (15-second buffer before 3:00 limit)

## Rubric Coverage

| Item (Weight) | Where Covered |
|---|---|
| **Motivation (10%)** | Step 2 — problem, why it matters |
| **Approaches (20%)** | Steps 4-5 — what, how, what's new, why it works |
| **Data (10%)** | Step 3 — source, size, features |
| **Results (25%)** | Step 6 — accuracy, features, sensitivity |
| **Comparison (part of Results)** | Step 7 — vs. logit, ANNs, dashboards with citations |
| **Delivery (10%)** | Timed to 2:45, clear pacing |
| **Poster Design (25%)** | Visible throughout — smooth zooms show layout |

## Fact-Check Notes
- **7.7M records**: matches progress report and current app (proposal used an earlier 2.8M figure)
- **~73% accuracy**: from LightGBM training runs (printed at runtime, not saved as constant)
- **Multipliers, not model inference**: the live dashboard uses empirical multipliers from `weights.json`, not LightGBM `predict()` calls
- **Rain multiplier 1.03**: verified from `weights.json`; `2.51 x 1.03 ~ 2.585`
- **Fog removed from sensitivity table**: `weights.json` fog multiplier is 0.9976 (<1), so fog does not worsen severity in our data — replaced with Crossing (0.9253) which clearly decreases severity
- **H3 res-3 / res-5**: national view uses resolution 3 (688 hexes), state drill-down uses resolution 5

## YouTube Upload
- Title: `team096poster-choi`
- Visibility: **Unlisted** (not private, not public)
- Verify URL works in incognito mode
