import ast

import pytest
from deflines import Analyzer


@pytest.mark.parametrize(
    "code,expected",
    [
        (
            "x = 42",
            1,
        ),
        (
            """
# first comment
x = 42 # second comment

# third comment
            """,
            1,
        ),
        (
            """
def add(x, y):
    # sum of x and y
    z = x + y
    return z
            """,
            3,
        ),
        (
            """
def foo(x, y):
    z = (
        x +
        y
    )
    z = (
        z +
        x +
        # comment
        y
    )
    return z
          """,
            9,
        ),
    ],
)
def test_Analyzer(code, expected):
    tree = ast.parse(code)
    lc = Analyzer()
    lc.visit(tree)
    assert lc.lines == expected


@pytest.mark.parametrize(
    "code,expected",
    [
        (
            """
x = 42
            """,
            1,
        ),
        (
            """
if x == 5:
    x += 2
elif x == 6 and y == 7:
    x += 10
else:
    x = 0
            """,
            4,
        ),
        (
            """
try:
    raise ValueError
except ValueError:
    pass
except RuntimeError:
    pass
else:
    pass
            """,
            4,
        ),
        (
            """
for x in range(10):
    if x > 5:
        print(x)
else:
    print("something else")
            """,
            4,
        ),
        (
            """
[x for x in range(10) if x > 5]
            """,
            3,
        ),
        (
            "x and y or z",
            3,
        ),
        (
            """
while True:
    print("Woohooo!")
            """,
            2,
        ),
    ],
)
def test_Analyzer_cc(code, expected):
    tree = ast.parse(code)
    lc = Analyzer()
    lc.visit(tree)
    assert lc.cc == expected
