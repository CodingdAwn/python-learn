#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

with open('./test_file', 'r') as f:
    s = f.read()
    print('reading file ...')
    print(s)
