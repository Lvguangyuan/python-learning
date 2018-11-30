#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""learning use class demo"""

__author__ = 'Tyrion Lv'


class Student(object):
    count = 0

    # __slots__ = ('name', 'gender', 'score', 'grade', 'height')

    def __init__(self, name='duconghui', gender='female', score='98', height=160):
        self.__name = name
        self.__gender = gender
        self.__score = score
        self.__height = height
        Student.count += 1

    def print_info(self):
        print('name:%s gender:%s score:%s height:%scm' % (self.__name, self.__gender, self.__score, self.__height))

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    @property
    def score(self):
        return self.__score

    @property
    def height(self):
        return self.__height

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('not a gender')

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = score

    def __len__(self):
        return 3

    def __str__(self):
        return 'Student: %s' % self.__name

    __repr__ = __str__


from enum import Enum, unique


@unique
class Gender(Enum):
    Male = 0
    Female = 1
