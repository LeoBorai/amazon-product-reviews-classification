---
title: amazon-reviews-classification
emoji: 🗣️
colorFrom: yellow
colorTo: purple
sdk: gradio
sdk_version: 5.20.1
app_file: app.py
pinned: false
license: mit
short_description: Sentiment Analysis via Logistic Regression
---

<div>
  <h1 align="center">Amazon Product Reviews Classification</h1>
  <h4 align="center">
    Performing Sentiment Analysis on Amazon Product Reviews using Logistic Regression
  </h4>
</div>

## Archived and Moved to HuggingFace

This repository has been moved to HuggingFace as it has tools for ML/AI projects.
Visit it here: [Amazon Reviews Classification](https://huggingface.co/spaces/LeoBorai/amazon-reviews-classification)

## Run Locally

Build an run containers using `docker compose`

```bash
docker compose up --build notebook
```

> Using `Justfile` this is a matter of running `just build` and from
> there on `just dev`

After working you can release resources using:

```bash
docker compose down
```

> A [Justfile][1] is included!

[1]: https://just.systems
