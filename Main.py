
#--------------------------------------Dependencies-----------------------------------#
from  IngredientClass import Ingredient 
from RecipeClass import Recipe  
import FileHandlers as fh
import Fonctonarium as fm
#-------------------------------------------------------------------------------------#
#-----------------------------------------SetUp---------------------------------------#
setup = True
while setup:
    #config loader
    conf = {}
    try: fh.loadcfg(conf)
    except FileNotFoundError:
        setup = True
        l = input("Choose your desired language\n")
        p = input("Choose the path where files will be saved\n")
        fm.makecfg(conf,l,p)
    else: setup = False
    #language loader
    lang = []
    try: fh.loadlang(conf,lang)
    except FileNotFoundError:
        setup = True
        print("File not found, please check your config \n The language in yout config is "+conf["Language"])
        conf["Language"] = input("Please write your desired language\n")
        fh.savecfg(conf)
    else: setup = False
    #inventory loader
    print(lang[0])
    inv = {}
    try: fh.loadinv(inv,conf["Path"])
    except FileNotFoundError:
        setup = True
        try: fh.saveinv({},conf["Path"])
        except FileNotFoundError:
            print(lang[1]+lang[2][:-1]+conf["Path"])
            conf["Path"] = input(lang[3])
            fh.savecfg(conf)
        else:setup = False
    #reference loader
    print(lang[4])
    ref = set()
    try: loadref(ref,inv,conf["Path"])
    except FileNotFoundError: 
        setup = True
        fh.saveref(ref,conf["Path"])
    else: setup = False
    #recipe loader
    print(lang[5])
    rcps = []
    try: fh.loadrcp (rcps,inv,conf["Path"])
    except FileNotFoundError:
        setup = True
        fh.savercp(rcps,conf["Path"])
    else:setup = False
