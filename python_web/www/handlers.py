#!usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'dAwn_'

'url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
#    findUsers = await User.findAll()
#    return {
#        # 教程这里是template 而在app.py中调用时却使用的templating
#        '__templating__': 'test.html',
#        'users': findUsers
#    }
    summary = 'Some text'
    blogs = [
        Blog(id = '1', name = 'Test Blog', summary = summary, created_at = time.time() - 120),
        Blog(id = '2', name = 'something New', summary = summary, created_at = time.time() - 3600),
        Blog(id = '3', name = 'Learn Swift', summary = summary, created_at = time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }
