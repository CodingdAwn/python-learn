#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

obj = dict(name='小明', age=18)
s = json.dumps(obj, ensure_ascii = False)
print(s)
