from setuptools import setup, find_packages

setup(
    name='QA_Automation',
    version='1.0.0',
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
    url='https://github.com/udemeudofia/QA_Automation',
    license='BSD',
    author='Udeme Udofia',
    author_email='udemeudofia01@gmail.com',
    description='The complete solution of technical tasks for a Quality Assurance (QA) Automation Engineer',
    install_requires=['pytest==6.1.1',
                      'selenium==3.141.0',
                      'webdriver-manager==3.2.2'],
    tests_require=['pytest==6.1.1', 'click~=7.1.2']
)
