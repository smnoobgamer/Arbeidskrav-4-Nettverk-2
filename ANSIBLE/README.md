# Ansible cisco ios scripts for arbeidskrav 4 i Nettverk 2

## Fortutsetninger

1. Ansible er satt opp riktig

2. Enhetene er kobla opp riktig og satt opp med ssh


## Hvordan skriptene brukes

1. Du må kjøre skriptene for ruterne før du kjører skriptene til switchene for at det skal funke

2. Bruk bilde i mappen son referanse på hvilken switch jeg snakker om

3. Pass på at ip adressene i host filen matcher det enhetene er satt opp med

4. Vær under tittel til skriptene er navnet på tasken jeg snakker om i yml filen

## router1.yml

### HSRP port g0/0.10

1. Pass på at porten på parents linja matcher med porten du satt opp på ssh skriptet og at vlan ideen er riktig

2. pass på at ip adressen i linje to på "lines" er riktig defaolt gateway

### noshut g0/1

1. pass på at porten er riktig i parents linja, dette er porten koblet til SW1

### Set up port g0/1.10

1. Pass på at det er samme port som forrige task

2. Pass på at vlan id matcher til det du setter opp på switchene seinere, dette er vlanet til det vanlige nettverket

3. pass på at ipadressen og subnett masken er riktig, skal ikke være defaul gatewayen, dette blir satt opp seinere med hsrp

### Set up port g0/1.11

1. Pass på at det er samme port som forrige task

2. Pass på at vlan iden matcher det du satt opp for MGMT nettet, skal ikke være defaul gatewayen, dette blir satt opp seinere med hsrp

### HSRP port g0/1.10

1. Pass på at porten og vlan id er riktig i parents, skal matche "Set up port g0/1.10"

2. Pass på at ip adressen er riktig, skal være default gatewayen

### HSRP port g0/1.11

1. Pass på at porten og vlan id er riktig i parents, skal matche "Set up port g0/1.11"

2. 2. Pass på at ip adressen er riktig, skal være default gatewayen

### DHCP Exclusions

1. Denne tasken setter opp hvilken ip adresser DHCP serveren ikke får lov til å bruke, den burde ikke få gi ut ip adresser som er allerede brukt eller samme ipaddresser som router2

### DHCP pool

1. pass på at det er samme nettverk som hovednettet

## router2.yml

### HSRP port g0/0/0.10

1. Pass på at porten på parents linja matcher med porten du satt opp på ssh skriptet og at vlan ideen er riktig

2. pass på at ip adressen i linje to på "lines" er riktig defaolt gateway

### noshut g0/0/1

1. pass på at porten er riktig i parents linja, dette er porten koblet til SW1

### Set up port g0/0/1.10

1. Pass på at det er samme port som forrige task

2. Pass på at vlan id matcher til det du setter opp på switchene seinere, dette er vlanet til det vanlige nettverket

3. pass på at ipadressen og subnett masken er riktig, skal ikke være defaul gatewayen, dette blir satt opp seinere med hsrp

### Set up port g0/0/1.11

1. Pass på at det er samme port som forrige task

2. Pass på at vlan iden matcher det du satt opp for MGMT nettet, skal ikke være defaul gatewayen, dette blir satt opp seinere med hsrp

### HSRP port g0/0/1.10

1. Pass på at porten og vlan id er riktig i parents, skal matche "Set up port g0/0/1.10"

2. Pass på at ip adressen er riktig, skal være default gatewayen

### HSRP port g0/0/1.11

1. Pass på at porten og vlan id er riktig i parents, skal matche "Set up port g0/0/1.11"

2. 2. Pass på at ip adressen er riktig, skal være default gatewayen

### DHCP Exclusions

1. Denne tasken setter opp hvilken ip adresser DHCP serveren ikke får lov til å bruke, den burde ikke få gi ut ip adresser som er allerede brukt eller samme ipaddresser som router2

### DHCP pool

1. pass på at det er samme nettverk som hovednettet

## switch1.yml

### Setting up Vlan 10

1. pass på at vlan iden er riktig, dette er for det vanlige nettet

## switch2.yml

### Setting up Vlan 10

1. pass på at vlan iden er riktig, dette er for det vanlige nettet

### Setting up Vlan 20

2. pass på at vlan iden er riktig, dette er vlanet til gruppekameraten din

### access vlan 10

1. Pass på at det er riktig port på parents linja

2. Pass på at det er riktig vlan id, skal være for ditt vanlige nettverk

### access vlan 20

1. Pass på at det er riktig port på parents linja

2. Pass på at det er riktig vlan id, skal være for nettverket til gruppekameraten din

### Etherchannel

1. Pass på at det er riktig porter i parents linja

2. pass på at channel-group nummeret er samme som gruppekameraten din