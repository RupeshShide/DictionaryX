import requests
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.GREEN + """
╔══════════════════════════════════════╗
║        PY DICTIONARY TOOL v1         ║
║        [ Hacker Edition 🔥 ]         ║
╚══════════════════════════════════════╝
""" + Style.RESET_ALL)

def menu():
    print(Fore.CYAN + """
┌──────────────────────────────┐
│ 1. Search Word               │
│ 2. Exit                      │
└──────────────────────────────┘
""" + Style.RESET_ALL)

def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if isinstance(data, list):
            print(Fore.GREEN + "\n╔══════════════════════════════╗")
            print(Fore.GREEN + f"  Word: {word}")
            print(Fore.GREEN + "╚══════════════════════════════╝")

            for meaning in data[0].get('meanings', []):
                print(Fore.YELLOW + f"\n[+] {meaning.get('partOfSpeech', 'N/A')}")

                for definition in meaning.get('definitions', []):
                    print(Fore.WHITE + "  → " + definition.get('definition', 'N/A'))

                    if definition.get('example'):
                        print(Fore.MAGENTA + "     Example: " + definition['example'])

        else:
            print(Fore.RED + "\n[!] Word not found.")

    except requests.exceptions.RequestException:
        print(Fore.RED + "\n[!] Network Error!")

def main():
    while True:
        banner()
        menu()

        choice = input(Fore.GREEN + "Enter choice > ")

        if choice == "1":
            word = input(Fore.CYAN + "Enter word > ").strip()
            if word:
                get_meaning(word)

        elif choice == "2":
            print(Fore.RED + "\nExiting...")
            break

        else:
            print(Fore.RED + "\nInvalid choice!")

if __name__ == "__main__":
    main()
