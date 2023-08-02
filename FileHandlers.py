#--------------------------------------Dependencies-----------------------------------#
from IngredientClass import Ingredient
from RecipeClass import Recipe
import Fonctonarium as Fm
#=====================================================================================#
def loadinv (inventory,path):
    '''this function loads the inventory from ~/path/Inventory.txt into a dictionary with the form ID,Quantity'''
    path += "Inventory.txt"
    Archie = open(path,mode = "r",encoding = "utf-8")
    for line in Archie:
        tent = line.split(";")
        inventory[tent[0]]=int(tent[1][:-1])
    Archie.close()
    return inventory
def saveinv (inventory,path):
    '''this function saves the inventory in ~/path/Inventory.txt'''
    path += "Inventory.txt"
    Archie = open(path,mode = "w",encoding = "utf-8")
    for k,v in inventory.items():
        Archie.write(k+";"+str(v)+"\n")
    Archie.close()
    return inventory
#-------------------------------------------------------------------------------------#
def loadref (reference,inventory,path):
    '''loads references into a set ready to use'''
    path += "IngredientReferences.txt"
    Archie = open(path,mode = "r",encoding = "utf-8")
    for line in Archie:
        tent = line.split(";")
        if tent[0] in Inventory.keys():
            "this is so that we don't load references that we won't use, in order to avoid too much lag"
            tent[2] = (Fm.strtobool(tent[2]))
            tent[3] = (Fm.strtobool(tent[3]))
            reference.add(Ingredient(tent[0],tent[1],tent[2],tent[3],tent[4].split(",")))
            "note that the tags are saved without the [] from the list"
    Archie.close()
    return reference
def saveref (reference,path):
    '''saves references into a file'''
    path += "IngredientReferences.txt"
    Archie = open(path,mode = "w",encoding = "utf-8")
    esta = False
    for cosa in reference:
        while not esta:
            if Archie.readline().split(";")[0] == str(cosa): esta = True   
        if not esta: Archie.write(str(cosa)+";"+cosa.Units()+str(cosa.Dcook())+";"+str(cosa.Ising())+";"+str(cosa.Tags())[1:-1])
        Archie.seek(0,0)
    return reference
#-------------------------------------------------------------------------------------#
def loadrcp (recipes,inventory,path):
    '''Loads recipes in a list ready to use'''
    path +="Recipes.txt"
    Archie = open(path,mode = "r",encoding = "utf-8")
    for line in Archie: 
        tent = line.split(";")
        tent[2] = tent[2].split(",")
        tent[1] = tent[1].split(",")
        tent [1] = [tent[1][n].split(":") for n in range(len(tent[1]))]
        props  = {tent[1][n][0] : int(tent[1][n][1]) for n in range(len(tent[1]))}
        recipes.append(Recipe(tent[0],props,tent[2],tent[3]))
        Fm.rmvunvrcp(inventory,recipes)
        "removes recipes that cannot be done whith items in inventory"
    Archie.close()    
    return recipes
def savercp (recipes,path):
    '''saves recipes into a file'''
    path += "Recipes.txt"
    Archie = open(path,mode = "w",encoding = "utf-8")
    esta = False
    for cosa in recipes:
        while not esta:
            if Archie.readline().split(";")[0] == str(cosa):esta = True
        if not esta: Archie.write(str(cosa)+";"+str(cosa.reqingredients(1))[1:-1]+";"+str(cosa.Tags())[1:-1],cosa.steps())
#-------------------------------------------------------------------------------------#
def loadcfg (conf):
    Archie = open("Config.txt",mode = "r",encoding = "utf-8")
    for line in Archie:
        q = line.split("=")
        conf[q[0]] = q[1][:-1]
    Archie.close()
    return conf
def savecfg (conf):
    Archie = open("Config.txt",mode = "w",encoding = "utf-8")
    for k,v in conf.items():
        Archie.write(k+"="+v+"\n")
    return "Files saved correctly"
#-------------------------------------------------------------------------------------#
def loadlang(conf,lang):
    path = conf["Language"]+".txt" 
    Archie = open(path, mode = "r", encoding = "utf-8")
    for line in Archie:
        lang.append(line)
    return lang
