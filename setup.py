import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="getjson",
    version="1.2.0",
    description="Request JSON data en masse with backoff and failover",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/getjson",
    author="microprediction",
    author_email="info@microprediction.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["getjson"],
    test_suite='pytest',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=["backoff","requests","grequests"],
    entry_points={
        "console_scripts": [
            "getjson=getjson.__main__:main",
        ]
     },
     )
