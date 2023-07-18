"""A translation code"""
from deep_translator import MyMemoryTranslator
def englishtofrench(englishtext):
    """From En to Fr"""
    frenchtext=MyMemoryTranslator(source='english',\
         target='french').translate(englishtext)
    return frenchtext

def frenchtoenglish(frenchtext):
    """From Fr to En"""
    englishtext=MyMemoryTranslator(source='french',\
         target='english').translate(frenchtext)
    return englishtext
