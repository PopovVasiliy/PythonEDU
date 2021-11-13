# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import math

print('Решаем квадратное уравнение вида ax^2+bx+c = 0')
a = int(input('Введите a:'))
b = int(input('Введите b:'))
c = int(input('Введите c:'))

diskriminant = b*b - (4*a*c)
if diskriminant<0:
    print('Дискриминант отрицательный, решения нет')
elif diskriminant==0:
    result = (math.sqrt(diskriminant)-b)/(2*a)
    print('Один корень:', result)
else:
    result1 = (math.sqrt(diskriminant) - b) / (2 * a)
    result2 = (-math.sqrt(diskriminant) - b) / (2 * a)
    print('Один корень:', result1)
    print('Второй корень:', result2)