# DataChallengeENS

Mon avis c'est qu'il faut juste faire un graph qui comprends les relations entre les postings avec du NLP, le graphe devrait avoir des gros thèmes a certains endroits genre on imagine une partie du graphe tres conencté avec des jobs IA et de l'autre computer science par exemple, le lien entre deux nodes et la probabilité de passage d'un posting a une autre.
Puis parce que en vrai parfois les descirptions se ressemble mais en vrai il suffit d'un mot genre "biologie" qui pourrait degouter un utilisateur, il faut creer un score qui prends aussi en compte les sessions des autres utilisateurs.


Enfaite grace a noter premiere estimation de nlp sur les descriptions, on a une matrice d'adjacence puis apres pour toutes les sessions on va essayer d'estimer la suite de la session mais si on se rends co,pte qu'une connexion 'ai pas fait eon baisse le score et si une connexion est faire comme prevu on l'augmente en fonction de la rapidité du clic