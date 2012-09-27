from distutils.core import setup

setup(
    name='LinkedIn Client Library',
    version='1.0.8',
    author='Aaron Brenzel',
    author_email='abrenzel@millerresource.com',
    url='12.236.169.60:4830/liclient',
    install_requires = ['lxml', 'httplib2'],
    description='Library for accessing the LinkedIn API in Python',
    packages=['liclient', 'liclient.parsers', 'liclient.oauth2', 'liclient.analysis'],
    license='MIT',
    package_data={'':['*.txt']},
    requires=['httplib2']
)
