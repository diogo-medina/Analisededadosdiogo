def buscar_pedido(idpedido):
    try:
        id_procurado = int(input("Digite o número do cartão/ID do pedido: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return None

    for pedido, id_atual in idpedido.items():
        if id_atual == id_procurado:
            print("\n=== CONSUMO LOCALIZADO ===")
            print(f"Consumo: {pedido}")
            print(f"Número do cartão/ID: {id_atual}")
            return pedido

    print("\nConsumo não encontrado.")
    return None
