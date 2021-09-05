********************
The Qubinode Project
********************

The Qubinode documentation page uses sphinx_rtd_theme to create a web browser for the `Qubinode <http://qubinode.io>`__  project.

Building the Qubinode documentation page
=========================================

Required applications to build and configure qubinode documentation
--------------------------------------------------------------------

+------------------+-------------------------------------------+
| applications     | web links                                 |
+==================+===========================================+
| pandoc           | `https://pandoc.org`                      |
+------------------+-------------------------------------------+
| sphinx_rtd_theme | `https://sphinx-rtd-theme.readthedocs.io` |
+------------------+-------------------------------------------+
| reference        | `https://purduecam2project.github.io/CAM2WebUI/basicSetup/sphinx.html` |
+------------------+-------------------------------------------+

Notable files and directories
------------------------------
 * The docsource folder is the build directory 
 * The docs folder is the publish directory 
 * the conf.py is the configuration file for sphinx
 * the MAKE file is the build file for sphinx 

Building Qubionde web page
--------------------------

1. Under the docsource directory:
   .. code-block:: bash
   make github

   

2. Test the build by running:
   .. code-block:: bash
   open ../docs/index.html
   
   
3. To convert .md files to .rst:
      pandoc example.md --from markdown --to rst -s -o example.rst
   .. code-block:: bash
   
