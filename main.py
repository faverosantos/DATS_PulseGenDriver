

import pgdriver as pgdriver

def main():
    print("Main says: aloha!")

    pgdriver.configure()
    pgdriver.enable()
    pgdriver.disable()

    print("Main says: see you, space cowboy!")




if __name__ == '__main__':
    main()