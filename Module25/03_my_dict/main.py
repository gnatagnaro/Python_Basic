class MyDict(dict):
    def get(self, key):
        if key not in self:
            return 0
        else:
            return self[key]

    # можно еще так:
    # def get(self, key, default_value=0):
    #     return super().get(key, default_value)


b = MyDict()
b[1] = 123
b[2] = 654
print(b.get(1))
print(b.get(3))
