from pathlib import Path

import setuptools

setuptools.setup(
    name='pg-mutex',
    version="1.0.0",
    long_description_content_type="text/markdown",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    py_modules=['mutex'],
    install_requires=['psycopg2-binary'],
    python_requires='>=3.7',
)
