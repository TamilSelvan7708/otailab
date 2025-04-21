from setuptools import setup, find_packages

setup(
    name='otailab',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'networkx>=2.0',
        'matplotlib>=3.0',
        'numpy>=1.19.0',
        'scipy>=1.6.0',
        'sympy>=1.8'
    ],
    author='Tamilselvan A K',
    author_email='aktamil13@gmail.com',
    description='A Python package for Operations Research and Optimization Algorithms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/otailab',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Operations Research'
    ],
    python_requires='>=3.6',
)
