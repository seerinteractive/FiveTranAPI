from setuptools import setup

with open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="FiveTranAPI",
    version="1.0",
    description="Simple wrapper for FiveTran's API",
    author="Ethan Lyon",
    author_email="ethanlyon@gmail.com",
    install_requires=["pytest==5.4.1", "requests==2.23.0"],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["fivetran", "fivetran.common"],
    package_data={"": ["registry.yaml"]},
    include_package_data=True,
)
__author__ = "Ethan Lyon"
