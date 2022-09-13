import sys

def horas_trabalho():
    global horas_uso_motor
    global potencia_kw
    print("Quantas horas por mês o motor trabalhará? Insira o valor inteiro de horas trabalhadas, sem pontos ou vírgula. Ex.: 100")
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
        "Bandeira Verde" : "0.19829",
        "Bandeira Amarela" : "0.22818",
        "Bandeira Vermelha 1" : "0.26329",
        "Bandeira Vermelha 2" : "0.29624",
        "Bandeira Escassez" : "0.34029"
    }

    print("As bandeiras de consumo de eletricidade da CEMIG são: \n")


    for x in bandeiras:
        print (x, "\n", "-" * 20, "\n")


    def bandeira():
        while True:
            print("Qual é a bandeira de consumo de energia na região do sítio? Digite exatamente como as opções, inclusive com letras maiúsculas. \n")
            global escolha_bandeira_atual
            escolha_bandeira_atual = input(">: ")

            if escolha_bandeira_atual in bandeiras:
                print(f"Certo, então atualmente estamos em {escolha_bandeira_atual}. \n")
                global custo_kwh
                custo_kwh = float(bandeiras[escolha_bandeira_atual])
                preco_eel()

            else:
                print("Certifique-se que você digitou a bandeira corretamente.\n")
    
    bandeira()


def preco_eel():
    print(f"Dessa maneira, o custo do kWh é de R$ {custo_kwh} \n")
    global total_eel
    total_eel = (custo_kwh * consumo_mensal_kwh)
    global total_eel_f
    total_eel_f = "{:.2f}".format(total_eel)

    print(f"Isso significa que o valor do consumo mensal de energia elétrica, ao utilizar um motor elétrico de 45kW por {horas_uso_motor} horas é de R$ {total_eel_f}, considerando o valor de R$ {custo_kwh} por kWh, em período de {escolha_bandeira_atual}. \n")
    print(f"Òtimo! Agora que sabemos os custos da energia elétrica, precisamos dar uma olhada no diesel. \n")
    print ("\n", "-" * 20, "\n")

    custo_diesel()


def custo_diesel():
    print("Atualmente, qual é o valor do litro do diesel?: \n")
    print("Insira o valor até a segunda casa decimal, separado por ponto ou vírgula. Ex.: 6,72 \n")

    preco_diesel = input(">: ")
    preco_diesel_conv = float(preco_diesel.replace(',', '.'))
    consumo_hora = 13
    global valor_mensal_diesel
    valor_mensal_diesel = (preco_diesel_conv * consumo_hora * horas_uso_motor)
    global valor_mensal_diesel_f
    valor_mensal_diesel_f = "{:.2f}".format(valor_mensal_diesel)
    consumo_diesel_total = (consumo_hora * horas_uso_motor)

    print(f"Legal! O valor mensal gasto atualmente em diesel é de aproximadamente R$ {valor_mensal_diesel}, considerando um valor de R$ {preco_diesel} por litro, com {horas_uso_motor} horas de uso, incorrendo no consumo de {consumo_diesel_total} litros de diesel.")
    print ("\n", "-" * 20, "\n")
    print("Calculados os custos com diesel e energia elétrica, podemos partir para as despesas com a conversão do sistema.")
    print ("\n", "-" * 20, "\n")

    custos_totais()


def custos_totais():
    print("ATENÇÃO!")
    print("Insira somente valores inteiros, sem vírgulas ou pontos. Ex.: 45000. Não considere centavos nesta conta.")
    print ("\n", "-" * 20, "\n")
    print("Insira o preço do motor elétrico \n")

    motor_preco = input(">: ")
    motor_preco_c = float(motor_preco.replace(',', '.'))

    print("Insira o preço total dos cabos de eletricidade \n")
    cabos_preco = (input(">: "))
    cabos_preco_c = float(cabos_preco.replace(',', '.'))

    print("Insira o preço dos postes-padrão \n")
    postes_preco = (input(">: "))
    postes_preco_c = float(postes_preco.replace(',', '.'))

    print("Insira quaisquer valores adicionais não previstos pela calculadora. Insira 0 para nenhum gasto adicional.\n")
    adicionais_preco = (input(">: "))
    adicionais_preco_c = float(adicionais_preco.replace(',', '.'))

    print ("\n", "-" * 20, "\n")
    print("Ótimo! Temos todas as variáveis necessárias para descobrir o valor total da transição, além dos custos mensais.")

    transicao_preco = float(motor_preco_c + cabos_preco_c + postes_preco_c + adicionais_preco_c)

    print ("\n", "-" * 20, "\n")
    print(f"O preço para trocar o sistema a diesel para o sistema elétrico é de R$ {transicao_preco}")
    print ("\n", "-" * 20, "\n")
    print(f"Um motor a diesel atualmente gera despesas de R$ {valor_mensal_diesel_f}")
    print ("\n", "-" * 20, "\n")
    print(f"Um motor elétrico de mesma potência, operando o mesmo numero de horas, irá gerar despesas de R$ {total_eel_f}")
    print ("\n", "-" * 20, "\n")

    dif_mensal = (valor_mensal_diesel - total_eel)
    dif_mensal_f = "{:.2f}".format(dif_mensal)
    dif_percentual = ((total_eel)-(valor_mensal_diesel))/(valor_mensal_diesel)*100
    dif_percentual_f = "{:.2f}".format(dif_percentual)
    print(f"A economia do motor diesel é de R$ {dif_mensal_f} por mês, uma diferença de {dif_percentual_f}%.")
    print ("\n", "-" * 20, "\n")
    sys.exit("Cálculos feitos! Encerrando aplicação.")


start = input("Pressione qualquer tecla para começar: \n")

if start == True:
    horas_trabalho()    
else:
    horas_trabalho()
