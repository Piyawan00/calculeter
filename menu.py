import one #prototype
import two
import three
import four

Add=1
Substeact=2
Multiply=3
Divide=4
Quit=5

def main():
    chioce = 0
    while chioce !=Quit:
        display_manu()
        chioce =int(input("Selec your operation"))
        if chioce ==Add:
            num1=float(input("Enter you first number: "))
            num2=float(input("Enter you second number: "))
            print("The result is",one.add(num1,num2))
        elif chioce== Substeact:
             num1=float(input("Enter you first number: "))
             num2=float(input("Enter you second number: "))
             print("The result is",two.substract(num1,num2))
        elif chioce == Multiply:
             num1=float(input("Enter you first number: "))
             num2=float(input("Enter you second number: "))
             print("The result is",three.multiply(num1,num2))   
        elif chioce==Divide:
             num1=float(input("Enter you first number: "))
             num2=float(input("Enter you second number: "))
             print("The result is",four.devide(num1,num2)) 
        elif chioce==Quit:
            print("Exite program.")
        else:
            print("Eror")

def display_manu():
    print('Select operation from number')
    print('')
    print('-'*10)
    print('1)Add')
    print('2)Substract   ')
    print('3)Multiply')
    print('4)Devide')
    print('5)Quit')
    print('-'*10)
main()
