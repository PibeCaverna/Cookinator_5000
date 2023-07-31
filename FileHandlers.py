#----------------------------------------------------------------------------------Dependencies---------------------------------------------------------------------------------------#
from IngredientClass import Ingredient
from RecipeClass import Recipe

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def loadinv (inventory,path):
    '''this function loads the inventory from ~/path/Inventory.txt into a dictionary with the form ID,Quantity'''
    path += "Inventory.txt"
    Archie = open(path,mode = "r",encoding = "utf-8")
    for line in Archie:
        tent = line.split(";")
        inventory[tent[0]]=int(tent[1])
    Archie.close()
    return inventory
def saveinv (inventory,path):
    '''this function saves the inventory in ~/path/Inventory.txt'''
    path+="Inventory.txt"
    Archie = open(path,mode = "w",encoding = "utf-8")
    for k,v in inventory.items():
        Archie.writeline(k+";"+str(v))
    Archie.close()
def loadref (reference,path):


