<a href="https://imgflip.com/i/7u9wco"><img src="https://i.imgflip.com/7u9wco.jpg" title="made at imgflip.com"/></a>


# module-inator 🕹️

The module-inator, dynamically loading python classes.

## Introduction

The inspiration behind this idea was, i was creating a api project that is using multiple different apis from different vendors that have their platforms but in general do the same thing, but they do not follow a consistent api pattern so that use similar functions and names and just change the vendor name.

So i created this project to dynamicaly load classes and abstract away the specific vendor details. 
Anddd it works..

## How it works 
Project Structure.
```bash
\project-dir
    \modules
        \some-vendor
            SomeVendorApi.py
        \another-vendor
            AnotherVendorApi.py
        \one-more-vendor
            OneMoreVendorApi.py
        models.py
        __init__.py

    loader.py
    __main__.py
    __init__.py

```

- In the above dir structure describes a `modules` dir in which different apis from vendors reside.
- All of the modules implement same functions defined in the `models.py` as a base class.
- The logic of implementation is different with each vendor and implemented in `VENDOR_NAMEApi.py` file
- Comming out of the modules dir into the `project-dir` the `__main__.py` file is where the modules are dynamically loaded by depending on the name of the vendor.
- `loader.py` file contains two functions and `modules_` dict that stores the path and name of class
- `__main__.py` calls the `loader.py` file to return the file path for the given `VENDOR_NAME`
- With the path and class name `__main__.py` loads the class with `__import__()` function.


## Installation
Install Locally
```bash
git clone https://github.com/salmansyyd/module-inator.git
```
- Use in a codespace

<a href='https://codespaces.new/salmansyyd/module-inator'><img src='https://github.com/codespaces/badge.svg' alt='Open in GitHub Codespaces' style='max-width: 100%;'></a>

## Usage 
- List all available modules

```bash
python3 module-inator -s
```

- Load a module and run it.

```bash
python3 module-inator -q MODULE_NAME
```

- Get help

```bash
python3 module-inator -h
```