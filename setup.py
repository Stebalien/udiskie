# encoding: utf-8
from distutils.core import setup

setup(
    name='udiskie',
    version='0.4.2',
    description='Removable disk automounter for udisks',
    author='Byron Clark',
    author_email='byron@theclarkfamily.name',
    maintainer='Thomas Gläßle',
    maintainer_email='t_glaessle@gmx.de',
    url='https://github.com/coldfix/udiskie',
    license='MIT',
    packages=[
        'udiskie',
    ],
    scripts=[
        'bin/udiskie',
        'bin/udiskie-umount',
    ],
)
