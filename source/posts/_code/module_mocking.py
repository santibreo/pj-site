# Stdlib
import sys
import importlib
from unittest import mock
from types import ModuleType
from typing import Optional, Sequence
from importlib.machinery import ModuleSpec
from importlib.abc import MetaPathFinder, Loader


class MockModule(mock.MagicMock):
    """Mocks a module so anything that is imported from it is also a
    :class:`MockModule`
    `"""

    class MockModuleLoader(Loader):
        """Dummy loader to be used when defining :class:`MockModule` modules"""

        def create_module(self, spec: ModuleSpec):
            return sys.modules[spec.name]

        def exec_module(self, module: ModuleType):
            pass


    def __init__(self, name: str = '', prefix: str='', *args, **kwargs):
        """Creates an object that you can import things from.

        Args:
            name: Name of the module.
            prefix: Fully-qualified name prefix, what is before ``name`` removing
                last dot ('.')
        """
        name = name if name else self.__class__.__name__
        kwargs['name'] = name
        super().__init__(ModuleType(name), *args, **kwargs)
        self.name = name
        self.__all__ = []
        self.__path__ = []
        self.__name__ = self.get_fully_qualified_name(name, prefix)
        self.__loader__ = self.MockModuleLoader()
        self.__spec__ = ModuleSpec(
            name = self.__name__,
            loader = self.__loader__,
            is_package = True
        )
        sys.modules[self.__name__] = self
        globals()[self.__name__] = importlib.import_module(self.__name__)

    def __getattr__(self, name: str):
        if name.startswith('_'):
            raise AttributeError(f"MockModule has no attribute {name}")
        self.__all__.append(name)
        child_module = sys.modules.get(self.get_fully_qualified_name(name, self.__name__))
        if child_module is None:
            child_module = MockModule(name=name, prefix="{self.__name__}")
        return child_module

    @staticmethod
    def get_fully_qualified_name(mod_name: str, prefix: str = '') -> str:
        """Built fully qualified either for top or lower level packages and
        modules"""
        suffix = ('.' if prefix else '') + mod_name
        return f"{prefix}{suffix}"


class MockModuleMetaPathFinder(MetaPathFinder):
    """Finder for :class:`MockModule` so those can be imported"""

    def find_spec(
        self,
        fullname: str,
        path: Optional[Sequence[str]],
        target: Optional[ModuleType] = None,
    ) -> Optional[ModuleSpec]:
        *prefixes, mod_name = fullname.split('.')
        mod_parent = sys.modules.get('.'.join(prefixes))
        if isinstance(mod_parent, MockModule):
            return getattr(mod_parent, mod_name).__spec__
        return None


# Set the hook so MOCKED_MODULES return mocks for everything requested
sys.meta_path.insert(0, MockModuleMetaPathFinder())

# -----------------------------------------------------------------------------
# Moodules that would provide MagicMocks instead of in-use Python objects
MOCKED_PACKAGES = [
    'unavailable_lib',
]

for pkg_name in MOCKED_PACKAGES:
    sys.modules[pkg_name] = MockModule(pkg_name)
