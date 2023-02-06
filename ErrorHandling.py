#Error Handling 

while  True:
    try:
        age = int (input('What is your age?'))
        10/age
        raise Exception('Hey cut it out')
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        print('Thank You')
        break  
    finally:
        print('ok ,i am finally done')          

def sum(num1,num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(err)
    except (ValueError,ZeroDivisionError) as err:
        print(err)    

print(sum(1,jankj))            