<a href="https://imgflip.com/i/7u9wco"><img src="https://i.imgflip.com/7u9wco.jpg" title="made at imgflip.com"/></a>


# module-inator 🕹️

The Module-inator: Dynamically Loading Python Classes for API Abstraction

## Introduction

Have you ever faced the challenge of integrating multiple APIs from different vendors, all with varying patterns and functions? If so, you're not alone! As a developer, I encountered this problem while working on an API project that required integrating various APIs from different vendors. These vendors provided similar functionalities but followed inconsistent API patterns.

To address this issue, I came up with an innovative solution – the Module-inator! This project aims to dynamically load Python classes, abstracting away vendor-specific details and making the integration process a breeze. Let's dive into how it works and how you can utilize it to simplify your API integration woes.


## How it works 
Before we delve into the mechanics, let's explore the project's directory structure:

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

In this structure, the modules directory holds subdirectories for each vendor's API. Each API implementation resides in a corresponding `VENDOR_NAMEApi.py` file. All of these API classes implement the same functions defined in `models.py`, which serves as the base class.

### Vendor-specific implementations 
Each vendor API's logic is encapsulated within their respective `VENDOR_NAMEApi.py` file. Despite the differences in implementation, the API classes maintain the same set of functions defined in the base class. This uniformity enables seamless integration.

### Dynamically Loading Modules
The magic happens in the `loader.py` file, which contains two crucial functions and a `modules_` dictionary. The modules_ dictionary stores the paths and class names for each vendor.

### Loading and Running Modules
In `__main__.py`, we call the `loader.py` file to retrieve the file path for a given `VENDOR_NAME`. Armed with the path and class name, we use the `__import__()` function to dynamically load the corresponding API class.


## Installation
### Install Locally
To get started, simply clone the module-inator repository:
```bash
git clone https://github.com/salmansyyd/module-inator.git
```
### Use in a codespace

<a href='https://codespaces.new/salmansyyd/module-inator'><img src='https://github.com/codespaces/badge.svg' alt='Open in GitHub Codespaces' style='max-width: 100%;'></a>

## Usage 
The Module-inator offers a simple and user-friendly command-line interface. Here are some essential commands:
### List all available modules
To see a list of all available modules, run the following command:

```bash
python3 module-inator -s
```

### Load and run a module
To load a specific module and execute it, use the following command:
```bash
python3 module-inator -q MODULE_NAME
```
Replace MODULE_NAME with the name of the desired vendor's module.

### Get help
For additional assistance or information about the available commands, you can run:
```bash
python3 module-inator -h
```

## Conclusion 
With the Module-inator pattern, integrating APIs from different vendors becomes an efficient and painless.This Python project dynamically loads classes, abstracting away vendor-specific details, and brings consistency to your API integration workflow.

If you find the Module-inator helpful and appreciate the effort put into its development, I would be incredibly grateful if you could show your support by giving it a star on GitHub. 

Thank you for exploring the Module-inator with me, and I look forward to seeing your contributions and hearing about your experiences using it. Happy coding and remember to keep creating and innovating! 🌟