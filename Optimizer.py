import os
import shutil
import tempfile
import platform

def clean_temp_files():
    temp_dir = tempfile.gettempdir()
    deleted = 0

    print(f"Nettoyage de : {temp_dir}")

    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)

        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                deleted += 1
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                deleted += 1
        except Exception:
            pass

    print(f"✅ {deleted} éléments supprimés.")

def system_info():
    print("\n=== Informations système ===")
    print("OS :", platform.system())
    print("Version :", platform.version())
    print("Machine :", platform.machine())
    print("Processeur :", platform.processor())

def menu():
    while True:
        print("\n=== PC Optimizer ===")
        print("1. Nettoyer les fichiers temporaires")
        print("2. Afficher les informations système")
        print("3. Quitter")

        choice = input("Choix : ")

        if choice == "1":
            clean_temp_files()
        elif choice == "2":
            system_info()
        elif choice == "3":
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    menu()