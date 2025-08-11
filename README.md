# 🧪 Build Your Own Evals for Local LLMs

Test and benchmark **any** local large language model (LLM) with your own datasets.  
Easily compare models, track results over time, and design custom evaluation pipelines.

---

## 🚀 Features
- **Plug & play model testing** — works with `Ollama`, `transformers`, `llama.cpp`, or any local model API.
- **Custom datasets** — add your own `.jsonl` or `.csv` files for evaluation.
- **Example tests included** — start with built-in QA, summarization, and reasoning evals.
- **Simple metrics** — accuracy, BLEU, ROUGE, and custom scoring hooks.
- **Repeatable results** — same tests, different models, comparable outputs.

---

## 📦 Installation

```bash
git clone https://github.com/yourname/local-llm-evals.git
cd local-llm-evals
pip install -r requirements.txt
🗂 Project Structure
perl
Copy
Edit
local-llm-evals/
├── datasets/          # Example datasets (JSONL, CSV)
├── tests/             # Example test scripts
├── results/           # Saved run outputs + metrics
├── evals/             # Core evaluation functions
├── config.yaml        # Config for model + dataset selection
└── README.md
⚡ Quick Start
Run a test with the default dataset and model:

bash
Copy
Edit
python run_eval.py --model ollama:llama3 --dataset datasets/simple_qa.jsonl
Example Output:

yaml
Copy
Edit
Model: llama3 (Ollama)
Dataset: simple_qa
Accuracy: 83%
Avg Latency: 1.8s
🧩 Adding Your Own Dataset
Create a .jsonl file in datasets/:

json
Copy
Edit
{"prompt": "What is the capital of France?", "expected": "Paris"}
{"prompt": "2 + 2 =", "expected": "4"}
Run:

bash
Copy
Edit
python run_eval.py --model ollama:mistral --dataset datasets/my_dataset.jsonl
🔬 Example Tests
We include a few out of the box:

simple_qa.jsonl — Basic factual recall.

math_reasoning.jsonl — Step-by-step math reasoning.

summarization.jsonl — Text summarization scoring.

📊 Metrics
By default, we compute:

Exact Match for QA

String Similarity (Levenshtein)

ROUGE / BLEU for summarization

You can add your own metrics in evals/metrics.py.

🔌 Supported Backends
Ollama

HuggingFace transformers (with AutoModelForCausalLM)

llama.cpp

Any custom API endpoint

Switch models via:

bash
Copy
Edit
python run_eval.py --model transformers:meta-llama/Llama-2-7b-chat-hf
📅 Roadmap
 Add multi-turn conversation evals

 Add leaderboard-style web UI

 Add noise injection / robustness tests

🤝 Contributing
Pull requests welcome!

Fork it

Create your feature branch

Submit a PR


