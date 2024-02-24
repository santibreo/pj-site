:draft: false
:date: 19-08-2023

#########################
Mocking modules in Python
#########################

When writing unit tests in Python there is an issue that pops up quite often: *You are testing something that depends on many of libraries that are not available on your development environment*. Normally you do not need that libraries functionality, you are going to mock objects imported from those libraries and assert that they are properly called.

I have recently come up with a solution for this problem that ensures that everything imported from a user-defined list of libraries (independent from the import level) is a ``MagicMock``, lets see how this can be achieved:

.. literalinclude:: ../_code/module_mocking.py
   :language: python
   :linenos:

Lets understand what is going on. Until line 85 we are monkey-patching the Python import machinery so every time it looks for a module that comes from a ``MockedModule`` it is imported also as a ``MockedModule``. When you import something in Python what Python does is:

1. Look for its fully-qualified name in ``sys.modules`` (it is here if it has been imported before). If it is found then **import finishes here**. If not found...
2. The ``find_spec`` method of every ``MetaPathFinder`` in ``sys.meta_path`` list is called. What you are doing is registering a new ``MetaPathFinder`` so, **if a module or class is being imported from a** ``MockModule`` **then** ``find_spec`` **returns a new** ``MockModule`` **spec**.

   If all ``find_spec`` methods return ``None`` then ``ImportError`` is raised, but if anyone has returned a ``ModuleSpec`` then it is loaded.
3. The way a module is loaded is described by `this code chunk <https://docs.python.org/3/reference/import.html#loading>`_. What is happening in our code is we are abusing that the ``MetaPathFinder`` has already registered the module in ``sys.modules`` so we are just getting it.

Rest of the code is just the ``MockModule`` and ``MockModuleLoader`` definition which is quite straight forward.

After executing this code, every of the following statements is perfectly fine:


.. code-block:: python

   from unavailable_lib.external_apis import ExternalApiClient
   from unavailable_lib.external_databases import ExternalDatabaseHandler
   ...

Everything imported this way is going to be a ``MagicMock``, so you can check and assert calls as you would normally do.


.. note::
    If you are a `pytest <https://docs.pytest.org/en/latest/>`_ user as you should, adding this code to the ``conftest.py`` file might solve many problems


**********
References
**********

- Python docs: `The import statement <https://docs.python.org/3/reference/simple_stmts.html#import>`_
- Python docs: `The import system <https://docs.python.org/3/reference/import.html#importsystem>`_
