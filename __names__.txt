__names__
=========
if __name__ == '__main__': function()
----------------------
1. is a variable; his value depend on how script is run
-------------------------------------------------------
if script is run as current file: __name__ == '__main__'
if script is run as module (imported in current file): __name__ == name of module

2. is a scope - namespace
-------------------------
when a script is run as current file: a scope/namespace is created with __name__: '__main__'
when a script is run as a module: another scope/namespace is created with __name__: name of module

Explanations:
-------------

if __name__ == 'main': tell a module not to be executed directly when is imported; code will be executed when you want.

With: if __name__ == '__main__' run the code when is a primary module or when intentioally call it from another script.

For package, the same effect can be achived by including a __main__.py module, the content of which will be executed when the module is runt with -m.

It allow the module and its functions and classes to be imported without running the main function and also allow the module and its function and classes to be called when running from a different module.

For package, the same effect can be achived by including a __main__.py module, the content of which will be executed when the module is runt with -m.

Examples:
---------

1. CASE 1

We have two file: program.py and module.py.
    module.py - code:
        def a_function_of_a_module():
            """A function of a module program."""
            print("1. __name__ in module.py became: ", __name__)  # __name__ =  __main__
            print("2. __Another task to be done")
        a_function_of_a_module()

    program.py code:
        import module
        def a_function_of_a_program():
            """A function of a program."""
            print("\n1. __name__ in program.py became: ", __name__)  # __name__ = __main__
        a_function_of_a_program()
When run module.py as a program result is as we expect.
When run program.py result is a bit odd. The module is imported and executed entirely. Normaly we should specify what function or class to be run, like:
module.methods() ...


2. CASE 2

Let's create another files: module1.py
    module1.py code:
        def a_function_of_a_module():
            """A function of a module program."""
            print("1. __name__ in module1.py became: ", __name__)  # __name__ =  __main__
            print("2. Another task to be done")
        if __name__ == '__main__':
            a_function_of_a_module()
We add: if __name__ == '__main__': 
            a_function_of_a_module() # run the function.

    program1.py
        import module1
        def a_function_of_a_program():
            """A function of a program."""
            print("\n1. __name__ in program1.py became: ", __name__)  # __name__ = __main__
        a_function_of_a_program()
The only difference betwen program.py and program1.py is first line: module is replaced with module1, where we add if __name__ == '__main__': ...

When run module.py as a program result is as we expect.
The code in program1.py will have the expected result. We import function without runing code. Code will be runned when we decide. To run code: module1.method() ...

1. Program work without: if __name__ == '__main__':
2. Program work and is controlled better with: if __name__ == '__main__' and 
3. Program work the best with next code: 
        
        def a_function():
            codes
        def main():
            codes 
        if __name__ == '__main__':
            main()

