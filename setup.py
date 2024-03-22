import setuptools 

setuptools.setup(
    name='crypto-sine-waver',
    version='0.0.1',
    author='Tahmi ogosi',
    packages=setuptools.find_packages(),
    description="A price transform for cryptocurrency",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'matplotlib'],
)
