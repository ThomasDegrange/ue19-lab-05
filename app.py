import requests

def get_a_joke():
    URL = "https://official-joke-api.appspot.com/random_joke"
    reponse = requests.get(URL)

    if reponse.status_code == 200:
        contenu_reponse = reponse.json()
        print("Blague : ", contenu_reponse["setup"])
        print("Réponse : ", contenu_reponse["punchline"])
    else:
        print("Une erreur est survenue : ", reponse.status_code)

if __name__ == "__main__":
    get_a_joke()
