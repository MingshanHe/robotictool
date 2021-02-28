import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robotictools", # Replace with your own username
    version="0.0.1",
    author="He Mingshan",
    author_email="hemingshan_1999@163.com",
    description="A small package tool for robotic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MingshanHe/robotictool",
    project_urls={
        "Bug Tracker": "https://github.com/MingshanHe/robotictool/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)