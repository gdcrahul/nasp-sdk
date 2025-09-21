# NASP SDK – Neural Agent Security Protocol

This is a prototype SDK that wraps around an LLM to provide input/output safety features.  
The project is being built in **weekly phases** as part of internship progress.

---

## 📌 Week 1 – Initial Setup ✅

- Created the **project structure** (`nasp/` package with `agent.py`, `filters.py`, `__init__.py`)
- Implemented **NASPAgent** class with a simple `safe_ask` method
- Added **basic filter** (`block_bad_words`) to detect unsafe words like _password, hack, attack, credit card_
- Built a **demo script** (`demo.py`) to test safe and unsafe queries
- Wrote **basic unit tests** in `tests/test_agent.py` to check filtering logic

📂 **Repo at the end of Week 1:**

- Could detect and block unsafe words
- Showed basic demo working with both safe and unsafe inputs

---

## 📌 Week 2 – Improvements ✅

- Expanded **filtering system** with a stronger bad words list
- Improved `safe_ask` response to clearly return ⚠️ _Unsafe content blocked_
- Enhanced **unit tests** with additional unsafe input cases
- Updated **demo script** to showcase both scenarios (safe + unsafe queries)
- **GitHub repo management:**
  - Tagged commits as `week1` and `week2` for clean milestones
  - Professional commit messages for clarity

📂 **Repo at the end of Week 2:**

- More reliable blocking of unsafe queries
- Improved testing and demo examples
- Repo structured with professional history (tags for each week)

---

## 🚀 Next (Planned Week 3)

- Add configurable filters (from JSON/YAML instead of hardcoded list)
- Add logging to keep track of blocked queries
- Prepare the SDK for packaging (`pip install nasp-sdk`)

# NASP SDK — Week 3

## Week 3 deliverables

- Input gate with **JailbreakDetector** (roleplay/system override rules).
- Contextual intent detection (cluster patterns for bomb/hacking etc).
- Output gate with **PII redaction** + **profanity sanitization**.
- Full pipeline: Input → LLM → Output with metrics.
- Updated tests & demo.

## Run

- Run demo:
  ```bash
  python demo.py
  ```
