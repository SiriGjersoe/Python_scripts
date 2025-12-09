
import requests
from bs4 import BeautifulSoup
import spacy
import csv
nlp = spacy.load("nb_core_news_sm")

"""
Author: Siri Moen Gjersøe
Date: 2025-xx-xx
File: snl_nominal_phrases.py

Description:
    This Python script automatically extracts nominal phrases (noun phrases) from 
    selected Store norske leksikon (SNL) articles using the spaCy Norwegian model.
    It collects each sentence and its detected nominal phrases, saving them to a CSV file 
    (nominalfraser.csv) for further linguistic or corpus-based analysis.

Features:
    • Fetches and cleans article text from multiple SNL pages.
    • Uses spaCy’s Norwegian model (nb_core_news_sm) for part-of-speech tagging and phrase chunking.
    • Extracts noun chunks (nominal phrases) for each sentence.
    • Saves results as a UTF-8 CSV file with:
        - Full sentence
        - Source URL
        - List of nominal phrases

Requirements:
    Python 3.9+ (tested on Python 3.13)
    Required packages (install via pip):
        pip install requests beautifulsoup4 spacy
        python -m spacy download nb_core_news_sm

Packages and Purpose:
    requests         → Fetch webpage HTML
    beautifulsoup4   → Parse and extract article text
    spacy            → Perform linguistic analysis
    nb_core_news_sm  → Norwegian Bokmål language model for spaCy

Usage:
    1. Save this script as 'snl_nominal_phrases.py'.
    2. Run it in the terminal:
           python snl_nominal_phrases.py
    3. The script will process all SNL URLs and save results to:
           nominalfraser.csv

Output:
    CSV file with the following columns:
        Sentence | Source_URL | Nominal_Phrases
"""

# URLs to analyze

urls = [
   "https://snl.no/psykologi",
    "https://snl.no/psykologiens_historie",
    "https://snl.no/humanistisk_psykologi",
    "https://snl.no/biologisk_psykologi",
    "https://snl.no/kognitiv_psykologi",
    "https://snl.no/evolusjonspsykologi",
    "https://snl.no/personlighetspsykologi",
    "https://snl.no/anvendt_psykologi",
    "https://snl.no/Klinisk_psykologi",
    "https://snl.no/Harald_Krabbe_Schjelderup",
    "https://snl.no/%C3%85se_Gruda_Skard",
    "https://snl.no/Lev_Vygotskij",
    "https://snl.no/fenomenologi",
    "https://snl.no/fysiologisk_psykologi",
    "https://snl.no/pedagogisk_psykologi",
    "https://snl.no/behaviorisme",
    "https://snl.no/S-R-psykologi",
    "https://snl.no/fenomenologisk_psykologi",
    "https://snl.no/forskningsmetoder_i_psykologien",
    "https://snl.no/Ragnar_Rommetveit",
    "https://snl.no/Alfred_Binet",
    "https://snl.no/Carl_Jung",
    "https://snl.no/funksjonalisme_-_psykologi",
    "https://snl.no/Ivan_Pavlov",
    "https://snl.no/psykolog",
    "https://snl.no/S%C3%B8ren_Nordeide",
    "https://snl.no/strukturalisme_-_psykologi",
    "https://snl.no/begrep_-_psykologi",
    "https://snl.no/bevissthet_-_psykologi",
    "https://snl.no/gerontologisk_psykologi",
    "https://snl.no/Helga_Eng",
    "https://snl.no/Edward_Lee_Thorndike",
    "https://snl.no/filosofisk_behaviorisme",
    "https://snl.no/menneskets_psykologi",
    "https://snl.no/operativ_psykologi",
    "https://snl.no/Steinar_Kvale",
    "https://snl.no/Abraham_Maslow",
    "https://snl.no/assosiasjonspsykologi",
    "https://snl.no/bias_-_psykologi",
    "https://snl.no/dynamisk_psykologi",
    "https://snl.no/positiv_psykologi",
    "https://snl.no/sosialpsykologi"
]

# Function to fetch and clean text
def hent_tekst(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        tekst = " ".join([p.get_text(" ", strip=True) for p in soup.find_all("p")])
        return tekst
    except Exception as e:
        print(f"Feil ved {url}: {e}")
        return ""

# Create CSV file
with open("nominalphrases.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Sentence", "Source_URL", "Nominal_Phrases"])

    # Loop through URLs
    for url in urls:
        print(f"\n🔹 Analyserer: {url}")
        tekst = hent_tekst(url)
        doc = nlp(tekst)

        for sent in doc.sents:
            sentence_text = sent.text.strip()
            nominal_phrases = [chunk.text for chunk in sent.noun_chunks]

            if nominal_phrases:
                writer.writerow([
                    sentence_text,
                    url,
                    "; ".join(nominal_phrases)
                ])

print("Finished! Results saved in 'nominalphrases.csv'.")
