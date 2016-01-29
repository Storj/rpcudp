#!/usr/bin/env python
from setuptools import setup, find_packages
from storjrpcudp import version

setup(
    name="storjrpcudp",
    version=version,
    description="RPC via UDP",
    long_description=open("README.markdown").read(),
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="MIT",
    url="https://github.com/Storj/storjrpcudp",
    packages=find_packages(),
    requires=[
        "twisted.internet.protocol.DatagramProtocol", "umsgpack", "future"
    ],
    install_requires=['twisted>=12.0', "u-msgpack-python>=1.5", "future>=0.6"]
)
