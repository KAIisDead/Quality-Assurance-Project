import sys
import unittest

from validators import is_valid_email, is_strong_password, is_valid_age


def show(label, actual, expected):
    """Print PASS or FAIL for one check and return True if it passed."""
    ok = actual == expected
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: got {actual}, expected {expected}")
    return ok


def main():
    print("=== Quick manual checks ===")
    results = [
        show("email 'sam@example.com'", is_valid_email("sam@example.com"), True),
        show("email 'sam@example'", is_valid_email("sam@example"), False),
        show("password 'Passw0rdOK'", is_strong_password("Passw0rdOK"), True),
        show("password 'weak'", is_strong_password("weak"), False),
        show("age 30", is_valid_age(30), True),
        show("age 200", is_valid_age(200), False),
    ]
    print(f"\n{sum(results)}/{len(results)} manual checks passed\n")

    print("=== Full unit test suite ===")
    suite = unittest.defaultTestLoader.loadTestsFromName("test_validators")
    outcome = unittest.TextTestRunner(verbosity=2).run(suite)

    all_good = all(results) and outcome.wasSuccessful()
    print("\nQA RESULT:", "ALL GOOD" if all_good else "PROBLEMS FOUND")
    sys.exit(0 if all_good else 1)


if __name__ == "__main__":
    main()