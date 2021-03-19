# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from os.path import join, dirname

import setuptools

from rocketgram.version import version

setuptools.setup(
    name='rocketgram',
    version=version(),
    author='Vd',
    author_email='vd@vd2.org',
    url='https://github.com/rocketgram/rocketgram',
    license='MIT',
    description='Modern and powerful asynchronous telegram bot framework.',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    extras_require={
        'aiohttp': ["aiohttp >= 3.6.2"],
        'tornado': ["tornado >= 6.0.2"],
        'ujson': ["ujson >= 1.35"],
        'uvloop': ["uvloop >= 0.12.1"]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Environment :: Web Environment",
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
