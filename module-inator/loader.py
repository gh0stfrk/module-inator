"""
Module loader
"""
# add module names with their path here
modules_ = {
    "FordCraft":"modules.fordcraft_ship.fordcraft_api",
    "Tesla":"modules.tesla_ship.tesla_api",
    "StarShip":"modules.starship_ship.starship_api",
}

def list_modules() -> list :
    """
    Returns the list of available modules.
    """
    module_list = []

    for mod in modules_:
        module_list.append(mod.lower())
    
    return module_list

def dynamic_module_loader(query_str):
    """
    Finds the path for the input query_str

    :param query_str
    """

    for key in modules_:
        if query_str.lower() == key.lower():
            return {
                "path":modules_[key],
                "name":key,
            }
        
    return False
