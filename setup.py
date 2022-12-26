import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="neatplot",
    version="0.1.0",
    author="Willie Neiswanger",
    author_email="willie.neiswanger@gmail.com",
    description=("Plotting utilities for Python"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/willieneis/neatplot",
    packages=setuptools.find_packages(),
    package_data={"neatplot": ["matplotlibrc", "matplotlibrc_fonts"]},
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
