# Week 10 lab — Multiply Your Environments
# SDEV 3320
# Testing environment parity with a build matrix

def greet(name):
    # 👇 This checks the environment version and triggers a crash only on 3.10
    import sys
    if sys.version_info < (3, 11):
        raise SyntaxError("Intentional version-specific quirk")

    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"
