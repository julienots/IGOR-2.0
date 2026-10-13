"""Exemples : fondamentaux, vocabulaire et figures complémentaires."""

BASES = [
    ("C'est quoi le hollow body ?",
     "Le hollow body, c'est la position creuse de gymnastique : allongé sur le dos, bas du dos "
     "plaqué au sol, épaules et jambes décollées, bras tendus au-dessus de la tête. C'est LA base "
     "du gainage en calisthenics : on la retrouve dans la planche, le front lever, le handstand et "
     "le swing. Objectif : 3 x 30 à 60 s propres."),
    ("C'est quoi la protraction et la rétraction des omoplates ?",
     "- Protraction : tu écartes les omoplates, le haut du dos s'arrondit (on pousse le sol). "
     "Indispensable pour la planche.\n- Rétraction : tu serres les omoplates l'une vers l'autre. "
     "Utile pour le front lever et les tractions.\n- Dépression : tu abaisses les épaules, loin des "
     "oreilles. Utile presque partout.\n- Élévation : tu montes les épaules vers les oreilles. "
     "Utile en handstand.\nExercices : scapula push-ups et scapula pull-ups."),
    ("C'est quoi le false grip ?",
     "Le false grip, c'est une prise où le poignet passe au-dessus de la barre ou de l'anneau, la "
     "paume posée dessus plutôt qu'en dessous. Il facilite énormément la transition du muscle-up, "
     "surtout aux anneaux. Il est inconfortable au début : entraîne-le en suspension, puis en "
     "tractions."),
    ("Barre ou anneaux, c'est quoi la différence ?",
     "- La barre est stable : idéale pour le freestyle, le muscle-up explosif et les leviers.\n- Les "
     "anneaux sont instables : ils demandent plus de stabilisation, sont plus doux pour les "
     "articulations (les mains tournent librement) et permettent des figures spécifiques (croix de "
     "fer, maltese aux anneaux, support turned out).\nLes deux sont complémentaires."),
    ("C'est quoi les parallettes ?",
     "Ce sont de petites barres parallèles posées au sol. Elles soulagent les poignets (position "
     "neutre), permettent plus d'amplitude (pompes en déficit, HSPU profonds) et sont parfaites "
     "pour la planche, le L-sit, le handstand et la manna."),
    ("C'est quoi le tuck, le straddle et le full ?",
     "Ce sont les niveaux de difficulté d'une figure statique :\n- Tuck : genoux groupés contre la "
     "poitrine, le plus facile.\n- Advanced tuck : dos plat, genoux sous les hanches.\n- Straddle : "
     "jambes tendues écartées.\n- Half lay : jambes tendues, genoux pliés serrés ou une jambe.\n- "
     "Full : jambes tendues et serrées, le plus dur.\nPlus le corps est long, plus le bras de levier "
     "est grand, et plus la figure est dure."),
    ("C'est quoi le grease the groove ?",
     "Le grease the groove, c'est faire de nombreuses séries faciles (environ 50 % de ton max) "
     "réparties sur toute la journée, jamais jusqu'à l'échec. Ça marche très bien pour augmenter "
     "un nombre de tractions, de dips ou de pompes, ou pour automatiser un geste technique."),
    ("C'est quoi le German hang ?",
     "Le German hang, c'est la position de suspension où les bras sont tendus derrière toi, épaules "
     "en extension maximale, après avoir fait passer les jambes entre les bras. C'est une position "
     "d'étirement des épaules, et la base du back lever. Vas-y doucement : 3 x 10-20 s, sans "
     "forcer sur une douleur."),
    ("C'est quoi le dead hang et l'active hang ?",
     "- Dead hang : suspension passive, épaules relâchées. Bon pour décompresser et travailler la "
     "prise.\n- Active hang : suspension avec les épaules engagées (abaissées), bras tendus. C'est "
     "le point de départ correct des tractions, du front lever et du swing."),
    ("Comment avoir mes premières pompes ?",
     "Progressions :\n1. Pompes contre un mur.\n2. Pompes inclinées (mains sur une table ou un "
     "banc).\n3. Pompes sur les genoux.\n4. Négatives : descente lente de 3 à 5 s.\n5. Pompes "
     "classiques.\nGarde le corps gainé comme une planche et les coudes à environ 45° du corps."),
    ("C'est quoi les variantes de pompes avancées ?",
     "Après les pompes classiques :\n- diamond push-ups (triceps) ;\n- archer push-ups (vers la "
     "pompe à un bras) ;\n- pseudo planche push-ups (vers la planche) ;\n- pike push-ups (vers le "
     "HSPU) ;\n- pompes explosives et claquées (puissance) ;\n- one arm push-up ;\n- 90° push-ups et "
     "planche push-ups pour l'élite."),
    ("Comment avoir mes premières tractions ?",
     "Progressions :\n1. Suspension active : 3 x 20-30 s.\n2. Scapula pull-ups : 3 x 10.\n3. "
     "Rowing australien : 3 x 10-15.\n4. Négatives : saute en haut et descends en 5 s, 3 x 5.\n5. "
     "Tractions avec élastique.\n6. Première traction stricte !\n3 séances par semaine, et tu "
     "devrais avoir ta première traction en quelques semaines."),
    ("C'est quoi le rowing australien ?",
     "Le rowing australien (australian pull-up), c'est une traction horizontale : tu es sous une "
     "barre basse, corps gainé, pieds au sol, et tu tires la poitrine vers la barre. Plus le corps "
     "est horizontal, plus c'est dur. Parfait pour préparer les tractions et le front lever."),
    ("C'est quoi les dips coréens ?",
     "Les korean dips se font sur une barre droite, mais la barre est derrière toi : tu descends "
     "en amenant la barre dans le bas du dos. Ils demandent de bonnes épaules en extension. "
     "Commence avec une amplitude réduite et progresse lentement."),
    ("C'est quoi le pistol squat ?",
     "C'est un squat complet sur une jambe, l'autre jambe tendue devant toi. Progressions : squat "
     "sur une jambe vers une chaise, pistol assisté en tenant un support, négatives, puis pistol "
     "complet. Il demande force, équilibre et mobilité des chevilles."),
    ("Faut-il travailler les jambes en calisthenics ?",
     "Oui ! Des jambes fortes aident au freestyle (impulsions, sauts, sorties), à l'équilibre et à "
     "la santé globale. Exercices : pistol squats, shrimp squats, fentes, nordic curls, sauts. "
     "Pour la statique, garde toutefois des jambes pas trop lourdes : 2 séances courtes par "
     "semaine suffisent souvent."),
    ("C'est quoi le nordic curl ?",
     "Le nordic curl : à genoux, chevilles bloquées, tu descends le buste vers l'avant le plus "
     "lentement possible en gardant le corps droit. Il renforce énormément les ischio-jambiers et "
     "protège des blessures. Commence par des négatives et rattrape-toi avec les mains."),
    ("C'est quoi le crow pose ?",
     "Le crow (ou corbeau), c'est un équilibre sur les mains, genoux posés sur l'arrière des bras, "
     "bras légèrement fléchis. C'est une bonne première étape pour apprendre à mettre le poids "
     "vers l'avant, avant le frog stand et la tuck planche."),
    ("C'est quoi le tiger bend ?",
     "Le tiger bend : depuis le handstand, tu descends sur les avant-bras, puis tu remontes en "
     "handstand en poussant. Il demande une force énorme en triceps et en épaules, et un très bon "
     "contrôle de l'équilibre."),
    ("C'est quoi la pompe à un bras ?",
     "La one arm push-up : pompe sur une seule main, pieds écartés pour la stabilité, corps "
     "gainé. Progressions : archer push-ups, pompes à un bras inclinées, négatives à un bras, puis "
     "la version complète. Prérequis : environ 30 pompes classiques."),
    ("C'est quoi le clap muscle-up ?",
     "C'est un muscle-up si explosif que tu lâches la barre en haut pour taper dans les mains "
     "avant de la rattraper en appui. C'est une figure de freestyle de base qui demande un "
     "muscle-up très puissant et un rattrapage sûr : commence par des muscle-ups explosifs où tu "
     "décolles juste les mains."),
    ("C'est quoi les front lever pull-ups ?",
     "Ce sont des tractions réalisées en restant en position de front lever, corps horizontal : "
     "tu tires la barre vers les hanches puis tu reviens bras tendus. Progressions : tuck, "
     "advanced tuck, straddle, full. Exercice excellent pour le front lever et le muscle-up "
     "strict."),
    ("Combien de temps pour avoir un front lever ?",
     "Ça dépend de ton niveau de départ, de ton poids et de ta régularité. En moyenne, en partant "
     "de 10 tractions et avec 3 séances par semaine : tuck en quelques semaines, straddle en 6 à "
     "12 mois, full en 1 à 2 ans. Les personnes légères avec des membres courts progressent "
     "souvent plus vite."),
    ("Je suis grand, c'est plus dur ?",
     "Oui, en général : des bras et des jambes plus longs créent un bras de levier plus grand, "
     "donc les figures statiques comme la planche ou le front lever sont plus dures. Mais c'est "
     "tout à fait possible : il faut juste plus de patience. Les grands ont souvent un avantage "
     "en freestyle pour l'amplitude des swings."),
    ("Je suis débutant total, par quoi je commence ?",
     "Bienvenue ! Commence par les fondamentaux :\n- pompes (ou leurs progressions) ;\n- "
     "tractions (ou rowing australien et négatives) ;\n- dips (ou dips sur banc) ;\n- squats ;\n- "
     "gainage (hollow body).\n3 séances par semaine, en notant tes reps. Dis-moi combien de "
     "pompes, tractions et dips tu fais aujourd'hui, et je te fais un programme sur mesure."),
    ("Comment mesurer mon niveau en calisthenics ?",
     "Repères indicatifs :\n- Débutant : moins de 5 tractions, moins de 10 dips.\n- Intermédiaire "
     ": 10 à 15 tractions, 20 dips, muscle-up, L-sit, tuck front lever.\n- Avancé : 20 tractions, "
     "muscle-up strict, straddle front lever, straddle planche, handstand libre.\n- Élite : full "
     "planche, full front lever, one arm pull-up, figures comme la maltese ou le victorian.\nDonne-"
     "moi tes chiffres et je te situe."),
]
