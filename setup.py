from distutils.core import setup

setup(
    name='gcp_secret_manager_wrapper',
    packages=['gcp_secret_manager_wrapper'],
    version='0.0.1',
    license='AGPL',
    description='Python wrapper for Secret Manager',
    author='onsentamago',
    author_email='ontama_minimal@protonmail.com',
    url='https://github.com/onsentamago/gcp_secret_manager_wrapper',
    download_url='https://github.com/onsentamago/gcp_secret_manager_wrapper/archive/0.0.1.tar.gz',
    keywords=['GCP', 'Secret Manager'],
    install_requires=[
        'google-cloud-secret-manager ~= 2.1.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Cloud Tools',
        'License :: OSI Approved :: AGPL License',
        'Programming Language :: Python :: 3.8',
    ],
)
