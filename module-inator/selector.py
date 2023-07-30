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
import argparse
from loader import module_loader

# Static Imports with filepaths
from modules.fordcraft_ship.fordcraft_api import FordCarft
from modules.starship_ship.starship_api import StarShip
from modules.tesla_ship.tesla_api import Tesla

parser = argparse.ArgumentParser()
parser.add_argument("query")

# ford_craft_ = FordCarft("General Ken", "Asteroids", "3000ft", "339525")
# ford_craft_.authenticate()
# if ford_craft_.auth_status:
#     print("Oh yeah!, we are in baby.")

if __name__ == "__main__":
    args = parser.parse_args()

    if not args.query:
        print("enter a module name to load.")
        SystemExit(2)
    
    mod_info = module_loader(args.query)

    if mod_info:
        path = mod_info["path"]
        name = mod_info["name"]
        # from str(path) import str(name)
    