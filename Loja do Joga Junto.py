import requests

# Listas de estados com frete grátis
norte = ["AM", "PA", "AC", "RO", "RR", "TO", "AP"]
nordeste = ["MA", "PI", "CE", "RN", "PE", "PB", "SE", "AL", "BA"]

def verificar_frete_gratis(cep):
    """Consulta a API ViaCEP e retorna se o CEP tem frete grátis"""
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    if resposta.status_code != 200:
        return "Erro ao consultar o CEP."

    dados = resposta.json()
    
    # Verifica se o CEP é válido
    if "erro" in dados:
        return "CEP inválido. Tente novamente."

    estado = dados["uf"]

    if estado in norte or estado in nordeste:
        return f"O estado {estado} é elegível para frete grátis!"
    else:
        return f"O estado {estado} não possui frete grátis."

# Entrada do usuário
cep_usuario = input("Digite seu CEP (somente números): ")
resultado = verificar_frete_gratis(cep_usuario)
print(resultado)
