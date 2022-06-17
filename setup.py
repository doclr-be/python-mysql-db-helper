import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mysql_db_helper',
    version='0.0.1',
    author='Doclr',
    author_email='info@doclr.be',
    description='Simple mysql db helper functions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/doclr-be/python-mysql-db-helper',
    project_urls = {
        "Bug Tracker": "https://github.com/doclr-be/python-mysql-db-helper/issues"
    },
    license='MIT',
    packages=['mysql_db_helper'],
    install_requires=['requests'],
)