# Neural Thickets molab Notebook

An interactive [marimo](https://marimo.io/) notebook explaining the ideas behind
**Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights** by
Yulu Gan and Phillip Isola.

The notebook is written as a standalone Python marimo app in
[`neural_thickets.py`](neural_thickets.py). It was built for the molab Notebook
Competition and focuses on making the paper's central idea concrete: if useful
task experts are densely packed near pretrained weights, then random local
perturbations plus selection can become a plausible post-training strategy.

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
|-- main.py                     # Minimal project stub
|-- pyproject.toml              # Project metadata
`-- README.md
```

## Notes

- `neural_thickets.py` is the main entry point.
- `main.py` is only a minimal project stub and is not the notebook.
- The notebook imports local helpers from `simple_1D_signals_expts`, so run
  marimo from the repository root.
- The dependency list in `pyproject.toml` is intentionally minimal; the notebook
  dependencies live in the script header of `neural_thickets.py`.
