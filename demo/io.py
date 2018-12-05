#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""learning use io demo"""

__author__ = 'Tyrion Lv'

import os


def show_folder_details(path):
    for v in os.listdir(path):
        v_path = os.path.join(path, v)
        size = os.path.getsize(v_path)
        mtime = os.path.getmtime(v_path)
        print(size, v, mtime)

