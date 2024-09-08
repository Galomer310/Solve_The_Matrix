matrix_string = """
    7ii
    Tsx
    h%?
    i #
    sM 
    $a 
    #t%
    ^r!
"""

matrix_list = [list(line.strip()) for line in matrix_string.strip().splitlines()]

decoded_message = []
previous_was_alpha = False  

for col in range(len(matrix_list[0])):  
    for row in matrix_list:
        if col < len(row):  
            char = row[col]
            if char.isalpha():
                decoded_message.append(char)
                previous_was_alpha = True  
            else:
                if previous_was_alpha:  
                    decoded_message.append(' ')
                    previous_was_alpha = False 

final_message = ''.join(decoded_message).split()
final_message = ' '.join(final_message)

print(final_message)
