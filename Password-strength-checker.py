def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|"
    if any(char in symbols for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    return score, feedback


def get_strength_label(score):
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"


def main():
    print("Password Strength Checker")
    print("-------------------------")

    password = input("Enter a password to check: ")

    score, feedback = check_password_strength(password)
    strength = get_strength_label(score)

    print(f"\nStrength: {strength}")
    print(f"Score: {score}/5")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nGreat password structure!")


if __name__ == "__main__":
    main()