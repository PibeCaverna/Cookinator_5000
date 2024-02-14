#-----------------------------------Dependencies--------------------------------------#
from IngredientClass import Ingredient
from RecipeClass import Recipe
import FileHandlers as fh
import random as rd
#-----------------------------------Fonctonarium--------------------------------------#
def strtobool (cosa):
    '''takes a string as an input and returns it as a bool'''
    if cosa == "True" or "true": cosa = True
    elif cosa == "False" or "false": cosa = False
    else: cosa = "Error: string does't relate to a bool"
    return cosa
def rmvunvrcp (inventory,recipes):
    '''removes all recipes that cannot be done with the ingredients available'''
    for r in recipes:
        av = False
        for k,v in r.reqingredients(1).items():
            for q,u in inventory.items():
                if q == k and u > v: av = True
            if not av: recipes.remove(r)
    return recipes
def addrcp (recipes,ID,Ing,tags = [],recipe = ""):
    rcptadd = Recipe (ID,Ing,tags,recipe)
    recipes.append(rcptadd)
    return recipes
def addref (reference,ID,units,Dcook,Ising,Tags = []):
    reftadd = Ingredient(ID,units,Dcook,Ising,Tags)
    reference.add(reftadd)
    return reference
def changeinv(inventory,changes):
    '''changes the inventory by adding, removing or modifiying the key value pairs from the changes dictionary'''
    for k,v in changes.items():
        if k in inventory.values(): inventory[k] += v
        else: inventory[k] = v
        if inventory[k] <= 0: inventory.pop(k)
def randrcp(recipes,inventory,eaters):
    chosen = False
    while not chosen:
        rcp = recipes[rd.randint(0,len(recipes)-1)]
        can = True
        for k,v in rcp.reqingredients(eaters):
            if not(k in inventory.keys()) or not(inventory[k]< v): can = False
        if can: chosen = True
    changeinv(Inventory,rcp.reqingredients(-eaters))
    return rcp
def makecfg(cfg,lang,path):
    cfg["Language"] = lang
    cfg["Path"] = path
    fh.savecfg(cfg)
    return cfg
def showrecipes(rcps):
    '''Prints all available recipes in a list '''
    for i in rcps:
        print(i)
    return




