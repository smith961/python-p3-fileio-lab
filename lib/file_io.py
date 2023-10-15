def write_file(file_name, file_content):
    
    file = open(f"{file_name}.txt", mode='w', encoding='utf-8')
    file.write(file_content)

def append_file(file_name, append_content):
    
    file = open(f"{file_name}.txt", mode='a', encoding='utf-8')
    file.write(append_content)

def read_file(file_name):
    file = open(f"{file_name}.txt", mode='r', encoding='utf-8')
    return file.read()