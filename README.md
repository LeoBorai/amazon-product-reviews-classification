<div>
  <h1 align="center">Amazon Product Reviews Classification</h1>
  <h4 align="center">
    Performing Sentiment Analysis on Amazon Product Reviews using Logistic Regression
  </h4>
</div>

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
