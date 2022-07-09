import sys

def main():

    book=int(input('How many books do you want to order at wholesale?\n'))
    cp=24.95/40*100
    sc=0.75*book-1+3
    totalcost=book+cp+sc
    print('The cost of buying and shipping n books:',totalcost)
  

    
    
    
    
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))
