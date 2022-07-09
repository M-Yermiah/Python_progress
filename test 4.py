
import sys
import math



def main():
     
    
    bs=int(input('Input Basic salary\n'))
    
    da=bs/50*100
    
    print('DA:',da)
    
    hra=bs/30*100
    
    print('HRA',hra)
    
    totalsalary=bs+da+hra
    
    print('Total salary:',totalsalary)
    
    

    
    
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))
