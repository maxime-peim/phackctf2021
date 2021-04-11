# Journée portes ouvertes

## Sujet :

> Il y a des courants d'air au niveau du serveur comme s'il y avait des port(e)s ouvert(e)s.
> Url : journees-portes-ouvertes.phack.fr

Tags : `network` `port` `easy`

## Solution :
Au vu du nom du challenge et des tags, on est parti sur un petit scan de ports sur la machine.

```
sudo nmap -v -A -T4 -p0- journees-portes-ouvertes.phack.fr
```

Pleinnnnn de ports sont ouverts, certains renvoient juste un message "There is nothing there", d'autres renvoient un message composé d'étoile `*` et de bout de flag.

On rassemble chaque morceau, et on a le flag !

`PHACK{s4cr3_c0ur4nt_d'R}`