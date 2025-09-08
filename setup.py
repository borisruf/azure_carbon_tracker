from setuptools import setup, find_packages

setup(
    name="azure-carbon-tracker",
    version="0.3.0",
    description="Azure carbon tracking via Cost Management API.",
    author="Boris Ruf",
    url='https://github.com/borisruf/azure_carbon_tracker',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
        "requests",
        "azure-identity"
    ],
    package_data={
        "azure_carbon_tracker": ["data/*.csv"]
    },
    python_requires=">=3.8",
)