#!/usr/bin/python
import sys
import os

template = """\
import unittest

class Test%s(unittest.TestCase):
    def setUp(self):
        pass

    def teardown(self):
        pass

if __name__ == '__main__':
    unittest.main()
"""


def make_unit_test(file_name):
    abs_filename = os.path.abspath(file_name)
    abs_path, abs_name = os.path.split(abs_filename)
    if not abs_name.endswith('.py'):
        abs_name = abs_name.rsplit('.',1)[0] + '.py'
    raw_name = abs_name[:-3]
    test_name = 'test_' + abs_name

    if os.path.isfile(test_name):
        result = raw_input("File exists `%s`, overwrite (y/N)?" % test_name)
        if not result.lower() in ('y','yes'):
            print "Skipping..."
            return

    # Create test file
    with file(test_name, 'w') as f:
        f.write(template % raw_name.capitalize())


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "usage: new_unit_test.py <filename>"
        sys.exit(1)

    for f in sys.argv[1:]:
        make_unit_test(f)


