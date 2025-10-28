# keyword_extractor_keybert.py

from keybert import KeyBERT

# Last inn modell (kan være "paraphrase-multilingual-MiniLM-L12-v2" for norsk/engelsk)
kw_model = KeyBERT(model='paraphrase-multilingual-MiniLM-L12-v2')

def extract_keywords_bert(text, top_n=10):
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='norwegian',
        use_maxsum=True,
        nr_candidates=20,
        top_n=top_n
    )
    return keywords

if __name__ == "__main__":
    text = """Det matematisk-naturvitenskapelige fakultet ved Universitetet i Oslo tilbyr utdanning og forskning
    på høyt internasjonalt nivå innen naturvitenskap, teknologi og matematikk."""
    
    keywords = extract_keywords_bert(text, top_n=8)
    print("Nøkkelord hentet med KeyBERT:")
    for kw, score in keywords:
        print(f"{kw} ({score:.3f})")
