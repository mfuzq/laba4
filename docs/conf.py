import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Ваш Проект'
author = 'Ваше Имя'
release = '0.1'

extensions = ['breathe']
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

breathe_projects = {
    "Ваш Проект": "./docs/xml"
}
breathe_default_project = "Ваш Проект"
