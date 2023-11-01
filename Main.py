
#--------------------------------------Dependencies-----------------------------------#
from  IngredientClass import Ingredient 
from RecipeClass import Recipe  
import FileHandlers as fh
import Fonctonarium as fm
from os import system, name
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
    # srtipping and splitting the lang items for yes/no (for comparison reasons)
    lang[51] = lang[51].strip()
    lang[51] = lang[51].split()
    lang[52] = lang[52].strip()
    lang[52] = lang[52].split()
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
    try: fh.loadref(ref,inv,conf["Path"])
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
#---------------------------------------------------------------------------------------#
#-----------------------------------------Loop------------------------------------------#
Loop = True
while Loop:
    RCPM = False
    INVM = False
    Plan = False
    #cleaning terminal every time the menu is called#
    if name == 'nt': system('cls')
    else: system('clear')
    #Printing main menu, note that lang 7 to 10 and 22 to 25 are text#
    print(lang[6],lang[7],lang[8],lang[9],lang[10],lang[12],lang[13],lang[14],lang[15],lang[16],lang[17],lang[18],lang[19],lang[20],lang[21],lang[22],lang[23],lang[24],lang[25],lang[6].strip())
    select = input()
    #note that the slicing is used to avoid the "\n"
    #the strings asociated with the diferent menus go from lines 28 to 31 in the language files, and correspond to the ones explained in lines 23 to 26 respectively
    if select == lang[26].strip(): RCPM = True
    elif select == lang[27].strip(): INVM = True
    elif select == lang[28].strip(): Plan = True
    elif select == lang[29].strip(): Loop = False
    
    #Recipe Manager
    #Strings 32 to 56
    if RCPM: print(lang[6],lang[32],lang[33],lang[34],lang[35],lang[36],lang[37],lang[38],lang[39],lang[40],lang[41],lang[42],lang[43],lang[6].strip())
    while RCPM:
        VRCP = False
        select = input()
        if select == lang[44].strip():
            VRCP = True
            print(["Esto", "es", "un", "placeholder"])#print(showrecipes(rcps)) falta armar la función 
        elif select == lang[45].strip():
            rcpname = input(lang[53].strip())
            ingadder = True
            ingtadd = {}
            while ingadder:
                ing = input(lang[48].strip())
                q = int(input(lang[49].strip())) #should add an exeption, to ensure it is a number#
                ingtadd[ing] = q
                if input(lang[50]) in lang[52]: ingadder = False
            tadder = True
            tagtadd = []
            print(lang[54])
            while tadder:
                tadd = input()
                if tadd == lang[31].strip(): tadder = False
                else: tagtadd.append(tadd)
            texto = input(lang[55])
            rcps.append(Recipe(rcpname,ingtadd,tagtadd,texto))
        elif select == lang[46].strip(): RCPM = False
        elif select == lang[31].strip(): RCPM = False
        if VRCP:
            print(lang[48])
            print(lang[30][:-1])
        while VRCP:
            select = input()
            if select in [str(rcps[I]) for I in range(len(rcps))]:
                print("Esto es un placeholder, falta la función")
                #print(fm.detailrcp([[str(I) for I in range(len(rcps))].index(select)]))
            elif select == lang[31].strip(): VRCP = False
            elif select == lang[46].strip():
                VRCP = False
                RCPM = False
    #Inventory manager
    #strings 57 to 78
    if INVM: print(lang[6],lang[56],lang[57],lang[58],lang[59],lang[60],lang[61],lang[62],lang[63],lang[64],lang[65],lang[66],lang[67],lang[68],lang[69],lang[6].strip())
    while INVM:
        select = input()
        if select == lang[46].strip() or select == lang[31].strip(): INVM = False
    



    
