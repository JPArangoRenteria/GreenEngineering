from loops import LoopAnalyzer
from recursion import RecursionAnalyzer
import ast

if __name__ == "__main__":
    with open("ex1.py", "r") as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    LoopAnalyzer().visit(tree)
    RecursionAnalyzer().visit(tree)