fptr=lambda number1,number2:number1*number2;
def main():
    number1=int(input("Enter 1st number: "));
    number2=int(input("Enter 2nd number: "));
    print("lambda__Square is: ",fptr(number1,number2));

if __name__=="__main__":
    main();
