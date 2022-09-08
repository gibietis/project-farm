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

def potencia_kwh():
    global horas_uso
    global total_kwh
    horas_uso = float(input("Quantas horas por mês o motor trabalhará?: "))
    potencia_kw = 44129,9
    total_kwh = (horas_uso * potencia_kw)/1000
    print(f"Considerando um uso de {horas_uso} horas no mês, o consumo de eletricidade será de {total_kwh} kWh.")

def custo_energia():

    bandeiras = {
        "Bandeira Verde" : 0.19829,
        "Bandeira Amarela" : 0.22818,
        "Bandeira Vermelha 1" : 0.26329,
        "Bandeira Vermelha 2" : 0.29624,
        "Bandeira Escassez" : 0.34029
    }

    for x in bandeiras:
        print (f"As bandeirasx)

    escolha_bandeira_atual = input("Qual é a bandeira de consumo de energia na região do sítio?: ")
    if escolha_bandeira_atual in bandeiras:
        bandeira_atual = bandeiras[escolha_bandeira_atual]
    else:
        print("Certifique-se que você digitou a bandeira corretamente.")


    bandeira_verde = 
    bandeira_amarela = 
    bandeira_vermelha_1 = 
    bandeira_vermelha_2 = 
    bandeira_escassez = 
    bandeira = input
    custo_energia_eletrica = 


def custo_diesel():
    preco_diesel = float(input("Qual é o valor do litro do diesel atualmente?: "))
    consumo_hora = 13
    valor_diesel = preco_diesel * consumo_hora * horas_uso
    print(f"O valor mensal gasto em diesel é de aproximadamente R$ {valor_diesel}, considerando um valor de R$ {preco_diesel} por litro, com {horas_uso} horas de uso.")




    


