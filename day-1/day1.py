import re

def getSum(strings:list) -> int:

    str = strings.split("\n")

    digits = [re.findall(r"\d",x) for x in str]
    
    return sum(int(n[0] + n[-1]) for n in digits)
    
if __name__ == "__main__":
    with open("input.txt","r",encoding="utf-8") as f:
        strings = f.read().strip()

    print(getSum(strings))

    #Part 2
    strings = (strings.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
    )
    
    print(getSum(strings))