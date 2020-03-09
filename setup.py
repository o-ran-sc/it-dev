from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='HelmManager',
    version='1.0.0',
    description='RIC xApp helm chart manager',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gerrit.o-ran-sc.org/r/admin/repos/it/dev',
    author='Zhe Huang',
    author_email='zhehuang@research.att.com',
    include_package_data=True,
    packages=find_packages(),
    package_data={'': ['*.yaml', '*.tpl', '*.conf', 'HelmManager', 'cli']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
