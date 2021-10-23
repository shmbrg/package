from setuptools import setup, find_packages


setup(
    name='package',
    version='0.1.0',
    description='this is a test package',
    author='Sebastian Humberg',
    author_email='sebastian.humberg@gmail.com',
    url='https://github.com/shmbrg/package',
    packages=find_packages(exclude="tests"),
    install_requires=[
        'datatable==1.0.0',
        'pytest-6.2.5'
    ],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.8',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    keywords='test',
)