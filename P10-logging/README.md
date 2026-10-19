# Practical 10 --- Logs You Can Actually Search

*Levels, structured JSON events, and what must never be written down*

SCSE3040 Machine Learning Operations · Bennett University · Session 2026-27

| | |
|---|---|
| Follows lectures | L18 |
| Course Outcome | CO5 |
| Duration | 120 minutes |
| Peak memory | ~350 MB |
| Extra software | nothing beyond the course venv |
| Marks | 10 |

## Aim

1. Explain why `print()` is not good enough once software is deployed.
2. Use logging levels so you can turn detail up and down without editing code.
3. Write one JSON object per event, so logs can be searched by machine.
4. Recognise what must never appear in a log, and mask it.

## Before you start

- Practical P07 is finished. You have a service with a /predict endpoint.
- You know what a dictionary is and what JSON looks like.

## Background


In P08 your service ran inside a container. Suppose at nine at night a customer
complains that a prediction was wrong. What do you actually have to look at?

The container is gone. Its filesystem went with it. `print()` output vanished
with the process. You have nothing.

That is what **logging** is for. A log is a permanent, timestamped record of
what your software did. Three ideas make one useful.

**Levels.** Not every message matters equally. Python gives you five:
`DEBUG` (detail for developers), `INFO` (normal events worth recording),
`WARNING` (something odd but survivable), `ERROR` (this request failed), and
`CRITICAL` (the service is going down). You set a **threshold** and everything
below it is discarded. That is how the same code can be quiet in production and
chatty while you are debugging --- with no code change at all.

**Structure.** A human reads `"prediction took 42ms"`. A machine cannot. With
fifty containers producing thousands of lines an hour, nobody reads logs by
eye --- a tool searches them. So write one **JSON** object per line, with named
fields: `{"event": "prediction", "duration_ms": 42, "distance_km": 5.0}`. Now
"show me every prediction slower than 200 ms" is a query, not an afternoon.

**Where they go.** In a container you do **not** write to a log file. Write to
standard output, and let the platform collect it. That is what `kubectl logs`
reads, and what a collector like FluentD or Fluent Bit ships to a central store
such as the ELK stack. A log file inside a container dies with the container,
which is exactly the problem you were trying to solve.

One rule that is not technical. A log is a permanent record that many people can
read. Names, phone numbers, exact home addresses, card numbers --- none of it
belongs there. You will practise removing it today.


## What you will do

1. **Why print() is not enough**
2. **Set up a logger**
3. **The five levels**
4. **Turn the volume down without touching the code**
5. **One line, one event, as JSON**
6. **Send the same events to a file as well**
7. **Log a service doing its job**
8. **Search the logs like a machine would**
9. **What must never go in a log**
10. **Where logs go once you are in a cluster**

## Your turn

- **T1 --- Decide what gets recorded.** A colleague wants the service to record warnings and errors only ---
- **T2 --- A formatter for the delivery service.** Write a class `ServiceFormatter` (a `logging.Formatter`) whose `format`
- **T3 --- Answer a question from the logs.** Your manager asks: **"of the predictions we served, what fraction took

## What to submit

1. This notebook, with every cell run and its output visible.
2. Your `work/service.log`, showing at least 40 JSON lines.
3. In a markdown cell, three fields you would add to every log line in a real delivery service, and why each one helps.

## Marking

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, log file produced | 3 |
| Task T1 --- levels used to control what is recorded | 2 |
| Task T2 --- a formatter with the required fields | 3 |
| Task T3 --- a real question answered from the logs | 2 |
| **Total** | **10** |

## Read more

- Python --- Logging HOWTO --- <https://docs.python.org/3/howto/logging.html>
- Python --- Logging cookbook --- <https://docs.python.org/3/howto/logging-cookbook.html>
- Kubernetes --- Logging architecture --- <https://kubernetes.io/docs/concepts/cluster-administration/logging/>
- The twelve-factor app --- Logs --- <https://12factor.net/logs>

---

*Open `P10.ipynb` in Jupyter and work through it top to bottom.
The notebook contains everything in this handout, plus the code.*
