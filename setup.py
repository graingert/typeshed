import fnmatch
import os

from setuptools import setup


dir = os.path.dirname(os.path.abspath(__file__))
typeshed_dir = os.path.join(dir, 'typeshed' + os.path.sep)


def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]


def get_pyi_files():
    for root, dirnames, filenames in os.walk(typeshed_dir):
        for filename in fnmatch.filter(filenames, '*.pyi'):
            yield remove_prefix(os.path.join(root, filename), typeshed_dir)


pyi_files = list(get_pyi_files())
readme = open('README.rst').read()

setup(
    name='typeshed',
    version='0.0.0a0',
    description='Collection of library stubs for Python, with static types',
    long_description=readme,
    license="Apache 2",
    maintainer="Thomas Grainger",
    maintainer_email="typeshed@graingert.co.uk",
    url='https://github.com/graingert/typeshed',
    packages=['typeshed'],
    package_data={'typeshed': pyi_files},
    install_requires=[],
    classifiers=[],
)
