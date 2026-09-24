import unittest

from validators import is_valid_email, is_strong_password, is_valid_age


class TestEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("sam@example.com"))

    def test_missing_at_symbol(self):
        self.assertFalse(is_valid_email("samexample.com"))

    def test_missing_dot_in_domain(self):
        self.assertFalse(is_valid_email("sam@example"))

    def test_contains_space(self):
        self.assertFalse(is_valid_email("sam @example.com"))

    def test_not_a_string(self):
        self.assertFalse(is_valid_email(None))
        self.assertFalse(is_valid_email(123))


class TestPassword(unittest.TestCase):
    def test_strong_password(self):
        self.assertTrue(is_strong_password("Passw0rdOK"))

    def test_too_short(self):
        self.assertFalse(is_strong_password("short1A"))

    def test_no_uppercase(self):
        self.assertFalse(is_strong_password("alllowercase1"))

    def test_no_lowercase(self):
        self.assertFalse(is_strong_password("ALLUPPERCASE1"))

    def test_no_digit(self):
        self.assertFalse(is_strong_password("NoDigitsHere"))


class TestAge(unittest.TestCase):
    def test_valid_ages(self):
        for age in (0, 25, 120):
            self.assertTrue(is_valid_age(age))

    def test_out_of_range(self):
        self.assertFalse(is_valid_age(-1))
        self.assertFalse(is_valid_age(121))

    def test_wrong_type(self):
        for bad in ("25", 25.5, True, None):
            self.assertFalse(is_valid_age(bad))


if __name__ == "__main__":
    unittest.main()