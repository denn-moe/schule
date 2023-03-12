# https://www.sphinx-doc.org/en/master/usage/configuration.html



#  _        __      
# (_)      / _|     
#  _ _ __ | |_ ___  
# | | '_ \|  _/ _ \ 
# | | | | | || (_) |
# |_|_| |_|_| \___/ 
                  
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
                  
project = 'schule'
copyright = '2023, moe'
author = 'moe'


#                   __ 
#                  / _|
#   ___ ___  _ __ | |_ 
#  / __/ _ \| '_ \|  _|
# | (_| (_) | | | | |  
#  \___\___/|_| |_|_|  
                     
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_design",
    'sphinx.ext.mathjax',
    'sphinxcontrib.plantuml',

    'sphinxcontrib.nwdiag',
    'sphinxcontrib.rackdiag',
    'sphinxcontrib.packetdiag'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'de'



#  _     _             _ 
# | |   | |           | |
# | |__ | |_ _ __ ___ | |
# | '_ \| __| '_ ` _ \| |
# | | | | |_| | | | | | |
# |_| |_|\__|_| |_| |_|_|

# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "schule"
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css',]

# html_theme_options = {
#    "announcement": "Hamburger + Silbermann = <3",
# }

#  _       _            
# | |     | |           
# | | __ _| |_ _____  __
# | |/ _` | __/ _ \ \/ /
# | | (_| | ||  __/>  < 
# |_|\__,_|\__\___/_/\_\
                      
# source file, target tex file, document title, author, and document class
latex_documents = [
   ('hardware', 'hardware.tex', u'Hardware', u'Author', 'howto'),
]


