class Ingredient():
    def __init__(self,id,units,Dcoock,Ising,Tags = []):
        self._ID = id
        self._Units = units
        self._Dcoock = Dcoock
        self._Ing = Ising
        self._Tags = Tags
    def __str__ (self):
        return self._ID
    def __repr__(self):
        return self._ID+"("+self._Units+")"
    def Units (self):
        return self._Units
    def Dcoock (self):
        return self._Dcoock
    def Ising (self):
        return self._Ing
    def Tags (self):
        return tuple(self._Tags)
    def Tagadd (self,tag):
        if not tag in self._Tags:
            self._Tags.append(tag)
        else: return "error"
    def Tagout (self,tag):
        c = 0
        while tag in self._Tags:
            if self.Tags()[c] == tag: self._Tags.pop(c)
            else: c+=1
       
