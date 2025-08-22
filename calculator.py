#importing modules
import addition
import subtraction
import multipication
import division
import modulus

opertions=(
    "1.addition\n",
    "2.subtraction\n",
    "3.multiplication\n",
    "4.division\n",
    "5.modulus\n"
)



#main function
if __name__ ==  "__main__":
    print(opertions)
    choice=int(input("please select operation:"))
    if choice==1:
        a,b=map(int,input("please enter two values with space:").split())
        res=addition.add(a,b)
        print("sum of two numbers:",res)
    elif choice==2:
        a,b=map(int,input("please enter two values with space:").split())
        res=subtraction.sub(a,b)
        print("sub of two numbers:",res)
    elif choice==3:
        a,b=map(int,input("please enter two values with space:").split())
        res=multipication.mul(a,b)
        print("mul of two numbers:",res)
    elif choice==4:
        a,b=map(int,input("please enter two values with space:").split())
        res=division.div(a,b)
        print("div of two numbers:",res)
    elif choice==5:
        a,b=map(int,input("please enter two values with space:").split())
        res=modulus.mod(a,b)
        print("mod1 of two numbers:",res)
    else:
        print("please select between 1-5")
        




    

