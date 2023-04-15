# module no_accent du chatbot umapon
# pour enlever tous les accents dans une phrase

import unicodedata

def remove_accents(phrase:str) -> str:
    phrase = phrase.lower().strip()
    nfkd_form = unicodedata.normalize('NFKD', phrase)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])