from setuptools import setup,find_packages
from typing import List

def get_reqirements()->List[str]:

    """This function returns a list of requirements"""
    requirement_list:List[str] = [
        'pymongo==4.2.0',
        ]
    return requirement_list
__version__ = '0.0.1'
with open("README.md", "r", encoding="utf-8") as f:

    long_description=f.read()

setup(
    name="sensor",
    version="0.0.1",
    author="Abhishek",
    author_email="vvabhi@gmail.com",
    pakages=find_packages("sensor"),
    install_requires=get_reqirements(),
    package_dir={"": "sensor"},
    url="https://github.com/Abhishekyes/Sensor-Fault-Detection.git"

) 



 


