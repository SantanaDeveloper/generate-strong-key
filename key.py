import secrets
import subprocess
import sys


def copy_to_clipboard(data):
    """Copia o dado fornecido para o clipboard usando comandos nativos."""
    try:
        if sys.platform == "win32":  # Windows
            subprocess.run("clip", input=data, text=True, check=True)
        elif sys.platform == "darwin":  # macOS
            subprocess.run("pbcopy", input=data, text=True, check=True)
        else:  # Linux/Unix
            subprocess.run("xclip", input=data, text=True, check=True)
    except FileNotFoundError:
        print("Comando para copiar ao clipboard não encontrado. Verifique se está instalado.")


def generate_secret_key(length=50):
    """Gera uma chave secreta segura e a copia para o clipboard."""
    secret_key = secrets.token_urlsafe(length)
    copy_to_clipboard(secret_key)
    print("Chave secreta gerada e copiada para o clipboard.")
    print(f"Chave: {secret_key}")
    return secret_key


if __name__ == "__main__":
    generate_secret_key()
