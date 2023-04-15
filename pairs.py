# module pairs du chatbot umapon
# contanant les exemples de questions et réponses que peux comprendre et répondre le ChatBot umapon

my_pairs = [
    [
        r"mon nom est (.*)",
        ["Bonjour %1, je suis le ChatBot U-Mapon. Je peux vous donner les informations sur l'université Mapon. Que aimeriez-vous savoir ?"]
    ],
    [
        r"(.*)?(bonjour|salut|coucou|bonsoir|hello|hi|hey|slt|bjr|bsr|holla)",
        ["Bonjour, je suis le ChatBot U-Mapon. Je peux vous donner les informations sur l'université Mapon. Que aimeriez-vous savoir ?"]
    ],
    [
        r"(.*)?(tu peux|vous pouvez)?(.*)?faire quoi?",
        ["Je suis un chabot informatif de l'université Mapon. Je peux vous donner des informations liées à l'université Mapon comme :\nCombien de facultés elle organise \nQuelles sont les conditions pour être retenu comme étudiant \nLes modalités de frais académiques \nLes filières disponibles dans chaque faculté \nComment les cours sont organisés \nEt autres informations"]
    ],
    [
        r"(a propos)? de (toi|vous|tw|you)",
        ["Je suis un chabot informatif de l'université Mapon. Je peux vous donner des informations liées à l'université Mapon comme :\nCombien de facultés elle organise \nQuelles sont les conditions pour être retenu comme étudiant \nLes modalités de frais académiques \nLes filières disponibles dans chaque faculté \nComment les cours sont organisés \nEt autres informations"]
    ],
    [
        r"qui? (es tu|tu es|es-tu|vous etes|etes-vous)",
        ["Je suis un chabot informatif de l'université Mapon. Je peux vous donner des informations liées à l'université Mapon comme :\nCombien de facultés elle organise \nQuelles sont les conditions pour être retenu comme étudiant \nLes modalités de frais académiques \nLes filières disponibles dans chaque faculté \nComment les cours sont organisés \nEt autres informations relatives à l'U-MAPON"]
    ],
    [
        r"(.*)?(savoir|connaitre|plus de|sur|renseigner|renseignement)(.*)?(universite mapon|umapon|unimap|mapon|u-mapon|unimapon|universite)",
        ["L'université Mapon est une université polytechnique, bilingue axée sur la haute technologie, située en République Démocratique du Congo.\nElle organise deux grandes facultés dont la Polytechnique et les Sciences économiques. Et chaque faculté comporte différentes filières.\nPour savoir plus sur une faculté, taper le nom de la faculté."]
    ],
    [
        r"(.*)?(faculte|departement)",
        ["L'université Mapon est une université polytechnique, bilingue axée sur la haute technologie, située en République Démocratique du Congo.\nElle organise deux grandes facultés dont la Polytechnique et les Sciences économiques. Et chaque faculté comporte différentes filières.\nPour savoir plus sur une faculté, taper le nom de la faculté."]
    ],
    [
        r"(comment|cmt)(.*)(vas|va|allez|vous)",
        ["Je vais bien, merci. Comment puis-je vous aider ?"]
    ],
    [
        r"(.*)?(inscription|inscrire|insri|admission|admettre|retenu)(.*)?(universite mapon|umapon|unimap|mapon|u-mapon|unimapon|universite)?",
        ["Pour être admis comme étudiant à l'université Mapon, les nouveaux étudiants doivent passer un test d'admission qui permettra d'évaluer leurs niveaux. Ceux qui réussiront seront rétenus et les autres seront orientés vers une autre faculté.\nPour les étudiants ne se trouvant pas au lieu du test, il est possible de passer un test en ligne sur la plateforme de l'université.\nPour plus d'informations, veuillez vous rendre à l'apparitorat de l'université Mapon."]
    ],
    [
        r"(.*)?(adresse|adresses|localisation|localisations|siège|contact|contacts|se trouve|localise|se situe)(.*)?(universite mapon|umapon|unimap|mapon|u-mapon|unimapon|universite)?",
        ["L'Université Mapon se trouve en RDC, dans la province du Maniema, dans la ville de Kindu, Commune de Mikelenge, Quartier LUKUNDA, Avenue ATIBU, N°24"]
    ],
    [
        r"(.*)?(polytech|technique|polytechnique|polytechniques)",
        ["La faculté des ingérieurs est constituée des quatre filières dont :\n\t1. Le génie informatique\n\t2. Le génie électrique\n\t3. Le génie mécanique\n\t4. Les mines et géologie \nPOur savoir plus sur une filière, entrez le nom de la filière."]
    ],
    [
        r"(.*)?(electrique|electricite|elec|electriques|electricites|elecs)",
        ["L'U-MAPON vise à former des meilleurs ingénieurs en électricité, d'où elle est dotée des ateliers et laboratoires électriques de dernières générations afin de bien former les étudiants dans la pratique. Après les cours théoriques dispensés par des professeurs compétents, les étudiants sont invités en mettre en pratique les théories apprises dans l'atelier ou laboratoire et si nécessaire faire une descente sur terrain."]
    ],
    [
        r"(.*)?(informatique|computer|ordinateur|charles babbage)",
        ["La filière de génie informatique organisée à l'université Mapon ne vise pas seulement à former les simples informaticiens mais à former les ingénieurs informaticiens capables de travailler dans n'importe quel secteur informatique. D'où, les salles équipées d'ordinateurs et d'une bonne connexion internet sont mises à la disposition des étudiants pour but de faciliter leur apprentissage."]
    ],
    [
        r"(.*)?(mecanique|mecano)",
        ["La mécanique enseignée à l'université Mapon est celle donnée dans des grandes universités au monde. Les étudiants apprenent la mécanique en la vivant grâce au laboratoire mécanique de haute technologie. Le laboratoire mécanique regorge tous les matériels nécessaires pour un apprentissage de la mécanique et les cours sont dispensés par des professeurs hautement qualifiés."]
    ],
    [
        r"(.*)(mines|geologies|geologie|mines et geologie|geologie et mines|mines geologie)",
        ["La faculté polytechnique comporte la filière Mines & géologie qui est un mélange d'étude des mines et de la géologie. Les étudiants en mines et géologies sont hautement formés dans le but de leurs fournir une maitrise parfaite de toutes les notions de leur domaine."]
    ],
    [
        r"(.*)(economie|economique|economies|economiques|economi)",
        ["Hormis la faculté Polytechnique, l'université Mapon organise une autre faculté de Sciences économiques qui est constituée de deux filières dont économie mathématique et économie de gestion"]
    ],
    [
        r"(.*)(argent|frais|frais academiques|fais academique|paiement|payer|paie|paiement)",
        ["Voici les frais à payer pour chaque facultés:\n1. POLYTECHNIQUE\n-Frais académiques : 500$ (pour la promotion préparatoire) et 700$ (pour les promotions motantes) à payer à la banque TMB \n-Carte d'étudiants : 10$ (pour tous les étudiants) à payer à l'université auprès du comptable \n-Frais connexes(laboratoire) : 50$ (pour tous les étudiants) à payer à la banque \n-Frais d'inscription et réinscription : 20$ (pour tous les étudiants) à payer à la banque \n-Frais de session et fiches d'examens : 15$ (pour chaque session et pour tous les étudiants) à payer à l'université \n-Frais de stage(carnet de stage) : 12.5$ (pour les promotions BAC3 et M2) à payer à l'université \n-Recommandation de stage : 5$ (pour les promotions BAC3 et M2) à payer à l'université \n-Frais d'entérinement de diplôme : 75$ (pour les promotions BAC3 et M2) \n-Frais de logement : 300$ (uniquement pour les étudiants logé au HOME) à payer à la banque \n2. SCIENCES ECONOMIQUES\n-Frais académiques : 400$ (pour la promotion préparatoire) et 500$ (pour les promotions motantes) à payer à la banque TMB \n-Carte d'étudiants : 10$ (pour tous les étudiants) à payer à l'université auprès du comptable \n-Frais connexes(laboratoire) : 50$ (pour tous les étudiants) à payer à la banque \n-Frais d'inscription et réinscription : 20$ (pour tous les étudiants) à payer à la banque \n-Frais de session et fiches d'examens : 15$ (pour chaque session et pour tous les étudiants) à payer à l'université \n-Frais de stage(carnet de stage) : 12.5$ (pour les promotions BAC3 et M2) à payer à l'université \n-Recommandation de stage : 5$ (pour les promotions BAC3 et M2) à payer à l'université \n-Frais d'entérinement de diplôme : 75$ (pour les promotions BAC3 et M2) \n-Frais de logement : 300$ (uniquement pour les étudiants logé au HOME) à payer à la banque\nNB: Le montant à payer pour chaque frais peut varier!"]
    ],
    [
        r"(.*)(etudier|etud|bosse)?(.*)(gratuitement|gratos|gratuit)",
        ["L'université Mapon n'est pas gratuite mais elle permet même aux personnes n'ayant pas beaucoup de moyen d'étudier car elle offre la possibilité de payer les frais académiques par tranches..."]
    ],
    [
        r"(.*)master",
        ["Oui, l'université Mapon organise aussi des promotions Masters en Polytechnique tout comme en Sciences économiques."]
    ],
    [
        r"(.*)(logement|loger|home|campus|loge)",
        ["Les étudiants qui veulent peuvent rester au HOME et doivent payer 300$ comme frais de logement (payable en 3 tranches)", "L'université Mapon possède des HOME pour loger les étudiants. Les filles et garçons ne sont pas logés le même bâtiment.\nLes frais de logement sont fixés à 300$ (payé en trois tranches)"]
    ],
    [
        r"(.*)(etranger|nationalite|maniem|kindu|autocht)",
        ["L'université Mapon accepte tous les étudiants venant de n'importe quel pays, n'importe quelle province et n'importe quelle ville. Aucune discrimination n'est faite."]
    ],
    [
        r"(.*)(tricherie|triche|tricher)",
        ["N'est autorisé aucun étudiant de tricher ni collaborer lors d'une épreuve quelconque. Tout étudiant attrapé comme tricheur risque son exclusion définitive de l'université Mapon car l'université Mapon vise à former des personnes compétentes, utiles, et honnêtes dans la vie et non des tricheurs.", "Les tricheurs ne sont pas les bienvenus à l'universtité Mapon. Risque une exclusion définitive de l'université Mapon toute personne attrapée comme tricheur lors d'une quelconque épreuve."]
    ],
    [
        r"(au revoir|bye|a plus tard)$",
        ["Merci et j'espère que je vous ai été util. Sinon pour plus d'informations sur l'université, veuillez vous rendre sur son site web officiel (www.universitemapon.ac.cd) ou à l'université sur place."]
    ],
    [
        r"^aide$",
        ["Pour interagir avec moi, veuillez poser des questions contenant des mots clés comme par exemple: \nrenseignement\nbourse\nfacultes\nfrais academiques\nadmission\nlogement\nadresse"]
    ],
    [
        r"(.*)?(code|cree|fabrique|programmeur|codeur|createur)",
        ["Je suis un ChatBot informatif de l'université Mapon. J'ai été programmé par YUMA KITENGE VICTOIRE, étudiant en BAC2 génie informatique, dans le cadre du travail pratique du cours de Projet Multidisciplinaire dispensé par Pr. Dr. Ir. KALENGA KAUNDE KASONGO Jimmy."]
    ],
    [
        r"(.*)?(ton|votre) nom",
        ["Je suis ChatBot U-mapon. Comment puis-je vous aider ?"]
    ],
    [
        r"(.*)?(tu t'appel|t'appel|vous appel)",
        ["Vous pouvez m'appeler ChatBot U-mapon. Quelles informations puis-je vous fournir ?"]
    ],
    [
        r"(.*)?(bourse|boursier)",
        ["Les étudiants excellents sont pris en charge par la Fondation Mapon par octroiement d'une bourse d'études de 1500$. Seuls les étudiants ayant obtenu au moins 70 pourcents à la fin de l'année académique sont bénéficiers de cette bourse.\nPour les nouveaux qui veulent une bourse, doivent contacter l'unimapon pour des directives."]
    ],
    [
        r"(.*)?(livre|bibliot)",
        ["L'université Mapon est équipée d'une grande bibliothèque scientifique. Les livres sont à la disposition de tous les étudiants y compris des ordinateurs connectés à l'internet pour faciliter les recherches."]
    ],
    [
        r"(.*)(prof|cours|enseign)(.*)(prof|cours|enseign)",
        ["L'université Mapon se soucie de la qualité des professeurs qui doivent donner cours. Seuls les profs compétents et qualifiés sont invités à dispenser leurs cours. Beaucoup de fois, l'U-Mapon fait recours aux professeurs vivant à l'etranger qui sont invités à donner cours sur place ou en ligne."]
    ],
    [
        r"(.*)?universite(.*)?(privee|publiq|public)",
        ["L'université Mapon est une université privée de la Fondation Mapon."]
    ],
    [
        r"(.*)(enseignement|cours)",
        ["Les cours sont donnés par des professeurs hautement qualifiés qui se font accompagnés par des assistants. Ces derniers sont chargés de faire des travaux pratiques avec les étudiants dans le but de faciliter la compréhension des matières données par les prof.\nChaque prof est demandé de mettre à la disposition des étudiants les syllabus et livres du cours. Aucune vente de document n'est autorisée; les étudiants reçoivent les notes de cours en format électronique et c'est à eux d'imprimer ou pas.\nLes cours sont dispensé par la méthode de projection ou par écrit au tableau; et parfois en ligne."]
    ],
    [
        r"(.*)(date|creation|cree|quand|debut|fonde|anne)(.*)(date|creation|cree|quand|debut|fonde|anne)",
        ["L'université Mapon était opérationnelle depuis 2017"]
    ],
    [
        r"(.*)(jimmy|kalenga|kaunde|kasongo|recteur)",
        ["Pr. Dr. Ir. KALENGA KAUNDE KASONGO Jimmy est le recteur de l'université Mapon."]
    ],
    [
        r"(.*)(yuma|kitenge)",
        ["YUMA KITENGE Victoire est la personne qui m'a programmé.", "YUMA KITENGE Victoire est mon codeur"]
    ],
    [
        r"(.*)(activite|culture|programme|journe)(.*)?(activite|culture|programme|journe)",
        ["L'université Mapon organise des journées culturelles, des programmes sportifs qui permettent aux étudiants de se divertir et de montrer leurs savoirs en présentant des projets personnels ou en groupe lors des journées culturelles."]
    ],
    [
        r"(.*)(importan|impac|universite mapon|umapon|unimap|mapon|u-mapon|unimapon|universite|etud|garan|avantag|intere)(.*)(importan|impac|universite mapon|umapon|unimap|mapon|u-mapon|unimapon|universite|etud|garan|avantag|intere)",
        ["Etudier à l'université Mapon a plusieurs avantages. L'université Mapon met tous ses moyens afin que quand un étudiant finit son cursus académique, qu'il ne peine pas pour être embauché ou trouver de boulot mais c'est le travail qui doit le chercher."]
    ],
    [
        r"(.*)(dure|academi|annee|fai)(.*)?(dure|academi|annee|fai)(.*)?(dure|academi|annee|fai)",
        ["Comme toute autre université, une année académique à l'université Mapon équivaut à 10 mois."]
    ],
    [
        r"(.*)(lmd|system|traditi)(.*)?(lmd|system|traditi)?",
        ["L'université Mapon est dans le système LMD(Licence, Master, Doctorat)"]
    ],
    [
        r"(.*)(docto|docte)",
        ["Jusque là le doctorat n'est pas encore organisé à l'université Mapon. Mais d'ici peu de temps, il sera disponible."]
    ],
    [
        r"(.*)(sport|basket|foot)",
        ["<Un corps sain dans un esprit sain>. Différents sports et activités sportives sont disponibles à l'université Mapon tel quel basketball, football, voleyball, handball, tenis, ping-pong et autres."]
    ]
]

unknown = "Désolé, je ne suis pas programmé pour répondre à cette question. Pour un guide sur mon utilisation, veuillez taper aide."