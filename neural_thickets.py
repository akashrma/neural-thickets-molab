# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "altair==6.0.0",
#     "anywidget>=0.10.0",
#     "marimo>=0.23.2",
#     "numpy>=2.4.4",
#     "pandas==3.0.2",
#     "plotly>=6.0.0",
#     "torch>=2.11.0",
# ]
# ///

import marimo

__generated_with = "0.23.2"
app = marimo.App(width="medium", css_file="", auto_download=["html"])


@app.cell(hide_code=True)
def _():
    import anywidget
    import copy
    import marimo as mo
    import random
    import math
    from dataclasses import dataclass, replace
    from types import SimpleNamespace

    import pandas as pd
    import altair as alt
    import html as html_lib

    import numpy as np
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import torch
    import traitlets

    from simple_1D_signals_expts import datasets as signal_datasets_module
    from simple_1D_signals_expts import models as signal_models_module

    return (
        SimpleNamespace,
        anywidget,
        copy,
        go,
        html_lib,
        mo,
        np,
        signal_datasets_module,
        signal_models_module,
        torch,
        traitlets,
    )


@app.cell(hide_code=True)
def _(mo):
    banner = """
    <style>
      .nt-paper-hero {
        color: #1f2937;
        margin: 0 0 24px;
        overflow: hidden;
        position: relative;
      }

      .nt-paper-hero__grid {
        align-items: stretch;
        display: grid;
        gap: 22px;
        grid-template-columns: minmax(0, 1.25fr) minmax(260px, 0.75fr);
        padding: 30px 28px;
        position: relative;
      }

      @media (max-width: 760px) {
        .nt-paper-hero__grid {
          grid-template-columns: 1fr;
          padding: 24px 18px;
        }

        .nt-paper-hero h1 {
          font-size: 1.9rem !important;
        }
      }
    </style>
    <div class="nt-paper-hero">
      <div class="nt-paper-hero__grid">
        <div>
          <div style="display:inline-flex;align-items:center;gap:8px;padding:6px 10px;border:1px solid #bae6fd;background:rgba(240,249,255,0.78);border-radius:999px;color:#0369a1;font-size:0.76rem;font-weight:800;letter-spacing:0;text-transform:uppercase;">
            Paper Explainer
          </div>
          <h1 style="margin:14px 0 10px;color:#111827;font-size:2.35rem;line-height:1.06;font-weight:850;letter-spacing:0;">
            Neural Thickets
          </h1>
          <p style="margin:0;max-width:650px;color:#374151;font-size:1.05rem;line-height:1.52;">
            What if pretraining does more than initialize a model? This notebook explores the
            paper's claim that many task-specialized experts can live densely near pretrained
            weights, making random local perturbations a plausible post-training strategy.
          </p>
          <div style="margin-top:18px;color:#475569;font-size:0.92rem;line-height:1.5;">
            <div>
              Submission for the
              <a href="https://marimo.io/pages/events/notebook-competition" style="color:#2563eb;text-decoration:none;font-weight:750;">molab Notebook Competition</a>
            </div>
            <div>
              Notebook by <b style="color:#111827;">Akash Sharma</b>
              · <a href="https://x.com/mathcrush247" style="color:#2563eb;text-decoration:none;font-weight:750;">X</a>
              · <a href="https://github.com/akashrma" style="color:#2563eb;text-decoration:none;font-weight:750;">GitHub</a>
            </div>
          </div>
        </div>
        <div style="display:flex;flex-direction:column;justify-content:space-between;gap:14px;border:1px solid rgba(148,163,184,0.35);background:rgba(255,255,255,0.62);border-radius:8px;padding:16px 16px 14px;box-shadow:0 12px 30px rgba(148,163,184,0.13);">
          <div>
            <div style="color:#64748b;font-size:0.72rem;font-weight:850;letter-spacing:0;text-transform:uppercase;margin-bottom:7px;">Original paper</div>
            <div style="font-size:1rem;line-height:1.35;font-weight:800;color:#111827;">Diverse Task Experts Are Dense Around Pretrained Weights</div>
            <div style="margin-top:7px;color:#475569;font-size:0.9rem;line-height:1.35;">Yulu Gan · Phillip Isola</div>
            <a href="https://www.alphaxiv.org/abs/2603.12228" style="display:inline-block;margin-top:8px;color:#2563eb;font-size:0.9rem;font-weight:750;text-decoration:none;">alphaxiv:2603.12228</a>
          </div>
          <svg viewBox="0 0 320 148" role="img" aria-label="Abstract thicket of nearby task experts around pretrained weights" style="width:100%;height:auto;display:block;">
            <defs>
              <radialGradient id="nt-thicket-glow" cx="50%" cy="50%" r="55%">
                <stop offset="0%" stop-color="#ffffff" stop-opacity="0.98"/>
                <stop offset="38%" stop-color="#bfdbfe" stop-opacity="0.82"/>
                <stop offset="68%" stop-color="#bbf7d0" stop-opacity="0.52"/>
                <stop offset="100%" stop-color="#fed7aa" stop-opacity="0"/>
              </radialGradient>
              <radialGradient id="nt-point-blue" cx="38%" cy="35%" r="68%">
                <stop offset="0%" stop-color="#ffffff" stop-opacity="0.95"/>
                <stop offset="100%" stop-color="#60a5fa" stop-opacity="0.96"/>
              </radialGradient>
              <radialGradient id="nt-point-green" cx="38%" cy="35%" r="68%">
                <stop offset="0%" stop-color="#ffffff" stop-opacity="0.95"/>
                <stop offset="100%" stop-color="#4ade80" stop-opacity="0.96"/>
              </radialGradient>
              <radialGradient id="nt-point-peach" cx="38%" cy="35%" r="68%">
                <stop offset="0%" stop-color="#ffffff" stop-opacity="0.95"/>
                <stop offset="100%" stop-color="#fb923c" stop-opacity="0.92"/>
              </radialGradient>
              <radialGradient id="nt-point-pink" cx="38%" cy="35%" r="68%">
                <stop offset="0%" stop-color="#ffffff" stop-opacity="0.95"/>
                <stop offset="100%" stop-color="#f472b6" stop-opacity="0.92"/>
              </radialGradient>
              <filter id="nt-soft-blur" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="0.5"/>
              </filter>
              <filter id="nt-star-shadow" x="-40%" y="-40%" width="180%" height="180%">
                <feDropShadow dx="0" dy="7" stdDeviation="6" flood-color="#64748b" flood-opacity="0.25"/>
              </filter>
            </defs>
            <rect x="0" y="0" width="320" height="148" rx="8" fill="#f8fafc"/>
            <circle cx="160" cy="74" r="82" fill="url(#nt-thicket-glow)"/>
            <g filter="url(#nt-soft-blur)">
              <circle cx="108" cy="45" r="12" fill="#93c5fd" opacity="0.24"/>
              <circle cx="219" cy="47" r="16" fill="#86efac" opacity="0.24"/>
              <circle cx="105" cy="105" r="15" fill="#fdba74" opacity="0.22"/>
              <circle cx="225" cy="103" r="13" fill="#f9a8d4" opacity="0.24"/>
            </g>
            <g stroke="#ffffff" stroke-width="1.4">
              <circle cx="120" cy="59" r="4.8" fill="url(#nt-point-blue)"/>
              <circle cx="139" cy="43" r="3.4" fill="url(#nt-point-green)" opacity="0.88"/>
              <circle cx="184" cy="46" r="4.6" fill="url(#nt-point-peach)"/>
              <circle cx="210" cy="64" r="3.7" fill="url(#nt-point-pink)" opacity="0.9"/>
              <circle cx="132" cy="93" r="4.4" fill="url(#nt-point-peach)"/>
              <circle cx="188" cy="99" r="4.2" fill="url(#nt-point-blue)" opacity="0.9"/>
              <circle cx="219" cy="91" r="3.2" fill="url(#nt-point-green)" opacity="0.84"/>
              <circle cx="100" cy="82" r="3.5" fill="url(#nt-point-pink)" opacity="0.82"/>
              <circle cx="151" cy="109" r="3.1" fill="url(#nt-point-green)" opacity="0.78"/>
              <circle cx="231" cy="44" r="2.8" fill="url(#nt-point-blue)" opacity="0.74"/>
              <circle cx="91" cy="52" r="2.7" fill="url(#nt-point-green)" opacity="0.72"/>
              <circle cx="244" cy="78" r="2.5" fill="url(#nt-point-peach)" opacity="0.7"/>
            </g>
            <path d="M160 63.5 L163 70.3 L170.4 71.1 L164.8 76.1 L166.4 83.4 L160 79.7 L153.6 83.4 L155.2 76.1 L149.6 71.1 L157 70.3 Z" fill="#111827" stroke="#ffffff" stroke-width="1.8" stroke-linejoin="round" filter="url(#nt-star-shadow)"/>
          </svg>
        </div>
      </div>
    </div>
    """
    mo.Html(banner)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Reader's note.** This notebook is best viewed in **app view** with the **vertical** layout setting, and it is meant to be read after running all cells once. It is CPU-friendly, should run directly from the molab link and default experimental settings are recommended $-$ however, settings have been configurable so the reader can experiment independently.

    If you want to tinker with it locally, especially with the imports for the 1D toy experiment, use the GitHub repo: [akashrma/neural-thickets-molab](https://github.com/akashrma/neural-thickets-molab).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **The Post-Training Bottleneck**

    The modern LLM pipeline is firmly established: massive self-supervised pretraining followed by alignment-focused post-training. While pretraining endows a model with general representations and reasoning priors, post-training is required to surface specialized behaviors—like instruction following, code generation, or complex mathematical reasoning.

    However, post-training is computationally brutal and notoriously brittle. Algorithms like RLHF, PPO, DPO, and GRPO require calculating gradients through massive networks, maintaining KL-divergence penalties, training auxiliary reward models, and navigating extreme hyperparameter sensitivity.

    If explicit post-training is this expensive and difficult, is there a simpler alternative?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Enter Neural Thickets**

    In this notebook, we explore an alternative by diving into the core ideas of [Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights](https://www.alphaxiv.org/abs/2603.12228) by Yulu Gan and Phillip Isola.

    The authors observe an interesting after-effect of scaling and pretraining: in the parameter space of large language models, high-performing, task-specific "expert" solutions reside densely in the immediate neighborhood of the pretrained base weights. Even better, as models scale up, the density of these solutions increases.

    This phenomenon unlocks an idea that sounds almost absurd at first: **_what if we just randomly perturb the pretrained weights and keep the ones that work?_** Because of this dense "thicket" of solutions, we can achieve state-of-the-art post-training alignment not through expensive gradient-based optimization, but through highly parallel random guessing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **What does this all mean and how is it useful?**

    The main goal of this notebook is to make the Neural Thickets idea feel concrete. The paper's proposal can sound strange on first contact: instead of carefully optimizing a model after pretraining, sample random nearby perturbations and keep the ones that work. Why should that ever be reasonable?

    We will build up to that answer in three layers:

    1. **Intuition for random guessing.** We start with a small grid game to show the difference between a sparse needle-in-a-haystack regime and a dense thicket regime.
    2. **Interactive extensions of the paper's 1D toy experiment.** We use the original RandOpt toy-model code and extend the visualizations so you can inspect solution density, perturbation diversity, complementary experts, and top-k ensembling directly.
    3. **A new exploratory direction: Controllable RandOpt.** This part is our notebook extension, not a result from the paper. We sketch how changing the sampling distribution could reduce the need for brute-force parallel perturbation evaluation when parallel compute is limited.

    In short: the paper gives the thicket hypothesis and RandOpt; this notebook tries to make the geometry, trade-offs, and possible next questions easier to see.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **A Game of Random Guessing**

    As we've established, traditional post-training methods like PPO or SFT can be a delicate, computationally expensive dance. This paper proposes bypassing this complexity by leaning entirely on the geometry of the pretrained model's local weight landscape. **_Instead of carefully steering the model with gradients, what if we just roll the dice?_**

    To intuitively grasp why this seemingly naïve approach might actually succeed, let's play a quick game.

    Imagine the center of the grid ⭐ below represents your base pretrained model. Each click on the board is a random tweak (perturbation) to those weights, and a hidden diamond 💎 represents a "task expert" $-$ a specific configuration that performs much better on your downstream task.

    - **1 Diamond**: If there is only one diamond hidden on the board, you are in the **needle-in-a-haystack regime**. Randomly clicking around is frustrating and highly unlikely to yield a good result.

    - **Multiple Diamonds**: As you increase the number of diamonds, you enter the **thicket regime**. Here, useful task experts are so densely packed around the starting point that you are almost guaranteed to stumble upon one with just a few guesses.

    <u>**Your goal is simple**</u>: adjust the number of diamonds to see the difference in density, and start clicking (or use Auto search) until you uncover an expert. Also note how scaling the grid makes the needle-in-a-haystack regime harder to win.
    """)
    return


@app.cell(hide_code=True)
def _(html_lib, mo):
    game_html = r"""
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <div id="nt-self-contained-game" class="nt-game">
      <style>
        body {
          margin: 0;
        }

        #nt-self-contained-game {
          --nt-cell-size: 24px;
          color: #24292f;
          font-family: var(--nt-parent-font-family, inherit);
        }

        #nt-self-contained-game * {
          box-sizing: border-box;
        }

        #nt-self-contained-game .nt-game-layout {
          align-items: flex-start;
          display: flex;
          flex-wrap: wrap;
          gap: 16px;
          width: 100%;
        }

        #nt-self-contained-game .nt-panel {
          background: #f8fafc;
          border: 1px solid #d0d7de;
          border-radius: 8px;
          box-shadow: 0 6px 18px rgba(15, 23, 42, 0.10);
          padding: 12px 14px;
        }

        #nt-self-contained-game .nt-left {
          flex: 1.2 1 430px;
          min-width: min(100%, 430px);
        }

        #nt-self-contained-game .nt-right {
          flex: 0.8 1 250px;
          min-width: min(100%, 250px);
        }

        #nt-self-contained-game h2,
        #nt-self-contained-game h3 {
          margin: 0 0 8px;
        }

        #nt-self-contained-game h2 {
          font-size: 1rem;
        }

        #nt-self-contained-game h3 {
          font-size: 0.9rem;
        }

        #nt-self-contained-game p {
          line-height: 1.5;
          margin: 0 0 10px;
        }

        #nt-self-contained-game .nt-left > p,
        #nt-self-contained-game .nt-right h3,
        #nt-self-contained-game .nt-right p {
          display: none;
        }

        #nt-self-contained-game .nt-controls {
          align-items: end;
          display: flex;
          flex-wrap: wrap;
          gap: 10px;
          margin-bottom: 12px;
        }

        #nt-self-contained-game .nt-control {
          flex: 1 1 160px;
          min-width: 160px;
        }

        #nt-self-contained-game label {
          color: #57606a;
          display: block;
          font-size: 0.82rem;
          font-weight: 600;
          margin-bottom: 7px;
        }

        #nt-self-contained-game input[type="range"] {
          accent-color: #0969da;
          width: 100%;
        }

        #nt-self-contained-game .nt-value {
          color: #24292f;
          font-variant-numeric: tabular-nums;
          font-weight: 600;
        }

        #nt-self-contained-game .nt-action-button {
          background: #f6f8fa;
          border-color: #ffffff #7b7b7b #7b7b7b #ffffff;
          border-style: solid;
          border-width: 2px;
          color: #24292f;
          cursor: pointer;
          font-weight: 600;
          min-height: 36px;
          padding: 6px 14px;
        }

        #nt-self-contained-game .nt-action-button:active {
          border-color: #7b7b7b #ffffff #ffffff #7b7b7b;
          padding: 7px 13px 5px 15px;
        }

        #nt-self-contained-game .nt-action-button:disabled {
          color: #6e7781;
          cursor: default;
        }

        #nt-self-contained-game .nt-auto-active {
          background: #fff8c5;
        }

        #nt-self-contained-game .nt-board-wrap {
          overflow-x: visible;
          padding-bottom: 4px;
        }

        #nt-self-contained-game .nt-mine-board {
          background: #bdbdbd;
          border-color: #7b7b7b #ffffff #ffffff #7b7b7b;
          border-style: solid;
          border-width: 3px;
          display: inline-block;
          padding: 6px;
        }

        #nt-self-contained-game .nt-mine-topbar {
          align-items: center;
          background: #bdbdbd;
          border-color: #7b7b7b #ffffff #ffffff #7b7b7b;
          border-style: solid;
          border-width: 3px;
          display: flex;
          justify-content: space-between;
          margin-bottom: 6px;
          padding: 4px;
        }

        #nt-self-contained-game .nt-counter {
          background: #111111;
          border-color: #7b7b7b #ffffff #ffffff #7b7b7b;
          border-style: solid;
          border-width: 2px;
          color: #f43f3f;
          font-size: 0.92rem;
          font-weight: 700;
          font-variant-numeric: tabular-nums;
          line-height: 1;
          min-width: 46px;
          padding: 4px 5px;
          text-align: right;
        }

        #nt-self-contained-game .nt-face {
          align-items: center;
          background: #c6c6c6;
          border-color: #ffffff #7b7b7b #7b7b7b #ffffff;
          border-style: solid;
          border-width: 2px;
          cursor: pointer;
          display: flex;
          font-size: 0.9rem;
          font-weight: 700;
          height: 30px;
          justify-content: center;
          line-height: 1;
          padding: 0;
          width: 30px;
        }

        #nt-self-contained-game .nt-face:active {
          border-color: #7b7b7b #ffffff #ffffff #7b7b7b;
        }

        #nt-self-contained-game .nt-grid {
          display: grid;
          gap: 0;
        }

        #nt-self-contained-game .nt-cell {
          align-items: center;
          background: #c6c6c6;
          border-color: #ffffff #7b7b7b #7b7b7b #ffffff;
          border-style: solid;
          border-width: 1px;
          color: #111111;
          cursor: pointer;
          display: flex;
          font-size: clamp(0.35rem, calc(var(--nt-cell-size) * 0.52), 0.9rem);
          font-weight: 700;
          height: var(--nt-cell-size);
          justify-content: center;
          line-height: 1;
          padding: 0;
          user-select: none;
          width: var(--nt-cell-size);
        }

        #nt-self-contained-game .nt-cell:hover {
          background: #d3d3d3;
        }

        #nt-self-contained-game .nt-cell:disabled {
          cursor: default;
        }

        #nt-self-contained-game .nt-cell.nt-revealed {
          background: #bdbdbd;
          border-color: #9a9a9a;
          border-width: 1px;
          color: #555555;
        }

        #nt-self-contained-game .nt-cell.nt-diamond {
          color: #111111;
        }

        #nt-self-contained-game .nt-cell.nt-origin {
          color: #111111;
          cursor: default;
        }

        #nt-self-contained-game .nt-status {
          align-items: center;
          background: #ffffff;
          border: 1px solid #d8dee4;
          border-radius: 6px;
          display: flex;
          font-weight: 600;
          gap: 8px;
          margin: 8px 0 10px;
          padding: 8px 10px;
        }

        #nt-self-contained-game .nt-info-grid {
          display: grid;
          gap: 8px;
          grid-template-columns: repeat(2, minmax(0, 1fr));
          margin: 8px 0 10px;
        }

        #nt-self-contained-game .nt-stat {
          background: #ffffff;
          border: 1px solid #d8dee4;
          border-radius: 6px;
          padding: 8px 10px;
        }

        #nt-self-contained-game .nt-stat-label {
          color: #57606a;
          display: block;
          font-size: 0.74rem;
          font-weight: 600;
          line-height: 1.2;
          margin-bottom: 4px;
          text-transform: uppercase;
        }

        #nt-self-contained-game .nt-stat-value {
          color: #24292f;
          display: block;
          font-size: 1.02rem;
          font-weight: 600;
          font-variant-numeric: tabular-nums;
          line-height: 1.25;
        }

        @media (max-width: 900px) {
          #nt-self-contained-game .nt-game-layout {
            gap: 12px;
          }

          #nt-self-contained-game {
            --nt-cell-size: 22px;
          }

          #nt-self-contained-game .nt-cell {
            height: var(--nt-cell-size);
            width: var(--nt-cell-size);
          }

          #nt-self-contained-game .nt-counter {
            font-size: 0.95rem;
            min-width: 44px;
          }

          #nt-self-contained-game .nt-info-grid {
            grid-template-columns: 1fr;
          }
        }
      </style>

      <div class="nt-game-layout">
        <section class="nt-panel nt-left">
          <h2>Grid controls</h2>
          <p>
            Start with <strong>1 diamond</strong> for the needle-in-a-haystack
            regime. Increase the number of diamonds to create a denser thicket.
          </p>
          <div class="nt-controls">
            <div class="nt-control">
              <label for="nt-grid-size">Grid size: <span class="nt-value" data-role="grid-value">9</span></label>
              <input id="nt-grid-size" data-role="grid-size" type="range" min="9" max="81" step="2" value="9">
            </div>
            <div class="nt-control">
              <label for="nt-diamond-count">Number of diamonds: <span class="nt-value" data-role="diamond-value">1</span></label>
              <input id="nt-diamond-count" data-role="diamond-count" type="range" min="1" max="200" step="1" value="1">
            </div>
            <button class="nt-action-button" type="button" data-role="new-game">New game</button>
            <button class="nt-action-button" type="button" data-role="auto-search">Auto search</button>
          </div>

          <h2>Grid game</h2>
          <div class="nt-board-wrap">
            <div class="nt-mine-board" data-role="board">
              <div class="nt-mine-topbar">
                <div class="nt-counter" data-role="mines-left">001</div>
                <button class="nt-face" type="button" data-role="face">:)</button>
                <div class="nt-counter" data-role="step-count">000</div>
              </div>
              <div class="nt-grid" data-role="grid"></div>
            </div>
          </div>
        </section>

        <section class="nt-panel nt-right">
          <h2>Probabilistic details</h2>
          <div class="nt-status">
            <span data-role="status-icon">?</span>
            <span data-role="status-text">Still searching.</span>
          </div>
          <div class="nt-info-grid" data-role="stats"></div>
          <h3>Interpretation</h3>
          <p>
            With <strong>one diamond</strong>, useful solutions are sparse: this
            is the <strong>needle-in-a-haystack</strong> regime.
          </p>
          <p>
            As the number of diamonds increases, the local neighborhood becomes
            denser with useful solutions: this is the <strong>thicket</strong> regime.
          </p>
        </section>
      </div>

      <script>
        (() => {
          const root = document.currentScript.closest("#nt-self-contained-game");
          if (!root) {
            return;
          }

          try {
            const parentFontFamily = window.parent.getComputedStyle(
              window.parent.document.body
            ).fontFamily;
            if (parentFontFamily) {
              root.style.setProperty("--nt-parent-font-family", parentFontFamily);
            }
          } catch {
            root.style.setProperty("--nt-parent-font-family", "inherit");
          }

          const els = {
            gridSize: root.querySelector("[data-role='grid-size']"),
            gridValue: root.querySelector("[data-role='grid-value']"),
            diamondCount: root.querySelector("[data-role='diamond-count']"),
            diamondValue: root.querySelector("[data-role='diamond-value']"),
            newGame: root.querySelector("[data-role='new-game']"),
            autoSearch: root.querySelector("[data-role='auto-search']"),
            face: root.querySelector("[data-role='face']"),
            grid: root.querySelector("[data-role='grid']"),
            minesLeft: root.querySelector("[data-role='mines-left']"),
            stepCount: root.querySelector("[data-role='step-count']"),
            statusIcon: root.querySelector("[data-role='status-icon']"),
            statusText: root.querySelector("[data-role='status-text']"),
            stats: root.querySelector("[data-role='stats']"),
          };

          let game = null;
          let autoTimer = null;

          function centerCell(size) {
            return Math.floor(size / 2);
          }

          function cellKey(row, col) {
            return `${row},${col}`;
          }

          function clampDiamondCount(size, count) {
            return Math.max(1, Math.min(count, size * size - 1));
          }

          function formatCounter(value) {
            return String(Math.max(0, value)).padStart(3, "0").slice(-3);
          }

          function formatPercent(value) {
            return `${(value * 100).toFixed(4)}%`;
          }

          function setCompactCellSize(size) {
            const cellSize = Math.max(4, Math.min(24, Math.floor(330 / size)));
            root.style.setProperty("--nt-cell-size", `${cellSize}px`);
          }

          function combinationsRatio(total, diamonds, guesses) {
            if (guesses <= 0) {
              return 0;
            }
            if (guesses > total - diamonds) {
              return 1;
            }

            let miss = 1;
            for (let i = 0; i < guesses; i += 1) {
              miss *= (total - diamonds - i) / (total - i);
            }
            return 1 - miss;
          }

          function isAutoRunning() {
            return autoTimer !== null;
          }

          function updateAutoButton() {
            els.autoSearch.textContent = isAutoRunning() ? "Stop auto" : "Auto search";
            els.autoSearch.classList.toggle("nt-auto-active", isAutoRunning());
            els.autoSearch.disabled = Boolean(game && game.won);
          }

          function stopAuto() {
            if (autoTimer !== null) {
              window.clearInterval(autoTimer);
              autoTimer = null;
            }
            updateAutoButton();
          }

          function hiddenClickableCells() {
            const center = centerCell(game.size);
            const cells = [];

            for (let row = 0; row < game.size; row += 1) {
              for (let col = 0; col < game.size; col += 1) {
                const key = cellKey(row, col);
                if ((row !== center || col !== center) && !game.revealed.has(key)) {
                  cells.push([row, col]);
                }
              }
            }

            return cells;
          }

          function autoStep() {
            if (!game || game.won) {
              stopAuto();
              return;
            }

            const cells = hiddenClickableCells();
            if (cells.length === 0) {
              stopAuto();
              return;
            }

            const [row, col] = cells[Math.floor(Math.random() * cells.length)];
            reveal(row, col);
          }

          function startAuto() {
            if (!game || game.won || isAutoRunning()) {
              return;
            }

            autoTimer = window.setInterval(autoStep, 90);
            autoStep();
            updateAutoButton();
          }

          function toggleAuto() {
            if (isAutoRunning()) {
              stopAuto();
            } else {
              startAuto();
            }
          }

          function makeGame() {
            stopAuto();

            const size = Number(els.gridSize.value);
            const requestedDiamonds = Number(els.diamondCount.value);
            const diamonds = clampDiamondCount(size, requestedDiamonds);
            const center = centerCell(size);
            const candidates = [];

            setCompactCellSize(size);
            els.diamondCount.max = String(size * size - 1);
            els.diamondCount.value = String(diamonds);
            els.gridValue.textContent = String(size);
            els.diamondValue.textContent = String(diamonds);

            for (let row = 0; row < size; row += 1) {
              for (let col = 0; col < size; col += 1) {
                if (row !== center || col !== center) {
                  candidates.push(cellKey(row, col));
                }
              }
            }

            const diamondSet = new Set();
            while (diamondSet.size < diamonds) {
              const index = Math.floor(Math.random() * candidates.length);
              diamondSet.add(candidates[index]);
            }

            game = {
              size,
              diamonds,
              diamondSet,
              revealed: new Set(),
              steps: 0,
              won: false,
            };

            render();
          }

          function reveal(row, col) {
            if (!game || game.won) {
              return;
            }

            const center = centerCell(game.size);
            const key = cellKey(row, col);
            if ((row === center && col === center) || game.revealed.has(key)) {
              return;
            }

            game.revealed.add(key);
            game.steps += 1;
            game.won = game.diamondSet.has(key);
            if (game.won) {
              stopAuto();
            }
            render();
          }

          function renderGrid() {
            const center = centerCell(game.size);
            els.grid.innerHTML = "";
            els.grid.style.gridTemplateColumns = `repeat(${game.size}, var(--nt-cell-size))`;

            for (let row = 0; row < game.size; row += 1) {
              for (let col = 0; col < game.size; col += 1) {
                const button = document.createElement("button");
                const key = cellKey(row, col);
                button.className = "nt-cell";
                button.type = "button";
                button.setAttribute("aria-label", `Reveal row ${row + 1}, column ${col + 1}`);

                const shouldReveal = game.won || game.revealed.has(key);

                if (row === center && col === center) {
                  button.classList.add("nt-origin");
                  button.disabled = true;
                  button.textContent = "⭐";
                  button.title = "pretrained weights";
                } else if (shouldReveal) {
                  button.classList.add("nt-revealed");
                  button.disabled = true;
                  if (game.diamondSet.has(key)) {
                    button.classList.add("nt-diamond");
                    button.textContent = "💎";
                    button.title = "task expert";
                  } else {
                    button.title = "empty cell";
                  }
                } else {
                  button.title = "covered cell";
                  button.addEventListener("click", () => reveal(row, col));
                }

                els.grid.appendChild(button);
              }
            }
          }

          function renderStats() {
            const total = game.size * game.size - 1;
            const revealedDiamonds = [...game.revealed].filter((key) => game.diamondSet.has(key)).length;
            const remainingHidden = total - game.revealed.size;
            const remainingDiamonds = game.diamonds - revealedDiamonds;
            const initialSuccess = game.diamonds / total;
            const nextSuccess = remainingHidden === 0 || game.won
              ? 0
              : remainingDiamonds / remainingHidden;
            const cumulative = combinationsRatio(total, game.diamonds, Math.min(game.steps, total));
            const expected = (total + 1) / (game.diamonds + 1);

            const stats = [
              ["Guesses made", String(game.steps)],
              ["Clickable cells", String(total)],
              ["Diamonds in grid", String(game.diamonds)],
              ["Initial success", formatPercent(initialSuccess)],
              ["Next-click success", formatPercent(nextSuccess)],
              ["Won by now", formatPercent(cumulative)],
              ["Expected guesses", expected.toFixed(2)],
            ];

            els.stats.innerHTML = stats.map(([label, value]) => `
              <div class="nt-stat">
                <span class="nt-stat-label">${label}</span>
                <span class="nt-stat-value">${value}</span>
              </div>
            `).join("");
          }

          function render() {
            if (!game) {
              return;
            }

            const revealedDiamonds = [...game.revealed].filter((key) => game.diamondSet.has(key)).length;
            els.minesLeft.textContent = formatCounter(
              game.won ? 0 : game.diamonds - revealedDiamonds
            );
            els.stepCount.textContent = formatCounter(game.steps);
            els.face.textContent = game.won ? "B)" : ":)";
            els.statusIcon.textContent = game.won ? "💎" : "?";
            els.statusText.textContent = game.won
              ? "You found a task expert."
              : "Still searching.";

            renderGrid();
            renderStats();
            updateAutoButton();
          }

          els.gridSize.addEventListener("input", makeGame);
          els.diamondCount.addEventListener("input", makeGame);
          els.newGame.addEventListener("click", makeGame);
          els.autoSearch.addEventListener("click", toggleAuto);
          els.face.addEventListener("click", makeGame);
          makeGame();
        })();
      </script>
    </div>
    </body>
    </html>
    """

    mo.Html(
        f"""
        <iframe
          title="Minesweeper grid game"
          srcdoc="{html_lib.escape(game_html, quote=True)}"
          style="border: 0; display: block; height: 520px; width: 100%;"
        ></iframe>
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **From Grids to the Loss Landscape: The Scaling Law**

    With one diamond, random guessing is painfully inefficient: useful solutions are sparse, like a needle in a haystack.

    As you increase the number of diamonds, finding one becomes much easier. This represents the paper's density scaling claim: as models scale up and undergo massive pretraining, the nearby parameter space can contain many task-specialized solutions.

    We do not know the exact solution locations, but the thicket hypothesis says many good solutions are nearby. Why does this matter? The answer comes down to **computational time**. Let's map our 2D grid game onto an actual 3D **Loss Landscape** (where lower elevation means fewer errors):

    - **The Starting Point (Black Diamond):** The pretrained base model weights ($\theta$). It sits on a high plateau, meaning its performance on our specific downstream task isn't great yet.
    - **The Pockets:** The deep holes surrounding the center. These are the "Diamonds" from our game—local minima that act as "experts" for our specific task.
    - **A Random Guess:** Adding one random Gaussian perturbation to the pretrained weights ($\theta + \epsilon$), constrained by the search window.

    In sparse _needle-in-a-haystack_ regimes, random guessing is usually impractical, so we rely on sequential optimization methods such as SGD or post-training algorithms. In dense thicket regimes, parallel random perturbations can become competitive because many nearby directions already contain useful experts.

    Interact with the landscape below to see how optimization changes when we enter the thicket regime:

    1.  **Run SGD (Sequential):** Stochastic Gradient Descent calculates the slope and takes a step downward. Use the slider to watch it navigate. It successfully finds an expert, but it requires **$T$ sequential forward and backward passes** to get there.
    2.  **Run Random Perturbation Search (Parallel):** If we know the landscape around $\theta$ is a densely packed thicket, we don't need to walk step-by-step. We can sample 50 Gaussian perturbations inside the dashed search window and evaluate them simultaneously. This can hit a minimum in exactly **1 step** ($\mathcal{O}(1)$ time).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    active_mode, set_active_mode = mo.state("start")
    perturbation_run, set_perturbation_run = mo.state(0)
    return active_mode, perturbation_run, set_active_mode, set_perturbation_run


@app.cell(hide_code=True)
def _(mo):
    sgd_frame = mo.ui.slider(
        start=0,
        stop=32,
        step=1,
        value=0,
        show_value=True,
        label="SGD frame",
        full_width=True,
    )
    return (sgd_frame,)


@app.cell(hide_code=True)
def _(mo, set_active_mode, set_perturbation_run):
    def run_perturbation_click(_):
        set_perturbation_run(lambda run: run + 1)
        set_active_mode("perturbation")

    run_sgd = mo.ui.button(
        label="Run SGD",
        kind="neutral",
        on_click=lambda _: set_active_mode("sgd"),
    )
    run_perturbation_search = mo.ui.button(
        label="Run Random Perturbation Search",
        kind="neutral",
        on_click=run_perturbation_click,
    )
    reset = mo.ui.button(
        label="Reset",
        kind="neutral",
        on_click=lambda _: set_active_mode("start"),
    )
    return reset, run_perturbation_search, run_sgd


@app.cell(hide_code=True)
def _(active_mode, mo, reset, run_perturbation_search, run_sgd, sgd_frame):
    controls = [run_sgd, run_perturbation_search, reset]
    if active_mode() == "sgd":
        controls.append(sgd_frame)

    time_to_minima_controls = mo.hstack(
        controls,
        justify="start",
        align="center",
        wrap=True,
        gap=1.0,
    )
    return (time_to_minima_controls,)


@app.cell(hide_code=True)
def _(
    active_mode,
    go,
    mo,
    np,
    perturbation_run,
    sgd_frame,
    time_to_minima_controls,
):
    pocket_centers = np.array(
        [
            [0.78, -0.52],
            [-0.76, 0.46],
            [0.38, 0.86],
            [-0.28, -0.88],
            [1.08, 0.18],
            [-1.08, -0.18],
        ]
    )
    pocket_depths = np.array([0.72, 0.64, 0.60, 0.62, 0.50, 0.48])
    pocket_widths = np.array([0.24, 0.25, 0.22, 0.23, 0.27, 0.26])
    pretrained_width = 0.65
    pretrained_height = 0.04
    global_curvature = 0.10
    sample_sigma = 0.68
    search_radius = 1.30
    hit_radius = 0.52
    pocket_tail = pocket_depths * np.exp(
        -np.sum(pocket_centers**2, axis=1) / (2 * pocket_widths**2)
    ) / (pocket_widths**2)
    landscape_tilt_x, landscape_tilt_y = 0.5 * np.sum(
        pocket_tail[:, None] * pocket_centers,
        axis=0,
    )

    def loss_surface(x, y):
        z = 1.0 + global_curvature * (x**2 + y**2)
        z += pretrained_height * np.exp(-(x**2 + y**2) / (2 * pretrained_width**2))
        z += landscape_tilt_x * x + landscape_tilt_y * y
        for (cx, cy), depth, width in zip(
            pocket_centers,
            pocket_depths,
            pocket_widths,
            strict=True,
        ):
            dist2 = (x - cx) ** 2 + (y - cy) ** 2
            z -= depth * np.exp(-dist2 / (2 * width**2))
        return z

    def loss_gradient(x, y):
        grad = np.array(
            [
                2 * global_curvature * x + landscape_tilt_x,
                2 * global_curvature * y + landscape_tilt_y,
            ],
            dtype=float,
        )
        pretrained_exp = np.exp(-(x**2 + y**2) / (2 * pretrained_width**2))
        grad -= pretrained_height * pretrained_exp * np.array([x, y]) / (
            pretrained_width**2
        )
        for (cx, cy), depth, width in zip(
            pocket_centers,
            pocket_depths,
            pocket_widths,
            strict=True,
        ):
            pocket_exp = np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * width**2))
            grad += depth * pocket_exp * np.array([x - cx, y - cy]) / (width**2)
        return grad

    grid = np.linspace(-2.2, 2.2, 96)
    x_grid, y_grid = np.meshgrid(grid, grid)
    z_grid = loss_surface(x_grid, y_grid)
    z_start = float(loss_surface(0.0, 0.0))
    search_theta = np.linspace(0.0, 2 * np.pi, 160)
    search_x = search_radius * np.cos(search_theta)
    search_y = search_radius * np.sin(search_theta)
    search_z = loss_surface(search_x, search_y) + 0.035
    landscape_colorscale = [
        [0.0, "#153b2f"],
        [0.30, "#2d9c6a"],
        [0.55, "#d8c06d"],
        [0.78, "#c87a52"],
        [1.0, "#5b3f36"],
    ]

    surface = go.Surface(
        x=x_grid,
        y=y_grid,
        z=z_grid,
        colorscale=landscape_colorscale,
        colorbar={"title": "Loss"},
        contours={
            "z": {
                "show": True,
                "usecolormap": True,
                "highlightcolor": "#ffffff",
                "project_z": True,
            }
        },
        hovertemplate="x=%{x:.2f}<br>y=%{y:.2f}<br>L=%{z:.3f}<extra></extra>",
        opacity=0.92,
        showscale=True,
    )
    contour = go.Contour(
        x=grid,
        y=grid,
        z=z_grid,
        colorscale=landscape_colorscale,
        contours={
            "coloring": "heatmap",
            "showlabels": False,
            "start": float(z_grid.min()),
            "end": float(z_grid.max()),
            "size": 0.18,
        },
        line={"color": "rgba(255,255,255,0.32)", "width": 1},
        hovertemplate="x=%{x:.2f}<br>y=%{y:.2f}<br>L=%{z:.3f}<extra></extra>",
        name="Loss surface",
        showscale=False,
    )

    traces_3d = [surface]
    traces_2d = [contour]
    mode = active_mode()
    title = "Time Steps: 0"

    search_window_3d = go.Scatter3d(
        x=search_x,
        y=search_y,
        z=search_z,
        mode="lines",
        line={"color": "#111827", "width": 4, "dash": "dash"},
        name="Gaussian search window",
        hoverinfo="skip",
        showlegend=True,
    )
    search_window_2d = go.Scatter(
        x=search_x,
        y=search_y,
        mode="lines",
        line={"color": "#111827", "width": 2, "dash": "dash"},
        name="Gaussian search window",
        hoverinfo="skip",
        showlegend=False,
    )

    pretrained_trace_3d = go.Scatter3d(
        x=[0.0],
        y=[0.0],
        z=[z_start],
        mode="markers+text",
        marker={
            "size": 11,
            "color": "#111827",
            "symbol": "diamond",
            "line": {"color": "#1f2937", "width": 3},
        },
        text=["pretrained weights"],
        textposition="top center",
        name="Pretrained weights",
        hovertemplate=(
            "pretrained weights<br>"
            "x=0.00<br>y=0.00<br>L=%{z:.3f}<extra></extra>"
        ),
    )
    pretrained_trace_2d = go.Scatter(
        x=[0.0],
        y=[0.0],
        mode="markers+text",
        marker={
            "size": 15,
            "color": "#111827",
            "symbol": "diamond",
            "line": {"color": "#ffffff", "width": 2},
        },
        text=["pretrained weights"],
        textposition="top center",
        name="Pretrained weights",
        hovertemplate=(
            "pretrained weights<br>"
            "x=0.00<br>y=0.00<br>L=%{customdata:.3f}<extra></extra>"
        ),
        customdata=[z_start],
    )

    if mode == "sgd":
        frame = int(sgd_frame.value)
        steps = 32
        rng = np.random.default_rng(0)
        position = np.array([0.0, 0.0])
        sgd_points = np.zeros((steps + 1, 2))

        for step in range(1, steps + 1):
            gradient = loss_gradient(position[0], position[1])
            noise_scale = 0.85 * np.exp(-step / 9.0)
            stochastic_gradient = gradient + rng.normal(0.0, noise_scale, size=2)
            update = -0.18 * stochastic_gradient
            update_norm = np.linalg.norm(update)
            if update_norm > 0.09:
                update *= 0.09 / update_norm

            position = position + update
            position_norm = np.linalg.norm(position)
            if position_norm > search_radius:
                position *= search_radius / position_norm
            sgd_points[step] = position

        sgd_x = sgd_points[:, 0]
        sgd_y = sgd_points[:, 1]
        sgd_z = loss_surface(sgd_x, sgd_y)
        current = max(1, min(frame + 1, steps + 1))

        traces_3d.append(
            go.Scatter3d(
                x=sgd_x[:current],
                y=sgd_y[:current],
                z=sgd_z[:current],
                mode="lines+markers",
                line={"color": "#2563eb", "width": 8},
                marker={"size": 5, "color": "#2563eb"},
                name="SGD path",
                hovertemplate=(
                    "SGD step %{customdata}<br>"
                    "x=%{x:.2f}<br>y=%{y:.2f}<br>L=%{z:.3f}<extra></extra>"
                ),
                customdata=np.arange(current),
            )
        )
        traces_3d.append(
            go.Scatter3d(
                x=[float(sgd_x[current - 1])],
                y=[float(sgd_y[current - 1])],
                z=[float(sgd_z[current - 1])],
                mode="markers",
                marker={
                    "size": 9,
                    "color": "#1d4ed8",
                    "line": {"color": "#ffffff", "width": 2},
                },
                name="Current SGD step",
                hovertemplate="current step<br>L=%{z:.3f}<extra></extra>",
            )
        )
        traces_2d.append(
            go.Scatter(
                x=sgd_x[:current],
                y=sgd_y[:current],
                mode="lines+markers",
                line={"color": "#2563eb", "width": 4},
                marker={"size": 7, "color": "#2563eb"},
                name="SGD path",
                customdata=list(zip(np.arange(current), sgd_z[:current], strict=True)),
                hovertemplate=(
                    "SGD step %{customdata[0]}<br>"
                    "x=%{x:.2f}<br>y=%{y:.2f}<br>L=%{customdata[1]:.3f}<extra></extra>"
                ),
            )
        )
        traces_2d.append(
            go.Scatter(
                x=[float(sgd_x[current - 1])],
                y=[float(sgd_y[current - 1])],
                mode="markers",
                marker={
                    "size": 13,
                    "color": "#1d4ed8",
                    "line": {"color": "#ffffff", "width": 2},
                },
                name="Current SGD step",
                customdata=[float(sgd_z[current - 1])],
                hovertemplate="current step<br>L=%{customdata:.3f}<extra></extra>",
            )
        )
        title = f"SGD requires T sequential passes. Time Steps: {frame}"
    elif mode == "perturbation":
        rng = np.random.default_rng(perturbation_run())
        rand_points = []
        while len(rand_points) < 50:
            candidate = rng.normal(0.0, sample_sigma, size=2)
            if np.linalg.norm(candidate) <= search_radius:
                rand_points.append(candidate)
        rand_points = np.array(rand_points)
        rand_x = rand_points[:, 0]
        rand_y = rand_points[:, 1]
        rand_z = loss_surface(rand_x, rand_y)
        distances = np.sqrt(
            (rand_x[:, None] - pocket_centers[:, 0]) ** 2
            + (rand_y[:, None] - pocket_centers[:, 1]) ** 2
        )
        hits = distances.min(axis=1) < hit_radius
        point_colors = np.where(hits, "#16a34a", "#71717a")

        traces_3d.append(
            go.Scatter3d(
                x=rand_x,
                y=rand_y,
                z=rand_z,
                mode="markers",
                marker={
                    "size": np.where(hits, 8, 5),
                    "color": point_colors,
                    "line": {"color": "#ffffff", "width": 1},
                    "opacity": 0.92,
                },
                name="Parallel random samples",
                customdata=np.where(hits, "hit", "miss"),
                hovertemplate=(
                    "%{customdata}<br>"
                    "x=%{x:.2f}<br>y=%{y:.2f}<br>L=%{z:.3f}<extra></extra>"
                ),
            )
        )
        traces_2d.append(
            go.Scatter(
                x=rand_x,
                y=rand_y,
                mode="markers",
                marker={
                    "size": np.where(hits, 11, 8),
                    "color": point_colors,
                    "line": {"color": "#ffffff", "width": 1},
                    "opacity": 0.92,
                },
                name="Parallel random samples",
                customdata=list(zip(np.where(hits, "hit", "miss"), rand_z, strict=True)),
                hovertemplate=(
                    "%{customdata[0]}<br>"
                    "x=%{x:.2f}<br>y=%{y:.2f}<br>L=%{customdata[1]:.3f}<extra></extra>"
                ),
            )
        )
        title = "Random perturbation search finds minima instantly. Time Steps: 1"

    traces_3d.extend([search_window_3d, pretrained_trace_3d])
    traces_2d.extend([search_window_2d, pretrained_trace_2d])

    fig_3d = go.Figure(data=traces_3d)
    fig_3d.update_layout(
        height=500,
        margin={"l": 0, "r": 0, "t": 12, "b": 0},
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        showlegend=True,
        uirevision="time-to-minima-landscape-race",
        scene={
            "xaxis": {"title": "weight direction x", "range": [-2.2, 2.2]},
            "yaxis": {"title": "weight direction y", "range": [-2.2, 2.2]},
            "zaxis": {"title": "loss", "range": [float(z_grid.min()) - 0.2, 2.6]},
            "aspectratio": {"x": 1, "y": 1, "z": 0.58},
            "camera": {
                "eye": {"x": 1.55, "y": -1.65, "z": 1.05},
                "center": {"x": 0.0, "y": 0.0, "z": -0.08},
                "up": {"x": 0.0, "y": 0.0, "z": 1.0},
            },
        },
        legend={
            "x": 0.02,
            "y": 0.98,
            "bgcolor": "rgba(255,255,255,0.72)",
            "bordercolor": "rgba(39,39,42,0.18)",
            "borderwidth": 1,
        },
    )
    fig_2d = go.Figure(data=traces_2d)
    fig_2d.update_layout(
        height=500,
        margin={"l": 0, "r": 0, "t": 12, "b": 0},
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        showlegend=False,
        uirevision="time-to-minima-landscape-race-2d",
        xaxis={
            "title": "weight direction x",
            "range": [-2.2, 2.2],
            "scaleanchor": "y",
            "scaleratio": 1,
            "constrain": "domain",
        },
        yaxis={
            "title": "weight direction y",
            "range": [-2.2, 2.2],
            "constrain": "domain",
        },
    )
    landscape_views = mo.hstack(
        [fig_3d, fig_2d],
        justify="start",
        align="stretch",
        gap=0.8,
        widths=[0.58, 0.42],
    )

    time_to_minima_race = mo.vstack(
        [
            time_to_minima_controls,
            mo.md(f"**{title}**"),
            landscape_views,
        ],
        gap=0.8,
    )
    time_to_minima_race
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **The Math of the Thicket: Solution Density**
    The authors formalize this high hit-rate using a metric called **Solution Density**, denoted as $\delta(m)$:

    $$\delta(m) = P_{\epsilon \sim \mathcal{N}(0, \sigma^2 I)} [s(\theta + \epsilon) \geq s(\theta) + m]$$

    If we were to verbalize what this equation means, it would go like this $-$ *What is the probability that a Gaussian perturbation ($\epsilon$), sampled from a chosen search window around the pretrained weights ($\theta$), lands on a solution that is significantly better ($m$) than where we started?*

    As models scale to billions of parameters, pretraining reshapes the local neighborhood: the relevant search is no longer the entire weight space, and $\delta(m)$ can increase dramatically inside the Gaussian window. The thicket makes parallel random perturbation a mathematically sound and highly efficient post-training strategy.

    The "neighborhood" part is important! We are not guessing anywhere in the full weight space; we sample Gaussian perturbations around the pretrained weights, usually written as $\theta + \epsilon$ where $\epsilon \sim \mathcal{N}(0, \sigma^2 I)$.

    **Pretraining matters twice**:

    1) it places us in a smaller local search window, and <br>
    2) it makes useful solutions denser inside that window.

    Without pretraining, the same random search would still face a vast, sparse space.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Is Random Guessing Enough?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If solution density is high, random perturbation search gives us an incredibly cheap way to find experts. But there is a catch: **are these random experts actually good at everything?**

    A high solution density simply means we can easily find a set of weights that improves the loss on a specific task. However, these random jumps often create narrow specialists. A perturbation that creates a brilliant "Math Expert" might simultaneously destroy the model's ability to write coherent code.

    The paper frames this disagreement as **Solution Diversity** or **Spectral Discordance**. Dense nearby experts are not just redundant copies of the same generalist behavior; they specialize in orthogonal, conflicting features.

    To quantify this, the authors introduce the **Spectral Discordance** metric ($\mathcal{D}$). Given the percentile-rank matrix of $N$ random perturbations across $M$ different tasks, let $\mathbf{C} \in \mathbb{R}^{M \times M}$ be the Pearson correlation matrix between those tasks:

    $$ \mathcal{D} = 1 - \frac{1}{M(M-1)} \sum_{j \neq k} \mathbf{C}_{j,k} $$

    A value of $\mathcal{D} \to 1$ implies orthogonal rankings (highly diverse specialists), while $\mathcal{D} \to 0$ implies parallel rankings (redundant generalists). As models scale, $\mathcal{D}$ increases—meaning random perturbations produce increasingly disjoint, specialized capabilities.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **A Hands-on 1D Neural Thicket Lab: Understanding Solution Diversity**

    To visualize this spectral discordance without the overwhelming dimensionality of an LLM, let's use a 1D autoregressive setup. The paper also studies this toy setting, and the training/model/dataset code used here originates from the authors' RandOpt repository: [`simple_1D_signals_expts`](https://github.com/sunrainyg/RandOpt/tree/main/simple_1D_signals_expts). This setting is supposed to mirror the practical autoregressive LLMs where pretraining is done on wide variety of data (here this will be mixed signals) and post-trained and tested for specific tasks like reasoning, math, writing, chemistry etc.

    This molab notebook imports from the local `simple_1D_signals_expts` package, then extends the paper's 1D toy-model visualizations to make the local thicket geometry more interactive and easier to inspect. We will train a small Multilayer Perceptron (MLP) to predict the next value in a sequence, and then perturb it.

    For a signal sequence $x$, the model $f_\theta$ looks at a context window of past values ($c$) to predict the next value. We evaluate candidate perturbations using the **Autoregressive Mean Squared Error (MSE)** objective:

    $$ \mathcal{L}_{AR}(\theta) = \frac{1}{T} \sum_{t=1}^{T} \left( f_\theta(x_{t-c \ : \ t-1}) - x_t \right)^2 $$

    By generating random weight perturbations and scoring them against this objective across different signal shapes, we can observe diversity in real time:
    - A random perturbation might perfectly learn the slow, smooth trend of a wave (a low-frequency expert).
    - Another might perfectly capture the sharp, jagged spikes (a high-frequency expert).
    - But a single random guess rarely captures both, proving that these thickets consist of diverse, narrow specialists!

    The interactive lab below follows the same underlying 1D RandOpt setup, but splits it into the actual controls and views used in this notebook:

    - **Step 1: **choose a pretraining dataset and model configuration, then pretrain or initialize the base MLP,
    - **Step 2: **inspect a 2D local loss slice around the pretrained weights for any selected test set,
    - **Step 3: **sample random local perturbations, select a perturbation and compare its behavior across all signal categories,
    - **Step 4: **automatically find two complementary experts with different strengths,

    The base model is always the center of the local weight-space views. Changing the test set changes the loss surface being measured, not the origin of the search.
    """)
    return


@app.cell(hide_code=True)
def _(mo, signal_datasets_module):
    signal_dataset_names = sorted(signal_datasets_module.DATASET_GENERATORS.keys())
    dataset_options = {dataset_option_name: dataset_option_name for dataset_option_name in signal_dataset_names}
    pretrain_options = {"No pretraining": None, **dataset_options}

    ar_pretrain_dataset = mo.ui.dropdown(
        pretrain_options,
        value="mixed",
        searchable=True,
        label="Pretrain dataset",
        full_width=True,
    )
    ar_base_init = mo.ui.dropdown(
        ["xavier", "kaiming", "ortho"],
        value="xavier",
        label="Base initialization",
    )
    ar_ctx_sz = mo.ui.number(start=2, stop=80, step=1, value=10, label="Context size")
    ar_fut_sz = mo.ui.number(start=5, stop=120, step=5, value=60, label="Future horizon")
    ar_width = mo.ui.number(start=16, stop=256, step=16, value=128, label="Hidden width")
    ar_depth = mo.ui.number(start=2, stop=8, step=1, value=5, label="Depth")
    ar_pretrain_bsz = mo.ui.number(start=16, stop=512, step=16, value=128, label="Pretrain batch")
    ar_pretrain_iters = mo.ui.number(start=0, stop=1000, step=50, value=300, label="Pretrain iterations")
    ar_eval_bsz = mo.ui.number(start=4, stop=128, step=4, value=16, label="Eval batch")
    ar_sigma = mo.ui.number(start=0.0005, stop=0.02, step=0.0005, value=0.002, label="Sigma")
    ar_num_perturbations = mo.ui.number(start=20, stop=500, step=20, value=200, label="Perturbations (N)")
    return (
        ar_base_init,
        ar_ctx_sz,
        ar_depth,
        ar_eval_bsz,
        ar_fut_sz,
        ar_num_perturbations,
        ar_pretrain_bsz,
        ar_pretrain_dataset,
        ar_pretrain_iters,
        ar_sigma,
        ar_width,
        signal_dataset_names,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **Step 1: Choose training specifics**
    """)
    return


@app.cell(hide_code=True)
def _(
    ar_base_init,
    ar_ctx_sz,
    ar_current_base_cfg,
    ar_depth,
    ar_eval_bsz,
    ar_fut_sz,
    ar_num_perturbations,
    ar_pretrain_bsz,
    ar_pretrain_dataset,
    ar_pretrain_iters,
    ar_sigma,
    ar_width,
    mo,
    set_selected_ar_base_cfg,
):
    select_pretraining_config = mo.ui.button(
        label="Select pretraining configuration",
        kind="success",
        on_click=lambda _: set_selected_ar_base_cfg(ar_current_base_cfg),
    )
    training_controls = [
        ar_pretrain_dataset,
        ar_base_init,
        ar_ctx_sz,
        ar_fut_sz,
        ar_width,
        ar_depth,
        ar_pretrain_bsz,
        ar_pretrain_iters,
        ar_eval_bsz,
        ar_sigma,
        ar_num_perturbations,
        select_pretraining_config,
    ]

    mo.vstack(
        [
            mo.md("""
            These controls mirror the config cell in `1d_signals_randopt.py`: choose a pretraining dataset, model size, sequence length, and random perturbation scale. Click **Select pretraining configuration** to commit this setup before training.
            """),
            mo.hstack(
                training_controls,
                justify="start",
                align="center",
                wrap=True,
                gap=1.0,
            ),
        ],
        gap=0.6,
    )
    return


@app.cell(hide_code=True)
def _(ar_base_cfg, mo):
    ar_pretrain_button = mo.ui.run_button(label="Start pretraining", kind="success")
    if ar_base_cfg is None:
        ar_pretrain_action_view = mo.md("Select a pretraining configuration in Step 1.").callout(kind="info")
    else:
        pretraining_needed = ar_base_cfg.pretrain_dataset is not None and ar_base_cfg.pretrain_iters > 0
        action_pretrain_label = ar_base_cfg.pretrain_dataset if ar_base_cfg.pretrain_dataset is not None else "None"
        if pretraining_needed:
            ar_pretrain_action_view = mo.vstack(
                [
                    mo.md(
                        f"""
                        Selected configuration:

                        - pretrain dataset: `{action_pretrain_label}`
                        - pretraining iterations: `{ar_base_cfg.pretrain_iters}`
                        - model: width `{ar_base_cfg.width}`, depth `{ar_base_cfg.depth}`, context `{ar_base_cfg.ctx_sz}`, future `{ar_base_cfg.fut_sz}`
                        """
                    ).callout(kind="info"),
                    ar_pretrain_button,
                ],
                gap=0.6,
            )
        else:
            ar_pretrain_action_view = mo.md(
                f"""
                Selected configuration does not require pretraining.

                - pretrain dataset: `{action_pretrain_label}`
                - pretraining iterations: `{ar_base_cfg.pretrain_iters}`
                """
            ).callout(kind="warn")
    ar_pretrain_action_view
    return (ar_pretrain_button,)


@app.cell(hide_code=True)
def _(
    SimpleNamespace,
    ar_base_init,
    ar_ctx_sz,
    ar_depth,
    ar_eval_bsz,
    ar_fut_sz,
    ar_pretrain_bsz,
    ar_pretrain_dataset,
    ar_pretrain_iters,
    ar_width,
    signal_dataset_names,
    torch,
):
    selected_pretrain_dataset = ar_pretrain_dataset.value
    ar_current_base_cfg = SimpleNamespace(
        pretrain_dataset=selected_pretrain_dataset,
        res_x=0.1,
        pretrain_bsz=int(ar_pretrain_bsz.value),
        posttrain_dataset_sz=int(ar_eval_bsz.value),
        pretrain_iters=0 if selected_pretrain_dataset is None else int(ar_pretrain_iters.value),
        pretraining_lr=1e-3,
        test_bsz=int(ar_eval_bsz.value),
        base_init=ar_base_init.value,
        width=int(ar_width.value),
        depth=int(ar_depth.value),
        ctx_sz=int(ar_ctx_sz.value),
        fut_sz=int(ar_fut_sz.value),
        K=10,
        global_seed=0,
        device=torch.device("cpu"),
        dataset_names=tuple(signal_dataset_names),
    )
    return (ar_current_base_cfg,)


@app.cell(hide_code=True)
def _(mo):
    get_selected_ar_base_cfg, set_selected_ar_base_cfg = mo.state(None)
    return get_selected_ar_base_cfg, set_selected_ar_base_cfg


@app.cell(hide_code=True)
def _(get_selected_ar_base_cfg):
    ar_base_cfg = get_selected_ar_base_cfg()
    return (ar_base_cfg,)


@app.cell(hide_code=True)
def _(SimpleNamespace, ar_num_perturbations, ar_sigma):
    ar_search_cfg = SimpleNamespace(
        sigma=float(ar_sigma.value),
        N=int(ar_num_perturbations.value),
    )
    return (ar_search_cfg,)


@app.cell(hide_code=True)
def _(
    ar_base_cfg,
    ar_pretrain_button,
    mo,
    np,
    signal_datasets_module,
    signal_models_module,
    torch,
):
    def build_pretrained_ar_model():
        import random
        import time
        import warnings

        def set_seed(seed):
            random.seed(seed)
            np.random.seed(seed)
            torch.manual_seed(seed)

        def load_signal_data(batch_size, dataset_name, seed=None):
            if seed is not None:
                np.random.seed(seed)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                return signal_datasets_module.load_data(batch_size, dataset_name, ar_base_cfg)

        def compute_mse(predictions, targets):
            return float(torch.mean((predictions - targets) ** 2).detach().cpu().item())

        set_seed(ar_base_cfg.global_seed)
        model = signal_models_module.Net(
            width=ar_base_cfg.width,
            depth=ar_base_cfg.depth,
            dim_in=ar_base_cfg.ctx_sz,
            dim_out=1,
            init_type=ar_base_cfg.base_init,
            device=ar_base_cfg.device,
        )
        model.init_weights()
        losses = []
        started = time.time()
        if ar_base_cfg.pretrain_dataset is not None and ar_base_cfg.pretrain_iters > 0:
            optimizer = torch.optim.Adam(model.parameters(), lr=ar_base_cfg.pretraining_lr)
            training_steps = mo.status.progress_bar(
                range(ar_base_cfg.pretrain_iters),
                title="Pretraining autoregressive MLP",
                subtitle=f"Dataset: {ar_base_cfg.pretrain_dataset}",
                completion_title="Pretraining complete",
                completion_subtitle="Base model is ready for local search",
                total=ar_base_cfg.pretrain_iters,
                show_rate=True,
                show_eta=True,
            )
            for _step in training_steps:
                model.train()
                optimizer.zero_grad()
                _, ctx_y, _, fut_y = load_signal_data(
                    ar_base_cfg.pretrain_bsz,
                    ar_base_cfg.pretrain_dataset,
                    seed=None,
                )
                loss = model.compute_loss(ctx_y, fut_y[:, [0]])
                loss.backward()
                optimizer.step()
                losses.append(float(loss.detach().cpu().item()))
        model.eval()

        eval_dataset_items = mo.status.progress_bar(
            list(enumerate(ar_base_cfg.dataset_names)),
            title="Preparing evaluation datasets",
            subtitle="Scoring the pretrained base across all signal categories",
            completion_title="Evaluation data ready",
            total=len(ar_base_cfg.dataset_names),
            show_rate=False,
            show_eta=False,
        )
        eval_data = {
            dataset_name: load_signal_data(ar_base_cfg.test_bsz, dataset_name, seed=2000 + index)
            for index, dataset_name in eval_dataset_items
        }
        plot_data = {
            dataset_name: load_signal_data(1, dataset_name, seed=4000 + index)
            for index, dataset_name in enumerate(ar_base_cfg.dataset_names)
        }
        base_scores = {}
        with torch.no_grad():
            for dataset_name, (_, ctx_y, _, fut_y) in eval_data.items():
                base_scores[dataset_name] = compute_mse(model.AR_rollout(ctx_y, ar_base_cfg.fut_sz), fut_y)

        return {
            "cfg": ar_base_cfg,
            "model": model,
            "losses": losses,
            "elapsed": time.time() - started,
            "eval_data": eval_data,
            "plot_data": plot_data,
            "base_scores": base_scores,
            "compute_mse": compute_mse,
        }

    if ar_base_cfg is None:
        ar_base_pretrain_result = None
    elif ar_base_cfg.pretrain_dataset is not None and ar_base_cfg.pretrain_iters > 0 and not ar_pretrain_button.value:
        ar_base_pretrain_result = None
    else:
        ar_base_pretrain_result = build_pretrained_ar_model()
    return (ar_base_pretrain_result,)


@app.cell(hide_code=True)
def _(
    SimpleNamespace,
    ar_base_cfg,
    ar_base_pretrain_result,
    ar_search_cfg,
    go,
    mo,
):
    if ar_base_pretrain_result is None:
        ar_pretrain_result = None
        if ar_base_cfg is None:
            ar_pretrain_view = mo.md("No pretraining configuration has been selected yet.").callout(kind="info")
        else:
            pending_pretrain_label = ar_base_cfg.pretrain_dataset if ar_base_cfg.pretrain_dataset is not None else "None"
            ar_pretrain_view = mo.md(
                f"""
                Pretraining is ready to start for the selected setup.

                - pretrain dataset: `{pending_pretrain_label}`
                - pretraining iterations: `{ar_base_cfg.pretrain_iters}`
                - model: width `{ar_base_cfg.width}`, depth `{ar_base_cfg.depth}`, context `{ar_base_cfg.ctx_sz}`, future `{ar_base_cfg.fut_sz}`

                Click **Start pretraining** above to train the base model.
                """
            ).callout(kind="info")
    else:
        cfg = ar_base_pretrain_result["cfg"]
        ar_lab_cfg = SimpleNamespace(
            **vars(cfg),
            sigma=ar_search_cfg.sigma,
            N=ar_search_cfg.N,
        )
        ar_pretrain_result = {
            **ar_base_pretrain_result,
            "cfg": ar_lab_cfg,
        }
        losses = ar_pretrain_result["losses"]
        if losses:
            loss_fig = go.Figure(
                data=[
                    go.Scatter(
                        x=list(range(1, len(losses) + 1)),
                        y=losses,
                        mode="lines",
                        line={"color": "#2563eb", "width": 3},
                        name="Next-step loss",
                    )
                ]
            )
            loss_fig.update_layout(
                height=260,
                margin={"l": 8, "r": 8, "t": 16, "b": 8},
                paper_bgcolor="#ffffff",
                plot_bgcolor="#ffffff",
                xaxis={"title": "Pretraining step", "showgrid": True, "gridcolor": "#e5e7eb"},
                yaxis={"title": "MSE", "showgrid": True, "gridcolor": "#e5e7eb"},
            )
        else:
            loss_fig = mo.md("No pretraining was requested, so the base model remains at random initialization.").callout(kind="warn")

        ready_pretrain_label = cfg.pretrain_dataset if cfg.pretrain_dataset is not None else "None"
        ar_pretrain_view = mo.vstack(
            [
                mo.md(
                    f"""
                    Base model ready in `{ar_pretrain_result['elapsed']:.2f}s`.

                    - pretrain dataset: `{ready_pretrain_label}`
                    - model: width `{cfg.width}`, depth `{cfg.depth}`, context `{cfg.ctx_sz}`, future `{cfg.fut_sz}`
                    - perturbation setup: `N={ar_lab_cfg.N}`, `sigma={ar_lab_cfg.sigma}`, eval batch `{cfg.test_bsz}`
                    """
                ),
                loss_fig,
            ],
            gap=0.7,
        )
    ar_pretrain_view
    return (ar_pretrain_result,)


@app.cell(hide_code=True)
def _(anywidget, traitlets):
    class PerturbationSamplerWidget(anywidget.AnyWidget):
        _esm = """
        export default {
          render({ model, el }) {
            const root = document.createElement("div");
            root.className = "nt-sampler-root";
            el.replaceChildren(root);

            const getPoints = () => model.get("points") || [];

            function add(svg, tag, attrs) {
              const element = document.createElementNS("http://www.w3.org/2000/svg", tag);
              Object.entries(attrs).forEach(([key, value]) => element.setAttribute(key, value));
              svg.appendChild(element);
              return element;
            }

            function addPoint(svg, point, index, width, height) {
              const x = width / 2 + Number(point.x || 0) * 105;
              const y = height / 2 - Number(point.y || 0) * 105;
              const circle = add(svg, "circle", {
                cx: x,
                cy: y,
                r: point.hit ? 6.5 : 4.8,
                class: point.hit ? "nt-sampler-hit" : "nt-sampler-miss",
              });
              circle.style.animationDelay = `${Math.min(index, 160) * 28}ms`;
              circle.appendChild(document.createElementNS("http://www.w3.org/2000/svg", "title")).textContent =
                `seed ${point.seed}: ${Number(point.loss || 0).toFixed(4)}`;
            }

          function draw() {
            const points = getPoints();
            const width = 720;
            const height = 360;
            root.innerHTML = `<div class="nt-sampler-title">Random perturbations around pretrained weights</div><svg viewBox="0 0 ${width} ${height}" class="nt-sampler-svg" role="img" aria-label="Random perturbations around pretrained weights"></svg><div class="nt-sampler-caption">Points appear in sampled order. Center diamond is the pretrained model.</div>`;
            const svg = root.querySelector("svg");
            add(svg, "rect", { x: 8, y: 8, width: width - 16, height: height - 16, rx: 8, class: "nt-sampler-bg" });
            add(svg, "line", { x1: 40, y1: height / 2, x2: width - 40, y2: height / 2, class: "nt-sampler-axis" });
            add(svg, "line", { x1: width / 2, y1: 34, x2: width / 2, y2: height - 34, class: "nt-sampler-axis" });
            add(svg, "circle", { cx: width / 2, cy: height / 2, r: 118, class: "nt-sampler-window" });
            add(svg, "path", { d: `M ${width / 2} ${height / 2 - 12} L ${width / 2 + 12} ${height / 2} L ${width / 2} ${height / 2 + 12} L ${width / 2 - 12} ${height / 2} Z`, class: "nt-sampler-center" });
            points.forEach((point, index) => addPoint(svg, point, index, width, height));
          }
          draw();
          model.on("change:points", draw);
          }
        };
        """
        _css = """
        .nt-sampler-root { border: 1px solid #d1d5db; border-radius: 8px; background: #fff; padding: 12px; }
        .nt-sampler-title { color: #111827; font-size: 1rem; font-weight: 850; margin-bottom: 6px; }
        .nt-sampler-svg { display: block; width: 100%; height: auto; }
        .nt-sampler-bg { fill: #f8fafc; stroke: #e5e7eb; }
        .nt-sampler-axis { stroke: #cbd5e1; stroke-width: 1; }
        .nt-sampler-window { fill: none; stroke: #64748b; stroke-width: 1.5; stroke-dasharray: 6 5; }
        .nt-sampler-center { fill: #111827; stroke: #fff; stroke-width: 2; }
        .nt-sampler-hit { fill: #16a34a; stroke: #fff; opacity: 0; animation: nt-point-in 420ms ease forwards; }
        .nt-sampler-miss { fill: #94a3b8; stroke: #fff; opacity: 0; animation: nt-point-in 420ms ease forwards; }
        .nt-sampler-caption { color: #475569; font-size: .82rem; margin-top: 4px; }
        @keyframes nt-point-in { from { opacity: 0; transform: scale(.2); transform-origin: center; } to { opacity: .9; transform: scale(1); } }
        """
        points = traitlets.List(default_value=[]).tag(sync=True)

    return (PerturbationSamplerWidget,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **Step 2: Visualize solution density**
    """)
    return


@app.cell(hide_code=True)
def _(mo, signal_dataset_names):
    ar_density_dataset = mo.ui.dropdown(
        {name: name for name in signal_dataset_names},
        value="mixed",
        searchable=True,
        label="Loss landscape test set",
        full_width=True,
    )
    ar_density_controls = mo.vstack(
        [
            mo.md(r"""
            Choose the task whose local loss landscape we want to inspect. In this toy model, pretraining on `mixed` signals plays the same conceptual role as pretraining an LLM on a broad web-scale corpus: the model sees many kinds of structure before we ask it to specialize.

            Selecting a loss landscape test set is like choosing a task-specific benchmark for an LLM. A sinusoid, squarewave, sawtooth, or composite signal plays the role that GSM8K might play for math, MBPP for programming, USPTO for chemistry, or ROCStories for writing. The pretrained model stays fixed at the center; changing the test set changes the task-specific loss we measure around that same center.

            Lower regions in the heatmap are nearby perturbations that perform better on the selected task. If many low-loss pockets surround the center, then this task has higher local solution density under the sampled directions.
            """),
            ar_density_dataset,
        ],
        gap=0.5,
    )
    ar_density_controls
    return (ar_density_dataset,)


@app.cell(hide_code=True)
def _(ar_density_dataset, ar_pretrain_result, copy, go, mo, np, torch):
    def build_density_landscape():
        cfg = ar_pretrain_result["cfg"]
        model = ar_pretrain_result["model"]
        dataset_name = ar_density_dataset.value
        _, ctx_y, _, fut_y = ar_pretrain_result["eval_data"][dataset_name]
        param_count = sum(param.numel() for param in model.parameters())
        def direction(seed):
            torch.manual_seed(seed)
            raw = []
            norm_sq = 0.0
            for param in model.parameters():
                item = torch.randn_like(param)
                raw.append(item)
                norm_sq += float(torch.sum(item**2).item())
            target_norm = cfg.sigma * float(np.sqrt(param_count))
            return [item * (target_norm / float(np.sqrt(norm_sq))) for item in raw]
        dir_a = direction(1301)
        dir_b = direction(2602)
        axis = np.linspace(-2.0, 2.0, 13)
        values = []
        with torch.no_grad():
            for beta in axis:
                density_row = []
                for alpha in axis:
                    plane_model = copy.deepcopy(model)
                    for param, a_dir, b_dir in zip(plane_model.parameters(), dir_a, dir_b, strict=True):
                        param.add_(float(alpha) * a_dir + float(beta) * b_dir)
                    plane_model.eval()
                    preds = plane_model.AR_rollout(ctx_y, cfg.fut_sz)
                    density_row.append(ar_pretrain_result["compute_mse"](preds, fut_y))
                values.append(density_row)
        return {"axis": axis, "values": np.array(values), "dataset": dataset_name, "base_loss": ar_pretrain_result["base_scores"][dataset_name]}

    if ar_pretrain_result is None:
        density_view = mo.md("Complete Step 1 to visualize solution density.").callout(kind="info")
    else:
        density = build_density_landscape()
        axis = density["axis"]
        values = density["values"]
        min_beta, min_alpha = np.unravel_index(int(np.argmin(values)), values.shape)
        density_fig = go.Figure()
        density_fig.add_trace(go.Contour(x=axis, y=axis, z=values, colorscale="Viridis", contours={"coloring": "heatmap"}, colorbar={"title": "MSE", "len": 0.78, "thickness": 12}, hovertemplate="alpha=%{x:.2f}<br>beta=%{y:.2f}<br>MSE=%{z:.4f}<extra></extra>", name="Task loss"))
        density_fig.add_trace(go.Scatter(x=[0.0], y=[0.0], mode="markers", marker={"symbol": "diamond", "size": 15, "color": "#111827", "line": {"color": "#ffffff", "width": 1}}, name="Pretrained weights", hovertemplate="pretrained weights<br>loss=%{customdata:.4f}<extra></extra>", customdata=[density["base_loss"]]))
        density_fig.add_trace(go.Scatter(x=[float(axis[min_alpha])], y=[float(axis[min_beta])], mode="markers", marker={"symbol": "x", "size": 14, "color": "#ffffff", "line": {"color": "#111827", "width": 3}}, name="Best point in slice", hovertemplate="best point in this 2D slice<extra></extra>"))
        density_fig.update_layout(
            height=340,
            margin={"l": 8, "r": 8, "t": 32, "b": 60},
            title=f"Local task-loss slice for `{density['dataset']}`",
            paper_bgcolor="#ffffff",
            plot_bgcolor="#ffffff",
            xaxis={"title": "weight direction alpha", "showgrid": False, "zeroline": True},
            yaxis={"title": "weight direction beta", "showgrid": False, "zeroline": True},
            legend={"orientation": "h", "x": 0.0, "y": -0.24, "xanchor": "left", "yanchor": "top"},
            showlegend=True,
        )
        density_view = mo.vstack([density_fig, mo.md(f"Base loss at the center: `{density['base_loss']:.4f}`").callout(kind="info")], gap=0.6)
    density_view
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **Step 3: Random guessing around pretrained weights**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    ar_random_guess_button = mo.ui.run_button(label="Run random guessing", kind="success")
    mo.vstack(
        [
            mo.md(r"""
            Click the button to sample Gaussian perturbations around the pretrained model. The animation shows perturbations in sampled order; green points improve the currently selected loss-landscape test set.
            """),
            ar_random_guess_button,
        ],
        gap=0.5,
    )
    return (ar_random_guess_button,)


@app.cell(hide_code=True)
def _(
    PerturbationSamplerWidget,
    ar_density_dataset,
    ar_pretrain_result,
    ar_random_guess_button,
    copy,
    mo,
    np,
    torch,
):
    def run_random_guessing():
        cfg = ar_pretrain_result["cfg"]
        base_model = ar_pretrain_result["model"]
        density_dataset = ar_density_dataset.value
        rng = np.random.default_rng(777)
        display_coords = rng.normal(0.0, 0.72, size=(cfg.N, 2))
        rows = []
        all_scores = {}
        with torch.no_grad():
            for seed in range(cfg.N):
                perturbed = copy.deepcopy(base_model)
                perturbed.perturb_weights(seed, cfg.sigma)
                perturbed.eval()
                scores = {}
                for dataset_name, (_, ctx_y, _, fut_y) in ar_pretrain_result["eval_data"].items():
                    preds = perturbed.AR_rollout(ctx_y, cfg.fut_sz)
                    scores[dataset_name] = ar_pretrain_result["compute_mse"](preds, fut_y)
                density_loss = scores[density_dataset]
                base_density_loss = ar_pretrain_result["base_scores"][density_dataset]
                guess_row = {
                    "seed": seed,
                    "x": float(display_coords[seed, 0]),
                    "y": float(display_coords[seed, 1]),
                    "density_loss": density_loss,
                    "hit": density_loss < base_density_loss,
                }
                rows.append(guess_row)
                all_scores[seed] = scores
        return {"rows": rows, "all_scores": all_scores, "density_dataset": density_dataset}

    if ar_pretrain_result is None:
        ar_random_guess_result = None
        random_guess_view = mo.md("Complete Step 1 before random guessing.").callout(kind="info")
    elif not ar_random_guess_button.value:
        ar_random_guess_result = None
        random_guess_view = mo.md("Click **Run random guessing** to sample perturbations around the pretrained weights.").callout(kind="info")
    else:
        ar_random_guess_result = run_random_guessing()
        sampler_points = [
            {"seed": guess_result_row["seed"], "x": guess_result_row["x"], "y": guess_result_row["y"], "hit": guess_result_row["hit"], "loss": guess_result_row["density_loss"]}
            for guess_result_row in ar_random_guess_result["rows"]
        ]
        ar_perturbation_widget = mo.ui.anywidget(PerturbationSamplerWidget(points=sampler_points))
        hit_rate = np.mean([guess_result_row["hit"] for guess_result_row in ar_random_guess_result["rows"]])
        random_guess_view = mo.vstack(
            [
                ar_perturbation_widget,
                mo.md(f"Hit rate on `{ar_random_guess_result['density_dataset']}`: `{hit_rate:.1%}` across `{len(sampler_points)}` perturbations.").callout(kind="info"),
            ],
            gap=0.6,
        )
    random_guess_view
    return (ar_random_guess_result,)


@app.cell(hide_code=True)
def _(ar_random_guess_result, mo):
    if ar_random_guess_result is None:
        ar_selected_perturbation = None
        selector_view = mo.md("Run random guessing to choose a perturbation.").callout(kind="info")
    else:
        best_by_density = sorted(ar_random_guess_result["rows"], key=lambda selector_row: selector_row["density_loss"])
        options = {f"seed {selector_row['seed']} | loss {selector_row['density_loss']:.4f}": selector_row["seed"] for selector_row in best_by_density}
        ar_selected_perturbation = mo.ui.dropdown(
            options,
            value=next(iter(options)),
            label="Selected perturbation",
            searchable=True,
            full_width=True,
        )
        selector_view = mo.vstack(
            [
                mo.md(r"""
                #### Step 4: solution diversity across all test sets

                Select any sampled perturbation and compare it against the pretrained base model across every signal category.
                """),
                ar_selected_perturbation,
            ],
            gap=0.5,
        )
    selector_view
    return (ar_selected_perturbation,)


@app.cell(hide_code=True)
def _(
    ar_pretrain_result,
    ar_random_guess_result,
    ar_selected_perturbation,
    go,
    mo,
):
    if ar_random_guess_result is None or ar_selected_perturbation is None:
        diversity_view = mo.md("Run random guessing and select a perturbation to see the radar chart.").callout(kind="info")
    else:
        selected_seed = int(ar_selected_perturbation.value)
        dataset_names = list(ar_pretrain_result["cfg"].dataset_names)
        base_scores = ar_pretrain_result["base_scores"]
        selected_scores = ar_random_guess_result["all_scores"][selected_seed]
        ratios = [min(2.5, base_scores[ratio_dataset_name] / max(selected_scores[ratio_dataset_name], 1e-9)) for ratio_dataset_name in dataset_names]
        base_line = [1.0 for _ in dataset_names]
        categories = dataset_names + [dataset_names[0]]
        selected_r = ratios + [ratios[0]]
        base_r = base_line + [base_line[0]]
        radar_fig = go.Figure()
        radar_fig.add_trace(go.Scatterpolar(r=base_r, theta=categories, fill="toself", name="Base", line={"color": "#64748b", "width": 2}, opacity=0.32))
        radar_fig.add_trace(go.Scatterpolar(r=selected_r, theta=categories, fill="toself", name=f"Perturbation seed {selected_seed}", line={"color": "#16a34a", "width": 3}, opacity=0.72))
        radar_fig.update_layout(height=560, margin={"l": 36, "r": 36, "t": 30, "b": 30}, paper_bgcolor="#ffffff", polar={"radialaxis": {"visible": True, "range": [0, 2.5], "tickvals": [0.5, 1.0, 1.5, 2.0, 2.5]}, "angularaxis": {"tickfont": {"size": 10}}}, showlegend=True)
        improved = [improved_dataset_name for improved_dataset_name in dataset_names if selected_scores[improved_dataset_name] < base_scores[improved_dataset_name]]
        diversity_table = mo.Html(
            "<div style='overflow-x:auto;'><table style='width:100%;border-collapse:collapse;font-size:0.86rem;color:#1f2937;'>"
            "<thead><tr style='border-bottom:1px solid #d1d5db;'><th style='text-align:left;padding:6px;'>Dataset</th><th style='text-align:right;padding:6px;'>Base MSE</th><th style='text-align:right;padding:6px;'>Perturb MSE</th><th style='text-align:right;padding:6px;'>Base / perturb</th></tr></thead><tbody>"
            + "".join(
                f"<tr><td style='padding:6px;'>{table_dataset_name}</td><td style='padding:6px;text-align:right;'>{base_scores[table_dataset_name]:.4f}</td><td style='padding:6px;text-align:right;'>{selected_scores[table_dataset_name]:.4f}</td><td style='padding:6px;text-align:right;'>{base_scores[table_dataset_name] / max(selected_scores[table_dataset_name], 1e-9):.2f}x</td></tr>"
                for table_dataset_name in dataset_names
            )
            + "</tbody></table></div>"
        )
        diversity_view = mo.vstack(
            [
                radar_fig,
                mo.md(f"Perturbation `seed {selected_seed}` improves `{len(improved)}` of `{len(dataset_names)}` test sets. Values above `1.0` on the radar chart are better than the pretrained base.").callout(kind="info"),
                diversity_table,
            ],
            gap=0.7,
        )
    diversity_view
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **Step 4: Two experts, two different strengths**

    The radar chart above lets us inspect one perturbation at a time. To make the diversity more concrete, let's automatically choose a pair of perturbations whose strengths disagree.

    This is the point of spectral discordance in plain language: the nearby experts are not all better or worse in the same way. One random jump can help on smooth signals, while another helps on sharper signals. Neither one is the final answer by itself, but their mistakes are not identical.
    """)
    return


@app.cell(hide_code=True)
def _(ar_pretrain_result, ar_random_guess_result, go, mo, np):
    if ar_random_guess_result is None:
        complementary_view = mo.md("Run random guessing to see a complementary expert pair.").callout(kind="info")
    else:
        comp_dataset_names = list(ar_pretrain_result["cfg"].dataset_names)
        comp_base_scores = ar_pretrain_result["base_scores"]
        comp_all_scores = ar_random_guess_result["all_scores"]
        comp_seeds = sorted(comp_all_scores)

        ratio_by_seed = {
            seed: {
                dataset_name: comp_base_scores[dataset_name] / max(comp_all_scores[seed][dataset_name], 1e-9)
                for dataset_name in comp_dataset_names
            }
            for seed in comp_seeds
        }
        seed_quality = {
            seed: float(np.mean([ratio_by_seed[seed][dataset_name] for dataset_name in comp_dataset_names]))
            for seed in comp_seeds
        }
        candidate_seeds = sorted(comp_seeds, key=lambda seed: seed_quality[seed], reverse=True)[: min(60, len(comp_seeds))]

        best_pair = None
        best_pair_score = -float("inf")
        for left_index, seed_a in enumerate(candidate_seeds):
            for seed_b in candidate_seeds[left_index + 1 :]:
                ratios_a = ratio_by_seed[seed_a]
                ratios_b = ratio_by_seed[seed_b]
                improves_a = {name for name in comp_dataset_names if ratios_a[name] > 1.0}
                improves_b = {name for name in comp_dataset_names if ratios_b[name] > 1.0}
                unique_a = improves_a - improves_b
                unique_b = improves_b - improves_a
                best_of_two = [max(ratios_a[name], ratios_b[name]) for name in comp_dataset_names]
                disagreement = float(np.mean([abs(ratios_a[name] - ratios_b[name]) for name in comp_dataset_names]))
                pair_score = (
                    3.0 * len(improves_a | improves_b)
                    + 2.0 * min(len(unique_a), len(unique_b))
                    + 0.5 * disagreement
                    + 0.2 * float(np.mean(best_of_two))
                )
                if pair_score > best_pair_score:
                    best_pair_score = pair_score
                    best_pair = (seed_a, seed_b, improves_a | improves_b)

        seed_a, seed_b, covered = best_pair
        comp_categories = comp_dataset_names + [comp_dataset_names[0]]
        comp_base_r = [1.0 for _ in comp_categories]
        seed_a_r = [min(2.5, ratio_by_seed[seed_a][name]) for name in comp_dataset_names]
        seed_b_r = [min(2.5, ratio_by_seed[seed_b][name]) for name in comp_dataset_names]
        seed_a_r = seed_a_r + [seed_a_r[0]]
        seed_b_r = seed_b_r + [seed_b_r[0]]

        pair_fig = go.Figure()
        pair_fig.add_trace(go.Scatterpolar(r=comp_base_r, theta=comp_categories, fill="toself", name="Base", line={"color": "#64748b", "width": 2}, opacity=0.22))
        pair_fig.add_trace(go.Scatterpolar(r=seed_a_r, theta=comp_categories, fill="toself", name=f"Expert A: seed {seed_a}", line={"color": "#dc2626", "width": 3}, opacity=0.62))
        pair_fig.add_trace(go.Scatterpolar(r=seed_b_r, theta=comp_categories, fill="toself", name=f"Expert B: seed {seed_b}", line={"color": "#2563eb", "width": 3}, opacity=0.58))
        pair_fig.update_layout(
            height=560,
            margin={"l": 36, "r": 36, "t": 30, "b": 30},
            paper_bgcolor="#ffffff",
            polar={
                "radialaxis": {"visible": True, "range": [0, 2.5], "tickvals": [0.5, 1.0, 1.5, 2.0, 2.5]},
                "angularaxis": {"tickfont": {"size": 10}},
            },
            showlegend=True,
        )

        def strongest(seed, other_seed):
            ordered = sorted(
                comp_dataset_names,
                key=lambda name: ratio_by_seed[seed][name] - ratio_by_seed[other_seed][name],
                reverse=True,
            )
            return ", ".join(f"`{name}`" for name in ordered[:3])

        complementary_summary = mo.md(
            f"""
            The pair finder chose `seed {seed_a}` and `seed {seed_b}` because their gains are not parallel.

            - Expert A is strongest relative to Expert B on {strongest(seed_a, seed_b)}.
            - Expert B is strongest relative to Expert A on {strongest(seed_b, seed_a)}.
            - Taking the better of the two experts per dataset would improve `{len(covered)}` of `{len(comp_dataset_names)}` categories.

            This still is not RandOpt. It is the reason RandOpt can help: diversity gives the ensemble something useful to average.
            """
        ).callout(kind="info")
        complementary_view = mo.vstack([pair_fig, complementary_summary], gap=0.7)
    complementary_view
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **RandOpt: Random Guess and Then, Ensemble**

    Now we can turn the observation into the actual algorithm proposed in the paper utilizing the two main insights $-$ Solution Density and Solution Diversity.

    RandOpt has two stages:

    1. **Sample** many local perturbations around the pretrained weights.
    2. **Select and ensemble** the useful perturbations instead of trusting only the single best one.

    Top-1 selection asks, "Which one random guess scored best on my target?" Top-k ensembling asks a slightly different question: "Which small set of good, nearby experts should vote together?" If the experts are diverse, the average can preserve the parts they agree on while canceling some of their idiosyncratic mistakes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **Select the target and ensemble size**
    """)
    return


@app.cell(hide_code=True)
def _(mo, signal_dataset_names):
    ar_randopt_target = mo.ui.dropdown(
        {name: name for name in signal_dataset_names},
        value="composite_sin_square" if "composite_sin_square" in signal_dataset_names else "mixed",
        searchable=True,
        label="RandOpt target",
        full_width=True,
    )
    ar_randopt_top_k = mo.ui.number(start=1, stop=25, step=1, value=5, label="Top-k ensemble size")
    ar_show_top_k = mo.ui.switch(value=True, label="Show top-k experts")
    ar_show_ensemble = mo.ui.switch(value=True, label="Show ensemble")
    mo.vstack(
        [
            mo.md(r"""
            The random perturbations have already been evaluated across every signal category. Here, RandOpt sorts those same perturbations by the selected target, takes the top-k, and averages their rollouts.
            """),
            mo.hstack(
                [ar_randopt_target, ar_randopt_top_k, ar_show_top_k, ar_show_ensemble],
                justify="start",
                align="center",
                wrap=True,
                gap=1.0,
            ),
        ],
        gap=0.6,
    )
    return ar_randopt_target, ar_randopt_top_k, ar_show_ensemble, ar_show_top_k


@app.cell(hide_code=True)
def _(
    ar_pretrain_result,
    ar_random_guess_result,
    ar_randopt_target,
    ar_randopt_top_k,
    copy,
    torch,
):
    def compute_mse_with_se(predictions, targets):
        squared_error = ((predictions - targets) ** 2).detach().cpu().numpy().reshape(-1)
        mse = float(squared_error.mean())
        se = float(squared_error.std() / max(1.0, float(squared_error.size) ** 0.5))
        return mse, se

    def perturbation_model(seed):
        model = copy.deepcopy(ar_pretrain_result["model"])
        model.perturb_weights(seed, ar_pretrain_result["cfg"].sigma)
        model.eval()
        return model

    if ar_random_guess_result is None:
        ar_randopt_result = None
    else:
        randopt_target_name = ar_randopt_target.value
        randopt_cfg = ar_pretrain_result["cfg"]
        randopt_sorted_rows = sorted(
            ar_random_guess_result["rows"],
            key=lambda row: ar_random_guess_result["all_scores"][row["seed"]][randopt_target_name],
        )
        randopt_top_k = min(int(ar_randopt_top_k.value), len(randopt_sorted_rows))
        randopt_top_k_seeds = [row["seed"] for row in randopt_sorted_rows[:randopt_top_k]]

        _, randopt_eval_ctx_y, _, randopt_eval_fut_y = ar_pretrain_result["eval_data"][randopt_target_name]
        randopt_plot_ctx_x, randopt_plot_ctx_y, randopt_plot_fut_x, randopt_plot_fut_y = ar_pretrain_result["plot_data"][randopt_target_name]

        with torch.no_grad():
            randopt_base_eval_preds = ar_pretrain_result["model"].AR_rollout(randopt_eval_ctx_y, randopt_cfg.fut_sz).detach()
            randopt_top_k_eval_preds = [
                perturbation_model(seed).AR_rollout(randopt_eval_ctx_y, randopt_cfg.fut_sz).detach()
                for seed in randopt_top_k_seeds
            ]
            randopt_ensemble_eval_preds = torch.stack(randopt_top_k_eval_preds).mean(dim=0)

            randopt_base_plot_preds = ar_pretrain_result["model"].AR_rollout(randopt_plot_ctx_y, randopt_cfg.fut_sz).detach()
            randopt_top_k_plot_preds = [
                perturbation_model(seed).AR_rollout(randopt_plot_ctx_y, randopt_cfg.fut_sz).detach()
                for seed in randopt_top_k_seeds
            ]
            randopt_ensemble_plot_preds = torch.stack(randopt_top_k_plot_preds).mean(dim=0)

        randopt_base_mse, randopt_base_se = compute_mse_with_se(randopt_base_eval_preds, randopt_eval_fut_y)
        randopt_top_1_mse, randopt_top_1_se = compute_mse_with_se(randopt_top_k_eval_preds[0], randopt_eval_fut_y)
        randopt_ensemble_mse, randopt_ensemble_se = compute_mse_with_se(randopt_ensemble_eval_preds, randopt_eval_fut_y)

        ar_randopt_result = {
            "target": randopt_target_name,
            "top_k": randopt_top_k,
            "top_k_seeds": randopt_top_k_seeds,
            "plot_data": (randopt_plot_ctx_x, randopt_plot_ctx_y, randopt_plot_fut_x, randopt_plot_fut_y),
            "base_plot_preds": randopt_base_plot_preds,
            "top_k_plot_preds": randopt_top_k_plot_preds,
            "ensemble_plot_preds": randopt_ensemble_plot_preds,
            "metrics": {
                "base_mse": randopt_base_mse,
                "base_se": randopt_base_se,
                "top_1_mse": randopt_top_1_mse,
                "top_1_se": randopt_top_1_se,
                "ensemble_mse": randopt_ensemble_mse,
                "ensemble_se": randopt_ensemble_se,
            },
        }
    return (ar_randopt_result,)


@app.cell(hide_code=True)
def _(ar_randopt_result, ar_show_ensemble, ar_show_top_k, go, mo):
    if ar_randopt_result is None:
        randopt_view = mo.md("Run random guessing first; RandOpt will reuse those sampled perturbations.").callout(kind="info")
    else:
        randopt_ctx_x, randopt_ctx_y, randopt_fut_x, randopt_fut_y = ar_randopt_result["plot_data"]
        randopt_x_context = randopt_ctx_x[0].detach().cpu().numpy()
        randopt_y_context = randopt_ctx_y[0].detach().cpu().numpy()
        randopt_x_future = randopt_fut_x[0].detach().cpu().numpy()
        randopt_y_future = randopt_fut_y[0].detach().cpu().numpy()

        randopt_fig = go.Figure()
        randopt_fig.add_trace(go.Scatter(x=randopt_x_context, y=randopt_y_context, mode="lines", name="Context", line={"color": "#2563eb", "width": 4}))
        randopt_fig.add_trace(go.Scatter(x=randopt_x_future, y=randopt_y_future, mode="lines", name="Ground truth", line={"color": "#2563eb", "width": 4, "dash": "dash"}))
        randopt_fig.add_trace(go.Scatter(x=randopt_x_future, y=ar_randopt_result["base_plot_preds"][0].detach().cpu().numpy(), mode="lines", name="Base model", line={"color": "#111827", "width": 2.4}))
        randopt_fig.add_trace(go.Scatter(x=randopt_x_future, y=ar_randopt_result["top_k_plot_preds"][0][0].detach().cpu().numpy(), mode="lines", name="Top-1 perturbation", line={"color": "#dc2626", "width": 3.2}))

        if ar_show_top_k.value:
            top_k_to_plot = min(5, len(ar_randopt_result["top_k_plot_preds"]))
            for index in range(1, top_k_to_plot):
                seed = ar_randopt_result["top_k_seeds"][index]
                randopt_fig.add_trace(
                    go.Scatter(
                        x=randopt_x_future,
                        y=ar_randopt_result["top_k_plot_preds"][index][0].detach().cpu().numpy(),
                        mode="lines",
                        name="Other top-k experts" if index == 1 else f"seed {seed}",
                        line={"color": "rgba(220,38,38,0.42)", "width": 1.8},
                        showlegend=index == 1,
                    )
                )

        if ar_show_ensemble.value:
            randopt_fig.add_trace(
                go.Scatter(
                    x=randopt_x_future,
                    y=ar_randopt_result["ensemble_plot_preds"][0].detach().cpu().numpy(),
                    mode="lines",
                    name="Ensemble",
                    line={"color": "#eab308", "width": 4},
                )
            )

        randopt_fig.update_layout(
            height=430,
            margin={"l": 8, "r": 8, "t": 36, "b": 8},
            title=f"RandOpt rollout on `{ar_randopt_result['target']}`",
            paper_bgcolor="#ffffff",
            plot_bgcolor="#ffffff",
            xaxis={"title": "x", "showgrid": True, "gridcolor": "#e5e7eb"},
            yaxis={"title": "signal value", "showgrid": True, "gridcolor": "#e5e7eb"},
            legend={"orientation": "h", "y": -0.18},
        )

        metrics = ar_randopt_result["metrics"]
        metric_table = mo.Html(
            "<div style='overflow-x:auto;'><table style='width:100%;border-collapse:collapse;font-size:0.9rem;color:#1f2937;'>"
            "<thead><tr style='border-bottom:1px solid #d1d5db;'><th style='text-align:left;padding:7px;'>Model</th><th style='text-align:right;padding:7px;'>MSE</th><th style='text-align:right;padding:7px;'>SE</th></tr></thead><tbody>"
            f"<tr><td style='padding:7px;'>Base model</td><td style='padding:7px;text-align:right;'>{metrics['base_mse']:.4f}</td><td style='padding:7px;text-align:right;'>{metrics['base_se']:.4f}</td></tr>"
            f"<tr><td style='padding:7px;'>Top-1 perturbation</td><td style='padding:7px;text-align:right;'>{metrics['top_1_mse']:.4f}</td><td style='padding:7px;text-align:right;'>{metrics['top_1_se']:.4f}</td></tr>"
            f"<tr><td style='padding:7px;'>Top-{ar_randopt_result['top_k']} ensemble</td><td style='padding:7px;text-align:right;'>{metrics['ensemble_mse']:.4f}</td><td style='padding:7px;text-align:right;'>{metrics['ensemble_se']:.4f}</td></tr>"
            "</tbody></table></div>"
        )
        seed_list = ", ".join(str(seed) for seed in ar_randopt_result["top_k_seeds"])
        randopt_summary = mo.md(
            f"""
            RandOpt selected seeds `{seed_list}` for `{ar_randopt_result['target']}`.

            The top-1 line is the best single guess. The ensemble line is the arithmetic mean of the top `{ar_randopt_result['top_k']}` perturbation rollouts. This is the key move: random search finds nearby specialists, and averaging turns a set of narrow experts into a broader predictor.
            """
        ).callout(kind="info")
        randopt_view = mo.vstack([randopt_fig, metric_table, randopt_summary], gap=0.75)
    randopt_view
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Exploration: Controllable RandOpt**

    Here, we get into uncharted territory and some new exploration. This section is a notebook extension, not a result claimed by the paper.

    Vanilla RandOpt throws a spherical net of random guesses evenly in all directions. But what if we could *aim* the net?

    If useful experts for a target task are clustered more strongly in some local directions than others, blindly sampling a round cloud may waste computation. **Controllable RandOpt** asks whether a cheap probe could guide the random search:

    - **Gradient nudge:** shift the center of the random cloud toward a promising direction.
    - **Covariance shaping:** stretch the cloud into an oval along directions where useful experts seem more likely.
    - **Combined:** move *and* stretch the search cloud.

    The hope is to increase the **effective hit rate** under the sampling distribution. The risk is that the probe may be wrong, expensive, or too narrow, so the demo below should be read as an intuition pump rather than a solved algorithm.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    ctrl_target_profile = mo.ui.dropdown(
        {
            "Instruction mix": "instruction",
            "Sharp specialist": "sharp",
            "Smooth specialist": "smooth",
        },
        value="Instruction mix",
        label="Target task thicket",
    )
    ctrl_strategy_choice = mo.ui.dropdown(
        {
            "Compare all": "all",
            "Vanilla isotropic": "vanilla",
            "Gradient nudge": "nudge",
            "Covariance shaping": "covariance",
            "Nudge + covariance": "combined",
        },
        value="Compare all",
        label="Search strategy",
    )
    ctrl_sample_count = mo.ui.number(start=80, stop=800, step=40, value=320, label="Samples")
    ctrl_random_seed = mo.ui.number(start=0, stop=9999, step=1, value=42, label="Seed")
    mo.vstack(
        [
            mo.md(r"""
            ## **Controllable search simulation**

            The center diamond is the pretrained model. The translucent ellipses are useful local task experts. Each strategy uses the same sample budget; the only difference is the mean and covariance of the perturbation distribution.
            """),
            mo.hstack(
                [ctrl_target_profile, ctrl_strategy_choice, ctrl_sample_count, ctrl_random_seed],
                justify="start",
                align="center",
                wrap=True,
                gap=1.0,
            ),
        ],
        gap=0.6,
    )
    return (
        ctrl_random_seed,
        ctrl_sample_count,
        ctrl_strategy_choice,
        ctrl_target_profile,
    )


@app.cell(hide_code=True)
def _(
    ctrl_random_seed,
    ctrl_sample_count,
    ctrl_strategy_choice,
    ctrl_target_profile,
    np,
):
    def ctrl_build_regions(profile):
        ctrl_profiles = {
            "instruction": [
                {"name": "smooth behavior", "center": np.array([-0.72, 0.45]), "radii": np.array([0.42, 0.18]), "angle": -0.35},
                {"name": "sharp behavior", "center": np.array([0.82, 0.42]), "radii": np.array([0.36, 0.16]), "angle": 0.48},
                {"name": "calibration", "center": np.array([0.22, -0.68]), "radii": np.array([0.34, 0.15]), "angle": 1.08},
            ],
            "sharp": [
                {"name": "sharp transition", "center": np.array([0.9, 0.34]), "radii": np.array([0.42, 0.14]), "angle": 0.42},
                {"name": "edge correction", "center": np.array([0.55, -0.48]), "radii": np.array([0.28, 0.12]), "angle": -0.85},
            ],
            "smooth": [
                {"name": "low frequency", "center": np.array([-0.82, 0.36]), "radii": np.array([0.46, 0.18]), "angle": -0.28},
                {"name": "phase correction", "center": np.array([-0.35, -0.58]), "radii": np.array([0.32, 0.14]), "angle": 0.86},
            ],
        }
        return ctrl_profiles[profile]

    def ctrl_rotation(angle):
        ctrl_cos = np.cos(angle)
        ctrl_sin = np.sin(angle)
        return np.array([[ctrl_cos, -ctrl_sin], [ctrl_sin, ctrl_cos]])

    def ctrl_inside_region(points, region):
        ctrl_rot = ctrl_rotation(region["angle"])
        ctrl_shifted = points - region["center"]
        ctrl_local = ctrl_shifted @ ctrl_rot
        ctrl_scaled = ctrl_local / region["radii"]
        return np.sum(ctrl_scaled**2, axis=1) <= 1.0

    def ctrl_strategy_parameters(strategy, probe_direction):
        ctrl_unit = probe_direction / max(float(np.linalg.norm(probe_direction)), 1e-9)
        ctrl_perp = np.array([-ctrl_unit[1], ctrl_unit[0]])
        ctrl_base_sigma = 0.58
        if strategy == "vanilla":
            return np.array([0.0, 0.0]), np.eye(2) * ctrl_base_sigma**2
        if strategy == "nudge":
            return ctrl_unit * 0.42, np.eye(2) * ctrl_base_sigma**2
        if strategy == "covariance":
            ctrl_basis = np.column_stack([ctrl_unit, ctrl_perp])
            ctrl_scale = np.diag([0.84**2, 0.28**2])
            return np.array([0.0, 0.0]), ctrl_basis @ ctrl_scale @ ctrl_basis.T
        ctrl_basis = np.column_stack([ctrl_unit, ctrl_perp])
        ctrl_scale = np.diag([0.78**2, 0.24**2])
        return ctrl_unit * 0.42, ctrl_basis @ ctrl_scale @ ctrl_basis.T

    def ctrl_sample_strategy(strategy, regions, sample_count, seed):
        ctrl_probe_direction = np.mean([region["center"] for region in regions], axis=0)
        ctrl_mean, ctrl_cov = ctrl_strategy_parameters(strategy, ctrl_probe_direction)
        ctrl_rng = np.random.default_rng(seed)
        ctrl_points = ctrl_rng.multivariate_normal(ctrl_mean, ctrl_cov, size=sample_count)
        ctrl_hits = np.zeros(sample_count, dtype=bool)
        for ctrl_region in regions:
            ctrl_hits = ctrl_hits | ctrl_inside_region(ctrl_points, ctrl_region)
        return {
            "strategy": strategy,
            "points": ctrl_points,
            "hits": ctrl_hits,
            "mean": ctrl_mean,
            "cov": ctrl_cov,
            "hit_rate": float(np.mean(ctrl_hits)),
            "expected_hits": float(np.sum(ctrl_hits)),
        }

    def ctrl_build_simulation(profile, visible_strategy, sample_count, seed):
        ctrl_regions = ctrl_build_regions(profile)
        ctrl_strategy_names = ["vanilla", "nudge", "covariance", "combined"]
        ctrl_results = {
            strategy: ctrl_sample_strategy(strategy, ctrl_regions, int(sample_count), int(seed) + 101 * index)
            for index, strategy in enumerate(ctrl_strategy_names)
        }
        if visible_strategy == "all":
            ctrl_visible = ctrl_strategy_names
        else:
            ctrl_visible = [visible_strategy]
        return {
            "profile": profile,
            "regions": ctrl_regions,
            "results": ctrl_results,
            "visible": ctrl_visible,
            "sample_count": int(sample_count),
        }

    ctrl_sim_result = ctrl_build_simulation(
        ctrl_target_profile.value,
        ctrl_strategy_choice.value,
        ctrl_sample_count.value,
        ctrl_random_seed.value,
    )
    return (ctrl_sim_result,)


@app.cell(hide_code=True)
def _(ctrl_sim_result, go, mo, np):
    def ctrl_ellipse_points(region):
        ctrl_angles = np.linspace(0.0, 2.0 * np.pi, 120)
        ctrl_circle = np.column_stack([np.cos(ctrl_angles), np.sin(ctrl_angles)])
        ctrl_rot = np.array(
            [
                [np.cos(region["angle"]), -np.sin(region["angle"])],
                [np.sin(region["angle"]), np.cos(region["angle"])],
            ]
        )
        return ctrl_circle * region["radii"] @ ctrl_rot.T + region["center"]

    ctrl_strategy_labels = {
        "vanilla": "Vanilla isotropic",
        "nudge": "Gradient nudge",
        "covariance": "Covariance shaping",
        "combined": "Nudge + covariance",
    }
    ctrl_strategy_colors = {
        "vanilla": "#64748b",
        "nudge": "#2563eb",
        "covariance": "#7c3aed",
        "combined": "#16a34a",
    }

    ctrl_fig = go.Figure()
    for ctrl_region_index, ctrl_region in enumerate(ctrl_sim_result["regions"]):
        ctrl_region_xy = ctrl_ellipse_points(ctrl_region)
        ctrl_fig.add_trace(
            go.Scatter(
                x=ctrl_region_xy[:, 0],
                y=ctrl_region_xy[:, 1],
                mode="lines",
                name=ctrl_region["name"],
                fill="toself",
                line={"color": "rgba(22,163,74,0.58)", "width": 2},
                fillcolor="rgba(22,163,74,0.12)",
                hovertemplate=f"{ctrl_region['name']}<extra></extra>",
                showlegend=ctrl_region_index == 0,
            )
        )

    for ctrl_strategy in ctrl_sim_result["visible"]:
        ctrl_result = ctrl_sim_result["results"][ctrl_strategy]
        ctrl_points = ctrl_result["points"]
        ctrl_hits = ctrl_result["hits"]
        ctrl_fig.add_trace(
            go.Scatter(
                x=ctrl_points[~ctrl_hits, 0],
                y=ctrl_points[~ctrl_hits, 1],
                mode="markers",
                name=f"{ctrl_strategy_labels[ctrl_strategy]} misses",
                marker={"size": 5, "color": ctrl_strategy_colors[ctrl_strategy], "opacity": 0.22},
                hovertemplate=f"{ctrl_strategy_labels[ctrl_strategy]}<br>miss<extra></extra>",
                showlegend=False,
            )
        )
        ctrl_fig.add_trace(
            go.Scatter(
                x=ctrl_points[ctrl_hits, 0],
                y=ctrl_points[ctrl_hits, 1],
                mode="markers",
                name=f"{ctrl_strategy_labels[ctrl_strategy]} hits",
                marker={"size": 8, "color": ctrl_strategy_colors[ctrl_strategy], "line": {"color": "#ffffff", "width": 1}},
                hovertemplate=f"{ctrl_strategy_labels[ctrl_strategy]}<br>hit<extra></extra>",
            )
        )
        ctrl_fig.add_trace(
            go.Scatter(
                x=[ctrl_result["mean"][0]],
                y=[ctrl_result["mean"][1]],
                mode="markers",
                name=f"{ctrl_strategy_labels[ctrl_strategy]} center",
                marker={"symbol": "x", "size": 12, "color": ctrl_strategy_colors[ctrl_strategy], "line": {"width": 2}},
                hovertemplate=f"{ctrl_strategy_labels[ctrl_strategy]} center<extra></extra>",
                showlegend=False,
            )
        )

    ctrl_fig.add_trace(
        go.Scatter(
            x=[0.0],
            y=[0.0],
            mode="markers",
            name="Pretrained weights",
            marker={"symbol": "diamond", "size": 16, "color": "#111827", "line": {"color": "#ffffff", "width": 2}},
            hovertemplate="pretrained weights<extra></extra>",
        )
    )
    ctrl_fig.update_layout(
        height=560,
        margin={"l": 8, "r": 8, "t": 34, "b": 8},
        title="Controllable sampling changes effective solution density",
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        xaxis={"title": "local weight direction 1", "range": [-1.8, 1.8], "showgrid": True, "gridcolor": "#e5e7eb", "zeroline": True},
        yaxis={"title": "local weight direction 2", "range": [-1.5, 1.5], "showgrid": True, "gridcolor": "#e5e7eb", "zeroline": True, "scaleanchor": "x", "scaleratio": 1},
        legend={"orientation": "h", "y": -0.2},
    )

    ctrl_rows = []
    for ctrl_strategy_key, ctrl_result in ctrl_sim_result["results"].items():
        ctrl_rows.append(
            f"<tr><td style='padding:7px;'>{ctrl_strategy_labels[ctrl_strategy_key]}</td>"
            f"<td style='padding:7px;text-align:right;'>{ctrl_result['hit_rate']:.1%}</td>"
            f"<td style='padding:7px;text-align:right;'>{ctrl_result['expected_hits']:.0f} / {ctrl_sim_result['sample_count']}</td></tr>"
        )
    ctrl_metrics_table = mo.Html(
        "<div style='overflow-x:auto;'><table style='width:100%;border-collapse:collapse;font-size:0.9rem;color:#1f2937;'>"
        "<thead><tr style='border-bottom:1px solid #d1d5db;'><th style='text-align:left;padding:7px;'>Strategy</th><th style='text-align:right;padding:7px;'>Estimated hit rate</th><th style='text-align:right;padding:7px;'>Hits</th></tr></thead><tbody>"
        + "".join(ctrl_rows)
        + "</tbody></table></div>"
    )
    ctrl_best_strategy = max(ctrl_sim_result["results"], key=lambda strategy: ctrl_sim_result["results"][strategy]["hit_rate"])
    ctrl_vanilla_rate = ctrl_sim_result["results"]["vanilla"]["hit_rate"]
    ctrl_best_rate = ctrl_sim_result["results"][ctrl_best_strategy]["hit_rate"]
    ctrl_ratio = ctrl_best_rate / max(ctrl_vanilla_rate, 1e-9)
    ctrl_summary = mo.md(
        f"""
        In this simulation, `{ctrl_strategy_labels[ctrl_best_strategy]}` gives the highest hit rate. It is `{ctrl_ratio:.1f}x` the vanilla isotropic estimate for this target.

        This should be read as an argument for why controllability is worth studying, not as evidence that this exact strategy works in real LLM weight space. If the paper says useful experts are dense nearby, this extension asks whether we can spend the same parallel sampling budget more intelligently by learning the local shape of that density.
        """
    ).callout(kind="info")
    ctrl_view = mo.vstack([ctrl_fig, ctrl_metrics_table, ctrl_summary], gap=0.75)
    ctrl_view
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Compute Trade-Off: What If Parallelism Is Limited?**

    There is a hidden cost to vanilla RandOpt. It is mathematically fast ($\mathcal{O}(1)$ optimization steps), but practically, that wall-clock speed comes from evaluating many candidate models in parallel. If those workers are not available, evaluating thousands of random guesses turns into a slow serial queue.

    Traditional post-training makes the opposite trade-off: it uses many sequential steps, but it does not require evaluating hundreds of independent perturbed models at once.

    **Controllable RandOpt tries to get some of both worlds.** By spending a small amount of sequential compute upfront to "aim" the search cloud, it may reduce the number of parallel random guesses needed to find useful experts.

    **The catch:** this only helps when the probe is cheap and informative. A bad probe can point the random search toward an empty patch of the landscape, reduce diversity, or quietly reintroduce the sequential cost we were trying to avoid.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    ctrl_budget_workers = mo.ui.number(start=1, stop=512, step=1, value=48, label="Available workers")
    ctrl_budget_base_density = mo.ui.number(start=0.001, stop=0.2, step=0.001, value=0.025, label="Vanilla hit rate")
    ctrl_budget_target_hits = mo.ui.number(start=1, stop=20, step=1, value=5, label="Experts needed")
    ctrl_budget_confidence = mo.ui.number(start=0.5, stop=0.99, step=0.01, value=0.9, label="Success probability")
    ctrl_budget_probe_quality = mo.ui.number(start=-1.0, stop=1.0, step=0.1, value=0.6, label="Probe quality")
    ctrl_budget_probe_steps = mo.ui.number(start=0, stop=30, step=1, value=4, label="Probe time steps")
    mo.vstack(
        [
            mo.md(r"""
            ### **Parallel budget model**

            This toy model asks how many perturbations are needed to get at least `k` useful experts with a chosen probability. Vanilla RandOpt uses the base hit rate. Controllable RandOpt pays a probe cost, then changes the hit rate according to probe quality.
            """),
            mo.hstack(
                [
                    ctrl_budget_workers,
                    ctrl_budget_base_density,
                    ctrl_budget_target_hits,
                    ctrl_budget_confidence,
                    ctrl_budget_probe_quality,
                    ctrl_budget_probe_steps,
                ],
                justify="start",
                align="center",
                wrap=True,
                gap=1.0,
            ),
        ],
        gap=0.6,
    )
    return (
        ctrl_budget_base_density,
        ctrl_budget_confidence,
        ctrl_budget_probe_quality,
        ctrl_budget_probe_steps,
        ctrl_budget_target_hits,
        ctrl_budget_workers,
    )


@app.cell(hide_code=True)
def _(
    ctrl_budget_base_density,
    ctrl_budget_confidence,
    ctrl_budget_probe_quality,
    ctrl_budget_probe_steps,
    ctrl_budget_target_hits,
    ctrl_budget_workers,
    np,
):
    def ctrl_budget_prob_at_least(success_prob, trials, target_hits):
        ctrl_budget_p0 = (1.0 - success_prob) ** trials
        ctrl_budget_total = ctrl_budget_p0
        ctrl_budget_term = ctrl_budget_p0
        for ctrl_budget_hit_count in range(1, target_hits):
            ctrl_budget_term *= ((trials - ctrl_budget_hit_count + 1) / ctrl_budget_hit_count) * (success_prob / max(1.0 - success_prob, 1e-12))
            ctrl_budget_total += ctrl_budget_term
        return 1.0 - ctrl_budget_total

    def ctrl_budget_required_samples(success_prob, target_hits, confidence):
        ctrl_budget_cap = 10000
        for ctrl_budget_trials in range(target_hits, ctrl_budget_cap + 1):
            if ctrl_budget_prob_at_least(success_prob, ctrl_budget_trials, target_hits) >= confidence:
                return ctrl_budget_trials
        return ctrl_budget_cap

    ctrl_budget_base_p = float(ctrl_budget_base_density.value)
    ctrl_budget_quality = float(ctrl_budget_probe_quality.value)
    ctrl_budget_probe_multiplier = max(0.15, 1.0 + 2.8 * ctrl_budget_quality)
    ctrl_budget_controlled_p = min(0.65, ctrl_budget_base_p * ctrl_budget_probe_multiplier)
    ctrl_budget_k = int(ctrl_budget_target_hits.value)
    ctrl_budget_conf = float(ctrl_budget_confidence.value)
    ctrl_budget_worker_count = int(ctrl_budget_workers.value)
    ctrl_budget_probe_rounds = int(ctrl_budget_probe_steps.value)

    ctrl_budget_vanilla_samples = ctrl_budget_required_samples(ctrl_budget_base_p, ctrl_budget_k, ctrl_budget_conf)
    ctrl_budget_controlled_samples = ctrl_budget_required_samples(ctrl_budget_controlled_p, ctrl_budget_k, ctrl_budget_conf)
    ctrl_budget_posttrain_steps = int(80 + 8 * ctrl_budget_k)

    ctrl_budget_worker_axis = np.unique(
        np.clip(
            np.round(np.geomspace(1, max(ctrl_budget_vanilla_samples, ctrl_budget_controlled_samples, ctrl_budget_worker_count, 2), 80)).astype(int),
            1,
            10000,
        )
    )
    ctrl_budget_vanilla_rounds = np.ceil(ctrl_budget_vanilla_samples / ctrl_budget_worker_axis).astype(int)
    ctrl_budget_controlled_rounds = ctrl_budget_probe_rounds + np.ceil(ctrl_budget_controlled_samples / ctrl_budget_worker_axis).astype(int)
    ctrl_budget_posttrain_rounds = np.full_like(ctrl_budget_worker_axis, ctrl_budget_posttrain_steps)

    ctrl_budget_summary_data = {
        "base_hit_rate": ctrl_budget_base_p,
        "controlled_hit_rate": ctrl_budget_controlled_p,
        "probe_multiplier": ctrl_budget_probe_multiplier,
        "target_hits": ctrl_budget_k,
        "confidence": ctrl_budget_conf,
        "workers": ctrl_budget_worker_count,
        "probe_rounds": ctrl_budget_probe_rounds,
        "vanilla_samples": ctrl_budget_vanilla_samples,
        "controlled_samples": ctrl_budget_controlled_samples,
        "posttrain_steps": ctrl_budget_posttrain_steps,
        "worker_axis": ctrl_budget_worker_axis,
        "vanilla_rounds": ctrl_budget_vanilla_rounds,
        "controlled_rounds": ctrl_budget_controlled_rounds,
        "posttrain_rounds": ctrl_budget_posttrain_rounds,
        "vanilla_current_rounds": int(np.ceil(ctrl_budget_vanilla_samples / ctrl_budget_worker_count)),
        "controlled_current_rounds": int(ctrl_budget_probe_rounds + np.ceil(ctrl_budget_controlled_samples / ctrl_budget_worker_count)),
        "posttrain_current_rounds": ctrl_budget_posttrain_steps,
    }
    return (ctrl_budget_summary_data,)


@app.cell(hide_code=True)
def _(ctrl_budget_summary_data, go, mo):
    ctrl_budget_fig = go.Figure()
    ctrl_budget_fig.add_trace(
        go.Scatter(
            x=ctrl_budget_summary_data["worker_axis"],
            y=ctrl_budget_summary_data["posttrain_rounds"],
            mode="lines",
            name="Sequential post-training",
            line={"color": "#111827", "width": 3, "dash": "dot"},
            hovertemplate="workers=%{x}<br>time steps=%{y}<extra></extra>",
        )
    )
    ctrl_budget_fig.add_trace(
        go.Scatter(
            x=ctrl_budget_summary_data["worker_axis"],
            y=ctrl_budget_summary_data["vanilla_rounds"],
            mode="lines",
            name="Vanilla RandOpt",
            line={"color": "#dc2626", "width": 3},
            hovertemplate="workers=%{x}<br>evaluation rounds=%{y}<extra></extra>",
        )
    )
    ctrl_budget_fig.add_trace(
        go.Scatter(
            x=ctrl_budget_summary_data["worker_axis"],
            y=ctrl_budget_summary_data["controlled_rounds"],
            mode="lines",
            name="Controllable RandOpt",
            line={"color": "#16a34a", "width": 3},
            hovertemplate="workers=%{x}<br>probe + evaluation rounds=%{y}<extra></extra>",
        )
    )
    ctrl_budget_fig.add_vline(
        x=ctrl_budget_summary_data["workers"],
        line={"color": "#2563eb", "width": 2, "dash": "dash"},
        annotation_text="available workers",
        annotation_position="top",
    )
    ctrl_budget_fig.update_layout(
        height=450,
        margin={"l": 8, "r": 8, "t": 36, "b": 8},
        title="Parallel workers trade off against sequential time",
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        xaxis={"title": "parallel workers available", "type": "log", "showgrid": True, "gridcolor": "#e5e7eb"},
        yaxis={"title": "wall-clock time steps / evaluation rounds", "type": "log", "showgrid": True, "gridcolor": "#e5e7eb"},
        legend={"orientation": "h", "y": -0.2},
    )

    ctrl_budget_table = mo.Html(
        "<div style='overflow-x:auto;'><table style='width:100%;border-collapse:collapse;font-size:0.9rem;color:#1f2937;'>"
        "<thead><tr style='border-bottom:1px solid #d1d5db;'><th style='text-align:left;padding:7px;'>Method</th><th style='text-align:right;padding:7px;'>Candidates / steps</th><th style='text-align:right;padding:7px;'>Workers for one evaluation round</th><th style='text-align:right;padding:7px;'>Rounds with current workers</th></tr></thead><tbody>"
        f"<tr><td style='padding:7px;'>Sequential post-training</td><td style='padding:7px;text-align:right;'>{ctrl_budget_summary_data['posttrain_steps']}</td><td style='padding:7px;text-align:right;'>1</td><td style='padding:7px;text-align:right;'>{ctrl_budget_summary_data['posttrain_current_rounds']}</td></tr>"
        f"<tr><td style='padding:7px;'>Vanilla RandOpt</td><td style='padding:7px;text-align:right;'>{ctrl_budget_summary_data['vanilla_samples']}</td><td style='padding:7px;text-align:right;'>{ctrl_budget_summary_data['vanilla_samples']}</td><td style='padding:7px;text-align:right;'>{ctrl_budget_summary_data['vanilla_current_rounds']}</td></tr>"
        f"<tr><td style='padding:7px;'>Controllable RandOpt</td><td style='padding:7px;text-align:right;'>{ctrl_budget_summary_data['controlled_samples']} + {ctrl_budget_summary_data['probe_rounds']} probe steps</td><td style='padding:7px;text-align:right;'>{ctrl_budget_summary_data['controlled_samples']}</td><td style='padding:7px;text-align:right;'>{ctrl_budget_summary_data['controlled_current_rounds']}</td></tr>"
        "</tbody></table></div>"
    )

    if ctrl_budget_summary_data["controlled_current_rounds"] < ctrl_budget_summary_data["vanilla_current_rounds"]:
        ctrl_budget_verdict = "Here, the probe is useful enough that Controllable RandOpt needs fewer wall-clock rounds than vanilla RandOpt under the worker limit."
        ctrl_budget_kind = "success"
    elif ctrl_budget_summary_data["controlled_current_rounds"] == ctrl_budget_summary_data["vanilla_current_rounds"]:
        ctrl_budget_verdict = "Here, controllability is roughly neutral: the smaller sample count is canceled by the probe cost."
        ctrl_budget_kind = "info"
    else:
        ctrl_budget_verdict = "Here, controllability is not worth it: the probe cost or probe quality is bad enough that vanilla RandOpt wins."
        ctrl_budget_kind = "warn"

    ctrl_budget_summary = mo.md(
        f"""
        Vanilla hit rate: `{ctrl_budget_summary_data['base_hit_rate']:.2%}`. Controlled hit rate after the probe: `{ctrl_budget_summary_data['controlled_hit_rate']:.2%}`.

        {ctrl_budget_verdict}

        This is the actual trade-off. Controllable RandOpt is attractive when a small amount of sequential probe work reduces the required perturbation count by more than it costs. It is not attractive when the probe is expensive, noisy, or diversity-destroying.
        """
    ).callout(kind=ctrl_budget_kind)
    ctrl_budget_view = mo.vstack([ctrl_budget_fig, ctrl_budget_table, ctrl_budget_summary], gap=0.75)
    ctrl_budget_view
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Closing: What We Built**

    That's the notebook.

    We started with a deliberately silly random guessing game, then used it to build the intuition that random search is only silly when useful targets are sparse. If useful solutions are dense around pretrained weights, random perturbations stop looking like blind luck and start looking like a parallel search strategy.

    Then we moved into the 1D toy model. We trained a small autoregressive network, looked at task-specific loss slices around the pretrained weights, sampled perturbations, compared narrow experts, and finally averaged top-k experts with RandOpt. The key lesson is that density and diversity are not competing ideas. Density helps us find nearby experts; diversity makes ensembling useful.

    We ended with a speculative extension: Controllable RandOpt. The point was not to claim a solved algorithm, but to ask a practical question. If vanilla RandOpt trades sequential optimization for a large parallel evaluation budget, can cheap probes make each sample more likely to hit, especially when parallel compute is limited?

    If the original paper felt abstract before, I hope the main idea is now easier to picture: pretraining may pack many specialized behaviors into the local neighborhood of a model, and RandOpt is one way to search that neighborhood. For the full technical treatment, experiments, and precise claims, the original paper is still the place to go next.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Acknowledgments**

    The original writing, notebook structure, and ideas behind the visualizations and games came from the author of this notebook. The writing was polished using **Gemini 3.1 Pro**. Most, if not all, of the code was written using **Codex with GPT-5.5 (High)**.
    """)
    return


if __name__ == "__main__":
    app.run()
