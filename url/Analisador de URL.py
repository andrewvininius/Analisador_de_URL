from urllib.parse import urlparse, parse_qs
import socket

def obter_ip(dominio):
    try:
        ip = socket.gethostbyname(dominio)
        return ip
    except socket.gaierror:
        return None

def analisar_url(url):
    parsed_url = urlparse(url)

    if not all([parsed_url.scheme, parsed_url.netloc]):
        print("URL inválida. Certifique-se de fornecer uma URL válida.")
        return

    protocolo = parsed_url.scheme
    dominio = parsed_url.netloc
    porta = parsed_url.port if parsed_url.port else "Padrão"
    caminho = parsed_url.path if parsed_url.path else "Sem caminho"
    segmentos_do_caminho = caminho.strip("/").split("/")
    parametros = parse_qs(parsed_url.query) if parsed_url.query else {}
    fragmento = parsed_url.fragment if parsed_url.fragment else "Sem fragmento"
    esquema_autenticacao = parsed_url.username if parsed_url.username else "Sem esquema de autenticação"

    print("Análise da URL:")
    print(f"Protocolo: {protocolo}")
    print(f"Domínio: {dominio}")
    ip = obter_ip(dominio)
    if ip:
        print(f"Endereço IP: {ip}")
    print(f"Porta: {porta}")
    print("Caminho:")
    for segmento in segmentos_do_caminho:
        print(f" - {segmento}")
    print("Parâmetros:")
    for chave, valor in parametros.items():
        print(f" - {chave}: {valor}")
    print(f"Fragmento: {fragmento}")
    print(f"Esquema de autenticação: {esquema_autenticacao}")

if __name__ == "__main__":
    url = input("Digite a URL para análise: ")
    analisar_url(url)
