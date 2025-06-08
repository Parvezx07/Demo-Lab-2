

def greet_user(name: str) -> str:
    return f"Hello, {name}! Welcome to the upgraded Demo Lab."

def main():
    print("=== Demo Lab GitHub Actions Test ===")
    try:
        user_name = input("Enter your name: ").strip()
        if not user_name:
            raise ValueError("Name cannot be empty.")
        print(greet_user(user_name))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
