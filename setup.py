from setuptools import setup,find_packages
from typing import List

def get_reqirements()->List[str]:

    """This function returns a list of requirements"""

    requirement_list:List[str] =[]
    
    """
    write a code to read requirements.txt file and append each requirement
    """
    
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="Abhishek",
    author_email="vvabhi@gmail.com",
    pakages=find_packages(),
    install_requires=get_reqirements(),#[],

) 