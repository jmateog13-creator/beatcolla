# BeatColla

Crea música per capes, en català, per a cicle superior de Primària i primers cursos d'ESO. Inspirat en la mecànica dels creadors musicals per capes: arrossegues sons a uns personatges i tot encaixa a temps.

**Obre-la aquí:** https://jmateog13-creator.github.io/beatcolla/

## Què hi ha

- **Dos nivells:** Primària (vocabulari senzill, botons amb paraules, menys dades) i ESO (acords, BPM, tonalitat, patrons).
- **5 estils:** hip-hop, reggaeton, techno, trap i rumba catalana. 20 sons per estil, en 5 capes (ritme, baix, harmonia, melodia, efectes).
- **Tutorial interactiu** de 17 passos.
- **Visor «Què toca?»** amb el patró de cada so en semicorxeres.
- **Reptes:** textures (monodia, melodia acompanyada, polifonia…), escolta i reprodueix, i quin estil és.
- **Forma musical:** seccions A, B i C per construir formes A-B-A, A-B-C i A-A-A, amb reproducció encadenada, gravació i repte «Quina forma és?».
- **Mode professor:** vista de projector, dictat de capes, QR per compartir una base amb la classe, ruleta de torns i temporitzador.
- **Entregues:** gravació d'àudio i codi de mescla (per exemple `HH-04C____`).

## Enllaços directes

- `…/beatcolla/#app` obre l'app sense la portada.
- `…/beatcolla/#HH-04C____` obre directament aquesta mescla.
- `…/beatcolla/#HH-04C____-1G_____-_______-ABA` obre una obra amb les seves seccions i la seva forma.

## Desenvolupament

Tot el codi és a `beatcolla.html` (Tone.js per al so, sense servidor). `python3 build.py` genera `index.html`, la pàgina completa que publica GitHub Pages.
