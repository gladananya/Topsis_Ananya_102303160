from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='topsis_ananya_102303160',
    version='1.0.7',
    author='Ananya',
    description='A Python implementation of TOPSIS for multiple-criteria decision making.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'topsis-ananya=topsis_ananya.topsis:run'
        ]
    },
)
