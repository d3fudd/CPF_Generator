import sys
from random import randint

def cpf_generate():
    while True:
        cpf = [randint(0, 9) for i in range(9)]
        if cpf != cpf[::-1]:
            break

    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        cpf.append(digit)

    result = ''.join(map(str, cpf))
    return result

def main():
    if len(sys.argv) != 2:
        print("\n [!] É necessário informar a quantidade de CPFs a serem gerados.")
        print("     Ex: python cpf_generator.py 15\n")
        return
    
    try:
        count = int(sys.argv[1])
        if count <= 0:
            raise ValueError()
    except ValueError:
        print("\n [!] É necessário informar a quantidade de CPFs a serem gerados.")
        print("     Ex: python cpf_generator.py 15\n")
        return

    for _ in range(count):
        cpf = cpf_generate()
        print(f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')

if __name__ == "__main__":
    main()
