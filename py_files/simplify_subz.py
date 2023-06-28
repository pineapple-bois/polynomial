import ast
import operator

class Simplify:
    operators = {ast.Mult: operator.mul,
                 ast.Div: operator.truediv,
                 ast.Add: operator.add,
                 ast.Sub: operator.sub}

    class Transformer(ast.NodeTransformer):
        def visit_BinOp(self, node):
            self.generic_visit(node)

            if isinstance(node.op, (ast.Mult, ast.Div, ast.Add, ast.Sub)):
                if isinstance(node.left, ast.Constant) and isinstance(node.right, ast.Constant):
                    return ast.copy_location(ast.Constant(Simplify.operators[type(node.op)]
                                                          (node.left.n, node.right.n)), node)

            return node

    def __new__(cls, expression):
        expr = ast.parse(expression, mode='eval').body
        expr = cls.Transformer().visit(expr)
        return ast.unparse(expr)
