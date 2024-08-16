from setuptools import setup,find_packages
from typing import List

hypen_e_dot='-e .'
def get_requrirements(file_path:str) -> List[str]:
    with open(file_path,'r') as file_obj:
        requirements=[line.strip() for line in file_obj.readlines()]
    if hypen_e_dot in requirements :
        requirements.remove(hypen_e_dot)

    return requirements



setup(
    name='ml project',
    description='end to end ml project with deployment',
    author='simhadri',
    author_email='simhadrisriram3@gmail.com',
    url='https://github.com/sriramsriram3',
    install_requires=get_requrirements('requirements.txt')         #
)

