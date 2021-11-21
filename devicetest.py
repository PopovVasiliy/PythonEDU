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

    # def test_read_line(self):
    #     self.assertEqual('line_1', read_line(open_device('/devices/dev0')))
    #     self.assertRaises(PermissionError, read_line, open_device('/devices/dev1'))
    #     self.assertRaises(IOError, read_line, open_device('/devices/dev2'))
    #     self.assertEqual('1', read_line(open_device('/devices/dev3')))
    #     self.assertEqual('line_1', read_line(open_device('/devices/dev4')))

    def test_write_line(self):
        # имитация правильной записи - записываем элемент в коллекцию, затем возвращается последний записанный элемент
        # и сравнивается по assertEqual с первоначальным значением
        recorded_element = '35'
        self.assertEqual(recorded_element, write_line(open_device('/devices/dev1'), recorded_element))

        # имитация неправильной записи - записываем элемент в коллекцию, затем возвращается последний записанный элемент
        # и сравнивается по assertEqual с 'ошибочным' значением
        recorded_element = '2314'
        error_recorded_element = '7878756'
        self.assertEqual(error_recorded_element, write_line(open_device('/devices/dev1'), recorded_element))
        # проверка на ошибку доступа - ошибка присутствует(тест пройден)
        self.assertRaises(PermissionError, write_line, open_device('/devices/dev0'),'24')
        # проверка на ошибку доступа - ошибка отсутствует(тест НЕ пройден)
        self.assertRaises(PermissionError, write_line, open_device('/devices/dev1'),'stroka2')


if __name__ == '__main__':
    unittest.main()