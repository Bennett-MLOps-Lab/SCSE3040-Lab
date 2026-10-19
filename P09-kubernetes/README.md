# Practical 09 --- Describing the Service to a Cluster

*Deployment, Service and probes, written as YAML and checked before they run*

SCSE3040 Machine Learning Operations · Bennett University · Session 2026-27

| | |
|---|---|
| Follows lectures | L15-L17 |
| Course Outcome | CO4 |
| Duration | 120 minutes |
| Peak memory | ~200 MB |
| Extra software | nothing beyond the course venv |
| Marks | 10 |

## Aim

1. Explain what a Deployment and a Service each do, in plain words.
2. Write both as YAML manifests for the delivery-time container.
3. Check a manifest is correct before it ever reaches a cluster.
4. Add readiness and liveness probes, and say what each one is for.

## Before you start

- Practical P08 is finished. You have an image called `delivery-api:1.0`.
- You have seen YAML in P05. Remember: spaces only, never tabs.
- `kubectl` and a cluster are **optional** today. Every graded task is about writing correct manifests, which you can do on any machine. If Docker Desktop has Kubernetes enabled, the notebook will also run the real commands for you.

## Background


In P08 you ran one container with `docker run`. That works until you need a
second copy, or the machine reboots, or the container dies at two in the
morning. Somebody has to notice and start it again.

**Kubernetes** is the software that does the noticing. You do not tell it what
to do; you tell it **what you want**, and it works continuously to make reality
match. That style is called **declarative**, and it is the single idea behind
everything today.

Three objects matter for us.

A **Pod** is one running copy of your container. It is the smallest thing
Kubernetes handles. Pods are disposable: they get killed and replaced, and they
get a new address every time.

A **Deployment** is a standing order: *keep three copies of this image running
at all times*. If one dies, the Deployment makes another. If you change the
image, it replaces them one at a time so the service never goes down.

A **Service** is one permanent address in front of those changing Pods. Since
Pods come and go with new addresses, nothing could reliably call them. The
Service is the fixed name that spreads requests across whichever Pods exist now.

The glue between Deployment and Service is **labels**. A Deployment stamps a
label on its Pods; a Service says "send traffic to anything with this label". If
those two strings do not match, everything appears healthy and nothing works.
That is the most common Kubernetes mistake in the world, and you will fix it in
Task T3.

Finally, **probes**. Kubernetes cannot guess what "working" means for your
service, so you tell it. A **readiness** probe asks *should traffic come yet?*
--- a model that takes 30 seconds to load should not receive requests at second
2. A **liveness** probe asks *are you still alive?* --- if it fails, the
container is restarted. Confusing the two is how one slow pod becomes an endless
restart loop.


## What you will do

1. **Check whether a cluster is available**
2. **Write the Deployment**
3. **Check the YAML before anybody runs it**
4. **Write the Service**
5. **Prove the Service can find the Pods**
6. **Add the health probes**
7. **What each probe does when it fails**
8. **Send it to a cluster, if you have one**
9. **Reading a broken deployment**

## Your turn

- **T1 --- Write a Service for a second version.** Write `work/service-v2.yaml`: a Service named `delivery-api-v2-svc`
- **T2 --- Probes for a slow model.** A new model takes **40 seconds** to load. The Deployment in Step 6 has a
- **T3 --- Find the mismatch.** The two manifests below look fine and would deploy without a single

## What to submit

1. This notebook, with every cell run and its output visible.
2. Your `work/deployment.yaml` and `work/service.yaml`.
3. In a markdown cell, two sentences: what happens when a readiness probe fails, and what happens when a liveness probe fails.

## Marking

| What is marked | Marks |
|---|---|
| Walkthrough run end to end, manifests written and checked | 3 |
| Task T1 --- a correct Service manifest | 2 |
| Task T2 --- probes added with sensible delays | 3 |
| Task T3 --- the label mismatch found and fixed | 2 |
| **Total** | **10** |

## Read more

- Kubernetes --- Deployments --- <https://kubernetes.io/docs/concepts/workloads/controllers/deployment/>
- Kubernetes --- Service --- <https://kubernetes.io/docs/concepts/services-networking/service/>
- Kubernetes --- Configure liveness, readiness and startup probes --- <https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/>
- Kubernetes --- kubectl quick reference --- <https://kubernetes.io/docs/reference/kubectl/quick-reference/>

---

*Open `P09.ipynb` in Jupyter and work through it top to bottom.
The notebook contains everything in this handout, plus the code.*
