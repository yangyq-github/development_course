#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/17 16:04
# @File  : settings.py
__author__ = 'yangyanqin'

class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.game_title = "Alien Invasion"