from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


def consultar_estoque_por_carro(carro_nome):
    cloud_config = {
        'secure_connect_bundle': 'C:\\Users\\spide\\Inatel VSCODE\\S202-Banco_de_dados-\\EAV4\\secure-connect-exercicio-proposto.zip'
    }

    auth_provider = PlainTextAuthProvider(
        'hTZirkaPIaRimTrXLUmhZSyt',
        'wjZZIxC_K+7KyrajM,gnwSi,75LnPqQIZC0yAnKdOK7ccmCrp5Z+i-_KFqt3PQZ8.5DxG5rsXKXg,__X5xmCqAu.uj1bz-.1wcN4_mBvtPYsBE8W92B8HRD-8sSk-XWg'
    )

    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()

    query = f"SELECT nome, estante, quantidade FROM estoque WHERE carro = '{carro_nome}'"

    result = session.execute(query)

    for row in result:
        print(
            f"Nome: {row.nome}, Estante: {row.estante}, Quantidade: {row.quantidade}")

    cluster.shutdown()


carro_desejado = input("Digite o modelo de carro desejado: ")
consultar_estoque_por_carro(carro_desejado)
