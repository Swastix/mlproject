from setuptools import setup, find_packages
from typing import List


def read_requirements(file_path: str) -> List[str]:
    """Read a requirements file and return a list of packages."""
    
    requirements = []
    with open(file_path, 'r') as file:
        requirements =  file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
        
        
    return requirements   
        
setup (
    
    name='ml_project',
    version='0.0.1',
    author='Swastik',
    author_email='panda.swastik06@gmail.com',
    install_requires=read_requirements('requirements.txt'),
    packages=find_packages()
    
)