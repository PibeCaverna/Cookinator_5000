#-----------------------Dependencies--------------------------#
from RecipeClass import Recipe
#-----------------------Fonctonarium--------------------------#
def strtobool (cosa):
    '''takes a string as an input and returns it as a bool'''
    if cosa == "True" or "true": Cosa = True
    elif cosa == "False" or "false": Cosa = False
    else cosa = "Error: string does't relate to a bool"
    return cosa
def rmvunvrcp (inventory,recipes):
    '''removes all recipes that cannot be done with the ingredients available'''
    for r in recipes:
        av = False
        for k,v in recipes.reqingrediens(1).items():
            for q,u in inventory.items():
                if q == k and u > v: av = True
            if not av: recipes.popitems(k,v)
    return recipes

