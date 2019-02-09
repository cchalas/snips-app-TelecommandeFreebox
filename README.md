- [Documentation](#Documentation)
- [Démo](#Démo)
- [Command-List](#Command-list)
- [Tips](#Tips)


## Documentation

Permet le control de la freebox révolution V6 via snips.

Il vous faudra :
 - récuperer le code de votre télécommande pour ce faire :
Dans les **réglages** de la freebox player ensuite **système**, **informations freebox player et server**, vous verrez alors à droite de l'écran : **Code télécommande réseau**
 - connaitre le numéro hd présent dans l'url de la remote commande : 1 par défaut, mais si vous êtes en multi room cela peut être 1 ou 2. Pour le savoir lancer les 2 url. Cela doit soit allumer votre freeboxtv si elle est éteinte soit l'allumer : 
    http://hd1.freebox.fr/pub/remote_control?code=mettre le code de votre télécommande&key=power
    ou
    http://hd2.freebox.fr/pub/remote_control?code=mettre le code de votre télécommande&key=power


## Démo

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/ntSlGBUQ0c0/0.jpg)](https://youtu.be/ntSlGBUQ0c0)


## Command list

**List of command** :
* démarrer la freebox (ex : hey snips démarre la freebox)
* arrêter la freebox (ex : hey snips arrête la freebox)
* mettre en pause un programme télé (ex : hey snips met en pause)
* reprendre le programme télé (ex : hey snips reprend le programme)
* avancer dans le timeshift (ex : hey snips avance dans le programme)
* reculer dans le timeshift (ex : hey snips recule dans le prgramme)
* reprendre le direct (ex : hey snips remet le direct)
* active le PiP (ex :hey snip active le pip)
* desactive le PiP (ex: hey snips desactive le pip)
* permute de chaine pour le pip (ex : hey snips permute le pip)
* Augmenter le volume par pas de 25 (ex : Hey snips monte le son de la télé)
* Diminuer le volume par pas de 25 (ex : Hey snips baisse le son de la télé)
* Muter la télé (ex : Hey snips coupe le son de la télé)
* Unmute la télé (ex : Hey snips remet le son de la télé)
* Accès à la télévision (ex : Hey snips mets la télévision)
* Accès à l'application twitch (ex : Hey snips mets twitch | le stream)
* Accès au programme télé (ex : Hey snips affiche le programme télé)
* Quitte le programme télé (ex : Hey snips quitte le programme télé)
* Changer de chaine (ex : Hey snips met France 4)

## change log

### V0.0.2

-   Allumer / éteindre la freebox (ex hey snips démarre la télé, hey snips arrête la télé, hey snips peux tu demarrer la télé)
-   Ajout du chaine par defaut afin de zapper directement dessus à l'allumage de la Freebox
-   Ajout du volume par defaut, permet de définir le volume minimum lors de l'allumage de la Freebox

### V0.0.1
-   Initial realese

## Tips

1. CEC option

    If you leave your TV on standby and your TV is CEC compatible you can activate the CEC options of the freebox player and also of your TV. Thanks to this you will be able to turn on your freebox player by voice with snips which will wake up your TV too. And the opposite is true when you turn off your freebox it will put your TV on standby

    To activate this in the freebox player go to **Réglages > Affichage > Réglages HDMI CEC ** then activate this options :

    * Activer le HDMI CEC
    * Mise en veille des équipements HDMI CEC depuis la Freebox
    * Don’t forget to activate CEC option in your TV if this is possible
