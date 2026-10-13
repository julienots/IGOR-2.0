"""Exemples : programmes, compétitions, santé et récupération."""

PROGRAMMES = [
    ("Fais-moi un programme débutant",
     "Programme débutant, 3 séances par semaine (ex. lundi, mercredi, vendredi), séances A et B "
     "en alternance :\n\nSéance A\n- Tractions (ou négatives) : 4 x max -2\n- Dips (ou dips sur "
     "banc) : 4 x 8-12\n- Squats : 3 x 15-20\n- Hollow body hold : 3 x 20-30 s\n\nSéance B\n- "
     "Rowing australien : 4 x 10-12\n- Pompes : 4 x 10-20\n- Fentes : 3 x 10/jambe\n- Support "
     "hold aux barres parallèles : 3 x 20-30 s\n- Élévations de genoux suspendu : 3 x 10\n\n"
     "Repos : 1 min 30 à 2 min. Quand tu fais le haut de la fourchette sur toutes les séries, "
     "passe à une variante plus dure. Objectif à 3 mois : 8 tractions, 15 dips, 30 pompes."),
    ("Fais-moi un programme pour la planche",
     "Programme planche, 3 séances par semaine. Je pars du principe que tu tiens une tuck planche "
     "5 s (sinon, dis-le-moi et j'adapte).\n\nÉchauffement (10 min) : poignets, épaules, scapula "
     "push-ups, planche lean légère.\n\n1. Tenues à ta progression : 5 x 6-10 s, repos 2-3 min\n2. "
     "Tuck planche push-ups ou presses : 4 x 3-6\n3. Pseudo planche push-ups : 3 x 6-10\n4. Planche "
     "lean : 3 x 15-20 s\n5. Dips : 3 x 8-12\n6. Hollow body hold : 3 x 30 s\n\nProgression : "
     "quand tu tiens 5 x 10 s propres, passe à l'étape suivante (advanced tuck, straddle…). "
     "Une semaine allégée toutes les 4 à 6 semaines pour les tendons."),
    ("Fais-moi un programme pour le front lever",
     "Programme front lever, 3 séances par semaine. Base supposée : 10 tractions strictes.\n\n"
     "Échauffement : suspension active, scapula pull-ups, rotations d'épaules.\n\n1. Tenues de "
     "front lever à ta progression : 5 x 6-10 s, repos 2-3 min\n2. Front lever raises : 4 x 3-6\n3. "
     "Négatives de front lever : 3 x 3 (5 s de descente)\n4. Tractions lestées ou tractions "
     "strictes : 4 x 5-8\n5. Rowing australien pieds surélevés : 3 x 10\n6. Dragon flag négatif "
     "ou hollow body : 3 x 5 / 30 s\n\nPasse à la progression suivante quand tu tiens 5 x 10 s "
     "propres."),
    ("Fais-moi un programme pour le muscle-up",
     "Programme muscle-up, 3 séances par semaine, sur 6 à 8 semaines. Prérequis : 8 tractions "
     "strictes.\n\n1. Tractions explosives (chest-to-bar) : 5 x 3-5\n2. Négatives de muscle-up : 4 x "
     "2-3, descente lente\n3. Transition sur barre basse, pieds au sol : 3 x 5\n4. Dips sur barre "
     "droite : 4 x 8-10\n5. Tractions strictes : 3 x max -2\n6. Hollow body : 3 x 30 s\n\nChaque "
     "semaine, ajoute 1 rep sur les exercices explosifs. Dès que tu as ton premier muscle-up, "
     "remplace les négatives par des séries de 1 à 3 muscle-ups."),
    ("Fais-moi un programme freestyle",
     "Programme freestyle, 3 à 4 séances par semaine.\n\nÉchauffement (15 min) : épaules, "
     "poignets, swings faciles, quelques muscle-ups légers.\n\n1. Technique (30 min) : 2 figures "
     "en cours d'apprentissage, 5 à 8 essais chacune, repos complet. Qualité avant quantité.\n2. "
     "Combos (15 min) : enchaîne des figures acquises par blocs de 2 ou 3.\n3. Force spécifique "
     "(15 min) : muscle-ups explosifs 4 x 3, tractions 3 x 8, dips 3 x 10.\n4. Gainage : hollow, "
     "arch, 3 x 30 s.\n\nUne séance par semaine : enchaîne un passage complet chronométré pour "
     "simuler la compétition. Arrête les figures risquées dès que la fatigue arrive."),
    ("Fais-moi un programme pour la traction à un bras",
     "Programme one arm pull-up, 2 à 3 séances par semaine. Base : 15 tractions strictes.\n\n1. "
     "Tractions lestées lourdes : 5 x 3-5\n2. Archer pull-ups : 4 x 3-5 par côté\n3. Négatives à "
     "un bras : 3 x 2 par côté (5 s de descente)\n4. Tenues en haut à un bras : 3 x 5-10 s\n5. "
     "Curl biceps ou tractions supination : 3 x 8\n6. Suspension à un bras : 3 x 20 s\n\nAvance "
     "lentement, les coudes ont besoin de temps. Objectif réaliste : 6 mois à 2 ans selon ton "
     "niveau de départ."),
    ("Fais-moi un programme complet statique pour 4 séances par semaine",
     "Split sur 4 séances :\n\nLundi — Poussée statique\n- Planche (tenues) : 5 x 6-10 s\n- Planche "
     "push-ups à ta progression : 4 x 3-6\n- Handstand : 10 min de pratique\n- Dips lestés : 4 x 6"
     "\n\nMardi — Traction statique\n- Front lever (tenues) : 5 x 6-10 s\n- Front lever raises : 4 "
     "x 4\n- Back lever : 4 x 8 s\n- Tractions lestées : 4 x 5\n\nJeudi — Poussée (variante)\n- "
     "Planche leans et presses : 4 x 5\n- HSPU : 4 x 5\n- Pseudo planche push-ups : 3 x 8\n- "
     "L-sit / V-sit : 4 x 15 s\n\nVendredi — Traction (variante)\n- Front lever pull-ups : 4 x 3\n"
     "- Muscle-ups stricts : 4 x 3\n- Drapeau : 4 x 5-8 s par côté\n- Dragon flag : 3 x 5\n\n"
     "Mercredi, samedi et dimanche : repos ou mobilité."),
    ("J'ai que 30 minutes par séance",
     "Pas de souci, on optimise :\n- 5 min d'échauffement ciblé ;\n- 15 min sur ta figure "
     "prioritaire (tenues + 1 exercice dynamique) ;\n- 10 min de force de base en superset "
     "(ex. tractions + dips, 3 tours).\n3 à 4 séances de 30 minutes bien ciblées valent mieux "
     "qu'une longue séance par semaine. Dis-moi ton objectif et je te détaille la séance."),
    ("Fais-moi un programme pour m'entraîner chez moi sans barre",
     "Programme maison sans barre, 3 séances par semaine :\n1. Pompes (variante adaptée à ton "
     "niveau : classiques, archer, pseudo planche) : 4 x 8-15\n2. Pike push-ups : 4 x 6-10\n3. "
     "Planche lean au sol : 4 x 15-20 s\n4. Rowing sous une table solide : 4 x 8-12\n5. Dips entre "
     "deux chaises stables : 3 x 10\n6. Squats ou pistol squats : 3 x 10\n7. Hollow body : 3 x "
     "30 s\nL'idéal reste d'investir dans une barre de traction de porte et une paire de "
     "parallettes : c'est peu cher et ça ouvre énormément de figures."),
    ("Combien de séances par semaine en calisthenics ?",
     "Ça dépend de ton niveau :\n- Débutant : 3 séances corps complet.\n- Intermédiaire : 3 à 4 "
     "séances, en séparant poussée et traction.\n- Avancé : 4 à 6 séances, avec le travail des "
     "figures réparti sur la semaine.\nLe facteur limitant, ce sont les tendons et les "
     "articulations, pas les muscles. Garde des jours de repos et une semaine allégée toutes les "
     "4 à 6 semaines."),
    ("Je stagne depuis des semaines, je fais quoi ?",
     "Vérifions dans l'ordre :\n1. Sommeil et alimentation suffisants ? (7-9 h, assez de "
     "protéines).\n2. Fatigue accumulée ? Fais une semaine allégée.\n3. Toujours les mêmes "
     "exercices ? Change de variante : négatives, presses, élastique, autre amplitude.\n4. Point "
     "faible ? Souvent la force de base (tractions/dips lestés) ou la technique.\n5. Tu notes tes "
     "séances ? Sans suivi, difficile de progresser.\nDonne-moi ta figure, ton niveau et ton "
     "programme actuel, et je trouve le blocage."),
    ("Comment s'échauffer avant une séance ?",
     "Échauffement de 10 à 15 min :\n1. Cardio léger 2-3 min (corde à sauter, jumping jacks).\n2. "
     "Mobilité : rotations des poignets, coudes, épaules, hanches.\n3. Activation : scapula "
     "pull-ups, scapula push-ups, suspension active, support hold.\n4. Séries progressives de "
     "l'exercice du jour, à faible intensité.\nPour la statique, insiste sur les poignets et les "
     "coudes : ce sont eux qui encaissent le plus."),
    ("Comment éviter les blessures ?",
     "Mes règles :\n- Échauffe-toi à chaque séance, surtout poignets, coudes et épaules.\n- "
     "Augmente le volume en bras tendus très progressivement : les tendons s'adaptent moins vite "
     "que les muscles.\n- Ne force jamais sur une douleur articulaire vive.\n- Garde une "
     "technique propre, même si tu dois reculer d'une progression.\n- Fais des semaines allégées "
     "régulières.\n- En freestyle, apprends à chuter et utilise des tapis.\nUne douleur qui "
     "persiste plus d'une semaine : consulte un professionnel de santé."),
    ("J'ai mal au coude",
     "Les douleurs au coude sont fréquentes en calisthenics (tendinites des épicondyles ou du "
     "biceps), surtout avec beaucoup de tractions, de bras tendus ou de muscle-ups.\n- Réduis "
     "temporairement le volume des exercices qui déclenchent la douleur.\n- Varie les prises "
     "(neutre, anneaux) pour soulager l'articulation.\n- Ajoute du renforcement léger et "
     "progressif (curls, extensions de poignet).\nJe ne suis pas médecin : si la douleur est vive, "
     "gonfle ou dure, consulte un médecin ou un kinésithérapeute."),
    ("Que manger pour progresser en calisthenics ?",
     "Les bases :\n- Protéines suffisantes : environ 1,6 à 2 g par kg de poids de corps par jour.\n"
     "- Assez de calories pour récupérer.\n- En calisthenics, le poids de corps compte : un "
     "léger surplus pour prendre de la force, un léger déficit si tu veux t'alléger pour la "
     "statique.\n- Hydratation et sommeil.\nPour un plan alimentaire précis, rapproche-toi d'un "
     "diététicien."),
    ("Comment progresser en tractions ?",
     "Si tu en fais moins de 5 : négatives lentes, rowing australien, tractions avec élastique.\n"
     "Entre 5 et 12 : 4 à 5 séries à 1-2 reps de l'échec, plusieurs fois par semaine, et des "
     "méthodes comme le grease the groove (séries faciles réparties dans la journée).\nAu-delà de "
     "12 : ajoute du lest (3 à 6 reps lourdes) et des variantes (archer, explosives, front lever "
     "pull-ups). Garde une amplitude complète : bras tendus en bas, menton au-dessus de la barre."),
    ("Calisthenics ou musculation pour la force ?",
     "Les deux fonctionnent. La calisthenics développe une force relative énorme (force par "
     "rapport au poids de corps), la coordination et le contrôle. La musculation permet une "
     "surcharge plus simple à doser. Beaucoup d'athlètes combinent : figures au poids du corps + "
     "tractions et dips lestés. Si ton objectif ce sont les figures, priorité à la calisthenics."),
]

COMPETITIONS = [
    ("Comment se passent les compétitions de street workout ?",
     "Il existe plusieurs formats selon les organisateurs :\n- Freestyle : un passage "
     "chronométré à la barre, noté par des juges sur la difficulté, l'exécution, les combos, la "
     "créativité et la fluidité.\n- Battles : deux athlètes s'affrontent en alternant des passages, "
     "les juges ou le public désignent le gagnant.\n- Statique / force : on présente des figures et "
     "des enchaînements de force, notés selon la difficulté et la qualité de tenue.\n- Endurance : "
     "maximum de répétitions (tractions, dips, muscle-ups).\n- Street lifting : charges maximales "
     "en traction et dips lestés.\nLe règlement exact dépend toujours de l'organisateur."),
    ("C'est quoi la WSWCF ?",
     "La WSWCF (World Street Workout & Calisthenics Federation) est l'une des principales "
     "fédérations internationales de street workout. Elle organise des championnats du monde "
     "depuis le début des années 2010, avec notamment des épreuves de freestyle. D'autres "
     "organisations et circuits indépendants existent aussi. Pour les dates, catégories et "
     "règlements à jour, consulte directement leurs sites et réseaux officiels."),
    ("Comment sont notées les figures en compétition freestyle ?",
     "Les critères habituels :\n- Difficulté : les figures dures (rotations, gros lâchers, "
     "statiques avancées) rapportent plus.\n- Exécution : bras tendus quand il faut, corps gainé, "
     "pas de chute ni de pause.\n- Combos et fluidité : enchaîner sans temps mort.\n- Variété et "
     "créativité : montrer différents types de figures.\n- Présence et énergie.\nUne chute ou une "
     "figure mal tenue fait perdre des points : mieux vaut un passage propre qu'un passage "
     "trop risqué."),
    ("Comment me préparer à ma première compétition ?",
     "Plan de préparation (6 à 8 semaines) :\n1. Lis le règlement : durée du passage, critères, "
     "figures interdites.\n2. Construis un passage avec des figures que tu réussis à plus de 90 % "
     "à l'entraînement.\n3. Répète le passage complet 1 à 2 fois par semaine, chronométré et "
     "filmé.\n4. Garde de la force de base pour ne pas t'épuiser en fin de passage.\n5. Dernière "
     "semaine : allège, ne tente plus de nouvelles figures.\n6. Le jour J : échauffement complet, "
     "magnésie, et prends du plaisir. L'expérience compte plus que le classement la première fois."),
    ("C'est quoi une battle de street workout ?",
     "Dans une battle, deux athlètes s'affrontent directement : chacun fait un passage court à la "
     "barre, puis l'autre répond, sur plusieurs manches. Les juges (ou parfois le public) "
     "désignent le vainqueur selon la difficulté, la créativité, la propreté et l'impact. La "
     "stratégie compte : garde des figures fortes pour les derniers rounds."),
]
