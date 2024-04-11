import requests
import sys

# Avoin API, jolla voi testata toimivuutta: https://jsonplaceholder.typicode.com/todos/2

def save_content(content: str, file_name: str):
    """Tallentaa sisällön annettuun tiedostoon

    Args:
        content: Kirjoitettava sisältö
        file_name: Tiedoston nimi. Annettu tiedosto yliajetaan, tai mikäli tiedostoa ei ole olemassa niin se luodaanw
    """
    with open(file_name, "w") as f:
        f.write(content)

def get_content(url: str) -> str:
    """Tekee HTTP GET kutsun annettuun osoitteeseen.

    Args:
        url: Osoite, jonne GET kutsu lähetetään.
    Returns:
        GET kutsun vastauksen body string muodossa.
    """
    result = requests.get(url)
    return result.text

if __name__ == "__main__":
    # Tarkistetaan, että parametrejä on riittävästi.
    if len(sys.argv) < 3:
        print("Ei tarpeeksi argumentteja. Anna URL ja tiedostonimi.")
        sys.exit(1)

    """
    sys.argv on lista parametreistä, jotka on annettu ohjelmaa suoritettaessa.
    Esimerkiksi:
    `python3 main.py https://yle.fi yle.html`
    sys.argv[0] == "main.py"
    sys.argv[1] == "https://yle.fi"
    sys.argv[2] == "yle.html"
    """

    url = sys.argv[1]
    file_name = sys.argv[2]
    content = get_content(url)
    save_content(content, file_name)
