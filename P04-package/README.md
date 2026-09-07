# Practical 04 --- From Notebook to Package

*Turn scattered cells into a folder of code that someone else can run*

SCSE3040 Machine Learning Operations · Bennett University · Session 2026-27

| | |
|---|---|
| Follows lectures | L07 |
| Course Outcome | CO3 |
| Duration | 120 minutes |
| Peak memory | ~300 MB |
| Extra software | nothing beyond the course venv |
| Marks | 10 |

## Aim

1. Explain why a notebook stops being good enough for real work.
2. Turn cells into functions, and functions into a package of modules.
3. Import your own code and use it, the way a library is used.
4. Run your project from the command line, with no notebook at all.

## Before you start

- Practicals P01-P03 are finished. You have trained and scored a model.
- You know what a function is, and what `import` does.

## Background


Everything you have written so far lives in notebook cells. That is fine for
exploring. It stops being fine the moment somebody else needs to run your work.

There are three reasons.

**Hidden state.** A notebook remembers everything you ran, including cells you
have since edited or deleted. The screen can show code that never actually ran,
next to a result produced by code that no longer exists. Nobody can tell by
looking.

**Order.** Notebook cells can be run in any order. Yours works because you
happened to run them in the right sequence today. On another machine, top to
bottom, it may not.

**Nothing can import a notebook.** A web service cannot `import` a cell. A test
cannot call a cell. A scheduled job cannot run a cell. To be used by other
software, code must live in a **module**: an ordinary `.py` file.

So today you refactor. **Refactoring** means changing how code is arranged
without changing what it does. You will take the working code from P02, put it
into functions, group those functions into files by job, and put those files
into a folder with an `__init__.py` in it. A folder like that is called a
**package**, and Python can import it.

At the end you will run your whole training pipeline from a terminal, with one
command and no notebook. That is the shape every later practical needs: P05
tests this package, P07 serves it, P08 puts it in a container.


## What you will do

1. **See the problem before fixing it**
2. **Plan the package before writing it**
3. **Write the first module: data.py**
4. **Write features.py**
5. **Write model.py**
6. **Add __init__.py to make it a package**
7. **Import your own package and use it**
8. **Save the trained model to a file**
9. **Write the script a human runs**
10. **Run it as a real program**

## Your turn

- **T1 --- Add a function to the package.** Add a function `average_speed_kmph(distance_km, delivery_min)` to
- **T2 --- Reject an impossible order.** Write a **new module** `delivery/validate.py` containing one function,
- **T3 --- A second command-line script.** Write `work/predict.py`: a script that loads the saved model from

## What to submit

1. This notebook, with every cell run and its output visible.
2. The `work/delivery/` folder you built, zipped.
3. In a markdown cell, one sentence per module saying what its single job is.

## Marking

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, package builds and imports | 3 |
| Task T1 --- a new function added to the package | 2 |
| Task T2 --- validation logic that rejects bad orders | 3 |
| Task T3 --- a script that runs from the command line | 2 |
| **Total** | **10** |

## Read more

- Python docs --- Modules and packages --- <https://docs.python.org/3/tutorial/modules.html>
- Python docs --- The module search path --- <https://docs.python.org/3/tutorial/modules.html#the-module-search-path>
- joblib --- Persistence --- <https://joblib.readthedocs.io/en/stable/persistence.html>
- scikit-learn --- Model persistence --- <https://scikit-learn.org/stable/model_persistence.html>

---

*Open `P04.ipynb` in Jupyter and work through it top to bottom.
The notebook contains everything in this handout, plus the code.*
