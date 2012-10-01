from distutils.core import setup

setup(
    name='LinkedIn Client Library',
    version='1.0.17',
    author='Yaroslav Klyuyev',
    author_email='yaroslav,klyuyev@gmail.com',
    install_requires = ['lxml', 'httplib2'],
    description='Library for accessing the LinkedIn API in Python',
    packages=['liclient', 'liclient.parsers', 'liclient.oauth2', 'liclient.analysis'],
    license='MIT',
    package_data={'':['*.txt']},
    requires=['httplib2']
)
