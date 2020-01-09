# menuNavigator
A generic template application to generate command-line menus

## Example of usage

For a toy example of the functionality of this module, run

    python mainExample.py --p [project_folder] --source example_folder
    
where `[project_folder]` must be replaced by the path to the folder where the application is expected to store the result files.

The options of the navigation tree are defined in `config/options_menu.yaml`.

## Integrating `menuNavigator` into your application

In order to integrate `menuNavigator` into your application, you do not need to modify the following files:

* `code/menu_navigator/menu_navigator.py`: It contains the main class of the module, MenuNavigator, which manages the used interaction through the menus.

* `code/base_taskmanager.py`

You should modify the followinf files


The options of the navigation tree are defined in `config/options_menu.yaml`.

You should modify this file to fit the module to your python application.

All tasks selected thhrough the menu options will be ran by methods in the `TaskManager` class in `code/task_manager.py`. You should add your own methods here to adapt the code to you application.

The `TaskManager` class inherits from `baseTaskManager`, defined in `code/base_taskmanager`. This base class is not expected to be modified (though you can overwrite methods usigng the child class). It provides basic functionality to create, load or update an application project.


