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

## Teknologjitë e përdorura
- Python 3
- requests
- beautifulsoup4

## Instalimi
1. Klono projektin:
```bash
git clone https://github.com/romeoballaaa/books-scraping-project.git
cd books-scraping-project
