import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crypto_secret_manager",
    version="0.0.1",
    author="onsentamago",
    author_email="ontama_minimal@protonmail.com",
    description="GCP Secret Manager library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/onsentamago/crypto_secret_manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.7',
)