L'api qu'on va explorer est celle de la sncf, commencez par creer un compte ici

https://www.digital.sncf.com/startup/api

Une fois vos access recu, vous allez apprendre a manier les api et leurs donnees en json.

Repondez aux questions suivantes dans un script python que vous mettrez sur github.

    manipuler un json dans python:

lisez le fichier json joint a ce brief (stop_areas.json)

afficher le avec le module prettyprint

rajouter un arret dans le json (utiliser dump ou dumps)

    requeter une api
    renseignez vous sur les differents endpoints (qu'est ce que c'est?)
    lire le json donnee par le endpoint https://api.sncf.com/v1/coverage/sncf/stop_areas (utilisez requests)
    Trouver l’ensemble des gares disponibles sur l’API et créer un fichier csv avec les codes de la gare, son nom et ses coordonnées latitude et longitude, ainsi que les informations administratives de la région quand elles sont disponibles
    Récupérer les informations sur un trajet entre Paris Gare de Lyon et Lyon Perrache

Paris - Gare de Lyon (code de la gare : stop_area:OCE:SA:87686006) Lyon - Gare Lyon Perrache (code de la gare : stop_area:OCE:SA:87722025) Indice : utiliser la requête “journeys”

1

 combien y a-t-il d’arrêts entre ces deux gares ? (utilisez la clé ‘journeys’)

combien de temps d’arrêt à chacune d’elles ?

    Vous êtes Gare de Lyon et il est 18h00.

    1

    Combien de tgv partent entre 18h00 et 20h00 ?

    Lequel arrive le plus tôt à sa destination finale ?

    Essayer de trouver toutes les correspondances possibles depuis un trajet entre Paris et Perpignan

    Transformer une ou plusierus des donneess renvoyes par lapi en une ou plusieurs tables CSV

    Bonus: Représenter toutes les gares atteignables avec un graphique type scatter. Distinguer les gares atteintes en un seul trajet et celles atteintes avec une correspondance.

​

