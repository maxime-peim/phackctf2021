# Strong Daddy

## Sujet :

> Ton pote se vante car son père est militaire dans l'armée de terre et il lui aurait soit-disant appris toutes les techniques pour pouvoir échanger des messages sans que l'ennemi ne puisse comprendre.
>
> Il est temps de montrer à cette tête de noeud qu'il n'est pas aussi fort qu'il le prétend

Tags : `stegano` `alphabet` `easy`

## Solution :

On remarque vite qu'il suffit de prendre les premières lettres de chaque mots pour voir apparaître le flag.
On peut alors lire la première lettre de chaque mot lorsqu'il ne s'agit pas d'un nombre ou d'un caractère spécial.

```
PAPA            -> P
HOTEL           -> H
ALPHA           -> A
CHARLIE         -> C
KILO            -> K
ACCOLADEGAUCHE  -> {
WHISKY          -> W
THREE           -> 3
INDIA           -> I
ROMEO           -> R
DELTA           -> D
THREE           -> 3
SIERRA          -> S
TANGO           -> T
UNDERSCORE      -> _
FIVE            -> 5
TANGO           -> T
THREE           -> 3
GOLF            -> G
ALPHA           -> A
NOVEMBER        -> N
ZERO            -> 0
UNDERSCORE      -> _
THREE           -> 3
VICTOR          -> V
THREE           -> 3
ROMEO           -> R
ACCOLADEDROITE  -> }
```

`PHACK{W3IRD3ST_5T3GAN0_3VER}`