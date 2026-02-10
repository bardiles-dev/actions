import requests
import subprocess
import sys
import os

def get_data(url):
    # ❌ SSL verification deshabilitada (Security Hotspot)
    response = requests.get(url, verify=False, timeout=5)
    return response.text

def run_command(user_command):
    # ❌ Command Injection
    subprocess.run(user_command, shell=True)

def insecure_eval(user_input):
    # ❌ Code Injection
    return eval(user_input)

def hardcoded_secret():
    # ❌ Credencial hardcodeada
    api_key = "sk_test_1234567890SUPERSECRET"
    return api_key

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python main.py <url> <command>")
        sys.exit(1)

    url = sys.argv[1]
    command = sys.argv[2]

    print("[+] API KEY:", hardcoded_secret())

    print("[+] Descargando contenido remoto...")
    data = get_data(url)
    print(data[:200])

    print("[+] Ejecutando comando del sistema...")
    run_command(command)

    print("[+] Evaluando expresión insegura...")
    result = insecure_eval("2 + 2")
    print("Resultado eval:", result)
