def check(para):
    no_of_square_brackets = 0
    no_of_round_brackets = 0
    no_of_curly_brackets = 0

    for symbol in para:
        if symbol == '(':
            no_of_round_brackets += 1
        elif symbol == '{':
            no_of_curly_brackets += 1
        elif symbol == '[':
            no_of_square_brackets += 1
        elif symbol == ')':
            no_of_round_brackets -= 1
        elif symbol == '}':
            no_of_curly_brackets -= 1
        elif symbol == ']':
            no_of_square_brackets -= 1

    if no_of_round_brackets+no_of_curly_brackets+no_of_square_brackets == 0:
        return 'The File Brackets are Balanced'
    else:
        return 'The File Brackets are not Balanced'


file_path = 'test.txt'
file_text=''


try:
    with open(file_path, 'r') as file:
        for line in file:
            file_text += line.strip()
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


print(check(file_text))