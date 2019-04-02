# Copyright (C) 2015-2019 by Vd.
# This file is part of RocketGram, the modern Telegram bot framework.
# RocketGram is released under the MIT License (see LICENSE).


from os.path import join, dirname

import setuptools

import rocketgram

setuptools.setup(
    name='rocketgram',
    version=rocketgram.version(),
    author='Vd',
    author_email='vd@vd2.org',
    url='https://github.com/vd2org/rocketgram',
    license='MIT',
    description='Modern and powerful asynchronous telegram bot framework.',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    packages=['rocketgram'],
    install_requires=open(join(dirname(__file__), 'requirements.txt')).read().split('\n'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
