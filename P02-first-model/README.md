# Practical 02 --- Your First Honest Model

*Split the data, train a model, and prove it beats guessing*

SCSE3040 Machine Learning Operations · Bennett University · Session 2026-27

| | |
|---|---|
| Follows lectures | L03 |
| Course Outcome | CO2 |
| Duration | 120 minutes |
| Peak memory | ~300 MB |
| Extra software | nothing beyond the course venv |
| Marks | 10 |

## Aim

1. Split a dataset into a training part and a testing part, and say why.
2. Train a linear regression model on the delivery data.
3. Measure the error with MAE and RMSE.
4. Compare your model against a baseline, so the score means something.

## Before you start

- Practical P01 is finished. You know what a seed is and why it matters.
- You can run a notebook cell with Shift + Enter.
- You have seen the delivery dataset and its five columns.

## Background


Today you build a model that predicts how many minutes a food delivery will
take. The idea is simple: show a program many past deliveries, and let it work
out the pattern.

Two words first.

**Features** are the facts you know *before* the delivery happens: the distance,
how long the restaurant takes to cook, the traffic, whether it is raining. We
call this collection `X`.

**Target** is the thing you want to predict: the actual minutes taken. We call
it `y`.

Now the important part, and the part students get wrong for years. If you train
a model on 600 deliveries and then test it on those same 600 deliveries, of
course it does well --- it has seen the answers. That is not a test; it is
memory. So we cut the data in two: a **training set** the model learns from,
and a **test set** it never sees until we score it. The test score is the only
honest one.

Finally, a score on its own means nothing. Is an error of 4 minutes good? You
cannot say until you know what a *stupid* method scores. So we build a
**baseline** first: always predict the average delivery time, ignoring every
feature. If your clever model cannot beat that, it is not clever.

The measure we use is **MAE** (Mean Absolute Error): on average, how many
minutes were we off by? It is in minutes, so anyone can understand it.


## What you will do

1. **Load the deliveries and look at them**
2. **Separate the features from the target**
3. **Cut the data in two**
4. **The number to beat: always guess the average**
5. **Train a real model**
6. **Score it on the data it has never seen**
7. **Ask the model what it learned**
8. **Predict one new order**

## Your turn

- **T1 --- Work out the baseline yourself.** Step 4 used the **mean** (the average) as the baseline. Another common
- **T2 --- Does the split change the answer?.** Everything so far used an 80/20 split with seed 42. Redo the whole
- **T3 --- One order in, one number out.** Write a function `predict_minutes(distance_km, prep_time_min,

## What to submit

1. This notebook, with every cell run and its output visible.
2. In a markdown cell at the end, one sentence saying whether your model beat the baseline and by how much.

## Marking

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, outputs visible | 3 |
| Task T1 --- baseline computed correctly | 2 |
| Task T2 --- model retrained on a different split | 2 |
| Task T3 --- a working single-order predictor | 3 |
| **Total** | **10** |

## Read more

- scikit-learn --- train_test_split --- <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html>
- scikit-learn --- Linear regression --- <https://scikit-learn.org/stable/modules/linear_model.html>
- scikit-learn --- Metrics for regression --- <https://scikit-learn.org/stable/modules/model_evaluation.html>

---

*Open `P02.ipynb` in Jupyter and work through it top to bottom.
The notebook contains everything in this handout, plus the code.*
## How to Run

Open `P02.ipynb` in Jupyter Notebook or VS Code and run the cells from top to bottom.