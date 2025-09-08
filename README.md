# Albumy + AI Azure Computer Vision

*Capture and share every wonderful moment.*

![Screenshot](https://helloflask.com/screenshots/albumy.png)

---

## What’s new in this fork

- **AI-generated descriptions (alt text)** on upload using **Azure AI Vision (Image Analysis 4.0)** 
- Photo page shows an **“AI Generated Description”** button under the tags to reveal the alternative text to users
- **Auto keyword tags** Searchable AI generated tags reusing Albumy's `Tag` model

---

## Requirements

- **Python 3.9.5 (64-bit)** recommended  
- An **Azure AI Vision / Computer Vision** resource in a region that supports **Image captions (4.0)**  
- Git + a terminal (Git Bash / PowerShell / macOS/Linux shell)

---

## Installation
Bash assumed

Clone:
```
$ git clone https://github.com/arvinourian/albumy.git
$ cd albumy
```
Create & activate virtual env then install dependency:
```
$ python3 -m venv .venv  # Use 'py -3.9 -m venv .venv' on Windows
$ source .venv/bin/activate  # Use `env\Scripts\activate` on Windows
$ python -m pip install -r requirements.txt
```

Set Azure values:
```
$ cp .env.example .env # Paste ENDPOINT and KEY values from your Azure Computer Vision resource instance
```

Generate fake data then run:
```
$ export FLASK_APP=albumy
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
