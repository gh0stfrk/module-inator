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