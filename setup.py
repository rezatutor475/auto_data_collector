from setuptools import setup, find_packages
import os

# Load the long description from README.md
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Auto Data Collector: A Python library to collect, validate, and store personal data."

# Helper function to load requirements
def load_requirements(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

setup(
    name="auto_data_collector",
    version="0.1.1",
    author="Reza Torabi",
    author_email="rezatutor475@gmail.com",
    description="A Python library for automated data collection, validation, and storage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/auto_data_collector",
    project_urls={
        "Bug Tracker": "https://github.com/rezatutor475/auto_data_collector/issues",
        "Documentation": "https://github.com/rezatutor475/auto_data_collector?tab=readme-ov-file#readme",
    },
    packages=find_packages(exclude=["tests*", "examples"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.7',
    install_requires=load_requirements("requirements.txt"),
    extras_require={
        "dev": [
            "pytest",
            "flake8",
            "black"
        ]
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.md", "*.ini"]
    },
    entry_points={
        'console_scripts': [
            'auto-collect=data_collector.__main__:main',
        ],
    },
    zip_safe=False
)
