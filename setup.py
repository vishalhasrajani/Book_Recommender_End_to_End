from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Collaborative Based Books Recommender System"
AUTHOR_USER_NAME = "Vishal Hasrajani"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Vishal Hasrajani",
    description="A small local packages for Collaborative based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vishalhasrajani/Collaborative-Based-Book-Recommender-System",
    author_email="hasrajanivishal@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires="==3.10",
    install_requires=LIST_OF_REQUIREMENTS
)
