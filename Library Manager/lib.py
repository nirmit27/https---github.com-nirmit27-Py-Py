# Library Interface
from mgmt import Management as mgmt


class Library(mgmt):

    def show(self):
        i = 0
        with open('lib.txt') as f:
            self.lines = f.readlines()
            if len(self.lines):
                for line in self.lines:
                    auth, books = line.split(',')
                    i += 1
                    print(
                        f' {i}. Author Name : {auth} \n    Available Books : {books}')
            else:
                print(" The library is currently empty!")

    def find(self, b='', a='', occurence='first'):
        flag = 0
        with open('lib.txt') as f:
            self.lines = f.readlines()
        if len(self.lines):
            if a != '' and b != '':
                for line in self.lines:
                    if a.title() in line:
                        books = line.lstrip(f'{a.lower()}')
                        print(f'\n Books available from {a} :\n {books}')
                        flag = 1
                if flag == 0:
                    print(
                        '\n The requested author is not present in the list.\n   Do you want to add him/her to the list? (Y/N) : ')
                    ch = input().lower()
                    if ch == 'y':
                        book = input(
                            '\n Enter the name of the book written by  the author :')
                        super().add(book.lower(), a.lower())
                    else:
                        print("\n Okay, thank you.\n")
            elif b != '' and a == '':
                for line in self.lines:
                    if b.title() in line and occurence == 'first':
                        a = line.split(',')
                        print(f"\n Author of this books is : {a[0]}\n")
                        flag = 1
                        break
                    elif b.title() in line and occurence == 'all':
                        a = line.split(',')
                        print(f"\n Author of this book is : {a[0]}\n")
                        flag = 1
                if flag:
                    print(
                        "\n This book isn't present in the library.\n Do you want to add it to the library? (Y/N) : ")
                    ch = input().lower()
                    match ch:
                        case 'y':
                            a = input('\n Enter the name of the author : ')
                            super().add(b.lower(), a.lower())
                        case _:
                            print("\n Okay, thank you.\n")
        else:
            print(" The library is currently empty!")