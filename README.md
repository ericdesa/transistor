
<div align="center">
  <img src="doc/logo.png" alt="Transistor" width="200">

  <h4>Scrip pour m'annoncer la météo, mon temps de trajet et lancer la radio après avoir détecté mon entrée dans ma salle de bain.</h4>
  #raspberry #python

  <hr/>

</div>

## Fonctionnement

- Un détecteur infrarouge détecte une présence
- Si on est entre 5h et 11h du matin et qu'il s'agit de la 1ère détection de la journée, on continue
- On demande la météo à Yahoo
- En semaine, on demande le temps de parcours pour aller au boulot à Google
- La radio se lance pour 10 minutes, mais ce temps est prolongé à chaque détection
- S'il n'y a eu aucun mouvement pendant 10 minute, la radio s'arrête jusqu'au lendemain

Ce qui produit quelque chose de ce type : ```Le ciel est partiellement couvert. Il fait 8 degrés. En partant à 9 heures il vous faudra 25 minutes pour arriver au travail via N104. [lancement de la radio]```

<a href="doc/example.wav">Télécharger un exemple audio</a>


## Dépendances
- **pico2wave** pour la synthèse vocale (voir tuto sur  [framboise314.fr](http://www.framboise314.fr/donnez-la-parole-a-votre-raspberry-pi/))

- **VLC** via [la lib python](https://wiki.videolan.org/PythonBinding/) pour lancer la radio (en l'occurence France Inter - ne me jugez pas)

- **Yahoo API** pour la météo (faute de mieux - l'api retourne régulièrement un code 200 avec aucun résultat, j'insiste jusqu'à ce que ça passe)

- **Google Maps API** pour l'info trafic


## Matos
- 1 Raspberry

- 1 enceinte avec alimentation externe ([Ryght R480552](https://www.picwic.com/produit/r480552-enceinte-filaire-y-storm-noir-1723743) à 5€)

- 1 détecteur infrarouge ([Panasonic AMN31111](http://fr.farnell.com/panasonic-ew/amn31111/capteur-motion-5m-100-82-noir/dp/1373710) à 12€)


## Installation
```
# clone repo
git clone git@github.com:ericdesa/transistor.git

# install pico2wave pour la synthèse vocale
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install libttspico-utils

# run en tache de fond
python transistor/main.py &
```

## Sources
- http://www.framboise314.fr/raspberry-pi-et-detecteur-de-presence-infra-rouge/
- http://www.framboise314.fr/donnez-la-parole-a-votre-raspberry-pi