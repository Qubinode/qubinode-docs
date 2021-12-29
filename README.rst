********************
The Qubinode Project
********************

The Qubinode documentation page uses sphinx_rtd_theme to create a web browser for the http://qubinode.io  project.

Building the Qubinode documentation page
=========================================

To build the Qubinode documentation page use the following information

Required applications to build and configure qubinode documentation
--------------------------------------------------------------------
* https://pandoc.org
* https://sphinx-rtd-theme.readthedocs.io
* https://purduecam2project.github.io/CAM2WebUI/basicSetup/sphinx.html

Notable files and directories
------------------------------
 * The docsource folder is the build directory 
 * The docs folder is the publish directory 
 * the conf.py is the configuration file for sphinx
 * the MAKE file is the build file for sphinx 

Building Qubionde web page
--------------------------
.. highlight:: python

1. Under the docsource directory
.. :: 
   make github

2. Test the build by running
.. :: 
   open ../docs/index.html   
   
3. To convert .md files to .rst:
.. ::
   pandoc example.md --from markdown --to rst -s -o example.rst
