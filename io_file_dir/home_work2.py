#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('current dir is %s' % os.path.abspath('.'))


def OutputFile(dir, file_name):
    print('%s/%s' % (dir, file_name))


def OutputDir(dir):
    for f in os.listdir(dir):
        if os.path.isdir(f):
            OutputDir(f)
        else:
            OutputFile(dir, f)


OutputDir('.')
