from setuptools import setup, find_packages

setup(
    name="BlenderDataChart",
    version="0.1.0",
    description="A Blender animation library for charts and graphs",
    packages=find_packages(),
    python_requires=">=3.7",
    package_dir={"": "src"}
)