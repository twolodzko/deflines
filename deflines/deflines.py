import ast
from typing import List, NamedTuple


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.unique_lines = set()
        self.cc = 1

    def visit(self, node):
        self.line_counter(node)
        self.cc_counter(node)
        super().visit(node)

    def line_counter(self, node):
        """
        Count lines containing code
        """
        try:
            self.unique_lines.add(node.lineno)
        except AttributeError:
            pass

    def cc_counter(self, node):
        """
        Calculate cyclomatic complexity

        Same as radon:
        * https://radon.readthedocs.io/en/latest/intro.html
        * https://github.com/rubik/radon/blob/master/radon/visitors.py
        """

        if isinstance(node, (ast.If, ast.IfExp, ast.And, ast.Or, ast.ExceptHandler, ast.With, ast.Assert)):
            self.cc += 1
        elif isinstance(node, (ast.For, ast.AsyncFor, ast.While)):
            self.cc += bool(node.orelse) + 1
        elif isinstance(node, ast.Try):
            self.cc += bool(node.orelse)
        elif isinstance(node, ast.comprehension):
            self.cc += len(node.ifs) + 1

    @property
    def lines(self):
        return len(self.unique_lines)


class AnalysisResult(NamedTuple):
    path: str
    name: str
    lineno: int
    col_offset: int
    lines: int
    cc: int

    def __str__(self) -> str:
        return f"{self.lines:4d} {self.cc:2d} {self.path}:{self.lineno}:{self.col_offset} {self.name}"


class ModuleAnalyzer(ast.NodeVisitor):
    def __init__(self, path):
        self.path = path
        self.results: List[AnalysisResult] = []

    @classmethod
    def process(cls, path) -> List[AnalysisResult]:
        analyzer = cls(path)

        with open(analyzer.path, "r") as file:
            code = file.read()
        tree = ast.parse(code)

        analyzer.visit(tree)
        return analyzer.results

    def visit(self, node):
        if isinstance(node, ast.FunctionDef):
            analyzer = Analyzer()
            analyzer.visit(node)
            self.results.append(
                AnalysisResult(
                    self.path,
                    node.name,
                    node.lineno,
                    node.col_offset,
                    analyzer.lines,
                    analyzer.cc,
                ),
            )
        else:
            super().visit(node)
