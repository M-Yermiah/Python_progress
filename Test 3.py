

import sys
import math


def main():
    radius=int(input('Input radius\n'))
    p=round(math.pi,2)
    r=4/3*p*radius*3
    print('Print volume of a sphere.',r)
    
    
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))