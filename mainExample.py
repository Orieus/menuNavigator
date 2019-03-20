#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main program

Created on March 20 2019

@author: Jesús Cid Sueiro
"""

import os
import argparse

# Local imports
from menu_navigator.menu_navigator import MenuNavigator
from task_manager import TaskManager

# ########################
# Main body of application
# ########################

# ####################
# Read input arguments

# settings
parser = argparse.ArgumentParser()
parser.add_argument('--p', type=str, default=None,
                    help="path to a new or an existing project")
parser.add_argument('--source', type=str, default='../source_data',
                    help="path to the source data folder")
args = parser.parse_args()

# Read project_path
project_path = args.p
if args.p is None:
    while project_path is None or project_path == "":
        project_path = input('-- Write the path to the project to load or '
                             'create: ')
if os.path.isdir(args.p):
    option = 'load'
else:
    option = 'create'
active_options = None
query_needed = False

# Create SuperGraph Project
tm = TaskManager(project_path)

# ########################
# Prepare user interaction
# ########################

paths2data = {'input': os.path.join(project_path, 'input'),
              'imported': os.path.join(project_path, 'imported')}
path2menu = 'options_menu.yaml'

# ##############
# Call navigator
# ##############

menu = MenuNavigator(tm, path2menu, paths2data)
menu.front_page(title="An Application example using menuNavigator")
menu.navigate(option, active_options)
