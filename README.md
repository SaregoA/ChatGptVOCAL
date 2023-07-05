# ChatGPT Vocal

Strumento Python per l'**utilizzo di ChatGPT solo in vocale**. Pronuncia a voce una domanda e ottieni la risposta audio dopo averla ottenuta da ChatGPT.

Questa versione non utilizza le API di ChatGPT, ma tramite **Selenium** viene utilizzato il browser per invio della domanda e lettura della risposta. Per evitare l'accesso a ChatGPT e bloccare Selenium nel captcha, occorre eseguire l'accesso a ChatGPT dal proprio browser Chromium, chiuderlo e poi avviare questo script, il quale userà il profilo utente del tuo utente per evitare la fase di accesso e arrivare quindi dritto all'interfaccia principale.

## Scaricare il progetto e creare la cartella per il salvataggio delle conversazioni
```bash
git clone https://codeberg.org/SaregoA/ChatGptVOCAL.git
cd ChatGptVOCAL
mkdir history_chat
```

## Creare ed avviare l'ambiente virtuale

```bash
mkdir env
python3.8 -m venv env
source env/bin/activate
```

## Installazione

```bash
pip install -r requirements.txt
```

Occorre installare anche `ffplay`, per riprodurre la risposta velocizzata. Questo programma fa parte del pacchetto `ffmpeg` :

```bash
sudo apt install ffmpeg
```

Se hai installati sia Python2 che Python3:

```bash
pip3 install -r requirements.txt
```

Potresti ottenere un errore se non hai le librerie di sviluppo di PyAudio, che su distribuzioni derivate Debian puoi installare con:

```bash
sudo apt-get install portaudio19-dev
```

## Utilizzo

E' sufficiente eseguire lo script con:

```bash
python3 main.py
```

All'apertura di Chromium, attendere il caricamento della pagina di ChatGPT e poi dettare la domanda a voce sul microfono.
