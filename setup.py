import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="codelib", # Replace with your own username
    version="0.0.2",
    author="Madhava",
    author_email="alformint@gmail.com",
    description="handy tool encoding and decoding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Madhava-mng/codelib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
