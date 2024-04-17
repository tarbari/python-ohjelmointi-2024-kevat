# Ollama esimerkki

Ollama on framework eri kielimallien suorittamiseen paikallisesti.
[Github](https://github.com/ollama/ollama)

## Asennus

Asenna ja käynnistä ollama koneellesi githubista löytyvien ohjeiden mukaisesti.
Lataa `llama2` malli.
Tämän jälkeen luo venv, asenna riippuvuudet ja suorita main.py

```bash
ollama pull llama2
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

