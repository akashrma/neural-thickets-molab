# Neural Thickets

**Paper Explainer**

What if pretraining does more than initialize a model? This notebook explores the
paper's claim that many task-specialized experts can live densely near
pretrained weights, making random local perturbations a plausible post-training
strategy.

Submission for the
[molab Notebook Competition](https://marimo.io/pages/events/notebook-competition)

> **Original paper:** [Diverse Task Experts Are Dense Around Pretrained Weights](https://www.alphaxiv.org/abs/2603.12228)  
> Yulu Gan - Phillip Isola

## Run Locally

### Requirements

- Python `>=3.13`
- [`uv`](https://docs.astral.sh/uv/)

The notebook includes its Python dependencies directly in the script header via
inline script metadata. Those dependencies include:

- `marimo`
- `anywidget`
- `numpy`
- `pandas`
- `torch`
- `plotly`
- `altair`

### Interactive Notebook

From the repository root, run:

```bash
uvx marimo edit --sandbox neural_thickets.py
```

This opens the notebook in marimo's editor. The `--sandbox` flag tells marimo to
create an isolated environment from the dependencies embedded in
`neural_thickets.py`.

### App View

To launch it as a read-only app:

```bash
uvx marimo run --sandbox neural_thickets.py
```

The notebook is designed to be read in marimo's app view with the vertical layout
setting. It is CPU-friendly, and the default experimental settings are the
recommended starting point.

## What Is Inside the Notebook

The notebook includes:

- an intuition-building random guessing game for sparse vs. dense solution
  neighborhoods
- a toy loss-landscape visualization comparing local perturbation search with a
  sequential optimization path
- an interactive 1D signal lab using `simple_1D_signals_expts`
- pretraining controls for a small autoregressive network
- random perturbation sampling around the pretrained model
- RandOpt-style top-k expert selection and ensembling
- an exploratory Controllable RandOpt simulation for thinking about guided
  perturbation search under limited parallel compute

## Repository Layout

```text
.
|-- neural_thickets.py          # Main marimo notebook/app
|-- simple_1D_signals_expts/    # 1D signal datasets, model, pretrain, eval, RandOpt helpers
|-- pyproject.toml              # Project metadata
`-- README.md
```

## Notes

- `neural_thickets.py` is the main entry point.
- The notebook imports local helpers from `simple_1D_signals_expts`, so run
  marimo from the repository root.
- The dependency list in `pyproject.toml` is intentionally minimal; the notebook
  dependencies live in the script header of `neural_thickets.py`.
