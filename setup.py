from setuptools import setup

VERSION = "0.1.3"

setup(
    name="znode",
    version=VERSION,
    description="Znode, or Zero Node, is a messaging module built on the ØMQ framework.",
    url="https://github.com/ipritom/Znode",
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