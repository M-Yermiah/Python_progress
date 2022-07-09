import sys 
import math

def main():
    
    pn=int(input('Enter a positive number:\n'))
    value=(math.sqrt(pn))

    print('To','2','decimal place', pn,'square root','is',round(value,2))
    
    
    
    
    
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))
