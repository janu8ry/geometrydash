import setuptools
import re

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('geometrydash/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setuptools.setup(
    name="geometrydash",
    version=version,
    author="janu8ry",
    author_email="janu8ry0108@gmail.com",
    url="https://github.com/janu8ry/geomertydash",
    licence="GPL-3.0",
    description="A Python wrapper for Geometry Dash API.",
    long_decription=readme,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    project_urls={
        "Homepage": "https://janu8ry.github.io",
        "Source": "https://github.com/janu8ry/geometrydash",
        "Tracker": "https://github.com/janu8ry/geometrydash/issues"
    },
    install_requires=requirements,
    keywords=['GeometryDash', 'GD', 'GMD', 'Geometry Dash', 'game', 'api wrapper'],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
