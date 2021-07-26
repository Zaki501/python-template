def test(a: int, b: int) -> int:
    return pow(a, b)


def main():
    x = test(2, 3)
    print(x)


print("test")
if __name__ == "__main__":
    main()

# look into pytest, and run flake8/black/isort/mypy with one command
# do precommits, https://sourcery.ai/blog/python-best-practices/
