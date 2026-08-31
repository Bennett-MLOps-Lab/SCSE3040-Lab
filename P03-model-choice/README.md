# Practical 03 --- Choosing a Model Honestly

*Overfitting, the train/test gap, and cross-validation*

SCSE3040 Machine Learning Operations · Bennett University · Session 2026-27

| | |
|---|---|
| Follows lectures | L04-L05 |
| Course Outcome | CO2 |
| Duration | 120 minutes |
| Peak memory | ~400 MB |
| Extra software | nothing beyond the course venv |
| Marks | 10 |

## Aim

1. Train three different models on the same data and compare them fairly.
2. See overfitting happen, and measure it as a gap between two scores.
3. Use cross-validation instead of trusting one lucky split.
4. Choose a model for a reason you can defend, not because it scored best.

## Before you start

- Practical P02 is finished. You can split data, train a model and read an MAE.
- You remember that the test set is the only honest score.

## Background


In P02 you trained one model and it did well. A reasonable next thought is
"let me try a more powerful model and do even better". Today you find out why
that thought is dangerous.

A **decision tree** is a model that asks yes/no questions: *is the distance more
than 6 km? is it raining?* Ask enough questions and you can separate every
single training order from every other one. At that point the model has not
learned a pattern --- it has memorised the training data. It will look perfect
in training and fall apart on anything new.

That failure has a name: **overfitting**. And it has a measurement. Score the
model twice, once on the data it trained on and once on data it has never seen.
The distance between those two numbers is the **train/test gap**. A small gap
means the model learned something general. A big gap means it memorised.

There is one more problem to fix. In P02 your test set was one particular 120
orders, chosen by one particular seed. What if those 120 happened to be easy?
**Cross-validation** removes that luck: it cuts the data into 5 equal parts,
trains 5 times, and each time tests on a different part. You get 5 scores
instead of 1, and you report the average. It costs 5 times the computing time,
which on this dataset means well under a second.

The habit to build today: *the best score is not the best model.* A simple model
that scores almost as well is usually the one to ship, because you can explain
it, it trains faster, and it breaks less.


## What you will do

1. **Set up the data once, for all three models**
2. **A helper that scores a model both ways**
3. **Model 1: linear regression, the honest baseline**
4. **Model 2: a decision tree with no limits**
5. **Model 3: the same tree, but shallow**
6. **Model 4: a random forest**
7. **Put the four results side by side**
8. **Stop trusting one split: cross-validation**
9. **Tune one setting, properly**
10. **Choose, and be able to say why**

## Your turn

- **T1 --- Measure overfitting yourself.** Train a `DecisionTreeRegressor` with `max_depth=12` and
- **T2 --- Tune the forest, without touching the test set.** A random forest has a setting `max_depth` too. Use **5-fold
- **T3 --- A comparison you can reuse.** Write a function `compare(models)` that takes a **dictionary** of

## What to submit

1. This notebook, with every cell run and its output visible.
2. In a markdown cell at the end, three sentences: which model you would put in front of real customers, why, and what you gave up by choosing it.

## Marking

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, outputs visible | 3 |
| Task T1 --- overfitting measured as a gap | 2 |
| Task T2 --- best setting found by cross-validation | 3 |
| Task T3 --- a reusable comparison function | 2 |
| **Total** | **10** |

## Read more

- scikit-learn --- Underfitting vs overfitting --- <https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html>
- scikit-learn --- Cross-validation --- <https://scikit-learn.org/stable/modules/cross_validation.html>
- scikit-learn --- Decision trees --- <https://scikit-learn.org/stable/modules/tree.html>
- scikit-learn --- Ensemble methods --- <https://scikit-learn.org/stable/modules/ensemble.html>

---

*Open `P03.ipynb` in Jupyter and work through it top to bottom.
The notebook contains everything in this handout, plus the code.*
