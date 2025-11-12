
def reverse_str(s: str)->str:
    return s[::-1]

def to_upper(s: str)->str:
    return  s.upper()

def remove_vowels(s: str) -> str: 
    vowels = ["A","E","I","O","U"]
    for i in s:
        if i in vowels:
            s = s.replace(i, "")
    return s

print(reverse_str("HELLO WORLD"))
    

def remove_every_third(s: str) -> tuple[str, list[int], list[str]]: 
    pass

def letter_counts_map(s: str) -> dict[str, int]: 
    pass