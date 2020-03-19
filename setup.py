import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("src/flask/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="Indexio",
    version=version,
    project_urls={
        "Code": "https://github.com/saromanov/indexio",
    },
    license="MIT",
    author="Sergey Romanov",
    author_email="xxsmotur@gmail.com",
    description="Text indexing",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.8",
)