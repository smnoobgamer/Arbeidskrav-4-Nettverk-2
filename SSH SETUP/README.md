# Python ssh setup script for arbeidskrav 4 i Nettverk 2

## Fortutsetninger

1. Python er installert

2. Pyserial er installert

3. Du er koblet til Ruteren eller Switchen med en konsoll kabel

## Hvordan bruke skriptet (vært steg er inputsa som kommer opp når du kjører skriptet)

1. Første inputtet skriver du "1" om du bruker windows eller "2" om du bruker Linux

2. Skriv inn port nummerer til COM porten (Du kan finne det i device manager)

3. Velg om du skal settet opp en ruter eller switch "1" for ruter og "2" for switch

### Ruter

1. Skriv in hostnavnet du ønsker for enheten

2. Skriv inn brukernavnet for enheten (velg "cisco" om du ikke ønsker å endre noe på host filen i ansible skriptet)

3. Skriv inn passordet for enheten (velg "cisco" om du ikke ønsker å endre noe på host filen i ansible skriptet)

4. Skriv inn navnet på porten du ønsker å sette opp (Velg g0/0 for Ruter 1 og g0/0/0 på Ruter 2 om du ikke vil endre noe i Ansible skriptet), denne burde være porten på MGMT pcens subnett

5. Skriv inn vlan IDen til vlanet til MGMT pcen (velg "10" om du ikke ønsker å endre noe i ansible skriptet)

6. Skriv inn ip adressen og subnettmasken til porten slik "x.x.x.x x.x.x.x" (velg "192.168.0.253 255.255.255.0" på ruter 1 og "192.168.0.254" på ruter 2 om du ikke ønsker å endre på ansible skriptet)

### Switch

1. Skriv in hostnavnet du ønsker for enheten

2. Skriv inn brukernavnet for enheten (velg "cisco" om du ikke ønsker å endre noe på host filen i ansible skriptet)

3. Skriv inn passordet for enheten (velg "cisco" om du ikke ønsker å endre noe på host filen i ansible skriptet)

4. Skriv inn vlan IDen til MGMT vlanet (velg "10" på switchen til MGMT pcen og "11" på switchene til det vanlige nettverket om du ikke ønsker å endre noe i ansible skriptet)

5. Skriv inn vlan navnet til vlanet

6. Skriv inn ip adressen og subnettmasken til porten slik "x.x.x.x x.x.x.x" (Velg "172.16.11.4 255.255.255.0" på mellomlegg switchen og "172.16.11.5 255.255.255.0" på switchen med etherchanneling om du ikke øsnker å endre på ansible skriptet)

7. Skriv inn default gatewayen til switchen (Velg "192.168.0.1" på MGMT switchen og "172.16.11.1" på switchene til det vanlige nettverket om du ikke ønsker å endre noe i ansible skriptet)

8. Skriv inn portnavn formatet til switchen f.eks. g1/0/ (Ikke ta med tallet som tilsvarer den spesefike porten)

9. Om du trenger en access port så skriver du inn "1" om ikke skriver du "2" (Anbefales å velga ja om dette er switchen MGMT pcen er kobla til)

10. Om du valgte Yes i forrge input skriver du inn nummeret til porten du skal ha som access port
