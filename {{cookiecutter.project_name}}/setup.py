from setuptools import setup, find_packages
from os import path
import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='{{ cookiecutter.project_name }}',
    version=versioneer.get_version(),
    description='{{ cookiecutter.project_description }}',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='{{ cookiecutter.project_url }}',
    author='{{ cookiecutter.project_author }}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.5, <4',
    install_requires=[],
)
