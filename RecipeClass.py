class Recipe():
    def __init__(self,id,ingredientes,tags = [],recipe = ""):
        self._ID = id
        self._Ingredients = ingredientes
        self._Tags = tags   
        self._recipe = recipe
    def __str__ (self):
        return self._ID
    def __repr__ (self):
        return self._ID
    def reqingredients (self, amount):
        d = {}
        for k,v in self._Ingredients.items():
            d[k]=amount*v
        return d
    def steps (self):
        return self._recipe
