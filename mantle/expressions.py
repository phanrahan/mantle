import textwrap
import inspect
import ast
import astor


class Source:
    def __init__(self):
        self._source = ""

    def add_line(self, line, tab=""):
        self._source += tab + line + "\n"

    def add_lines(self, lines, tab=""):
        for line in lines:
            self.add_line(line, tab)


class ExprVisitor(ast.NodeVisitor):
    def __init__(self):
        super().__init__()
        self.source = Source()
        self.source.add_line("from magma import *")
        self.source.add_line("from mantle import *")
        self.__unique_id = -1
        self.args = []
        self.width_table = {}
        self.name = None

    def unique_id(self):
        self.__unique_id += 1
        return "inst{}".format(self.__unique_id)

    def visit_FunctionDef(self, node):
        args = []
        for arg in node.args.args:
            self.args.append(arg.arg)
            args.append("\"" + arg.arg + "\"")
            typ = arg.annotation
            args.append(astor.to_source(typ).rstrip())
            if isinstance(typ, ast.Call):
                assert typ.func.id in ["In", "Out"]
                assert len(typ.args) == 1
                if isinstance(typ.args[0], ast.Name) and typ.args[0].id == "Bit":
                    self.width_table[arg.arg] = 1
                elif isinstance(typ.args[0], ast.Call) and typ.args[0].func.id == "Array":
                    self.width_table[arg.arg] = typ.args[0].args[0].n
                else:
                    raise NotImplementedError()
            else:
                raise NotImplementedError(ast.dump(typ))
        self.name = node.name
        self.source.add_line(
                "{name} = DefineCircuit(\"{name}\", {args})".format(
                    name=node.name, args=", ".join(args)))
        for s in node.body:
            self.visit(s)
        self.source.add_line("EndCircuit()")

    def get_width(self, node):
        if isinstance(node, ast.Name):
            return self.width_table[node.id]
        raise NotImplementedError()

    def visit_Name(self, node):
        if node.id in self.args:
            return "{}.{}".format(self.name, node.id)
        raise NotImplementedError()

    def visit_Assign(self, node):
        value = self.visit(node.value)
        if len(node.targets) > 1:
            raise NotImplementedError(astor.to_source(node).rstrip())
        target = self.visit(node.targets[0])
        self.source.add_line("wire({}, {})".format(target, value))

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        left_width = self.get_width(node.left)
        right_width = self.get_width(node.right)
        if left_width != right_width: 
            raise NotImplementedError(
                "Mismatch widths not supported yet {}".format(ast.dump(node)))
        if isinstance(node.op, ast.Add):
            inst_id = self.unique_id()
            self.source.add_line("{} = Add({})({}, {})".format(inst_id, left_width, left, right))
            return inst_id
        raise NotImplementedError(ast.dump(node))


def circuit(fn):
    tree = ast.parse(textwrap.dedent(inspect.getsource(fn)))
    visitor = ExprVisitor()
    visitor.visit(tree)
    print(visitor.source._source)
    exec(visitor.source._source)
    return eval(visitor.name)
