from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
         requirements = [
        req.strip() for req in requirements
        if req.strip() and not req.strip().startswith('-e') and not req.strip().startswith('#')
    ]
    return requirements

setup(
    name="mlproject",
    version='0.0.1',
    author='sahasra',
    author_email='sahasra15082005@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)