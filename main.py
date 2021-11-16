from devices.Device import *
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        deviceRead: Device = open_device('/devices/dev4')
        for i in range(2):
            print(read_line(deviceRead))
    except Exception as exeption:
        print(f'Error: {Exception}')

    try:
        deviceWrite: Device = open_device('/devices/dev1')
        for i in range(3):
            quantity = write_line(deviceWrite,'stroka'+str(i))

        print('Элементов в коллекции после записи:', quantity)

    except Exception as exeption:
        print(f'Error: {Exception}')


