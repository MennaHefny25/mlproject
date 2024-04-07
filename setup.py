# Building our application as a pakage it self so anyone can downloaded and use it.

from setuptools import find_packages, setup

HYPHEN_E_DOT='-e .'
def get_requirements(file_path):
    """
    this function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements

# Meta data about the project
setup(
    name="mlproject",
    version="0.0.1",
    author="Menna",
    author_email="mennahefny25@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
