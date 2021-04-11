# Thief

## Sujet :

> Vous venez de découvrir quelque chose d'étrange en examinant un dump réseau de votre entreprise.
> Analysez ce fichier et remontez l'alerte si c'est nécessaire.

Tags : `network` `dns` `medium`

## Solution :
En ouvrant la capture, on remarque des requêtes DNS vers des noms de domaines au format un peu particulier :
`7b22696e646578223a202231222c202264617461223a20222b227d.phack.fr`.

En convertissant l'hexadécimal vers de l'ASCII, on obtient une chaîne lisable : `{"index": "1", "data": "+"}`.

On comprend qu'il faut récupérer chaque requête DNS de cette forme et mettre bout à bout les caractères désignés par le champs `data`.

Par flemme d'automatiser, et vu que le nombre de requêtes était assez faible, on le fait à la main :

`PHACK{3xf1ltR4ti0n_thRoUgh_dNs}`

Attention ! Les premiers caractères que l'on obtient (+-/ ...) ne font pas partis du flag.