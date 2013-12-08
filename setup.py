# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='signapadpy',
    version='0.0.1',
    author='Kevin Wetzels',
    author_email='kevin@roam.be',
    url='https://github.com/roam/signapadpy',
    install_requires=['Pillow>=1.7'],
    packages=['signapadpy'],
    license='BSD',
    description='Turn output from Signature Pad into images',
    long_description=open('README.rst').read(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
   ],
)
