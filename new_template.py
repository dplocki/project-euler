import os

existing_files = sorted((file for file in os.listdir('.') if file.endswith('.py')), reverse=True)
last_file = existing_files[0]
last_file_number = int(last_file[1:-3])
new_file_number = last_file_number + 1
new_file_name = f'p{new_file_number:04}.py'

with open(new_file_name, "w") as new_file:
    new_file.write(f'''# https://projecteuler.net/problem={new_file_number})

''')
