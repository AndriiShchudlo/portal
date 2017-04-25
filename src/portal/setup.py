from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'waitress',
    ]

setup(name='portal',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=requires,

      entry_points="""\
      [paste.app_factory]
      main = portal:main
      """,
)





