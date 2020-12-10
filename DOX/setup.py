from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Hamza',
    version='0.0.1',
    description='DOXING TOOL',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Hamza Chennou',
    author_email='Hamchenhbf3@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='DOXING TOOL',
    packages=find_packages(),
    install_requires=['']
)