- plan.txt - plan rada na projektu  
- link_DB2 - link ka bazi sa signalima koje koristimo u radu  
- priprema - Materijal pripremljen pre početka rada na projektu:  
             - vizualizacija_spektogram.py - kod za vizualizaciju signala spektrogramom  
             - CNN_model.py - kod za probni CNN klasifikator i  njegovo čuvanje u modelu   
             - evaluacija_modela.py - kod za pokretanje sačuvanog modela i njegova evaluacija  
             - spectrogram.py - probni kod za spectrogram  
             - windowing.py - probni kod za windowing  
- rad - Zvaničan rad na projektu:  
        - butterworth_filter.py - kod za implementaciju butterworth filtera  
        - notch_filter.py - kod za implementaciju notch filtera  
        - hampel_filter.py - kod za implementaciju hampel filtera  
        - spektrogram.py - kod za vizualizaciju metodom spektrograma  
        - windowing.py - kod za windowing metodu  
        - CNN_window_non.py - kod za arhitekturu mreže  
        - labele.py - kod za formiranje ulazne matrice labela za mrežu  
        - spajanje_fajlova.py - kod za formiraje ulaznih matrica podataka za mrežu  
        - spectrogrami.py - spajanje spectrograma za svaki kanal posebno u jednu matricu  
        - spektrogram_podela.py - formiranje pojedinačnih slika  
        - split_folders.py - kod za podelu podataka u tri seta - trening, validaciju i set  
- Slike - propratni materijal sačuvan u vidu slika  
---------------------------------------------------------------------------------------------
15.8.  

Prvog dana rada na projeku implementiran je Butterworth i Notch filter.  
Za implementaciju Butterworth bandpass filtera, određenje su granice od 30 do 300Hz.  
U sklopu implementacije Notch filtera na okolinu od 50Hz, implementiran je i bandpass filter na istom opsegu kao i Butterworth.  
Za svaku implementaciju filtera sačuvani su primeri u vidu slika:  
        - prikaz sirovog i procesiranog signala  
        - frekvencijski i fazni odziv  
---------------------------------------------------------------------------------------------
16.8.  
  
Drugog dana rada na projektu implementiran je Hampel filter i prvi način vizualizacije pomoću spektograma.  
Notch i Butterworth kodovi za predprocesiranje su izvršeni na celoj bazi podataka. Rezultati su čuvani u .npy binarnom formatu.  
Za Hampel filter i vizualizaciju spektrogramom sačuvani su primeri u vidu slika:  
        - prikaz sirovog i procesiranog signala za Hampel filter  
        - prikaz vizualizacije za metodu spektrogramom za:  
                1. butterworth filter  
                2. notch filter  
                3. hampel filter  
                4. neobrađeni signal
---------------------------------------------------------------------------------------------
17.8.  
  
Trećeg dana rada na projektu Hampel kod za predprocesiranje je izvršen na celoj bazi podataka. Rezultati su čuvani u .npy binarnom formatu.  
Napisan je kod za metodu vizualizacije - windowing i implementiran na prvom delu prvog pokreta.  
Kod je zatim prepravljen da formira po 16 slika za svako ponavljanje vežbe. Pošto svaka osoba izvršava 17 različitih pokreta,  
sa ponavljanjem svakog po 6 puta; ukupno se formira 16 * 6 * 17 = 1632 slike po osobi. Sve slike su dimenzija 252x200.  
Za windowing sačuvani su primeri u vidu slika:  
        - prikaz vizualizacije prvog dela prvog pokreta osobe 1  
        - prikaz vizualizacije drugog dela prvog pokreta osobe 1  
        - prikaz vizualizacije trećeg dela prvog pokreta osobe 1  
---------------------------------------------------------------------------------------------
18.8.

Četvrtog dana rada na projektu završen je kod za implementaciju windowinga. Zbog problema sa memorijom, ponovo su pokrenuti kodovi za Hampel,  
Butterworth i Notch filter i nakon toga su ti signali kao i oni nepretprocesirani vizualizovani procesom windowinga.  
Slike nastale prvim načinom vizualizacije su u .npy binarnom formatu.
Započeta je implementacija vizualizacije spektrogramom.  
---------------------------------------------------------------------------------------------
19.8.  
  
Četrtog dana rada na projektu završen je kod za vizualizaciju spektrogramom. Pokrenut je na većini signala.   
Započet je rad na arhitekturi mreže, sa odgovarajućim slojevima za windowing slike. Napravljen je fajl sa labelama za svaku sliku.  
---------------------------------------------------------------------------------------------
20.8.  
  
Petog dana rada na projektu ponovo su pokretani kodovi na svim podacima, zbog greške pri čuvanju i završena je prva verzija koda arhitekture  
konvolucione neuronske mreže.   
---------------------------------------------------------------------------------------------
21.8.  

Šestog dana rada na projektu izvršena je podela fajlova u podfoldere i  njihova grupacija u trening set, set za validaciju i test set.  
Formirane su matrice koje predstavljaju ulazne podatke za mrežu, kao i potrebne labele koje odgovaraju svakom setu podataka posebno.  
---------------------------------------------------------------------------------------------
22.8.  

Sedmog dana rada na projektu pokučano je pokretanje mreže, i debagovani su nastali problemi. Neki od njih su: veličine fajlova za podatke  
vizualizovane windowing metodom, dimenzije fajlova za podatke vizualizovane spectrogram metodom,...
---------------------------------------------------------------------------------------------
23.8.  

Osmog dana napravljana je pauza u radu, ali je i pored toga debagovana mreža, podešavane su dimenzije kernela, prepravljane su dimenzije ulaznih  
podataka, itd.  
---------------------------------------------------------------------------------------------
24.8.

Devetog dana rada na projektu odučile smo da početna testiranja i pokretanja mreže vršimo na manjem setu podataka. Odlučile smo da koristimo google cloud  
treniranje mreže, implementiran je kod za serijalizaciju podataka preko pickla. Debagovan je kod.  
