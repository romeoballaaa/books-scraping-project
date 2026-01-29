# Web Scraping & API Integration Project

## Përshkrimi
Ky projekt demonstron përdorimin e web scraping dhe integrimin e një API publike për të marrë dhe pasuruar të dhëna.

Të dhënat merren nga faqja:
https://books.toscrape.com

Nga faqja nxirren:
- Titulli i librit
- Çmimi në GBP
- Vlerësimi (rating)

Më pas përdoret API publike:
https://api.exchangerate.host  
për të konvertuar çmimin nga GBP në EUR.

Të gjitha të dhënat ruhen në një skedar CSV.



## 🧰 Çfarë të duhet përpara

Sigurohu që ke të instaluar:

- ✅ **Python 3**
- ✅ **pip**

Kontrollo nëse i ke:
```bash
python --version
pip --version
```

---
## 🚀 Si ta përdorësh projektin nga GitHub

### 1️⃣ Shkarko projektin nga GitHub

```bash
git clone https://github.com/romeoballaaa/books-scraping-project.git
cd books-scraping-project
```

### 2️⃣ (OPSIONALE) Krijo Virtual Environment

#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3️⃣ Instalo libraritë e nevojshme

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Ekzekuto programin

```bash
python main.py
```

## 🚀 Si ta përdorësh projektin (Pa Git)

### 1️⃣ Shkarko projektin si ZIP nga GitHub

1. Hape repository-n në GitHub
2. Kliko butonin **Code**
3. Zgjidh **Download ZIP**
4. Shkarko file-in `.zip` në kompjuterin tënd

---

### 2️⃣ Nxirre (Extract) projektin

- Kliko me të djathtën mbi ZIP
- Zgjidh **Extract All**
- Hape folder-in e nxjerrë

Duhet të shohësh diçka të tillë:
```
books-scraping-project/
├── main.py
├── requirements.txt
├── README.md
```

---

### 3️⃣ Hape terminalin në folder-in e projektit

#### Windows
- Hape folder-in
- Kliko në **address bar**
- Shkruaj `cmd` dhe shtyp Enter

#### macOS / Linux
- Kliko me të djathtën në folder
- Zgjidh **Open in Terminal**

---

### 4️⃣ (OPSIONALE) Krijo Virtual Environment

#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 5️⃣ Instalo libraritë e nevojshme

```bash
pip install -r requirements.txt
```
---

### 6️⃣ Ekzekuto programin

```bash
python main.py
```

Programi do fillojë scraping dhe do shfaqë mesazhe në terminal.

---

### 7️⃣ Shiko rezultatin

Pas përfundimit:
- Do krijohet file-i **`output.csv`**
- Mund ta hapësh me:
  - Excel
  - Google Sheets
  - LibreOffice

---

## 📂 Çfarë bën secili file

- `main.py` → kodi kryesor i scraping
- `requirements.txt` → libraritë që duhen instaluar
- `output.csv` → rezultati final (krijohet automatikisht)

---

