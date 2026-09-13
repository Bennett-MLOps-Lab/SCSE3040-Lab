# Practical 05 --- Settings in a File, Bugs Caught by a Robot

*YAML configuration and automated testing with pytest*

SCSE3040 Machine Learning Operations · Bennett University · Session 2026-27

| | |
|---|---|
| Follows lectures | L08 |
| Course Outcome | CO3 |
| Duration | 120 minutes |
| Peak memory | ~450 MB |
| Extra software | nothing beyond the course venv |
| Marks | 10 |

## Aim

1. Move every hardcoded setting out of your code and into a YAML file.
2. Read that file from Python and use it to control training.
3. Write automated tests that check your code without you watching.
4. Run the whole test suite with one command and read its report.

## Before you start

- Practical P04 is finished. You can write a module and import it.
- You know what a function is and what it means for one to return a value.

## Background


Two habits today. They look unrelated. They are both about the same thing:
being able to change your project safely.

**Configuration.** Your code is full of numbers somebody chose: the test size
of 0.2, the seed 42, the four column names. Right now they are typed into the
middle of your code. That is called a **magic number**, and it causes two
problems. To change one you must edit code, which risks breaking it. And to
find out what settings produced a result, someone must read every line.

The fix is to put settings in a separate file. We use **YAML** (YAML Ain't
Markup Language), a format designed to be read by humans. Indentation makes the
structure; no brackets, no commas. It is what Docker, Kubernetes and GitHub
Actions all use, so you will meet it constantly from P08 onwards.

**Testing.** Right now you check your code by looking at output and thinking
"that seems about right". That works until your project has forty functions,
and then it stops working entirely.

A **test** is a small piece of code that checks another piece of code, and says
PASS or FAIL without a human. **pytest** is the tool that finds all your tests
and runs them. One command, and you know whether anything broke.

The magic word is `assert`. `assert x == 5` does nothing at all if `x` is 5,
and raises an error if it is not. A test is just a function whose name starts
with `test_`, containing asserts.

Why this matters for MLOps: in P11 a server will run these tests automatically
every time you change your code, and refuse to deploy if any of them fail.


## What you will do

1. **Look at the problem: settings buried in code**
2. **Write the settings into a YAML file**
3. **Read the file into Python**
4. **Train using only the config**
5. **Prove it: change a setting, get a different run**
6. **Draw what the settings change**
7. **Now testing. What is an assert?**
8. **Write a module worth testing**
9. **Write the tests**
10. **Run the tests with one command**
11. **Break something on purpose**
12. **Draw the two runs, the way a pipeline shows them**
13. **Test the model's behaviour, not its exact score**
14. **Share setup with conftest.py**
15. **Draw what the behaviour tests promise**

## Your turn

- **T1 --- Add a setting, and use it.** Add a new section to the config called `training`, with one setting
- **T2 --- Write a test of your own.** Add a **new test file** `work/test_speed.py` containing two tests for
- **T3 --- A behaviour test for the model.** Add one more test to `work/test_model.py` --- **append**, do not

## What to submit

1. This notebook, with every cell run and its output visible.
2. Your `work/config.yaml` and `work/test_orders.py`.
3. In a markdown cell, one sentence explaining why `assert mae == 2.03` would be a bad test.

## Marking

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, all tests passing | 3 |
| Task T1 --- a new setting added and used | 2 |
| Task T2 --- a test you wrote that passes | 3 |
| Task T3 --- a behaviour test for the model | 2 |
| **Total** | **10** |

## Read more

- pytest --- Getting started --- <https://docs.pytest.org/en/stable/getting-started.html>
- pytest --- Fixtures --- <https://docs.pytest.org/en/stable/explanation/fixtures.html>
- PyYAML documentation --- <https://pyyaml.org/wiki/PyYAMLDocumentation>
- YAML specification --- indentation rules --- <https://yaml.org/spec/1.2.2/>

---

*Open `P05.ipynb` in Jupyter and work through it top to bottom.
The notebook contains everything in this handout, plus the code.*
