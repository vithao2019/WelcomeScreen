import string
import secrets

tamanho = 20

caracteres = string.ascii_letters + string.digits + "!@#$%&*"

senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))

print(f"Senha gerada: {senha}")