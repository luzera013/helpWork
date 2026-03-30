calculadora = input("Escolha a operação(1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): ")
for i in range(1,4):
    if calculadora == 1:
        soma1 = int(input("Digite o primeiro numero da soma: "))
        soma2 = int(input("Digite o segundo numero da soma: "))
        print("A soma dos numeros é: ", soma1 + soma2)
    elif calculadora == 2:
        sub1 = int(input("Digite o primeiro numero da subtração: "))
        sub2 = int(input("Digite o segundo numero da subtração: "))
        print("A subtração dos numeros é: ", sub1 - sub2)
    elif calculadora == 3:
        mult1 = int(input("Digite o primeiro numero da multiplicação: "))
        mult2 = int(input("Digite o segundo numero da multiplicação: "))
        print("A multiplicação dos numeros é: ", mult1 * mult2)
    elif calculadora == 4:
        div1 = int(input("Digite o primeiro numero da divisão: "))
        div2 = int(input("Digite o segundo numero da divisão: "))
        print("A divisão dos numeros é: ", div1 / div2)
    else
        print("Operação inválida, tente novamente!")