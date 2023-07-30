"""
Module loader
"""
modules_ = {
    "FordCraft":"modules.fordcraft_ship.fordcraft_api",
    "Tesla":"modules.tesla_ship.tesla_api",
    "StarShip":"modules.starship_ship.starship_api",
}

def module_loader(query_str):
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
