"""Automatic Google-style docstring injector for Python files."""

import ast
import sys
import os


class DocstringInjector(ast.NodeVisitor):
    """Find functions and classes without docstrings."""
    
    def __init__(self):
        self.missing = []
    
    def visit_FunctionDef(self, node):
        if not ast.get_docstring(node):
            self.missing.append((node.lineno, node.name, 'func', node))
        self.generic_visit(node)
    
    def visit_ClassDef(self, node):
        if not ast.get_docstring(node):
            self.missing.append((node.lineno, node.name, 'class', node))
        self.generic_visit(node)


def get_indent(line):
    """Get indentation of a line."""
    return line[:len(line) - len(line.lstrip())]


def generate_func_docstring(node, indent):
    """Generate function docstring."""
    args = [arg.arg for arg in node.args.args]
    args_str = ", ".join(args) if args else ""
    
    doc = f'{indent}"""\n'
    doc += f'{indent}{node.name}({args_str}).\n'
    doc += f'{indent}\n'
    doc += f'{indent}[Brief description].\n'
    
    if args:
        doc += f'{indent}\n'
        doc += f'{indent}Args:\n'
        for arg in args:
            doc += f'{indent}    {arg} ([type]): [Description].\n'
    
    doc += f'{indent}\n'
    doc += f'{indent}Returns:\n'
    doc += f'{indent}    [type]: [Description].\n'
    doc += f'{indent}"""\n'
    
    return doc


def generate_class_docstring(node, indent):
    """Generate class docstring."""
    doc = f'{indent}"""\n'
    doc += f'{indent}{node.name}.\n'
    doc += f'{indent}\n'
    doc += f'{indent}[Brief description].\n'
    doc += f'{indent}\n'
    doc += f'{indent}Attributes:\n'
    doc += f'{indent}    [attr] ([type]): [Description].\n'
    doc += f'{indent}"""\n'
    
    return doc


def process_file(filepath, output=None):
    """Process Python file and inject docstrings."""
    
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return
    
    if not filepath.endswith('.py'):
        print("Error: Must be a .py file")
        return
    
    # Read file
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Parse and find missing docstrings
    try:
        tree = ast.parse(''.join(lines))
    except SyntaxError as e:
        print(f"Syntax error: {e}")
        return
    
    visitor = DocstringInjector()
    visitor.visit(tree)
    
    # Sort by line number (reverse) to insert from bottom up
    missing = sorted(visitor.missing, key=lambda x: x[0], reverse=True)
    
    # Insert docstrings
    added = {'func': 0, 'class': 0}
    
    for line_num, name, node_type, node in missing:
        indent = get_indent(lines[line_num - 1])
        
        if node_type == 'class':
            doc = generate_class_docstring(node, indent)
            added['class'] += 1
        else:
            doc = generate_func_docstring(node, indent)
            added['func'] += 1
        
        lines.insert(line_num, doc)
    
    # Save result
    save_path = output or filepath
    with open(save_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"✓ Processed: {filepath}")
    print(f"  Functions: {added['func']}")
    print(f"  Classes: {added['class']}")
    print(f"✓ Saved to: {save_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task5.py <file.py> [output.py]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    process_file(input_file, output_file)
