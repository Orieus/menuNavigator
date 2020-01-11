# menuNavigator
A generic template application to generate command-line menus

## Example of usage

For a toy example of the functionality of this module, run

    python mainExample.py --p [project_folder] --source example_folder
    
where `[project_folder]` must be replaced by the path to the folder where the application is expected to store the result files.

The options of the navigation tree are defined in `config/options_menu.yaml`.

## Integrating `menuNavigator` into your application

In order to integrate `menuNavigator` into your application, you do **not** need to modify the following files:

* `code/menu_navigator/menu_navigator.py`: It contains the main class of the module, MenuNavigator, which manages the used interaction through the menus.

* `code/base_taskmanager.py`: It contains the `baseTaskManager` class, which provides basic functionality to create, load or update an application project.

You should modify the following files:

* `config/options_menu.yaml`: It defines the options to be shown through the navigation tree
* `code/task_manager.py`: It contains the `TaskManager` class, which runs the methods selected through the navigation tree. For each option in `options_menu.yaml`, a method should exist in the `TaskManager`class executing it. It inherits from the `baseTaskManager` class.
* `config/parameters.default.yaml`: It should contain the default values of the parameters required by your application. Some of these parameters can be specific of each application project. For this reason, each time a new project is created, a copy of this file is placed at the project folder, which can be modified by the user.

