# Sudoku v2

## Sujet :

> L'administrateur du serveur a voulu vous aider en ajoutant une aide visuelle lors de la saisie de votre mot de passe.
> 
> Hum Hum.. C'est pas une bonne idée !
>
> === Connexion SSH ===
> 
> Login : padawan
> 
> Mdp : padawan
> 
> Serveur : sudoku2.phack.fr

Tags : `system` `cve` `medium`

## Solution :
Après quelques recherches, on apprend que l'option pwfeedback, qui permet d'avoir des `*` dans sudo, était bugguée (un vulgaire buffer overflow) sur certaines versions.
C'est sûrement le cas pour nous ici, donc on ne perd rien à essayer.

On trouve un petit exploit (https://www.exploit-db.com/exploits/48052) qui nous rend root sur la machine.
C'est un peu dommage d'utiliser un exploit trouvé sur internet, mais comme disait un grand homme dont j'ai oublié le nom :
`Peut importe le chemin, tant que ça flag à la fin.`

`PHACK{*_****_****_****_***_**_*_****_***}`