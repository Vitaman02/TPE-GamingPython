import os
from setuptools import find_packages, setup

cwd = os.path.abspath(os.path.dirname(__file__))

# Load requirements
requirements = []
with open(os.path.join(cwd, "README.md")) as file:
    readme = file.read()

# Load README
readme = ""
with open(os.path.join(cwd, "requirements.txt")) as file:
    requirements = file.readlines()

# Extra requirements
requirements_dev = [
    "pre-commit==2.19.0",
    "black==22.3.0",
    "isort==5.10.1",
]

requirements_test = [
    "pytest==7.1.2",
    "pytest-cov==3.0.0",
]

extras = {
    "dev": requirements_dev,
    "test": requirements_test
}

# Run setup
setup(
    name="tpe-game",
    author="Vitaman02",
    version="0.0.1",
    packages=find_packages(),
    description="Game made with PyGame for TPE",
    install_requires=requirements,
    extras_require=extras,
    url="https://github.com/Vitaman02/TPE-GamingPython",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    project_urls={
        "Issue tracker": "https://github.com/Vitaman02/TPE-GamingPython/issues"
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)