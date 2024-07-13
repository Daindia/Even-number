def find_even_numbers(integer):
    
    print(f'Even numbers smaller than/equal to {integer}:')
    while integer > 0:
        if integer%2 == 0:
            integer += 1
            continue        
        print(integer)    
        integer -= 1
    