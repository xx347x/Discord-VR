from setuptools import find_packages, setup

setup(
    name="discord-vr",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="Make your discord.py bots appear as if they are in VR.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="discord vr discord.py discord bot status vr presence",
    url="https://github.com/xx347x/Discord-VR",
    author="xx347x",
    author_email="inquire@upset.bot",
    python_requires=">=3.8",
    install_requires=["discord.py>=2.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
