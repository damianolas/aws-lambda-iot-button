# Info

Il file function.py è il codice di una funzione AWS Lambda in grado di gestire il comportamento di un AWS IoT Button già configurato nell'account AWS.

La funzione gestisce tutti i casi di utilizzo, proponendo degli esempi per ognuno:

- Click "SINGLE" che approva il deploy all'interno di una pipeline di AWS CodePipeline

- Click "DOUBLE" che crea l'immagine di un'istanza EC2

- Click "LONG" che cancella uno stack di AWS CloudFormation

È necessario fornire alla funzione le permission per poter compiere le azioni.
