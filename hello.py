def say_hello(name: str) -> str:
    """Return a greeting message to students in the IDS class."""
    Welcm_msg= f"Hello, {name}, welcome to Data Engineering Systems (IDS 706)!" # welome message
    return Welcm_msg

def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    print(say_hello("Prof. Yu"))
    print("2 + 3 =", add(2, 3))
