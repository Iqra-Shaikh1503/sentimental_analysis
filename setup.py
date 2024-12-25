<<<<<<< HEAD
from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path):
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
    return requirements

setup(
    name='Amazon_Review_Sentimental_Analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
=======
from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path):
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
    return requirements

setup(
    name='Amazon_Review_Sentimental_Analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
>>>>>>> bf39c27c4385beeac68481d02f1993e06dd7f20b
