try:
    from setuptools import setup
except:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
    name = "protlib2",
    version = "1.0",
    py_modules = ["protlib2"],
    cmdclass = {'build_py': build_py},
    
    author = "Ilya Kitaev",
    author_email = "ilya.kitaev@gmail.com",
    description = "library for implementing binary network protocols",
    license = "BSD",
    url = "http://gitlab.cyberviz.org/uo/protlib2",
    download_url = "http://gitlab.cyberviz.org/uo/protlib2/repository/archive.tar.gz?ref=master",
    
    long_description = """
protlib makes it easy to implement binary network protocols. It uses
the struct and SocketServer modules from the standard library. It
provides support for default and constant struct fields, nested structs, 
arrays of structs, better handling for strings and arrays, struct 
inheritance, and convenient syntax for instantiating and using your 
custom structs.

protlib requires Python 2.6 or later and works in Python 3
""",
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking"
    ]
)