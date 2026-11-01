import string
import sys


def check_password_strength(password: str) -> dict:
    """Evaluates the strength of a given password based on defensive security criteria.

    Complexity: O(n) linear scan using Pythonic C-optimized built-ins.
    """
    # 1. Length Verification (Immediate fail if under 8 characters)
    length = len(password)
    if length < 8:
        return {
            "strength": "WEAK",
            "score": 0,
            "passed_length": False,
            "has_upper": any(c.isupper() for c in password),
            "has_lower": any(c.islower() for c in password),
            "has_digit": any(c.isdigit() for c in password),
            "has_symbol": any(c in string.punctuation for c in password),
            "feedback": "Password must be at least 8 characters long."
        }

    # 2. Pattern & Variety Recognition (Short-circuit Pythonic execution)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    # Calculate criteria score (Max score = 5)
    criteria_met = [has_upper, has_lower, has_digit, has_symbol]
    score = sum(criteria_met)

    # Bonus point for length >= 12
    if length >= 12:
        score += 1

    # 3. Risk Classification
    if score >= 4:
        strength = "STRONG"
        feedback = "Password meets high defensive security standards."
    elif score == 3:
        strength = "MEDIUM"
        feedback = "Password is moderate. Consider adding symbols or increasing length."
    else:
        strength = "WEAK"
        feedback = "Password lacks character variety (requires uppercase, numbers, and symbols)."

    return {
        "strength": strength,
        "score": score,
        "length": length,
        "passed_length": True,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "feedback": feedback
    }


def display_report(result: dict) -> None:
    """Displays a clean, professional security report in the console."""
    print("\n" + "=" * 45)
    print("      DECODELABS SECURITY ANALYST REPORT     ")
    print("=" * 45)
    print(f" Password Length  : {result.get('length', 0)} chars")
    print(f" Length Criteria  : {'[PASS]' if result['passed_length'] else '[FAIL]'}")
    print(f" Uppercase Letter : {'[YES]' if result['has_upper'] else '[NO]'}")
    print(f" Lowercase Letter : {'[YES]' if result['has_lower'] else '[NO]'}")
    print(f" Numeric Digit    : {'[YES]' if result['has_digit'] else '[NO]'}")
    print(f" Special Symbol   : {'[YES]' if result['has_symbol'] else '[NO]'}")
    print("-" * 45)
    print(f" CLASSIFICATION   : {result['strength']}")
    print(f" REMEDIATION      : {result['feedback']}")
    print("=" * 45 + "\n")


def main():
    """Interactive command-line gatekeeper module."""
    print("=============================================")
    print("  DecodeLabs Industrial Kit - Project 1")
    print("  Module: Password Strength Checker")
    print("=============================================")

    try:
        user_password = input("\nEnter password to evaluate: ")
        if not user_password:
            print("Error: Password input cannot be empty.")
            sys.exit(1)

        result = check_password_strength(user_password)
        display_report(result)

    except KeyboardInterrupt:
        print("\n[!] Operations halted by user.")


if __name__ == "__main__":
    main()