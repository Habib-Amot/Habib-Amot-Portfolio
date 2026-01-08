# dynamic import of modules in python is a very important concept which can be used when it comes to creation of plugins and extensions
# this is done in 4 different ways and I will be starting from the hardest to the simplest approach that is used for dynamic imports
# although a library exist to make this process to be seamlessly possible.

# this lesson uses a folder called plugins which contains all the modules that I will be using for this practice
# inside this function, there is a function (show_magic_number) that will be called. and when the function has been called, the file name will be printed alognside the number. But if the functin does not contain the function that is needed, the value "Unknown" we be attached to the front of the file

import os
import sys

# Approach one

def import_approach_one():
    plugins = load_plugins()
    plugin_entry_point = []

    for plugin in plugins:
        plugin_entry = get_plugin_entry(plugin)

        if plugin_entry is not None:
            plugin_entry_point.append(plugin_entry)
    
    # now that the plugins and the functions in them has been gotten, we can now make use of each of the functions to determine the filetype of each file that is given in the command line
    if sys.argv[1:]:
        for file in sys.argv[1:]:
            file_extension = os.path.splitext(file)[1]
            for plugin_function in plugin_entry_point:
                file_type = plugin_function(file_extension)
                if file_type is not None:
                    print("{0:.<40}{1}".format(file_type, file))
                    break
            else:
                print("{0:.<40}{1}".format("Unknown", file))


def get_plugin_entry(plugin):
    # getting a particular function from the given plugin

    if hasattr(plugin, 'main'):
        function = getattr(plugin, 'main')
        if hasattr(function, "__call__"):
            plugin_function =  getattr(plugin, 'main')
        else:
            plugin_function = None
    else:
        plugin_function = None
    
    return plugin_function


def approach_one_loading_method(plugin, plugin_name):
    with open(plugin) as plugin_file:
        plugin_content = plugin_file.read()
        module_type = type(sys)
        plugin_module = module_type(plugin_content)  # converting the plugin content to a module
        exec(plugin_content, plugin_module.__dict__)
        sys.modules[plugin_name] = plugin_module
        return plugin_module


loading_method = {
    "approach one": approach_one_loading_method,
    "approach two": "",
    "approach three": "",
    "approach four": "",
}


def approach_two_loading_method():
    pass


def approach_three_loading_method():
    pass


def approach_four_loading_method():
    pass


def load_plugins(path="./plugins", approach="approach one"):
    plugins = []
    for plugin in [f"{path}/{plugin}" for plugin in os.listdir(path=path)]:
        plugin_name = os.path.splitext(plugin.split('/')[-1])[0].strip()

        if plugin_name and plugin_name.isidentifier() and plugin_name not in sys.modules:  # checking if the module is valid and has not been imported
            try:
                plugin_module = loading_method[approach](plugin, plugin_name)
                plugins.append(plugin_module)

            except EnvironmentError as err:
                sys.modules.pop(plugin_name, None)
                print(err)
    return plugins


import_approach_one()

""" import importlib

module = importlib.import_module('branching-with-dictionary')
print(hasattr(module, 'main')) """