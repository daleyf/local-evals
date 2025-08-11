# Local LLM Evals

A tiny toolkit for running quick evaluations on local language models.  It trades
fancy features for simplicity so you can benchmark models on a laptop with just a
few commands.

## Install

```bash
pip install -r requirements.txt
```

To evaluate real models you also need a backend.  This project currently
supports [Ollama](https://ollama.ai/) via its local HTTP API.  Install and run
Ollama separately if you want to test actual models.

## Usage

```bash
python run_eval.py --model echo --dataset datasets/simple_qa.jsonl
```

`--model` selects the backend:

* `echo` – returns the prompt unchanged (useful for testing the pipeline).
* `ollama:MODEL` – queries an Ollama model like `ollama:llama2`.

Results show simple accuracy and average latency.  Use `--save results.json`
to keep raw outputs.

## Adding Datasets

Datasets are newline‑delimited JSON files with at least a `prompt` field and an
optional `expected` field used for scoring.

```jsonl
{"prompt": "What is the capital of France?", "expected": "Paris"}
{"prompt": "2 + 2 =", "expected": "4"}
```

Drop new files into the `datasets/` folder and reference them with
`--dataset path/to/file.jsonl`.

## Why so minimal?

The goal is to make running local model checks easy, even on a MacBook.
The code favours readability over raw performance and keeps dependencies light.
Feel free to extend it for your own experiments!
