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
    global horas_uso
    global potencia_kw
    print("Quantas horas por mês o motor trabalhará?")
    horas_uso = float(input(">: "))
    potencia_kw = 44129.9
    potencia_kwh()

def potencia_kwh():
    global total_kwh
    total_kwh = (horas_uso * potencia_kw)/1000
    print(f"Considerando um uso de {horas_uso} horas no mês, o consumo de eletricidade será de {total_kwh} kWh.\n")
    custo_energia()

def custo_energia():

    bandeiras = {
        "Bandeira Verde" : 0.19829,
        "Bandeira Amarela" : 0.22818,
        "Bandeira Vermelha 1" : 0.26329,
        "Bandeira Vermelha 2" : 0.29624,
        "Bandeira Escassez" : 0.34029
    }

    print("As bandeiras de consumo de eletricidade são: \n")

    for x in bandeiras:
        print (x, "\n", "-" * 20)

    def bandeira():
        while True:
            print("Qual é a bandeira de consumo de energia na região do sítio?")
            escolha_bandeira_atual = input(">: ")

            if escolha_bandeira_atual in bandeiras:
                global bandeira_atual
                bandeira_atual = bandeiras[escolha_bandeira_atual]
                print(bandeira_atual)
                global custo_kwh
                custo_kwh = val
                preco_eel()
            else:
                print("Certifique-se que você digitou a bandeira corretamente.\n")
    
    bandeira()

def preco_eel():
    total_eel = (custo_kwh * total_kwh)
    print(f"""O valor do consumo mensal de energia elétrica, ao utilizar um motor elétrico de 45kW por {horas_uso} horas é de 
    R$ {total_eel}, considerando o valor de R$ {custo_kwh} por kWh, em período de {bandeira_atual}. \n""")
    custo_diesel()

def custo_diesel():
    print("Qual é o valor do litro do diesel atualmente?: \n")
    preco_diesel = input(">: ")
    preco_diesel_conv = float(preco_diesel.replace(',', '.'))
    consumo_hora = 13
    valor_diesel = (preco_diesel_conv * consumo_hora * horas_uso)
    format(valor_diesel, '.2f')
    print(f"O valor mensal gasto atualmente em diesel é de aproximadamente R$ {valor_diesel}, considerando um valor de R$ {preco_diesel} por litro, com {horas_uso} horas de uso.\n")


    


