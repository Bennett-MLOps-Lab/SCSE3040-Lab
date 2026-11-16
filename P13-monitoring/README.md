# Practical 13 --- Watching a Model Get Worse

*Drift detection, alert rules, and an audit of who the model serves badly*

SCSE3040 Machine Learning Operations · Bennett University · Session 2026-27

| | |
|---|---|
| Follows lectures | L26, L28 |
| Course Outcome | CO5 |
| Duration | 120 minutes |
| Peak memory | ~500 MB |
| Extra software | nothing beyond the course venv |
| Marks | 10 |

## Aim

1. Measure a deployed model's error week by week instead of once.
2. Detect when the incoming data stops looking like the training data.
3. Write an alert rule that fires on a real problem, not on noise.
4. Audit whether the model serves some groups of customers worse.

## Before you start

- Practicals P02 and P07 are finished. You can train a model and serve it.
- You remember MAE from P02: the average miss, in minutes.

## Background


This is the second-last practical, and it covers the thing most courses leave
out. Your model is deployed. Nobody is watching it. It is quietly getting worse.
The last practical, P14, repairs what you find today.

It gets worse because the world moves. A new restaurant partner has slower
kitchens. The monsoon arrives. The company expands into a suburb 15 km out,
when every delivery you trained on was under 12 km. The code did not change; the
world did. That is **drift**.

There are two kinds and you must be able to tell them apart.

**Data drift** means the inputs changed shape --- distances are longer than they
used to be. You can detect this **immediately**, because you see every request
as it arrives.

**Concept drift** means the relationship changed --- the same 5 km trip now
takes longer than it used to, because traffic rules changed. To detect this you
need the **true answer**, which arrives only when the delivery is complete. In a
delivery service that is an hour later. In credit scoring it can be a year.

That gap is why we watch the inputs as well as the errors. The standard measure
is **PSI**, the Population Stability Index: it compares the shape of a feature
now against the shape it had in training. The conventional reading is below 0.1
stable, 0.1 to 0.25 worth watching, above 0.25 a real shift.

Then there is the part that is not statistics. A model with a good average can
still be bad for particular people. Yours might predict well for short trips in
dry weather and badly for long trips in the rain --- and the customers who
suffer are always the ones on the edge of town. An **average hides a
distribution**. So today you finish by splitting the error by group and looking
for who the model serves worst.

That last check is the whole of L28 in one habit: not "is my model accurate?"
but **"accurate for whom?"**


## What you will do

1. **Train the model that will go into production**
2. **Eight weeks of real traffic arrive**
3. **Measure the error week by week**
4. **Draw it, because a table hides a trend**
5. **Which way is it wrong? Find where the model breaks**
6. **Detect the drift in the inputs**
7. **See the drift: the two shapes PSI compares**
8. **Write an alert rule that does not cry wolf**
9. **Draw the warning and the alarm on one timeline**
10. **Triage: what should we do this week?**
11. **The numbers a service should publish**
12. **Accurate for whom?**
13. **Draw the audit, with the counts on the bars**
14. **Is the gap real, or a few bad orders?**
15. **The audit checklist**
16. **Write it down: the incident note**

## Your turn

- **T1 --- Drift in a different feature.** We watched `distance_km`. Check whether `prep_time_min` drifted too.
- **T2 --- A stricter alert.** The team decides the current rule is too slow. Apply `check_alerts`
- **T3 --- Who does this model serve worst?.** Using the `week8` table, build `T3_by_trip`: a dictionary mapping each

## What to submit

1. This notebook, with every cell run and every chart visible.
2. In a markdown cell, your answer to checklist question 1 for this model: which group is worst served, by how much, and what you would do about it. Write it in your own words; the incident note from Step 16 shows the shape.
3. In a markdown cell, the alert rule you would actually configure: the metric, the threshold, how long it must persist, and who is woken up.

## Marking

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, all charts produced | 3 |
| Task T1 --- drift measured with PSI | 2 |
| Task T2 --- an alert rule applied correctly | 2 |
| Task T3 --- the worst-served group identified | 3 |
| **Total** | **10** |

## Read more

- Prometheus --- Metric types --- <https://prometheus.io/docs/concepts/metric_types/>
- Prometheus --- Alerting rules --- <https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/>
- Grafana --- Introduction to dashboards --- <https://grafana.com/docs/grafana/latest/dashboards/>
- Fairlearn --- Assessing fairness --- <https://fairlearn.org/main/user_guide/assessment/index.html>
- scikit-learn --- Metrics and scoring --- <https://scikit-learn.org/stable/modules/model_evaluation.html>

---

*Open `P13.ipynb` in Jupyter and work through it top to bottom.
The notebook contains everything in this handout, plus the code.*
