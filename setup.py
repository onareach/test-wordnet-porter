from setuptools import setup, find_packages

setup(
    name="wordnet-porter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "psycopg2-binary",
        "tqdm",
    ],
    entry_points={
        'console_scripts': [
            'wordnet-porter=wordnet_porter.main:main',
        ],
    },
    python_requires='>=3.8',
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for porting WordNet to PostgreSQL",
    keywords="wordnet, postgresql, nlp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
