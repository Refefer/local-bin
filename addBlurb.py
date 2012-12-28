#!/usr/bin/python
import sys
import ast
import re

get_func      = lambda m: m.body[0]
get_func_name = lambda m: get_func(m).name
get_args      = lambda m: get_func(m).args
get_arg_names = lambda m: [a.id for a in get_args(m).args]
get_defaults  = lambda m: [a.id for a in get_args(m).defaults]

def get_arg_kwargs(m):
    args_obj = get_args(m)
    args = get_arg_names(m)
    return args
    kwargs = args[len(args_obj.defaults):]
    del args[len(kwargs):]

BLACKLIST_ARGS = ('self', 'cls')

def parse_definition(function):
    indention = re.match(r'^(\s*)', function).group()
    m = ast.parse(function.lstrip())
    name = get_func_name(m)
    args = get_arg_kwargs(m)
    new_indent = "%s    " % indention 
    doc_block = [ '%s"""' % new_indent] 
    for arg in args:
        if arg in BLACKLIST_ARGS: continue
        doc_block.append(new_indent)
        doc_block.append('%s@param %s: ' % (new_indent, arg))
        doc_block.append('%s@type  %s: ' % (new_indent, arg))

    doc_block.append('')
    doc_block.append("%s@return: " % new_indent)
    doc_block.append("%s@rtype: " % new_indent)

    doc_block.append('%s"""' % new_indent)
    return '\n'.join(doc_block)

if __name__ == '__main__':
    orig = sys.stdin.read()
    function =  orig + ' pass\n'
    sys.stdout.write(orig)
    sys.stdout.write(parse_definition(function))
