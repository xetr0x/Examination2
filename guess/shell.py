#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import game


class Shell(cmd.Cmd):
    """the cmd and its commands"""
    
    def __init__(self):
        super().__init__()
        self.game = game.Game()
    
    # TODO make some commands that can be useful
    # TODO making a menu with on press option
    # TODO look with teacher if keyboard library is allowed

