"""
Author : salmansyyd


The idea is to swap modules based on a query string and use the similar api functions over the
entire codebase to make the api more consistent.

MainDir(module-inator)
"the root directory"
    SubDir(modules)
    "contains all different modules"
        SubDir(m1)
        SubDir(m2)
        SubDir(m3)
        file(models.py)
        "this file contains the base class to create a consistent api"

    file(selectory.py)
    "this file choose a str to load module in based on the query str"
"""
import sys
import argparse
from loader import dynamic_module_loader, list_modules   # pylint: disable=import-error

# # Static Imports with filepaths

# from modules.fordcraft_ship.fordcraft_api import FordCarft
# from modules.starship_ship.starship_api import StarShip
# from modules.tesla_ship.tesla_api import Tesla

parser = argparse.ArgumentParser(description="Dynamicaly import modules with module-inator.")
parser.add_argument("-q", "--query", help="Name of the module you want to load.")
parser.add_argument("-s", "--show-modules", action="store_true", help="List all available modules")



# ford_craft_ = FordCarft("General Ken", "Asteroids", "3000ft", "339525")
# ford_craft_.authenticate()
# if ford_craft_.auth_status:
#     print("Oh yeah!, we are in baby.")

if __name__ == "__main__":
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    if args.show_modules:
        mod_list = list_modules()
        print("The available modules are:")
        for m in mod_list:
            print("\t"+m)
        exit(0)
    
    print(f"Requested Module: {args.query}\n")
    
    mod_info = dynamic_module_loader(args.query)

    if not mod_info:
        print(f"[!] Sorry {args.query} is not an available module.")
        exit(2)

    path = mod_info["path"]
    name = mod_info["name"]

    print("Class path : "+path+"."+name+"\n")

    the_module = __import__(path, fromlist=[name])
    klass = getattr(the_module, name)

    print(f"{klass}\n")

    space_ship = klass(
        name="General Sal",
        space_type = "Galaxy",
        size = "1900m",
        code = 194567,
    )

    space_ship.authenticate()
    