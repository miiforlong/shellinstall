import os
import platform
import subprocess
import shutil

def detect_platform():
    os_type = platform.system().lower()
    if os_type == "linux":
        return "linux"
    elif os_type == "windows":
        return "windows"
    else:
        return None

def check_winget():
    """ Vérifie si winget est installé et tente de l'installer si nécessaire (Windows uniquement). """
    if detect_platform() == "windows":
        if shutil.which("winget") is None:
            print("winget n'est pas installé. Installation de winget en cours...")
            os.system("start ms-windows-store://pdp/?productid=9NBLGGH4NNS1")  # Ouvre le Microsoft Store
            input("Installe winget dans le Microsoft Store puis appuie sur Entrée pour continuer.")
        else:
            print("winget est déjà installé.")

def search_package(package_name):
    print(f"Recherche du package '{package_name}'...")
    # Exemple avec apt pour Linux
    if detect_platform() == "linux":
        os.system(f"apt search {package_name}")
    elif detect_platform() == "windows":
        check_winget()
        os.system(f"winget search {package_name}")

def install_package(package_name):
    print(f"Installation de '{package_name}'...")
    # Commande d’installation en fonction de la plateforme
    if detect_platform() == "linux":
        os.system(f"sudo apt install -y {package_name}")
    elif detect_platform() == "windows":
        check_winget()
        os.system(f"winget install -e --id {package_name}")

def main():
    print("Bienvenue dans l'outil de téléchargement d'applications !")
    while True:
        action = input("Tape 's' pour chercher, 'i' pour installer, 'q' pour quitter : ").strip().lower()
        if action == 'q':
            print("À la prochaine !")
            break
        elif action in ['s', 'i']:
            package_name = input("Nom de l'application à rechercher ou installer : ")
            if action == 's':
                search_package(package_name)
            elif action == 'i':
                install_package(package_name)
        else:
            print("Option invalide, essaye encore.")

if __name__ == "__main__":
    main()
