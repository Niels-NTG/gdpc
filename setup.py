"""The repository setup file."""

from setuptools import find_packages, setup

__author__ = "Blinkenlights"
__version__ = "v5.0.2"

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="gdpc",
    version=__version__,
    description=(
        "The Generative Design Python Client is a Python-based "
        "interface for the Minecraft HTTP Interface mod.\n"
        "It was created for use in the "
        "Generative Design in Minecraft Competition."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avdstaaij/gdpc",
    author="Blinkenlights",
    author_email="blinkenlights@pm.me",
    maintainer="Arthur van der Staaij",
    maintainer_email="arthurvanderstaaij@gmail.com",
    license="MIT",
    packages=["gdpc"], # Note: subpackages must be listed explicitly
    install_requires=[
        "matplotlib",
        "NBT",
        "numpy",
        "opencv_python",
        "requests"
    ],
    python_requires=">=3.6, <4",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Simulation",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Version Control :: Git"
    ],
    keywords="GDMC, generative design, Minecraft, HTTP, development",
    project_urls={
        "Bug Reports": "https://github.com/avdstaaij/gdpc/issues",
        "Official Competition": "https://gendesignmc.engineering.nyu.edu",
        "Chat about it on Discord": "https://discord.gg/V9MW65bD",
        "Source": "https://github.com/avdstaaij/gdpc",
    },
    zip_safe=False
)
