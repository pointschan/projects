try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Learning Python',
    'author': 'pointschan',
    'url': '',
    'download_url': '',
    'author_email': 'my email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['control'],
    'scripts': [],
    'name': 'Projects'
}

setup(**config)

