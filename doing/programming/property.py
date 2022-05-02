class numproperty(property):
    def __init__(self, fget):
        self._attr_name = "_" + fget.__name__
        self._comp_name = fget.__qualname__
        super().__init__(fget=fget, fset=self.fset)

    def fset(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self._comp_name} value must be a number and not '{value}'")
        else:
            setattr(obj, self._attr_name, value)
class A:
    def __init__(self):
        self._a = "hola"
    @numproperty
    def a(self):
        return self._a
a = A()
a.a = 3
a.a
a.a = "perro"
