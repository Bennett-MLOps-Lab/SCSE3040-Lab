# Practical 12 --- A Pipeline You Can Re-run

*Tasks in the right order, failures that stop the line, and a schedule*

SCSE3040 Machine Learning Operations · Bennett University · Session 2026-27

| | |
|---|---|
| Follows lectures | L24-L25 |
| Course Outcome | CO4 |
| Duration | 120 minutes |
| Peak memory | ~400 MB |
| Extra software | nothing beyond the course venv |
| Marks | 10 |

## Aim

1. Break a job into small tasks and say which depends on which.
2. Work out a safe order to run them in, automatically.
3. Make a pipeline safe to re-run, and safe to fail half way through.
4. Read a cron schedule and say when a job will next run.

## Before you start

- Practicals P04 and P05 are finished. You can write functions and tests.
- You know what a dictionary and a list are.

## Background


Everything you have built so far runs when you press a button. Real systems do
not work like that. Every night, without anyone awake, the same steps have to
happen in the same order: fetch yesterday's deliveries, check them, build the
features, retrain, write a report.

That chain is a **data pipeline**, and the tool that runs it in production is
usually **Apache Airflow**. Airflow needs a database, a scheduler, a web server
and a couple of gigabytes of memory --- more than a lab machine can spare. So
today you build the *ideas* Airflow implements, in about forty lines of Python.
Everything you learn transfers directly.

The central idea is the **DAG**, short for **Directed Acyclic Graph**. Take that
apart:

- **Graph** --- tasks with arrows between them
- **Directed** --- the arrows point one way: *train* comes after *validate*
- **Acyclic** --- no loops. If A waits for B and B waits for A, nothing can
  ever start.

From a DAG you can work out an order to run things in. That calculation is
called a **topological sort**, and you will write one.

Two properties separate a pipeline that survives from one that ruins a Sunday.

**Idempotent** means running it twice gives the same result as running it once.
Yesterday's run crashed half way; you fix the bug and run it again. If the
pipeline appends rather than replaces, you now have every row twice, and nobody
notices for a month.

**Fail fast** means when a task fails, everything downstream is *skipped*, not
attempted. If validation fails, training must not run --- a model trained on bad
data is worse than no model, because it looks fine.

Finally, **cron**: five fields saying when to run. `0 2 * * *` means "minute 0,
hour 2, every day". You will meet it in Airflow, in Kubernetes CronJobs, and on
every Linux server you ever touch.


## What you will do

1. **Write the tasks as ordinary functions**
2. **Describe the order as a graph**
3. **Work out a safe order**
4. **Prove it catches a loop**
5. **Run the pipeline**
6. **Run it again, and check nothing changed**
7. **Watch a failure stop the line**
8. **Retry the things worth retrying**
9. **Say when it should run**
10. **Batch or stream?**

## Your turn

- **T1 --- Add a task to the pipeline.** The team wants a copy of the trained model saved every night, **after**
- **T2 --- Predict the damage.** No code to run for this one --- think it through.
- **T3 --- Read and write a schedule.** Two parts.

## What to submit

1. This notebook, with every cell run and its output visible.
2. Your `work/daily_report.txt`.
3. In a markdown cell, one sentence saying what would have gone wrong if `validate` had not stopped the pipeline in Step 7.

## Marking

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, pipeline succeeds then fails safely | 3 |
| Task T1 --- a new task wired into the graph | 3 |
| Task T2 --- the effect of a failure predicted correctly | 2 |
| Task T3 --- schedules read and written | 2 |
| **Total** | **10** |

## Read more

- Apache Airflow --- Core concepts: DAGs --- <https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html>
- Apache Airflow --- Tasks and dependencies --- <https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html>
- Apache Airflow --- Cron and time intervals --- <https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html>
- Kubernetes --- CronJob --- <https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/>

---

*Open `P12.ipynb` in Jupyter and work through it top to bottom.
The notebook contains everything in this handout, plus the code.*
