from setuptools import setup

setup(
    name='bsqrate',
    version='1.0.1',
    packages=['bsqrate'],
    package_dir={'bsqrate': 'src/bsqrate'},
    author='MSU CC Team',
    author_email='videocodec-testing@graphics.cs.msu.ru',
    url='https://compression.ru/video/codec_comparison/bsq-rate/',
    install_requires=[
        "numpy",
        "scipy"
    ]
)
