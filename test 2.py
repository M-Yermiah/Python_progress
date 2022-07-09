

import sys

def main():

    base=int(input('Enter Base:\n'))
    ex=int(input('Enter Exponent:\n'))
    p=(base**ex)
    print(base,'power',ex,'is',p)


    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))



