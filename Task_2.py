import re


pattern = r"\n"
removing = ""
cats_info = []

def get_cats_info(path):
    try:
        with open(path, "r", encoding='utf-8') as file:
            text_in_file = file.readlines()
            for ln in text_in_file:
                line_data = re.split(',', ln)
                new_cat_info = {"id": line_data[0], "name": line_data[1], "age": line_data[2]}
                #new_cat_info = {"id": line_data[0], "name": line_data[1], "age": (re.sub(pattern, removing, line_data[2]))}
                cats_info.append(new_cat_info)
        return cats_info    
    except FileNotFoundError:
        return print("file not found")


cats_info = get_cats_info("cats_info.txt")
print(cats_info)