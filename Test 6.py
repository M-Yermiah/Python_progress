import sys


def main():
    
    value=int(input('Enter a number\n'))
    print(value,value*2,value*3,value*4,value*5,sep='---')
    
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))