#!usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'dAwn_'

'url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    findUsers = await User.findAll()
    return {
        # 教程这里是template 而在app.py中调用时却使用的templating
        '__templating__': 'test.html',
        'users': findUsers
    }
