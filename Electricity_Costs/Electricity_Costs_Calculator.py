#Okay, so the irrigation system works with a diesel powedered pump, which takes water from the reservoir and delivers it to the plantation.
#This engine outputs 60cv, or about 45kW, while consuming 12 to 13 liters of diesel fuel each hour.
#The pump operates about 25 hours each week, split between 2-3 days.

#Variables I'll be using
#diesel consumption and price
#electricity consumption and price
#switching price (that includes new posts, cables, transformers and a new engine)
#solar energy setup price

#diesel price per liter, BRL

#energy price R$ kWh - special rural category for nighttime irrigation.
#okay, so 60cv (about 60hp) equals 44129,9 watts.
#The kWh formula is w x hours of use x days / 1000.
#That means 44129,9 x 8 x 12 / 1000, so 4412.99kWh. 

def horas_trabalho():
    global horas_uso_motor
    global potencia_kw
    print("Quantas horas por mês o motor trabalhará?")
    horas_uso_motor = float(input(">: "))
    potencia_kw = 44129.9
    potencia_kwh()

def potencia_kwh():
    global consumo_mensal_kwh
    consumo_mensal_kwh = (horas_uso_motor * potencia_kw)/1000
    print(f"Considerando um uso de {horas_uso_motor} horas no mês, o consumo de eletricidade será de {consumo_mensal_kwh} kWh.\n")
    print("Agora vamos aos custos da energia elétrica... \n")
    custo_energia()

def custo_energia():

    bandeiras = {
        "Bandeira Verde" : "19829",
        "Bandeira Amarela" : "22818",
        "Bandeira Vermelha 1" : "26329",
        "Bandeira Vermelha 2" : "29624",
        "Bandeira Escassez" : "34029"
    }

    print("As bandeiras de consumo de eletricidade da CEMIG são: \n")

    for x in bandeiras:
        print (x, "\n", "-" * 20, "\n")

    def bandeira():
        while True:
            print("Qual é a bandeira de consumo de energia na região do sítio? \n")
            global escolha_bandeira_atual
            escolha_bandeira_atual = input(">: ")

            if escolha_bandeira_atual in bandeiras:
                print(f"Certo, então atualmente estamos em {escolha_bandeira_atual}. \n")
                #I can't get this to work properly.
                #I need a way to transform the value of the key to a variable, so I can multiply it.
                #There are easier ways to do this, but I don't find them clean enough.

                #It is assigining the key to a function, but not the key I want to.
                for value in bandeiras[escolha_bandeira_atual]:
                    global custo_kwh
                    custo_kwh = int(value)

                preco_eel()

            else:
                print("Certifique-se que você digitou a bandeira corretamente.\n")
    
    bandeira()

def preco_eel():
    print(f"Dessa maneira, o custo do kWh é de R$ 0,{custo_kwh}")
    total_eel = (custo_kwh * consumo_mensal_kwh)
    print(f"Isso significa que o valor do consumo mensal de energia elétrica, ao utilizar um motor elétrico de 45kW por {horas_uso_motor} horas é de R$ {total_eel}, considerando o valor de R$ {custo_kwh} por kWh, em período de {escolha_bandeira_atual}. \n")
    print(f"Òtimo! Agora que sabemos os custos da energia elétrica, precisamos dar uma olhada no diesel. \n")
    custo_diesel()

def custo_diesel():
    print("Atualmente, qual é o valor do litro do diesel?: \n")
    preco_diesel = input(">: ")
    preco_diesel_conv = float(preco_diesel.replace(',', '.'))
    consumo_hora = 13
    valor_mensal_diesel = (preco_diesel_conv * consumo_hora * horas_uso_motor)
    consumo_diesel_total = (consumo_hora * horas_uso_motor)

    #format(valor_diesel, '.2f') -> dar um jeito de formatar isso
    print(f"Legal! O valor mensal gasto atualmente em diesel é de aproximadamente R$ {valor_mensal_diesel}, considerando um valor de R$ {preco_diesel} por litro, com {horas_uso_motor} horas de uso, incorrendo no consumo de {consumo_diesel_total} litros de diesel. \n")
    print("Calculados os custos com diesel e energia elétrica, podemos partir para as despesas com a conversão do sistema.")
    custos_adicionais()

def custos_adicionais():

    print("Insira o preço do motor elétrico")
    motor_preco = float(input(">: "))

    print("Insira o preço total dos cabos de eletricidade")
    cabos_preco = float(input(">: "))

    print("Insira o preço dos postes-padrão")
    postes_preco = float(input(">: "))

    print("Insira quaisquer valores adicionais não previstos pela calculadora")
    adicionais_preco = float(input(">: "))