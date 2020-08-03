import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="johnthomasg0215", # Replace with your own username
    version="0.1.1",
    author="John Thomas",
    author_email="johnthomasg0215@example.com",
    description="A small example package",
    long_description=long_description readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/John-G-Thomas/chaindata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',)




