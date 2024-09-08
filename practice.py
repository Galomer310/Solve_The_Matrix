crazy_string = """
        123
    sdf
        d j
        234
        !@#
        $%^
        &*+
"""

crazy_list = [list(line.strip()) for line in crazy_string.strip().splitlines()]

print(crazy_list)

decoded_message = []
previous_was_alpha = False  

print(range(len(crazy_list[0])))

# for col in range(len(crazy_list[0]))