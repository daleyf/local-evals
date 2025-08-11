import argparse
import json
import time
from pathlib import Path
from typing import List, Dict

from evals.model import get_model
from evals.metrics import exact_match, levenshtein_similarity


def load_dataset(path: str) -> List[Dict[str, str]]:
    data: List[Dict[str, str]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            data.append(json.loads(line))
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a simple evaluation")
    parser.add_argument("--model", default="echo", help="Model spec, e.g. 'echo' or 'ollama:llama2'")
    parser.add_argument("--dataset", default="datasets/simple_qa.jsonl", help="Path to JSONL dataset")
    parser.add_argument("--save", default=None, help="Optional path to save raw results as JSON")
    args = parser.parse_args()

    dataset = load_dataset(args.dataset)
    model = get_model(args.model)

    correct = 0
    results = []
    start = time.time()
    for row in dataset:
        prompt = row["prompt"]
        expected = row.get("expected")
        output = model(prompt)
        row_result = {
            "prompt": prompt,
            "expected": expected,
            "output": output,
        }
        row_result["exact_match"] = exact_match(output, expected)
        row_result["similarity"] = levenshtein_similarity(output, expected)
        if row_result["exact_match"]:
            correct += 1
        results.append(row_result)
    duration = time.time() - start

    total = len(dataset)
    print(f"Model: {args.model}")
    print(f"Dataset: {Path(args.dataset).name}")
    if total:
        print(f"Accuracy: {correct/total*100:.1f}%")
        print(f"Avg Latency: {duration/total:.2f}s")

    if args.save:
        with open(args.save, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()
