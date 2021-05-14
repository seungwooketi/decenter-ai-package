import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'flask',
    'flask_cors',
    'requests',
    'paho-mqtt'
    ]

setuptools.setup(name='decenter', 
                 version='0.6',
                 description='ai container pack for decenter',
                 url='http://decenter-project.eu',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 packages=setuptools.find_packages(),
                 install_requires=install_requires)
