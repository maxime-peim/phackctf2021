# WE-1 (FlagClub)

## Sujet :

> Une semaine avant le CTF, vous avez eu accès à un amuse bouche.
>
> Je vous transmets ce message que je viens de recevoir à votre attention :
>
```
    La première règle du Flag Club est : il est interdit de parler du Flag Club.
    La seconde règle du Flag Club est : il est interdit de parler du Flag Club.
    Troisième règle du Flag Club : rassemblez cinq morceaux de secret pour reconstituer le flag.
    Quatrième règle : les points rapportés par ce challenge uniquement seront dégressifs, en fonction du nombre de résolution.
    Cinquième règle : coopérer ou non, mentir ou dire la vérité, la décision vous revient.
    Sixième règle : pour ce challenge uniquement, les échanges d'informations entre les équipes sont autorisés.
    Septième règle : le challenge continuera aussi longtemps que nécessaire.

        - Adi Shamir
```
>
> Était également joint ceci :
>
```
38-4b8af6c974828dd6c60ab544e3c273a8b7c1b4ee773076982ef70ddab62944798c43eb62f1cc25d989d26e02ade2132ee3d18d619b20a5126a94b02d0144152a22e9e303ee4ae22e08f59a5663428146a605b26c3ded23f9f1cca6ef07a2f0f6b5
```

Tags : `starting` `shamir` `easy`

## Solution :

Après deux trois recherches, on comprend qu'il s'agit d'un système de partage de secret créé par Adi Sharmir. (https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing)
On demande gentimemt à d'autres équipes si on peut avoir leur part de secret, et on utilise un site qui permet de déchiffrer le secret à partir des coefficients qu'on fournit. (http://point-at-infinity.org/ssss/demo.html)

Pour notre part, nous avons réunit ceux-ci :
```
15-d76439aa22a213f152efe19b351b19a78ad4d7eeba72a9a38944269499785a19a629d13655693005de16d9df293477c71c7e8e1e7af006746d4bf753e4b1345023c9aced288c92a00b24e22a901cbc3b4d7567392d8df641b2ed9637444413d359
18-a3fe0dac3ee83db1216e5054a5083ed94892ed89701b6e48f446efe24e2280c6d6515275f55cdd6fe94ac9fde1cba9eb03e4acd35c6d7a8b84cd4a14504aae55f5b8ad64a1cf4b709c74769320e75767b2720761b223b64da460d911e186d7eaf7
24-d542d717d933b3fee5a88837b3c49a62faa4f701204018518c8cede1711f1f1d02462a1baed2e785c8b794fd60b67d346e0a4aa169898a823c9158bbd1a5ca4cc12a28899a0c3eeb0087e69d600f701978dd1951332c3a1201d9457a508ca1d05f
38-4b8af6c974828dd6c60ab544e3c273a8b7c1b4ee773076982ef70ddab62944798c43eb62f1cc25d989d26e02ade2132ee3d18d619b20a5126a94b02d0144152a22e9e303ee4ae22e08f59a5663428146a605b26c3ded23f9f1cca6ef07a2f0f6b5
39-29173e293536d2a099af92f90325eb3a899c520c099176affef69e390acd7552e6d3fe15d7715c5a0ed5ca2e2761396784e5a7f37eb5ee432efa99d5b4921aaa7f6cff7375f116d4fde89712b928bd919100ad050f1f8154f047665d4c8c0aad31
40-e31f57a97d924f8dc38b840d745f1df88a70517075498ba751f6c59a15766e6b98a86235eaef26d213dcdc5b8f6d627e02158c6e4d31187b25af27f933f13bd2c7c7ebbb434b11962089f56646b8a9d7b33eda50033fc4dacbe1170b79277256b6
```
Attention il faut bien mettre les coefficients par ordre croissant du nombre avant le `-`.

`PHACK{And the eighth and final rule, if this is your first night at Flag Club, you have to flag!}`