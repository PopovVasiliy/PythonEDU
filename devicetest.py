import unittest

from devices.Device import *


class DeviceTestCase(unittest.TestCase):
    def test_open_device(self):
        self.assertIsInstance(open_device('/devices/dev0'), Device)
        self.assertIsInstance(open_device('/devices/dev1'), Device)
        self.assertIsInstance(open_device('/devices/dev2'), Device)
        self.assertIsInstance(open_device('/devices/dev3'), Device)
        self.assertIsInstance(open_device('/devices/dev4'), Device)

        # self.assertRaises(IOError, open_device, '/devices/unknown')

    def test_read_line(self):
        self.assertEqual('line_1', read_line(open_device('/devices/dev0')))
        self.assertRaises(PermissionError, read_line, open_device('/devices/dev1'))
        self.assertRaises(IOError, read_line, open_device('/devices/dev2'))
        self.assertEqual('1', read_line(open_device('/devices/dev3')))
        self.assertEqual('line_1', read_line(open_device('/devices/dev4')))

    def test_write_line(self):
        self.assertEqual('35', write_line(open_device('/devices/dev1'), '35'))
        self.assertRaises(PermissionError, write_line, open_device('/devices/dev0'),'24')
        self.assertRaises(PermissionError, write_line, open_device('/devices/dev1'),'stroka2')
        self.assertEqual('7878756', write_line(open_device('/devices/dev1'), '2314'))


if __name__ == '__main__':
    unittest.main()