from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="lines-pubsub", # Replace with your own username
    version="0.0.1",
    author="Howard Jeong",
    author_email="1lines.maker@onelines.org",
    description="Lines Python Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keepinmindsh/lines_python_library",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)