from setuptools import setup, find_packages

setup(
    name="Proxy",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
        'threadpool',
        'sqlalchemy',
    ],

    url="https://github.com/SilverW0o0W/Proxy",
    author="Silver",
    author_email="silver.codingcat@gmail.com",
    license='MIT',
    description="",

    entry_points={
    }
)
