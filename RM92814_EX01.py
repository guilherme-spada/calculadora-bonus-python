#obtendo as informações do usuário
nivel_assinatura = str(input("Insira o nível de sua assinatura (Basic, Silver, Gold ou Platinum): "))
faturamento_anual = float(input("Insira seu faturamento anual: R$ "))

#realizando o teste lógico
if nivel_assinatura == "Basic":
    valor_bonus = (faturamento_anual * 0.3)

elif nivel_assinatura == "Silver":
    valor_bonus = (faturamento_anual * 0.2)

elif nivel_assinatura == "Gold":
    valor_bonus = (faturamento_anual * 0.1)

elif nivel_assinatura == "Platinum":
    valor_bonus = (faturamento_anual * 0.05)

#exibindo o valor a ser pago a título de bônus
print("O valor do bonus a ser pago é: R$ {:.2f}".format(valor_bonus))
