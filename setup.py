try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This package can convert a number to Pashto language',
    'author': 'Sadaf Waziry',
    'url': 'https://github.com/SadafWaziry/PashtoCardinals',
    'download_url': 'Where to download it.',
    'author_email': 'sadaf1.waziry@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pashto_cardinals'],
    'scripts': [],
    'name': 'Pashto Cardinals'
}

setup(**config)
