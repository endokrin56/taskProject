# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
a =[[]]*3
print(a)
b= a.pop()
print(b)
b.append(42)
print(b)

while True:
  filename = input(' Введите файл:')
  if  filename== "clear-memory":
      break
  f = open(filename)
  wordcount = 0
  for line in f:
    words = line.split()
    if words == 'червяк':
        words += 1
  print(wordcount)
