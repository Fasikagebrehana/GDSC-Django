def basic_operations(x, y):
    try:
        add = x + y
        substract = x - y
        multiply = x * y
        divide = x / y
        dic = {}
        lis = ["addition", "substraction", "multiplication", "division"]
        op = [add, substract, multiply, divide]
        for i in range(4):
            dic[lis[i]] = op[i]
        return dic
    except ZeroDivisionErr:
        print("Error: Division by zero")
    except Exception as e:
        print("Error", e)
print(basic_operations(5,10))



def power_operation(base, ex, **kwargs):
    try:
        ans = base ** ex
        if 'modulo' in kwargs:
            modulo = kwargs['modulo']
            ans = ans % modulo
        return ans
    except Exception as e:
        print("Error", e)
print(power_operation(2,4))
print(power_operation(2,4, modulo = 4))

def apply_operations(operation_list):
    try:
        results = []
        for operation, args in operation_list:
            result = operation(*args)
            results.append(result)
        return results
    except Exception as e:
        print("Error:", e)


operation_list = [
    (basic_operations, (10, 5)),
    (power_operation, (2, 3)),
    (power_operation, (2, 3), {'modulo': 5}),
]

results = apply_operations(operation_list)
print(results)

import os
import glob
import shutil
import time

def update_files(file_list):
    for file_path in file_list:
        with open(file_path, 'r') as file:
            content = file.read()

        timestamp = time.strftime("_%Y%m%d%H%M%S", time.localtime())
        updated_content = content + timestamp

        with open(file_path, 'w') as file:
            file.write(updated_content)

def main():
    current_directory = os.getcwd()

    folder_name = 'last_24hours'
    last_24hours_folder = os.path.join(current_directory, folder_name)
    if not os.path.exists(last_24hours_folder):
        os.mkdir(last_24hours_folder)

    pattern = '*'
    recent_files = glob.glob(pattern)
    recent_files = [file for file in recent_files if os.path.isfile(file) and time.time() - os.stat(file).st_mtime <= 24 * 60 * 60]

    update_files(recent_files)

    for file in recent_files:
        destination_path = os.path.join(last_24hours_folder, file)
        shutil.move(file, destination_path)

    print("Files updated and moved successfully!")

if __name__ == '__main__':
    main()