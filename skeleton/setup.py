try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = [
	'description':'My Project',
	'author': 'Itai Maimon',
	'url':'addlater',
	'download_url':'make new'
	'author_email':'itaimaimon@gmail.com'
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['NAME'],
	'scripts':[],
	'name':'projectname'
	]
	setup(**config)
	