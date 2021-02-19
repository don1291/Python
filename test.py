def main():
    name = 'Brave.Sir.Robin'
    for word in name.split('.'):
        print(word)
main()

def main():
    s = 'Trump 31 647.29'
    name,age,money = s.split()
    print(name)
    print(age)
    print(money)
main()

while True:
    try:
        x = int(input('Enter the number:  '))
        break
    except ValueError:
        print('No Valid Number.')
