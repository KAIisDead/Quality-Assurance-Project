# Simple QA Project

A tiny project that shows the basics of quality assurance: write code,
write tests for it, and run them to prove the code works.

## Files

| File | What it does |
|------|--------------|
| `validators.py` | The code being tested (email, password and age checks) |
| `test_validators.py` | Unit tests for `validators.py` |
| `demo.py` | Runs quick checks + all tests and prints a QA result |


## How to run

Run the demo:

```
python demo.py
```

Run only the unit tests:

```
python -m unittest -v
```

## Expected result

You should see `PASS` for every manual check, `ok` for every test,
and finally:

```
QA RESULT: ALL GOOD
```
    self.assertTrue(is_valid_email("me@site.co.za"))
```
