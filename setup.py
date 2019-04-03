import os

from setuptools import find_packages, setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='notejam',
    license='',
    author='',
    url='',
    author_email='akononov.job@gmail.com',
    description='',
    package_dir={'': 'notejam'},
    packages=find_packages('notejam'),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'notejam = main:main',
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Natural Language :: English',
        'Operating System :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)