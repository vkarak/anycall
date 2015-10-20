# anycall
A generic driver for calling any function from a Python module.

## Usage
    $ python anycall.py [modules=<modules>] <op> [op_kwargs]

List available operations

    $ python anycall.py list_ops
    Available operations:
    => list_ops(show_help)

List available operations of a module

    $ python anycall.py modules=example.hello list_ops
    Available operations:
    => list_ops(show_help)
    => greetings(msg)

List the functions of multiple modules

    $ python anycall.py modules=example.hello,re list_ops
    Available operations:
    => _subx(pattern, template)
    => list_ops(show_help)
    => search(pattern, string, flags)
    => finditer(pattern, string, flags)
    => _expand(pattern, match, template)
    => sub(pattern, repl, string, count, flags)
    => split(pattern, string, maxsplit, flags)
    => template(pattern, flags)
    => compile(pattern, flags)
    => purge()
    => greetings(msg)
    => _pickle(p)
    => escape(pattern)
    => subn(pattern, repl, string, count, flags)
    => _compile()
    => findall(pattern, string, flags)
    => match(pattern, string, flags)
    => _compile_repl()

Invoke module's function

    $ python anycall.py modules=example.hello greetings msg=World
    Hello, World!
