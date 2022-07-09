import sys

def main():
    
    priceofthemeal=int(input('Enter price for meal\n'))
    
    Tip=priceofthemeal/7*100
    print('Tip amount',round(Tip,0))
    
    Salestax=priceofthemeal/15*100
    print('sales tax amount=',round(Salestax,0))
    
    total=Tip+Salestax

    print('The total amount=',round(total,0))
    
    
    
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))





