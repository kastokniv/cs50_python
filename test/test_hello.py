from hello1 import hello


def test_default():
    hello("Dev") == "hello, Dev"


def test_argument():
    for name in ["Hermoine", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
