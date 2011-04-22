Use namespace packages with Django
==================================

Installation with Buildout
--------------------------

  - Add "nsdjango" to your requirements in setup.py


Example configuration with Buildout
-----------------------------------

*buildout.cfg* (excerpt)

    [buildout]
    find-links = http://download.rjdj.me/python

    [versions]
    Django=1.3
    zc.buildout=1.5.2
    nsdjango=0.1

    [instance]
    recipe = zc.recipe.egg:script
    eggs = my.project
    scripts = instance
    arguments = settings
    initialization = from my.project import settings
    

*setup.py* (excerpt)

    setup(name = "my.project",
          version = "0.0.1",
          author = '',
          author_email = '',
          description = 'My Project',
          url = '',
    	  namespace_packages = [],
          packages = find_packages('src'),
          package_dir = {'':'src'},
          install_requires = ['Django',
                              'nsdjango',
                             ],
          entry_points = {
              'console_scripts':['instance=nsdjango.management:execute_manager']
              },
          include_package_data = True,
          zip_safe = False,
          extras_require = dict(instance=[]),
    )

