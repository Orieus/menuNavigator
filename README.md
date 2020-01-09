# menuNavigator
A generic template application to generate command-line menus

## Usage

For a toy example of the functionality of this package, run

    python mainExample.py --p [project_folder] --source example_folder
    
where `[project_folder]` must be replaced by the path to the folder where the application is expected to store the result files.

The options of the navigation tree are defined in `config/options_menu.yaml`.

You should modify this file to be adapted to your python application.

All tasks selected thhrough the menu options will be ran by methods in the `TaskManager` class in `code/task_manager.py`. You should add your own methods here to adapt the code to you application.

The `TaskManager` class inherits from `baseTaskManager`, defined in `code/base_taskmanager`. This base class is not expected to be modified (though you can overwrite methods usigng the child class). It provides basic functionality to create, load or update an application project.


