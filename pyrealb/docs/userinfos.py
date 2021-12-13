
terminalsSect = {"fr":"Terminaux","en":"Terminals",
     "ex":[
        {"pattern":"N(…)",  "fr":["Nom",'N("joueur")'],
                            "en":["Noun",'N("player")'] },
        {"pattern":"A(…)",  "fr":["Adjectif",'A("grand")'],
                            "en":["Adjective",'A("tall")'] },
        {"pattern":"Pro(…)","fr":["Pronom",'Pro("je")'],
                            "en":["Pronoun",'Pro("I")'] },
        {"pattern":"D(…)",  "fr":["Déterminant",'D("le")'],
                            "en":["Determiner",'D("the")'] },
        {"pattern":"V(…)",  "fr":["Verbe",'V("apprendre")'],
                            "en":["Verb",'V("learn")'] },
        {"pattern":"Adv(…)","fr":["Adverbe",'Adv("bien")'],
                            "en":["Adverb",'Adv("well")'] },
        {"pattern":"P(…)",  "fr":["Préposition",'P("dans")'],
                            "en":["Preposition",'P("in")'] },
        {"pattern":"C(…)",  "fr":["Conjonction",'C("et")'],
                            "en":["Conjunction",'C("and")']},
        {"pattern":"DT(…)", "fr":["Date avec <a href='#dateFr'>options</a> facultatives",'DT()'],
                            "en":["Date possibly with <a href='#dateEn'>options</a>",'DT()']},
        {"pattern":"NO(…)", "fr":["Nombre avec <a href='#nombres'>options</a> facultatives",'NO(2)'],
                            "en":["Number possibly with <a href='#numbers'>options</a>",'NO(2)']},
        {"pattern":'"…"',  "fr":["Texte brut",'"Wow"'],
                            "en":["Raw text",'"Wow"']},
        {"pattern":"Q(…)",  "fr":["Texte brut auquel on peut ajouter des <a href='#optionsFr'>options</a>",
                                  'Q("Bang !").tag("i")'],
                            "en":["Raw text to which <a href='#optionsEn'>options</a> can be added",
                                  'Q("Bang !").tag("i")']}
    ]}

syntagmesSect = {"fr":"Syntagmes","en":"Phrases",
     "ex":[
         {"pattern":"NP(…)","fr":["Syntagme nominal",'NP(D("le"), N("voiture"))'],
                            "en":["Noun Phrase",'NP(D("the"), N("car"))']},
         {"pattern":"AP(…)","fr":["Syntagme adjectival",'AP(Adv("très"), A("grand"))'],
                            "en":["Adjective Phrase",'AP(Adv("very"), A("tall"))']},
         {"pattern":"AdvP(…)","fr":["Syntagme adverbial",'AdvP(Adv("bien"), Adv("heureusement"))'],
                            "en":["Adverbial Phrase",'AdvP(Adv("far"), Adv("back"))']},
         {"pattern":"VP(…)","fr":["Syntagme verbal",'VP(V("prendre"), NP(D("le"), N("course")))'],
                            "en":["Verbal Phrase",'VP(V("enjoy"), NP(D("a"), N("meal")))']},
         {"pattern":"PP(…)","fr":["Syntagme Prépositionnel",'PP(P("à"), NP(N("minuit")))'],
                            "en":["Prepositional Phrase",'PP(P("at"), NP(N("midnight")))']},
         {"pattern":"CP(…)","fr":["Syntagme coordonné",'CP(C("et"), AP(A("vaillant")), AP(A("gentil")), AP(A("serviable")))'],
                            "en":["Coordinated Phrase",'CP(C("and"), AP(A("kind")), AP(A("strong")), AP(A("beautiful")))']},
         {"pattern":"CP(…)","fr":["&nbsp;<code>CP</code> sans <code>C</code>",'CP(AP(A("vaillant")), AP(A("gentil")), AP(A("serviable")))'],
                            "en":["&nbsp;<code>CP</code> with no <code>C</code>",'CP(AP(A("kind")), AP(A("strong")), AP(A("beautiful")))']},
         {"pattern":"S(…)", "fr":["Phrase",'S(NP(D("le"),N("homme")), VP(V("dormir")))'],
                            "en":["Sentence",'S(NP(D("the"),N("man")), VP(V("sleep")))']},
         {"pattern":"SP(…)","fr":["Syntagme subordonné",'SP(Pro("que"), Pro("je"), VP(V("rencontrer").t("pc")))'],
                            "en":["Subordinated Phrase",'SP(Adv("that"), Pro("I"), VP(V("meet").t("ps")))']},
     ]};

optionsSect= {"fr":"","en":"",
     "ex":[
           {"group":".t(…)","fr":'Temps (défaut "p")',"en":'Tense (default "p")'},
           {"pattern":'.t("p")', "fr":["présent",'V("aimer").t("p")'],
                           "en":["present",'V("love").t("p")']},
           {"pattern":'.t("b")', "fr":["infinitif",'V("aimer").t("b")'],
                           "en":["infinitive",'V("love").t("b")']},
           {"pattern":'.t("i")', "fr":["imparfait",'V("aimer").t("i")'],
                           "en":["",'']},
           {"pattern":'.t("ps")', "fr":["passé simple",'V("aimer").t("ps")'],
                           "en":["simple past",'V("love").t("ps")']},
           {"pattern":'.t("f")', "fr":["futur",'V("aimer").t("f")'],
                           "en":["future",'V("love").t("f")']},
           {"pattern":'.t("ip")', "fr":["impératif présent",'V("aimer").t("ip").pe(2)'],
                           "en":["present imperative",'V("love").t("ip").pe(2)']},
           {"pattern":'.t("c")', "fr":["conditionnel présent",'V("aimer").t("c")'],
                           "en":["",'']},
           {"pattern":'.t("pr")', "fr":["participe présent",'V("aimer").t("pr")'],
                           "en":["present participle",'V("love").t("pr")']},
           {"pattern":'.t("s")', "fr":["subjonctif présent",'V("aimer").t("s")'],
                           "en":["",'']},
           {"pattern":'.t("si")', "fr":["subjonctif imparfait",'V("aimer").t("si")'],
                           "en":["",'']},
           {"pattern":'.t("pp")', "fr":["participe passé",'V("aimer").t("pp")'],
                            "en":["past participle",'V("love").t("pp")']},
           
           {"group":".t(…)","fr":'Temps composés (défaut "p")',"en":''},
           {"pattern":'.t("pc")', "fr":["passé composé",'V("aimer").t("pc")'],
                           "en":["",'']},
           {"pattern":'.t("pq")', "fr":["plus-que-parfait",'V("aimer").t("pq")'],
                           "en":["",'']},
           {"pattern":'.t("cp")', "fr":["conditionnel passé",'V("aimer").t("cp")'],
                           "en":["",'']},
           {"pattern":'.t("fa")', "fr":["futur antérieur",'V("aimer").t("fa")'],
                           "en":["",'']},
           {"pattern":'.t("spa")', "fr":["subjonctif passé",'V("aimer").t("spa")'],
                           "en":["",'']},
           {"pattern":'.t("spq")', "fr":["subjonctif plus-que-parfait",'V("aimer").t("spq")'],
                             "en":["",'']},
           
           {"group":".n(…)","fr":'nombre (défaut "s")',
                                  "en":'number (default "s")'},
           {"pattern":'.n("s")', "fr":["verbe au singulier",'V("manger").n("s")'],
                                 "en":["verb singular",'V("eat").n("s")']},
           {"pattern":'.n("p")', "fr":["verbe au pluriel",'V("manger").n("p")'],
                                 "en":["verb plural",'V("eat").n("p")']},
           {"pattern":'.n("s")', "fr":["nom au singulier",'N("joueur").n("s")'],
                                 "en":["noun singular",'N("player").n("s")']},
           {"pattern":'.n("p")', "fr":["nom au pluriel",'N("joueur").n("p")'],
                                 "en":["noun plural",'N("player").n("p")']},
           {"pattern":'.n("s")', "fr":["adjectif au singulier",'A("grand").n("s")'],
                                 "en":["adjective singular",'A("big").n("s")']},
           {"pattern":'.n("p")', "fr":["adjectif au pluriel",'A("grand").n("p")'],
                                 "en":["adjective plural",'A("big").n("p")']},
           {"pattern":'.n("p")', "fr":["déterminant au pluriel",'D("le").n("p")'],
                                 "en":["determiner plural",'D("the").n("p")']},
           {"pattern":'.n("p")', "fr":["déterminant au pluriel",'D("un").n("p")'],
                                 "en":["determiner plural",'D("a").n("p")']},
           {"pattern":'.n("p")…',"fr":["déterminant possessif au pluriel",'D("mon").n("p").pe(2)'],
                                 "en":["possessive determiner masculine (singular owner)",'D("my").n("p").g("m").ow("s")']},
           {"pattern":'.n("p")…',"fr":["déterminant possessif (sujet au pluriel)",'D("notre").n("p").pe(2)'],
                                 "en":["possessive determiner (plural owner)",'D("my").n("p").ow("p")']},

           {"group":".g(…)","fr":'Genre (défaut "m")',
                            "en":'Gender (default "n")'},
           {"pattern":'.g("m")', "fr":["nom masculin",'N("joueur").g("m")'],
                                       "en":["",'']},
           {"pattern":'.g("m")', "fr":["nom féminin",'N("joueur").g("f")'],
                                       "en":["",'']},
           {"pattern":'.g("m")', "fr":["adjectif masculin",'A("grand").g("m")'],
                                       "en":["",'']},
           {"pattern":'.g("m")', "fr":["adjectif féminin",'A("grand").g("f")'],
                                       "en":["",'']},
           {"pattern":'.g("m")', "fr":["déterminant masculin",'D("le").g("m")'],
                                       "en":["",'']},
           {"pattern":'.g("m")', "fr":["déterminant féminin",'D("le").g("f")'],
                                       "en":["",'']},
           
         
           {"group":".pe(…)","fr":'personne (défaut 3)',
                                  "en":'person (default 3)'},
           {"pattern":".pe(1)", "fr":["1ère personne du singulier",'V("aimer").pe(1)'],
                           "en":["first person singular",'V("be").pe(1)']},
           {"pattern":".pe(2)", "fr":["2e personne du singulier",'V("aimer").pe(2)'],
                           "en":["second person singular",'V("be").pe(2)']},
           {"pattern":".pe(3)", "fr":["3e personne du singulier",'V("aimer").pe(3)'],
                           "en":["third person singular",'V("be").pe(3)']},
           {"pattern":'.pe(1).n("p")', "fr":["1ère personne du pluriel",'V("aimer").pe(1).n("p")'],
                           "en":["first person plural",'V("be").pe(1).n("p")']},
           {"pattern":'.pe(2).n("p")', "fr":["2e personne du pluriel",'V("aimer").pe(2).n("p")'],
                           "en":["second person plural",'V("be").pe(2).n("p")']},
           {"pattern":'.pe(3).n("p")', "fr":["3e personne du pluriel",'V("aimer").pe(3).n("p")'],
                           "en":["third person plural",'V("be").pe(3).n("p")']},
           {"pattern":'.g("f").p(1)', "fr":["déterminant (adjectif possessif) féminin",'D("mon").g("f").pe(1)'],
                                       "en":["",'']},
           
           {"group":".f(…)","fr":'Comparaisons',"en":'Comparison'},
           {"pattern":'.f("co")', "fr":["comparatif",'A("bon").f("co")'],
                           "en":["comparative",'A("good").f("co")']},
           {"pattern":'.f("su")', "fr":["superlatif",'A("bon").f("su")'],
                           "en":["superlative",'A("good").f("su")']},
           
           {"group":".aux(…)","fr":"Changement d'auxiliaire, le défaut est donné par le lexique.",
                              "en":'Change of auxiliary (ignored in English)'},
           {"pattern":"", "fr":["par défaut",'V("aller").t("pc")'],
                           "en":["",'']},
           {"pattern":"", "fr":["par défaut",'V("changer").t("pc")'],
                           "en":["",'']},
           {"pattern":'.aux("av")', "fr":["auxiliaire avoir",'V("aller").t("pc").aux("av")'],
                           "en":["",'']},
           {"pattern":'.aux("êt")', "fr":["auxiliaire être",'V("changer").t("pc").aux("êt")'],
                           "en":["",'']},
           
           {"group":"","fr":"Verbe essentiellement réflexif indiqué dans le lexique.",
                              "en":'Reflexive verb using <a href="#typeChange"><code>.typ({refl:true})</code></a>'},
           {"pattern":'', "fr":["par défaut",'V("enfuir").t("pc")'],
                          "en":['.typ({"refl":true})','VP(V("wash")).typ({"refl":True})']},

]};

pronomsSect={"fr":"","en":"",
    "ex":[{"group":"","fr":'Pronom sujet',"en":'Pronoun as subject'},
          {"pattern":".pe(1)", "fr":["1ère personne du singulier",'Pro("je").pe(1)'],
                           "en":["First person singular",'Pro("I").pe(1)']},
          {"pattern":".pe(2)", "fr":["2e personne du singulier",'Pro("je").pe(2)'],
                           "en":["Second person singular",'Pro("I").pe(2)']},
          {"pattern":".pe(3)", "fr":["3e personne du singulier",'Pro("je").pe(3)'],
                           "en":["Third person singular",'Pro("I").pe(3)']},
          {"pattern":'.pe(3).g("f")', "fr":["3e personne du féminin singulier",'Pro("je").pe(3).g("f")'],
                           "en":["Third person feminine singular",'Pro("I").pe(3).g("f")']},
          {"pattern":'.pe(3).g("n")', "fr":["",''],
                           "en":["Third person neutral singular",'Pro("I").pe(3).g("n")']},
          {"pattern":'.pe(1).n("p")', "fr":["1ère personne du pluriel",'Pro("je").pe(1).n("p")'],
                           "en":["First person plural",'Pro("I").pe(1).n("p")']},
          {"pattern":'.pe(2).n("p")', "fr":["2e personne du pluriel",'Pro("je").pe(2).n("p")'],
                           "en":["Second person plural",'Pro("I").pe(2).n("p")']},
          {"pattern":'.pe(3).n("p")', "fr":["3e personne du pluriel",'Pro("je").pe(3).n("p")'],
                           "en":["Third person plural",'Pro("I").pe(3).n("p")']},
          {"pattern":'.pe(3).n("p").g("f")', "fr":["3e personne du pluriel au féminin", 'Pro("je").pe(3).n("p").g("f")'],
                           "en":["",'']},
          {"pattern":'', "fr":["'on' invariable", 'Pro("on")'],
                           "en":["",'']},

          {"group":"","fr":'Pronom sujet accentué',"en":'Pronoun as subject itself'},
          {"pattern":".pe(1)", "fr":["1ère personne du singulier",'Pro("moi").pe(1)'],
                           "en":["First person singular",'Pro("me").pe(1)']},
          {"pattern":".pe(2)", "fr":["2e personne du singulier",'Pro("moi").pe(2)'],
                           "en":["Second person singular",'Pro("me").pe(2)']},
          {"pattern":".pe(3)", "fr":["3e personne du singulier",'Pro("moi").pe(3)'],
                           "en":["Third person singular",'Pro("me").pe(3)']},
          {"pattern":'.pe(3).g("f")', "fr":["3e personne du féminin singulier",'Pro("moi").pe(3).g("f")'],
                           "en":["Third person feminine singular",'Pro("me").pe(3).g("f")']},
          {"pattern":'.pe(3).g("n")', "fr":["",''],
                           "en":["Third person neutral singular",'Pro("me").pe(3).g("n")']},
          {"pattern":'.pe(1).n("p")', "fr":["1ère personne du pluriel",'Pro("moi").pe(1).n("p")'],
                           "en":["First person plural",'Pro("me").pe(1).n("p")']},
          {"pattern":'.pe(2).n("p")', "fr":["2e personne du pluriel",'Pro("moi").pe(2).n("p")'],
                           "en":["Second person plural",'Pro("me").pe(2).n("p")']},
          {"pattern":'.pe(3).n("p")', "fr":["3e personne du pluriel",'Pro("moi").pe(3).n("p")'],
                           "en":["Third person plural",'Pro("me").pe(3).n("p")']},
          {"pattern":'.pe(3).n("p").g("f")', "fr":["3e personne du pluriel au féminin", 'Pro("moi").pe(3).n("p").g("f")'],
                           "en":["",'']},

          {"group":"","fr":'Autres types de pronoms',"en":'Other types of pronouns'},
          {"pattern":'.pe(3).n("s")', "fr":["Pronom possessif",'Pro("mien").pe(3).n("s")'],
                           "en":["Singular owner",'Pro("mine").pe(3).n("s").ow("s")']},
          {"pattern":'.pe(3).n("p")', "fr":["À soi",'Pro("nôtre").pe(3).n("p")'],
                           "en":["Plural owner",'Pro("mine").pe(2).n("p").ow("p")']},
          {"pattern":'.pe(3).n("p")', "fr":["Moi réflexif",'Pro("moi*refl").pe(3).n("p")'],
                           "en":["Reflexive",'Pro("myself").pe(3).n("p")']},
          {"pattern":'.pe(3).n("p")', "fr":["Me réflexif",'Pro("me*refl").pe(3).n("p")'],
                           "en":["",'']},
          {"pattern":'.pe(3).n("p")', "fr":["Me complément d'objet indirect",'Pro("me*coi").pe(3).n("p")'],
                           "en":["",'']},
]};

formatSect={"fr":"","en":"",
"ex":[ 
       {"group":".b(…)","fr":'ajouter avant',"en":'add before'},
       {"pattern":'.b("-")', "fr":["Ajouter un tiret avant",'N("homme").b("-")'],
                     "en":["Add a dash before",'N("man").b("-")']},
       {"pattern":'.b("*")', "fr":["Ajouter une étoile avant",'N("homme").b("*")'],
                     "en":["Add a star before",'N("man").b("*")']},

       {"group":".a(…)","fr":'ajouter après',"en":'add after'},
       {"pattern":'.a(".")', "fr":["Ajouter un point après",'N("homme").a(".")'],
                     "en":["Add a dash before",'N("man").b("-")']},
       {"pattern":'.a("!")', "fr":["Ajouter point d'exclamation après",'N("homme").a("!")'],
                     "en":["Add an exclamation point after",'N("man").a("!")']},
       {"pattern":'.a(";")', "fr":["Ajouter point virgule après",'N("homme").a(";")'],
                     "en":["Add a semi-colon after",'N("man").a(";")']},
       {"pattern":'.a("\'s")', "fr":["Réaliser le possessif en anglais",'N("cousin").a("\'s")'],
                     "en":["Realize an English possessive",'N("man").a("\'s")']},

       {"group":".en(…)","fr":'entourer',"en":'wrap with'},
       {"pattern":'.en("(")', "fr":["entourer de parenthèses",'N("homme").en("(")'],
                     "en":["Wrap within parentheses",'N("man").en("(")']},
       {"pattern":'.en("[")', "fr":["entourer de crochets",'N("homme").en("[")'],
                     "en":["Wrap within brackets",'N("man").en("[")']},
       {"pattern":'.en("*")', "fr":["entourer d'étoiles",'N("homme").en("*")'],
                     "en":["Wrap within stars",'N("man").en("*")']},
       {"pattern":'.en("*").en("(")', "fr":["entourer de plusieurs symboles",'N("homme").en("*").en("(")'],
                     "en":["Wrap within many symbols",'N("man").en("*").en("(")']},

       {"group":"","fr":'',"en":''},
       {"pattern":'.lier()', "fr":["lier par un trait d'union",'VP(V("lier").t("ip").pe(2).lier(),Pro("le"))'],
                     "en":["Combine with a dash",'NP(N("mother").lier(),P("in").lier(),N("law"))']},

       {"group":"","fr":'',"en":''},
       {"pattern":'.cap()', "fr":["Mettre la première lettre en majuscule",'N("joueur").cap()'],
                     "en":["Capitalize first letter",'N("player").cap()']},

       {"group":".tag(…)","fr":"balise HTML","en":'HTML tag'},
       {"pattern":'.tag(<em>nom</em>,<em>{attributs}</em>)', 
             "fr":["italique souligné",'N("joueur").tag("i",{"style":"text-decoration:underline"})'],
            "en":["underline italics",'N("player").tag("i",{"style":"text-decoration:underline"})']},
       {"pattern":'', 
             "fr":["hyperlien",'N("joueur").tag("a",{"href":"http://www.google.com"})'],
             "en":["hyperlink",'N("player").tag("a",{"href":"http://www.google.com"})']},
       {"pattern":'', 
             "fr":["combinaison de balises",'N("maison").tag("b").tag("i")'],
             "en":["combining tags",'N("house").tag("b").tag("i")']},
]};

nPmods={"fr":'',"en":'',
    "ex": [
        {"group":"","fr":"Placement de l'adjectif (dépendant de la langue)",
            "en":"Adjective positioning (language dependent)"},
        {"pattern":"", "fr":["Par défaut",'NP(D("le"),A("petit"),N("jouet"))'],
                           "en":["Default",'NP(D("the"),A("small"),N("toy"))']},
        {"pattern":"", "fr":["Par défaut",'NP(D("le"),A("bleu"),N("jouet"))'],
                           "en":["Default",'NP(D("the"),N("toy"),A("blue"))']},
        {"pattern":'.pos("pre")', "fr":["pré-posé",'NP(D("le"),A("bleu").pos("pre"),N("jouet"))'],
                           "en":["",'']},
        {"pattern":'.pos("post")', "fr":["postposé",'NP(D("le"),A("petit").pos("post"),N("jouet"))'],
                           "en":["",'']},

        {"group":".pro()","fr":"Pronominalisation","en":"Pronominalisation"},
        {"pattern":"", "fr":["du sujet",'S(NP(D("le"),N("joueur")).pro(),VP(V("jouer")))'],
                       "en":["of the subject",'S(NP(D("the"),N("player")).pro(),VP(V("play")))']},
        {"pattern":"", "fr":["de l'objet direct sur",
'S(Pro("je").pe(1),\n\
   VP(V("aimer"),NP(D("le"),N("pomme")).pro()))'],
                       "en":["of the direct object",
'S(Pro("I").pe(1),\n\
   VP(V("love"),NP(D("a"),N("apple").g("n")).pro()))']},
        {"pattern":"", 
         "fr":["de l'objet indirect sur <code>PP</code>",
'S(Pro("je").pe(1),\n\
   VP(V("aller"),\n\
       PP(P("vers"),NP(D("le"),N("maison"))).pro()))'],
         "en":["of the indirect object",
'S(Pro("I").pe(1),\n\
   VP(V("go"),\n\
      PP(P("to"),NP(D("a"),N("house").g("n")).pro())))']},
]};

sentType={"fr":'',"en":'',
    "ex": [
       {"pattern":".typ({\"neg\":True})",
        "fr":["Négation",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"neg":True})'],
        "en":["Negation",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"neg":True})']},
       {"pattern":'.typ({"neg":"..."})',
        "fr":["Négation spéciale",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"neg":"plus"})'],
        "en":["",'']},
       {"pattern":".typ({\"pas\":True})",
        "fr":["Passif",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"pas":True})'],
        "en":["Passive",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"pas":True})']},
       {"pattern":".typ({\"perf\":True})",
        "fr":['Perfect <i>Ignoré</i>','S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"perf":True})'],
        "en":["Perfect",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"perf":True})']},
       {"pattern":".typ({\"prog\":True})",
        "fr":["Progressif",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"prog":True})'],
        "en":["Progressive",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"prog":True})']},
       {"pattern":".typ({\"refl\":True})",
        "fr":["Réflexif",'S(NP(D("le"),N("chat")),\n  VP(V("laver"))).typ({"refl":True})'],
        "en":["Reflexive",'S(NP(D("the"),N("cat")),\n  VP(V("wash"))).typ({"refl":True})']},
       {"pattern":".typ({\"exc\":True})",
        "fr":["Exclamatif",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"exc":True})'],
        "en":["Exclamative",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"exc":True})']},
       {"pattern":".typ({\"contr\":True})",
        "fr":["Contraction (ignorée en français)",
              'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ(\n    {"neg":True,"contr":True})'],
        "en":["Contraction",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ(\n   {"neg":True,"contr":True})']},
       {"group":'.typ({"mod":"..."})',"fr":"Modalité","en":"Modality"}, 
       {"pattern":'.typ({"mod":"poss"})',
        "fr":["Possibilité",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"mod":"poss"})'],
        "en":["Possibility",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"mod":"poss"})']},
       {"pattern":'.typ({"mod":"perm"})',
        "fr":["Permission",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"mod":"perm"})'],
        "en":["Permission",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"mod":"perm"})']},
       {"pattern":'.typ({"mod":"nece"})',
        "fr":["Nécessité",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"mod":"nece"})'],
        "en":["Necessity",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"mod":"nece"})']},
       {"pattern":'.typ({"mod":"obli"})',
        "fr":["Obligation",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"mod":"obli"})'],
        "en":["Obligation",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"mod":"obli"})']},
       {"pattern":'.typ({"mod":"will"})',
        "fr":["Volonté",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"mod":"will"})'],
        "en":["Willingness",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"mod":"will"})']},
       {"group":'.typ({"int":"..."})',"fr":"Interrogation","en":"Interrogation"},         
       {"pattern":'.typ({"int":"yon"})',
        "fr":["Interrogative (oui/non)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"yon"})'],
        "en":["Interrogative (yes/no)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"yon"})']},
       {"pattern":'.typ({"int":"wos"})',
        "fr":["Interrogative (sujet humain?)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"wos"})'],
        "en":["Interrogative (who human?)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"wos"})']},
       {"pattern":'.typ({"int":"was"})',
        "fr":["Interrogative (sujet?)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"was"})'],
        "en":["Interrogative (who?)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"was"})']},
       {"pattern":'.typ({"int":"wod"})',
        "fr":["Interrogative (que subit l'objet)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"wod"})'],
        "en":["Interrogative (who is the object)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"wod"})']},
       {"pattern":'.typ({"int":"wad"})',
        "fr":["Interrogative (quoi subit l'objet)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"wad"})'],
        "en":["Interrogative (what is the object)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"wad"})']},
       {"pattern":'.typ({"int":"woi"})',
        "fr":["Interrogative (à qui l'objet humain)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"woi"})'],
        "en":["Interrogative (to whom the object human)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"woi"})']},
       {"pattern":'.typ({"int":"wai"})',
        "fr":["Interrogative (à qui l'objet)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"wai"})'],
        "en":["Interrogative (to whom the object)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"wai"})']},
       {"pattern":'.typ({"int":"whe"})',
        "fr":["Interrogative (où est l'action)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"whe"})'],
        "en":["Interrogative (where is the action)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"whe"})']},
       {"pattern":'.typ({"int":"why"})',
        "fr":["Interrogative (pourquoi)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"why"})'],
        "en":["Interrogative (why)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"why"})']},
       {"pattern":'.typ({"int":"whn"})',
        "fr":["Interrogative (quand)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"whn"})'],
        "en":["Interrogative (when)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"whn"})']},
       {"pattern":'.typ({"int":"how"})',
        "fr":["Interrogative (comment est l'action)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"how"})'],
        "en":["Interrogative (who is the action)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"how"})']},
       {"pattern":'.typ({"int":"muc"})',
        "fr":["Interrogative (combien est l'action)",'S(NP(D("le"),N("chat")),\n  VP(V("aimer"),NP(D("le"),N("souris")))).typ({"int":"muc"})'],
        "en":["Interrogative (how much is the action)",'S(NP(D("the"),N("cat")),\n  VP(V("love"),NP(D("the"),N("mouse")))).typ({"int":"muc"})']},
       ]}

dateCreation={"fr":"Création d'une date","en":"Date creation",
    "ex":[
        {"pattern":'DT()',"fr":["Date courante",'DT()'],
                          "en":["Current date",'DT()']},
        {"pattern":'DT("...")',"fr":["Date passée",'DT("2014-11-21 21:00:00")'],
                               "en":["Date in the past",'DT("2014-11-21 21:00:00")']},
        {"pattern":'DT("...")',"fr":["Date sans temps",'DT("2017-12-31")'],
                               "en":["Date without time ",'DT("2017-12-31")']},
        {"pattern":'DT(datetime)',"fr":["Date à partir de datetime",'DT(datetime.datetime(2014,12,31))'],
                                  "en":["Date from datetime",'DT(datetime.datetime(2014,12,31))']},
        ]}   

dateOption={"fr":"Formatage d'une date (défaut <code>.nat()</code>)",
                "en":"Date formatting (default <code>.nat()</code>)",
    "ex":[
        {"pattern":'.nat()',"fr":["en lettres, par défaut",'DT()'],
                            "en":["as words, by default",'DT()']},
        {"pattern":'.nat(False)',"fr":["en chiffres",'DT().nat(False)'],
                            "en":["as digits",'DT().nat(False)']},
        {"group":'.dOpt({"year": , "month": , "date": , "day": , "hour": , "minute": , "second": , "nat":, "det":, "rtime":})',
                            "fr":"Contrôle de l'affichage de chacun des éléments de la date",
                            "en":"Control over the display of date components"},
        {"pattern":'.dOpt(..)',"fr":["Heure seulement",'DT().dOpt({"year": False, "month": False, "date": False, "day": False})'],
                            "en":["Time only",'DT().dOpt({"year": False, "month": False, "date": False, "day": False})']},
        {"pattern":'{"nat":False}',"fr":["Affichage de l'heure et des minutes (en chiffres)",'DT().dOpt({"year": False, "month": False, "date": False,\n "day": False, "second": False, "nat":False})'],
                            "en":["Display hour and minutes as digits",'DT().dOpt({"year": False, "month": False, "date": False,\n "day": False, "second": False, "nat":False})']},
        {"pattern":'{"det":False}',"fr":["Non affichage des déterminants de la date",'DT().dOpt({"det": False})'],
                            "en":["Do not display determiner",'DT().dOpt({"det": False})']},
        {"pattern":'{"rtime":True}',"fr":["Date relative par rapport à aujourd'hui",'DT().dOpt({"rtime": True})'],
                            "en":["Relative date compared with today",'DT().dOpt({"rtime": True})']},
        {"pattern":'{"rtime":".." or Date}',"fr":["Date relative après une autre",'DT("2021-09-01").dOpt({"rtime": "2021-08-27"})'],
                            "en":["Relative date after another one",'DT("2021-09-01").dOpt({"rtime": "2021-08-27"})']},
        {"pattern":'{"rtime":".." or Date}',"fr":["Date relative avant une autre date",'DT("2021-09-01").dOpt({"rtime":datetime.datetime(2021,9,10)})'],
                            "en":["Relative date before another one",'DT("2021-09-01").dOpt({"rtime":datetime.datetime(2021,9,10)})']},        
        ]}

numberFormat={"fr":"Formatage d'un nombre","en":"Number formatting",
    "ex":[
        {"pattern":"{\"mprecision\":..}","fr":["arrondi",'NO(1.847584).dOpt({"mprecision": 0})'],
                                     "en":["rounding",'NO(1.847584).dOpt({"mprecision": 0})']},
        {"pattern":"{\"mprecision\":..}","fr":["maximum 4 décimales",'NO(1.847584).dOpt({"mprecision": 4})'],
                                     "en":["4 decimal rounding",'NO(1.847584).dOpt({"mprecision": 4})']},
        {"pattern":"{\"raw\":False}","fr":["nombre avec formattage",'NO("1.847584").dOpt({"raw": False})'],
                                "en":["number with formatting",'NO("1.847584").dOpt({"raw": False})']},
        {"pattern":"{\"raw\":True}","fr":["nombre sans formattage",'NO("1023.84").dOpt({"raw": True})'],
                                "en":["raw number without formatting",'NO("1023.84").dOpt({"raw": True})']},
        {"pattern":"{\"nat\":True}","fr":["nombre en toutes lettres",'NO("125").dOpt({"nat": True})'],
                                "en":["number in words",'NO("125").dOpt({"nat": True})']},
        {"pattern":"{\"ord\":True}","fr":["nombre ordinal",'NO("10").dOpt({"ord": True})'],
                                "en":["ordinal number",'NO("10").dOpt({"ord": True})']},
        ]} 

numberAgreement={"fr":"Accord du nom selon le nombre","en":"Noun agreement in number",
    "ex":[{"pattern":"","fr":["avec zéro",'NP(NO(0), N("avion"))'],
                        "en":["with zero",'NP(NO(0), N("plane"))']},
          {"pattern":"","fr":["avec un entier",'NP(NO(1), N("avion"))'],
                        "en":["with an integer",'NP(NO(1), N("plane"))']},
          {"pattern":"","fr":["avec un entier",'NP(NO(2), N("avion"))'],
                        "en":["with an integer",'NP(NO(2), N("plane"))']},
          {"pattern":"","fr":["avec un réel",'NP(NO(0.24), N("livre"))'],
                        "en":["with a real",'NP(NO(0.24), N("pound"))']},
          {"pattern":"","fr":["avec un réel",'NP(NO(2.94), N("livre"))'],
                        "en":["with a real",'NP(NO(2.94), N("pound"))']},
          {"pattern":"","fr":["avec un ordinal",'NP(NO(1).dOpt({"ord":True}),N("station"))'],
                        "en":["with an ordinal",'NP(NO(1).dOpt({"ord":True}),N("station"))']},
          {"pattern":"","fr":["accord de l'adjectif",'NP(NO(2),A("rouge"), N("avion"))'],
                        "en":["",'']},
    ]}

# cloneUse={"fr":"Illustration de l'utilisation de <code>.clone()</code>",
#               "en":"Simple example of use of <code>.clone()</code>",
#     "ex":[
#           {"pattern":"","fr":["déclaration",'pomme = N("pomme")'],
#                         "en":["declaration",'apple = N("apple")']},
#           {"pattern":"","fr":["déclaration",'gars = NP(D("le"),N("garçon"))'],
#                         "en":["declaration",'boy = NP(D("the"),N("boy"))']},
#           {"pattern":"","fr":["modification",'pomme.n("p")'],
#                         "en":["modification",'apple.n("p")']},
#           {"pattern":"","fr":["effet de bord visible",'pomme'],
#                         "en":["side-effect occurred",'apple']},
#           {"pattern":"","fr":["redéclaration",'pomme = N("pomme")'],
#                         "en":["redeclaration",'apple = N("apple")']},
#           {"pattern":"","fr":["sauve l'original",'pommes=pomme.clone().n("p")'],
#                         "en":["save the original",'apples=apple.clone().n("p")']},
#           {"pattern":"","fr":["original a bien été sauvé",'pomme'],
#                         "en":["original was saved",'apple']},
#           {"pattern":"","fr":["Autre exemple, plus subtil",'la_pomme = NP(D("le"),pomme)'],
#                         "en":["Another example, more devious",'the_apple = NP(D("the"),apple)']},
#           {"pattern":"","fr":["clone est utile pour la réutilisation",
#                              'S(la_pomme.clone().a(","),gars,VP(V("manger"),la_pomme.clone().pro()))'],
#                         "en":["close is useful for reuse",
#                               'S(the_apple.clone().a(","),boy,VP(V("eat"),the_apple.clone().pro()))']},
#           {"pattern":"","fr":["exemple précédent sans clone; <b>mauvais résultat</b> car <code>.pro()</code> a modifié <code>pomme</code> avant sa réalisation",
#                              'S(la_pomme.a(","),gars,VP(V("manger"),la_pomme.pro())).b("*")'],
#                         "en":["previous example without clone; <b>bad result</b> because <code>.pro()</code> modified <code>apple</code> before its realization",
#                               'S(the_apple.a(","),boy,VP(V("eat"),the_apple.pro())).b("*")']},
#     ]}

functionUse={"fr":"Fonctions pour la réutilisation d'expression",
              "en":"Functions for expression reuse",
    "ex":[
        {"pattern":"","fr":["définition de fonction",'autoF = lambda:NP(D("un"),N("auto"))'],
                      "en":["function definition",'carF = lambda:NP(D("a"),N("car"))']},
        {"pattern":"","fr":["appel avec modification",'autoF().n("p")'],
                      "en":["call with modifcation",'carF().n("p")']},
        {"pattern":"","fr":["appel original",'autoF()'],
                      "en":["original call",'carF()']},
        {"pattern":"","fr":["fonction avec paramètre",'pommeF = lambda n="s": NP(D("un"),N("pomme").n(n))'],
                      "en":["parameterized function",'appleF = lambda n="s": NP(D("a"),N("apple").n(n))']},
        {"pattern":"","fr":["appel de fonction",'pommeF()'],
                      "en":["function call",'appleF()']},
        {"pattern":"","fr":["appel paramétrisé",'pommeF("p")'],
                      "en":["parameterized call",'appleF("p")']},
    ]};

addUse={"fr":"Illustration de l'utilisation de <code>.add(..)</code>",
            "en":"Simple example of use of <code>.add(..)</code>",
    "ex":[
          {"pattern":"","fr":["déclaration",'pomme = NP(D("le"),N("pomme"))'],
                        "en":["declaration",'apple = NP(D("the"),N("apple"))']},
          {"pattern":"","fr":["déclaration",'gars = NP(D("le"),N("garçon"))'],
                        "en":["declaration",'boy = NP(D("the"),N("boy"))']},
          {"pattern":"","fr":["ajout à un syntagme vide",'S().add(pomme)'],
                        "en":["add to an empty phrase",'S().add(apple)']},
          {"pattern":"","fr":["ajouts à un syntagme existant",
                              'CP(C("et"),NP(D("le"),N("fruit"))).add(pomme).add(gars)'],
                        "en":["add to an existing phrase",
                              'CP(C("and"),NP(D("a"),N("fruit"))).add(apple).add(boy)']},
          {"pattern":"","fr":["ajout avec position",'S(VP().add(V("aimer")).add(pomme)).add(gars,0)'],
                        "en":["add with position",'S(VP().add(V("love")).add(apple)).add(boy,0)']},
        
]};