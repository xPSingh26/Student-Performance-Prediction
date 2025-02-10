from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath:str):
    """returns a list of required libraries from requirements.txt"""
    requirements = []
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='spp-project',
    version='0.1',
    author='Praval',
    author_email='p.singhx26@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)