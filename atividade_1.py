dados = {}

print("Cadastre-se:  ")

login = input("Login: ")
senha = input("Senha: ")

dados["login"] = login
dados["senha"] = senha

print("dados cadastrados>>>", dados)

login_cad = input("Login: ")
senha_cad = input("Senha: ")

if login_cad == login and senha_cad == senha:
    print("Seja bem vindo ao sistema Z")
    produtos = ["a", "b", "c"]
    valores = [10.55, 20.0, 30.0]

    carrinho = []
    total = []
    print("Escolha seu produto da lista a seguir:")
    print("Produto 1 ", produtos[0], "Preço ", valores[0])
    print("Produto 2", produtos[1], "Preço ", valores[1])
    print("Produto 3", produtos[2], "Preço ", valores[2])
    compra = input("Digite o número do produto que deseja comprar ")

    if compra == "1":
        carrinho.append(produtos[0])
        total.append(valores[0])
    if compra == "2":
        carrinho.append(produtos[1])
        total.append(valores[1])
    if compra == "3":
        carrinho.append(produtos[2])
        total.append(valores[2])

    mais = input("Deseja mais alguma coisa? ")
    if mais == "sim":
        compra2 = input("Digite o numero do proximo produto ")
        if compra2 == "1":
            carrinho.append(produtos[0])
            total.append(valores[0])
        if compra2 == "2":
            carrinho.append(produtos[1])
            total.append(valores[1])
        if compra2 == "3":
            carrinho.append(produtos[2])
            total.append(valores[2])

    print("Finalizando sua compra:")
    print("Você escolheu: ", carrinho)
    print("Com os preços: ", total)
    valor_compra = sum(total)
    print("Você pagará: R$", valor_compra)

    print("Escolha a seguir a forma de pagamento:")
    pagamento = input("Para cartão digite 1, para pix 2: ")

    if pagamento == "1":
        print("Aproxime ou introduza o cartão")
        print("Pagamento aceito. Obrigado")
    if pagamento == "2":
        print("Escaneie o QR Code")
        print("Pagamento aceito. Obrigado")

else:
    print("Digite os dados corretamente...")
