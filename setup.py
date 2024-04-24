from setuptools import find_packages, setup
#from typing import List

# return list of strings
def get_requirements()->list[str]:
    requirements_list = list[str] = []
    return requirements_list

setup(
    name='sensor',
    version="0.0.1",
    author="arun",
    author_email="arunchaudhary6515@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements(),  #["pymongo"]
)

#Execute through Command line the installation process for a python package or module.