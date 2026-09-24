# Simple QA Project

A small project that shows what quality assurance (QA) is by doing it:
write some code, write tests that check it, and run them to prove it works.

## What is Quality Assurance?

Quality assurance is the practice of making sure software does what it is
supposed to do, and keeps doing it as the code changes. Instead of hoping
the code works, you check it in a planned, repeatable way.

## How this project relates to QA

| QA idea | Where you see it in this project |
|---------|----------------------------------|
| The code under test | `validators.py` has three functions that check user input |
| Unit tests | `test_validators.py` has one test per scenario |
| Happy path (normal input) | `test_valid_email`, `test_strong_password`, `test_valid_ages` |
| Negative tests (bad input) | `test_missing_at_symbol`, `test_too_short`, `test_out_of_range` |
| Edge cases | Ages `0`, `120`, `-1`, `121`, and non-numbers like `True` or `"25"` |
| Automation and reporting | `demo.py` runs everything and prints `PASS`/`FAIL` and a final QA result |
| Regression checking | Change the code, re-run the tests, and see if anything broke |

## Files

| File | What it does |
|------|--------------|
| `validators.py` | The code being tested (email, password and age checks) |
| `test_validators.py` | The unit tests |
| `demo.py` | Runs quick manual checks, then all the tests, and prints a QA result |

## How to run

You need Python 3.8 or newer. No extra installs.

Run the demo:

```
python demo.py
```

Run only the unit tests:

```
python -m unittest -v
```

A healthy run ends with:

```
QA RESULT: ALL GOOD
```
Good habit: for every function, write at least one normal test, one bad
input test, and one edge case test.
