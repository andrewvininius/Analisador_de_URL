# Análise de URL

Este script Python analisa uma URL fornecida pelo usuário e exibe informações sobre seus componentes, incluindo protocolo, domínio, endereço IP, porta, caminho, parâmetros, fragmento e esquema de autenticação (se disponível).

## Como usar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Execute o script.
3. Digite a URL que você deseja analisar quando solicitado.
4. O script apresentará informações detalhadas sobre a URL fornecida.

## Requisitos

O script requer a biblioteca `socket` para obter o endereço IP associado ao domínio. Ele também usa a biblioteca `urllib.parse` para analisar a URL e extrair seus componentes.

## Observações

1. Certifique-se de fornecer uma URL válida. Caso contrário, o script exibirá uma mensagem de erro.
2. Se a URL não tiver uma porta especificada, será exibida a porta "Padrão".
3. Se a URL não tiver um caminho especificado, será exibido "Sem caminho".
4. Se a URL não tiver parâmetros especificados, será exibido "Sem parâmetros".
5. Se a URL não tiver um fragmento especificado, será exibido "Sem fragmento".
6. Se a URL não tiver um esquema de autenticação especificado, será exibido "Sem esquema de autenticação".

## Exemplo de uso
```python
from urllib.parse import urlparse, parse_qs
import socket

def obter_ip(dominio):
    try:
        ip = socket.gethostbyname(dominio)
        return ip
    except socket.gaierror:
        return None

def analisar_url(url):
    # ... (código do seu script) ...

if __name__ == "__main__":
    url = input("Digite a URL para análise: ")
    analisar_url(url)

