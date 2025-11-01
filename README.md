# Google Code Golf 2025 – Solutions Repository

This repository contains my personal solutions for the **NeurIPS 2025 — Google Code Golf Championship** hosted on Kaggle.

The challenge involves solving ARC (Abstraction & Reasoning Corpus)-style tasks using **the shortest possible Python code**, emphasizing reasoning, pattern recognition, and code-efficiency.


## Repository Structure

```
/code/                  # Python solutions (task001.py … task400.py)
/code_golf_utils/       # Loader, verifier, and visualization utilities
/data/                  # ARC-AGI and ARC-GEN JSON tasks
pack_now.py             # Build submission.zip from solved scripts
verify_task.py          # Test single task solution locally
requirements.txt        # Dependencies
.gitignore              # Ignore cache & temp files
README.md               # Project documentation
submission.zip          # Final submission bundle (auto-generated)
```


## Running Tests

### Test a single task

```bash
python verify_task.py <task_number>

# Example
python verify_task.py 1
```

### Generate competition submission

```bash
python pack_now.py
```

This creates `submission.zip` where solved tasks are included and missing ones are autofilled with a stub.

---

## Getting Started

### Clone repo

```bash
git clone https://github.com/SirHarginger/google-code-golf-2025-my-solution.git
cd google-code-golf-2025-my-solution
```

### Create env & install deps

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```


## Key Notes

* Each solution must expose a `p(g)` function to be validated.
* Code-length matters — shorter = better.
* ARC-style tasks require **pattern generalization**, not brute force.
* Stub generators ensure *every task file exists* in your zip even if unsolved.


## License

Released under **Apache License 2.0**.


## Contact

For collaboration or questions:

**Benjamin Boafo**
 `benjaminboafo120@gmail.com`

