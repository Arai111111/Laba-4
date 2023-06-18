class Obj:
    def __init__(self, softness, material, color): 
        self._softness = softness
        self._material = material
        self._color = color

    def get_softness(self):
        return self._softness

    def get_material(self):
        return self._material

    def get_color(self):
        return self._color


    def set_softness(self, softness):
        self._softness = softness

    def set_material(self, material):
        self._material = material

    def set_color(self, color):
        self._color = color

cube = Obj("soft", "plastic", "red")
print(cube.get_softness())
print(cube.get_material())
print(cube.get_color())
cube.set_softness("hard")
cube.set_material("metal")
cube.set_color("blue")
print(cube.get_softness())
print(cube.get_material())
print(cube.get_color())
