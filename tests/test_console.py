#!/usr/bin/python3
"""Unittest module for console"""
import unittest
import cmd
import os
import pep8
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import json

run = os.system


class TestHBNBCommand(unittest.TestCase):
    """Class to test console commands"""

    def test_docstring(self):
        """Checking docstring for all methods"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCOmmand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCOmmand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCOmmand.do_create.__doc__)
        self.assertIsNotNone(HBNBCOmmand.do_show.__doc__)
        self.assertIsNotNone(HBNBCOmmand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCOmmand.do_all.__doc__)
        self.assertIsNotNone(HBNBCOmmand.do_update.__doc__)

    def test_pep8(self):
        """Checking pep8 style"""
        pep8style = pep8.StyleGUide(quite=True)
        result = pep8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0)

    def test_first_create(self):
        """First create test"""
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        run("echo 'create State' | ./console.py" + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)

    def test_second_create(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        run('echo create State name="California" | ./console.py' + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)

    def test_third_create(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        command = 'echo create City state_id="1" name="San_Francisco" '
        command = command + '| ./console.py '
        run(command + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)
