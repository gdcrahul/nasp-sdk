from setuptools import setup, find_packages

setup(
    name="nasp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers>=4.30.0",
        "torch"
    ],
    entry_points={
        "console_scripts": [
            "nasp-demo=demo:main",
        ],
    },
    description="Neural Agent Security Protocol (NASP) SDK",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/nasp-sdk",
    python_requires=">=3.8",
)
