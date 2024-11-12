from mathsoperation.Mul import mulvalue
from mathsoperation.Div import divvalue
if __name__ == '__main__':
    print('this is main code')
    val1= int(input('Enter any number = '))
    val2= int(input('Enter any number = '))
    Oprant=input('Which math operation do you want to performed ')
    if Oprant.lower() == 'mul' :
        Mul =mulvalue(val1,val2)
        print(f'Multiplicatin = {Mul}')
    elif Oprant.lower() == 'div' :
        Div =divvalue(val1,val2)
        print(f'Divide= {Div}')
    else:
        print('Please choose correct operation either mul or div')