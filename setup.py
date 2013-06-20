import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'pymongo',
    'mongoengine',
    'redis',
    'hiredis',
    'gevent-socketio',
    'apscheduler',
    'flufl.enum',
    'jsonpickle',
    'beautifulsoup4',
    'mock',
]

setup(name='culpa',
      version='0.1',
      description='culpa',
      long_description=CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Jan Lievens',
      author_email='jan.lievens@gmail.com',
      url='',
      keywords='Culpa the blame generator...',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="culpa",
      entry_points="""\
      [paste.app_factory]
      main = culpa:main
      """,
)
