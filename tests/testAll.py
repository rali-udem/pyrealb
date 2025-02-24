import conjugation_en,conjugation_fr
import dates_en, dates_fr
import declension_en, declension_fr
import elision_en, elision_fr
import numbers_en, numbers_fr
import pronouns_en, pronouns_fr
import sentences_en, sentences_fr
import examples_en, exemples_fr

from test import test


totalOK=0
totaltests=0

badOnly=True

def update(oktests):
    global totalOK,totaltests
    totalOK+=oktests[0]
    totaltests+=oktests[1]

if __name__ == '__main__':
    update(test("English conjugation","en",conjugation_en.conjugation_en,badOnly=badOnly))
    update(test("Conjugaison en français","fr",conjugation_fr.conjugation_fr,badOnly=badOnly))
    
    update(test("English dates","en",dates_en.dates_en,badOnly=badOnly))
    update(test("Dates en français","fr",dates_fr.dates_fr,badOnly=badOnly))
    
    update(test("English declension","en",declension_en.declension_en,badOnly=badOnly))
    update(test("Déclinaisons en français","fr",declension_fr.declension_fr,badOnly=badOnly))
    
    update(test("English elision","en",elision_en.elision_en,badOnly=badOnly))
    update(test("Élision en français","fr",elision_fr.elision_fr,badOnly=badOnly))
    
    update(test("English numbers","en",numbers_en.numbers_en,badOnly=badOnly))
    update(test("Nombres en français","fr",numbers_fr.numbers_fr,badOnly=badOnly))
    
    update(test("English pronouns","en",pronouns_en.pronouns_en,badOnly=badOnly))
    update(test("Pronoms en français","fr",pronouns_fr.pronouns_fr,badOnly=badOnly))

    update(test("English sentences", "en", sentences_en.sentences_en, badOnly=badOnly))
    update(test("Phrases en français", "fr", sentences_fr.sentences_fr, badOnly=badOnly))

    update(test("English examples", "en", examples_en.examples_en, badOnly=badOnly))
    update(test("Exemples en français", "fr", exemples_fr.exemples_fr, badOnly=badOnly))

    print(f"{totalOK} successes over {totaltests}")
    if totalOK==totaltests:
        print("all tests succeeded")
    else:
        print(f"still {totaltests-totalOK} tests to check")
    