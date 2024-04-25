from setuptools import find_packages, setup
#from typing import List

# return list of strings
def get_requirements() -> List[str]:

    # This function will return list of requirements
    requirements_list: List[str] = []

    # Write a code to read requirements.txt file & append each requirements in requirement list variable 
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