from setuptools import setup

VERSION = "0.1.1"

setup(
    name="Znode",
    version=VERSION,
    description="Znode, or Zero Node, is a messaging module built on the ØMQ framework.",
    url="https://github.com/wpritom/Znode",
    author='Pritom Mojumder',
    author_email='pritom.blue2@gmail.com',
    license='MIT',
    packages=['znode'],
    install_requires=[
        "pyzmq==26.2.0"
    ],
    python_requires='>=3.8',
    zip_safe=False
)