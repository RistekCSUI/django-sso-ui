import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="django-sso-ui",
    version="1.0.0",
    description="A simple SSO UI CAS wrapper for Django",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/RistekCSUI/django-sso",
    author="Fata Nugraha",
    author_email="fatanugraha@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["django_sso_ui"],
    include_package_data=True,
    install_requires=["python-cas", "django"],
)
