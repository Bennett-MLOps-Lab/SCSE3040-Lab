# Practical 06 --- Remembering Every Experiment

*Tracking runs, comparing them, and registering the winner with MLflow*

SCSE3040 Machine Learning Operations · Bennett University · Session 2026-27

| | |
|---|---|
| Follows lectures | L11 |
| Course Outcome | CO5 |
| Duration | 120 minutes |
| Peak memory | ~700 MB |
| Extra software | nothing beyond the course venv |
| Marks | 10 |

## Aim

1. Record the settings and the score of every training run automatically.
2. Search past runs and find the best one without opening a notebook.
3. Save a trained model as an artifact you can load again later.
4. Register that model so it has a name and a version number.

## Before you start

- Practicals P02-P04 are finished. You can train a model and score it.
- You know what a dictionary is, and what a CSV file is.

## Background


By P03 you had trained six models. Could you say, right now, which settings
produced the best score? Most people cannot. They tried things, kept the good
number in their head, and lost it.

That is the problem **experiment tracking** solves. Every time you train, a
tool records four things:

- **Parameters** --- the settings you chose. `max_depth=4`, `test_size=0.2`.
- **Metrics** --- the numbers that came out. `mae=2.03`.
- **Artifacts** --- files the run produced, above all the trained model itself.
- **Tags** --- your own labels, such as who ran it or why.

**MLflow** is the most widely used tool for this, and it is free and open
source. You add about three lines to your training code and everything is kept
for you, in a database you can query later.

Then there is the second half: the **model registry**. Tracking answers "what
did I try?". The registry answers "which model is the one we actually use?" It
gives a model a name and a **version number**, so the team can say *delivery-time
model, version 3* and everybody means the same file.

One warning before you start, and it will save you an hour. Almost every
tutorial and textbook older than 2025 tells you MLflow stores runs in a folder
called `./mlruns`. **MLflow 3 put that folder store into maintenance mode.** If
you follow those instructions you will get confusing errors. The current
approach, and the one we use today, is a small database file. It is one line
different, and it works.


## What you will do

1. **The problem, in one cell**
2. **Point MLflow at a database**
3. **Your first tracked run**
4. **Read it back**
5. **Log a whole sweep of settings**
6. **Find the winner without looking at a notebook**
7. **Draw the sweep from the database**
8. **Save the winning model itself**
9. **Look at the registry**
10. **Load a model back, by name and version**
11. **See it in the web interface**

## Your turn

- **T1 --- Track a different kind of model.** Log one new run, named exactly `linear-baseline`, that:
- **T2 --- Ask the database, not your memory.** Without reading any earlier output, use `mlflow.search_runs` to find the
- **T3 --- A sweep you can filter later.** Run a small sweep of `DecisionTreeRegressor` at depths `[2, 4, 6]`.

## What to submit

1. This notebook, with every cell run and its output visible.
2. A screenshot of the MLflow run table in the browser, showing the `mae_minutes` column and at least six runs.
3. In a markdown cell, one sentence saying which settings won and by how much they beat the worst run.

## Marking

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, runs visible in MLflow | 3 |
| Task T1 --- a linear-regression run logged correctly | 2 |
| Task T2 --- the best run found by querying, not by eye | 2 |
| Task T3 --- a tagged sweep that can be filtered | 3 |
| **Total** | **10** |

## Read more

- MLflow --- Tracking quickstart --- <https://mlflow.org/docs/latest/getting-started/intro-quickstart/>
- MLflow --- Search runs syntax --- <https://mlflow.org/docs/latest/search-runs.html>
- MLflow --- Model Registry --- <https://mlflow.org/docs/latest/model-registry.html>
- MLflow --- Backend stores --- <https://mlflow.org/docs/latest/tracking/backend-stores.html>

---

*Open `P06.ipynb` in Jupyter and work through it top to bottom.
The notebook contains everything in this handout, plus the code.*
