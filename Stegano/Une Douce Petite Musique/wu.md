# Une Douce Petite Musique

## Sujet :

> Avec vos talents de hacker vous interceptez un échange plutôt louche.

Tags : `stegano` `musique` `medium`

Hints : `abc` `ABC`

## Solution :
On a deux e-mails que l'on peut ouvrir avec Thunderbird par exemple. On en extrait un tableur excel et un fichier `.mid`.
En ouvrant le fichier MIDI dans Audacity, on a une suite de notes. On peut retranscrire ces notes dans le format américain
(https://www.studybass.com/using-the-site/american-english-music-terminology/). On comprend vite qu'une note avec sa hauteur donne les coordonnées d'une cellule dans le tableur excel reçu.
A ajustement près (dans Audacity il fallait retirer 2 à la hauteur pour que ça colle avec le tableur), on peut déchiffrer à la main le flag.
On se rend compte qu'il s'agit des paroles de la musique `Allumer le feu` de Johnny Hallyday !

`PHACK{_ALLUMER_LE_FEU_ALLUMER_LE_FEU_ET_FAIRE_DANSER_LES_DIABLES_ET_LES_DIEUX_ALLUMER_LE_FEU_ALLUMER_LE_FEU_ET_VOIR_GRANDIR_LA_FLAMME_DANS_VOS_YEUX_ALLUMER_LE_FEU_}`