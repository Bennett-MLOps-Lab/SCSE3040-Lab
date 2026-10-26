# Practical 11 --- A Robot That Checks Your Work

*Continuous integration with GitHub Actions, rehearsed on your own machine*

SCSE3040 Machine Learning Operations · Bennett University · Session 2026-27

| | |
|---|---|
| Follows lectures | L20-L21 |
| Course Outcome | CO4 |
| Duration | 120 minutes |
| Peak memory | ~350 MB |
| Extra software | nothing beyond the course venv |
| Marks | 10 |

## Aim

1. Explain what continuous integration is and which problem it solves.
2. Write a GitHub Actions workflow that installs, tests and checks a project.
3. Run the pipeline's own steps on your machine before pushing anything.
4. Read a failed pipeline and say exactly which step broke and why.

## Before you start

- Practical P05 is finished. You can write tests and run pytest.
- You have seen YAML twice now. Spaces only.
- A GitHub account is useful for the optional last step, but nothing today requires one.

## Background


Picture the Friday-evening deploy. Someone pulls the latest code, runs the
tests on their laptop, sees green, and ships. On Monday it is broken, because
their laptop had a library the server does not, and because two of the tests
were never actually run.

**Continuous integration**, usually written **CI**, removes the human from that
sentence. Every time anybody pushes code, a clean machine somewhere fetches it,
installs everything from scratch, runs every test, and reports pass or fail. No
one has to remember. No one can skip it.

The vocabulary is small.

A **workflow** is the whole automated procedure, written as a YAML file that
lives in your repository at `.github/workflows/`.

A **trigger** says when to run it --- typically on every push, and on every
pull request.

A **job** runs on a fresh machine. A workflow can have several, and they can run
at the same time.

A **step** is one command inside a job. Steps run in order, and the first one to
fail stops the job.

That last rule is the whole mechanism. Remember from P04 and P05 that a program
returns an **exit code**: 0 for success, anything else for failure. `pytest`
returns 1 if any test failed. The pipeline simply looks at that number. Your
tests from P05 are what makes CI worth having --- without them the robot has
nothing to check.

Today you will write a real workflow file, and then run its steps on your own
machine with a small runner we build together. Rehearsing locally is a genuinely
professional habit: pushing a broken workflow and waiting three minutes to find
out is a slow way to work.


## What you will do

1. **Build a small project worth checking**
2. **Write the workflow**
3. **Check the workflow is valid YAML before pushing it**
4. **Build a runner for the steps you can rehearse**
5. **Rehearse the pipeline**
6. **Fix the pipeline**
7. **Now break a test and watch the robot catch it**
8. **Make the pipeline faster with a cache**
9. **What happens on GitHub**

## Your turn

- **T1 --- Trigger it on the right events.** Build a dictionary `T1_triggers` describing a workflow that runs:
- **T2 --- Add a step that would have caught a real bug.** Add one more step to the workflow, named exactly
- **T3 --- Rehearse it, and get it green.** Run your six-step pipeline with `run_pipeline` and store the result list

## What to submit

1. This notebook, with every cell run and its output visible.
2. Your `work/.github/workflows/ci.yml`.
3. In a markdown cell, two sentences: what the pipeline did when you broke the test, and why the steps after it did not run.

## Marking

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, pipeline goes green then red | 3 |
| Task T1 --- correct triggers on the workflow | 2 |
| Task T2 --- a useful step added to the pipeline | 3 |
| Task T3 --- the pipeline rehearsed and green | 2 |
| **Total** | **10** |

## Read more

- GitHub Docs --- Understanding GitHub Actions --- <https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions>
- GitHub Docs --- Workflow syntax --- <https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions>
- GitHub Docs --- Building and testing Python --- <https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python>
- GitHub Docs --- About protected branches --- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches>

---

*Open `P11.ipynb` in Jupyter and work through it top to bottom.
The notebook contains everything in this handout, plus the code.*
