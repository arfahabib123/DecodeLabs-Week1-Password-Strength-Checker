
import unittest

from src.main import check_password_strength


class TestPasswordStrengthChecker(unittest.TestCase):

    def test_weak_password(self):
        result = check_password_strength("abc")
        self.assertEqual(result["strength"], "WEAK")

    def test_medium_password(self):
        result = check_password_strength("Hello123")
        self.assertEqual(result["strength"], "MEDIUM")

    def test_strong_password(self):
        result = check_password_strength("Secure@Pass123")
        self.assertEqual(result["strength"], "STRONG")

    def test_empty_password(self):
        result = check_password_strength("")
        self.assertEqual(result["strength"], "WEAK")

    def test_uppercase_detection(self):
        result = check_password_strength("HELLO123")
        self.assertTrue(result["has_upper"])

    def test_lowercase_detection(self):
        result = check_password_strength("hello123")
        self.assertTrue(result["has_lower"])

    def test_digit_detection(self):
        result = check_password_strength("Hello123")
        self.assertTrue(result["has_digit"])

    def test_symbol_detection(self):
        result = check_password_strength("Hello@123")
        self.assertTrue(result["has_symbol"])

    def test_long_password_bonus(self):
        result = check_password_strength("Hello@123456")
        self.assertEqual(result["score"], 5)

    def test_password_length(self):
        result = check_password_strength("Hello123")
        self.assertTrue(result["passed_length"])
        self.assertEqual(result["length"], 8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
