# Practical 14 --- Teaching the Model the New Suburb

*Retrain on the right window, judge old against new on the same holdout, promote with a way back*

SCSE3040 Machine Learning Operations · Bennett University · Session 2026-27

| | |
|---|---|
| Follows lectures | L27-L28 |
| Course Outcome | CO5 |
| Duration | 120 minutes |
| Peak memory | ~600 MB |
| Extra software | nothing beyond the course venv |
| Marks | 10 |

## Aim

1. Choose which rows a retrained model should learn from, and say why.
2. Judge the old and the new model on the same held-out orders, never on training rows.
3. Write the promotion gate as code: beat the bar, and beat the old model.
4. Register the new version, move the alias, and keep the old version for rollback.

## Before you start

- Practical P13 is finished. You watched this model get worse and found who it served worst: long trips.
- Practical P06 is finished. You remember MLflow's registry: a model name, numbered versions, and loading by name.
- You remember MAE from P02: the average miss, in minutes.

## Background


P13 ended with an alarm. The delivery company opened a new suburb, trips got
longer, and the model's error tripled. The audit found the reason: past 12 km a
rider is on the highway, every extra kilometre costs more, and the training data
had never contained such a trip. The honest fix was named but not done:
**retrain**.

Retraining sounds like "run the training cell again". It is not, and this
practical is about the four decisions that separate a real retrain from that.

**Which rows?** Not all history --- most of it describes a city that no longer
exists. Not last week alone --- too few rows. The **recent window**, after the
world settled into its new shape. The rows from the new suburb are now the most
valuable rows you own.

**Judged how?** Both models, old and new, on the **same held-out orders** that
neither has trained on. A model judged on its own training rows always wins,
and always lies.

**Promoted when?** Two conditions, both required. The new model must **beat the
bar** --- a fixed quality the product promised --- and it must **beat the old
model**. Passing one is not enough. This is the **gate**, and today you write it
as a function so that it cannot be argued with at eleven at night.

**Replaced how?** The new model becomes **version 2** in the registry. The
alias `@champion` moves from 1 to 2. Version 1 is **kept**, because the way back
is the whole point of versions. The service loads `@champion` by name, so
nothing in the serving code changes.

The pipeline *proposes*; a named person *promotes*. Automation earns trust
slowly, and the alias stays a human decision in this course.


## What you will do

1. **Train the model that raised the alarm**
2. **Twelve weeks of traffic, and the alarm**
3. **Draw the timeline, and mark the window**
4. **Has the world stopped moving? Check before you retrain**
5. **Choose the window, and hold out before you touch anything**
6. **Candidate A: the same code, the new window**
7. **The gate, as code**
8. **Where candidate A still fails: the audit, again**
9. **Candidate B: teach the model the highway rule**
10. **Draw what each model still gets wrong**
11. **Audit all three models, group by group**
12. **Would the gate decide the same on a different exam?**
13. **Put the launch model into the registry as version 1**
14. **Register version 2 and move the alias, keeping version 1**
15. **Serving asks for @champion, and gets the new model**
16. **Old and new, across every distance**
17. **Close the loop: four more weeks with the new champion**
18. **Write it down: the promotion record**

## Your turn

- **T1 --- The stale window.** A teammate argues the retrain should use weeks **1 to 4** --- "that
- **T2 --- Roll back, then forward again.** Monday morning: a bug report blames version 2. Prove you can undo the
- **T3 --- A challenger of your own, through the whole gate.** Would a random forest (P03) do better than a straight line, now that

## What to submit

1. This notebook, with every cell run and every chart visible.
2. In a markdown cell, the two numbers the gate compared for candidate B, and one sentence on why candidate A was held even though it beat the old model.
3. In a markdown cell, the exact one-line command you would run to roll back, and who in a real team should be allowed to run it. Step 18's promotion record shows the shape; write it in your own words.

## Marking

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, all charts produced | 3 |
| Task T1 --- the stale window judged on the same holdout | 2 |
| Task T2 --- rollback and re-promotion through the alias | 2 |
| Task T3 --- a challenger taken through the full gate | 3 |
| **Total** | **10** |

## Read more

- MLflow --- Model Registry: aliases --- <https://mlflow.org/docs/latest/model-registry.html>
- MLflow --- Saving scikit-learn models (serialization formats) --- <https://mlflow.org/docs/latest/python_api/mlflow.sklearn.html>
- scikit-learn --- Pipelines and FunctionTransformer --- <https://scikit-learn.org/stable/modules/compose.html>
- Evidently --- When to retrain --- <https://www.evidentlyai.com/ml-in-production/model-retraining>
- Google --- Rules of ML (rule 37: measure training/serving skew) --- <https://developers.google.com/machine-learning/guides/rules-of-ml>

---

*Open `P14.ipynb` in Jupyter and work through it top to bottom.
The notebook contains everything in this handout, plus the code.*
