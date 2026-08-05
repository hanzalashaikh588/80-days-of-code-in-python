import os
folder_path= r"c:\Users\Lenovo\Desktop\PythonCode"
for day in range(46,101):
    file_name=f"python day {day}.py"
    file_path=os.path.join(folder_path, file_name)

    if not os.path.exists(file_path):
        with open(file_path,"w"):
            pass
        print(f"Created: {file_name}")
    else:
        print(f"skipped (already exists): {file_name}")
    