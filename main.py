def greet_user(name: str) -> str:
    return f"Hello, Welcome to Demo Lab 2."

def main():
    print("=== Demo Lab 2 GitHub ===")
    try:
        user_name = input("Enter your name: ").strip()
        if not user_name:
            raise ValueError("Name cannot be empty.")
        print(greet_user(user_name))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
