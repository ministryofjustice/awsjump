from setuptools import setup

setup(
    # Application name:
    name="awsjump",

    # Version number (initial):
    version="0.0.4",

    # Application author details:
    author="Stuart Munro",
    author_email="stuart.munro@digital.justice.gov.uk",

    # Packages
    packages=["awsjump"],

    # Executables
    scripts=['awsjump/jump'],

    # Details
    url="https://github.com/ministryofjustice/awsjump",

    # license="LICENSE.txt",
    description="Command line tool to SSH into EC2 servers from multiple accounts",

    # Dependent packages (distributions)
    install_requires=[
        "boto==2.34.0",
        "PyYAML==3.11",
        "prettytable==0.7.2"
    ],

    license = "MIT",

    platforms = "Posix; MacOS X",

    classifiers = ["Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Topic :: Internet"],
)
