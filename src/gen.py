import random
import string

def generate_config():
    chars = string.ascii_letters + string.digits + string.punctuation
    with open("config.cfg", 'w') as file:
        char1 = char2 = ""
        for line_c in range(random.randint(2, 7)):
            chars = chars.replace(char2, "")
            char1 = random.choice(chars)

            chars = chars.replace(char1, "")
            char2 = random.choice(chars)
            
            file.write(char1 + "=" + char2 + "\n")

def generate_text_file():
    chars = string.ascii_letters + string.digits + string.punctuation
    with open("text.txt", 'w') as file:
        for line_c in range(random.randint(5, 15)):
            line = ""
            for ch in range(random.randint(5, 15)):
                line += random.choice(chars)
            file.write(line + "\n")

if __name__ == "__main__":
    generate_config()
    generate_text_file()