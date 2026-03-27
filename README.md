pythontutor.com
(para aprender estrutura)

numero = int(input("Digite o numero: "))

if numero > 0:
    if numero %2 != 0:
        print("Positivo e impar")
    else:
        print("Negativo e par")
else:
    if numero == 0:
        print("Zero")
    else:
        print("Negaivo")
        
#Ex.2
            
valor = float(input("Digite um valor: "))
vip = input("É uma cliente vip (sim/Não)")

if valor >= 200 and vip == 'sim':
    print("Acesso liberado!")
elif valor < 200 and vip == 'sim':
    print("Vamos acionar o gerente para verificar!")
else:
    print("Cliente sem desconto!")
    
#Ex.3
senha = input("Digite sua senha: ")

if senha == "1234":
    print("Acesso liberado")
else:
    if senha != "1234":
        print("Senha errada!")
        senha_nova = input("Redefinir senha: ")
        print("Sua senha nova foi redefinada para:", senha_nova)
        
#Ex.4
senha_do_usuario = (input("Digite a senha de usuario: "))

if senha_do_usuario == '1234':
    print("Senha correta!!!")
else:
    print("Senha incorreta!")
    
#Ex.5
while True:
    numero = int(input("DIgite o numero, vamos analisar: "))

    if numero % 2 == 0:
        print("Numero par!")
    else:
       print("Numero impar!")
       
#Ex.6
    
salario = float(input("Digite o sálario: "))

if salario <= 2000:
    print("Não terá desconto nesse salário", salario)
elif salario <= 3500:
    print("Salario foi descontado:", salario - (salario * 10/100))
elif salario <= 5000:
    print("Salario foi descontado:", salario - (salario * 20/100))
elif salario > 5000:
    print("Salario foi descontado:", salario - (salario * 27.5/100))

#Ex.7

primeiro = int(input("Digite o primeiro numero para somar: "))
segundo = int(input("Digite o segundo numero para somar: "))

print("A soma dos numeros:", primeiro + segundo)


#Ex.8
import time

soma = int(input("Digite o numero para multiplicar: "))
soma2 = int(input("Digite os numero para multiplicar: "))

print("A multiplicação do numero", soma *soma2)
time.sleep(1)

divisao = int(input("Digite os numero para dividir: "))
divisao2 = int(input("Digite os numero para dividir: "))

print("A divisão do numero: ", divisao /divisao2)
