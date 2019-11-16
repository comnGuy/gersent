import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gersent",  # Replace with your own username
    version="0.0.5",
    author="Bernhrd Preisler",
    author_email="bpblub@gmail.com",
    description="Easy german sentiment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/comnGuy/gersent",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)
