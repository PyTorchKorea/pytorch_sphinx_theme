from setuptools import setup
from io import open
import re

def get_version():
    with open('pytorch_sphinx_theme/__init__.py', 'r') as f:
        return re.search(r"__version__ = '([^']+)'", f.read()).group(1)

setup(
    name = 'pytorch_sphinx_theme',
    version=get_version(),
    author = 'Shift Lab',
    author_email= 'info@shiftlabny.com',
    url="https://github.com/pytorchkorea/pytorch_sphinx_theme",
    docs_url="https://github.com/pytorchkorea/pytorch_sphinx_theme",
    description='PyTorch Sphinx Theme',
    py_modules = ['pytorch_sphinx_theme'],
    packages = ['pytorch_sphinx_theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={'pytorch_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/js/vendor/*.js',
        'static/fonts/FreightSans/*',
        'static/fonts/IBMPlexMono/*',
        'static/images/*.*',
        'theme_variables.jinja'
    ]},
    entry_points = {
        'sphinx.html_themes': [
            'pytorch_sphinx_theme = pytorch_sphinx_theme',
        ]
    },
    license= 'MIT License',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation"
    ],
    install_requires=[
       'sphinx'
    ]
)
