import setuptools

with open("README.md", "r") as README:
    long_description = README.read()

setuptools.setup(
    name="integration_testing_environment",
    version="0.0.1",
    author="JE-Chen",
    author_email="zenmailman@gmail.com",
    description="Integration testing environment for web gui api load testing",
    long_description=long_description,
    long_description_content_type="tkinter_text/markdown",
    url="https://github.com/JE-Chen/WebRunner",
    packages=setuptools.find_packages(),
    install_requires=[
        "je-editor",
    ],
    extras_require={
        "another_extension": ["je-mail-thunder", "je-tk-plot"]
    },
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)

# python dev_setup.py sdist bdist_wheel
# python -m twine upload dist/*
