from typing import Union

def replacing(string: str, config: Union[list, tuple]) -> tuple:
    "Prepare config string"
    pairs = {}
    for pair in config:
        p = pair.strip()
        pairs[p[0]] = p[-1]
    
    "Character replacement and counting substitutions"
    new_str = ""
    count = 0
    for ch in string:
        if ch in pairs:
            count += 1
            new_str += pairs[ch]
        else:
            new_str += ch
    return new_str, count

if __name__ == "__main__":
    print(replacing("aaadxxddxxdwww", ['d=x', 'x=6']))