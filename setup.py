import setuptools

setuptools.setup(
    name="samuranium",
    version="0.5.1",
    author="Alexis Giovoglanian",
    author_email="alexisgiovoglanian@southerncode.us",
    description="Testing framework",
    long_description='Samuranium',
    long_description_content_type="text/markdown",
    url="https://github.com/malazaysc/samuranium2",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "Samuranium"},
    packages=setuptools.find_packages(where="Samuranium"),
    python_requires=">=3.6",
    install_requires=[
        'selenium',
        'webdriver-manager',
        'behave',
    ],
)
