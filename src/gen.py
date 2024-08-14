import random
import string

def generate_configuration_file(file_name: str):
    chars = string.ascii_lowercase
    with open(file_name, 'w') as file:
        char1 = char2 = ""
        for line_c in range(random.randint(3, 10)):
            chars = chars.replace(char2, "")
            char1 = random.choice(chars)

            chars = chars.replace(char1, "")
            char2 = random.choice(chars)
            
            file.write(char1 + "=" + char2 + "\n")

def generate_text_file(file_name: str):
    chars = string.ascii_lowercase*15 + string.digits + string.punctuation
    with open(file_name, 'w') as file:
        for line_c in range(random.randint(7, 15)):
            line = ""
            for ch in range(random.randint(7, 15)):
                line += random.choice(chars)
            file.write(line + "\n")

if __name__ == "__main__":
    generate_configuration_file("config.cfg")
    generate_text_file("text.txt")