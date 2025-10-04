from setuptools import setup, find_packages

setup(
    name="IncubyteFramework",
    version="0.1.0",
    description="Automated test framework for Parabank using Playwright and Pytest-BDD",
    author="Shrithik Raj",
    packages=find_packages(),  # automatically finds core/, pages/, tests/
    install_requires=[
        "playwright>=1.35.0",
        "pytest>=8.0.0",
        "pytest-bdd>=8.1.0"
    ],
    python_requires=">=3.13",
)
