## Αυτοματοποίηση Προσομοιώσεων `advcomparch-ex3`

Το repository περιλαμβάνει αυτοματοποιημένο τρόπο για στήσιμο του docker container με τα απαραίτητα prerequisites για να μπορούν να τρέξουν τα scripts καθώς και σύνδεση με το τοπικό filesystem για εύκολη διακίνηση αρχείων.
```
docker-compose build
docker-compose up
```
Ο φάκελος `data` είναι mapped στον `/root/data` του container.

Οι υλοποιήσεις των μηχανισμών συγχρονισμού βρίσκονται στο `lock.h` και τα προ-μεταγλωττισμένα εκτελέσιμα στον φάκελο `bin`

Τα αποτελέσματα των προσομοιώσεων είναι στους αντίστοιχους φακέλους.

Για επανάληψη των προσομοιώσεων αρκεί να οριστούν κατάλληλα οι παράμετροι της προσομοιώσης στο εκάστοτε αρχείο `parameters.json` και να εκτελεστούν διαδοχικά τα scripts.

```bash
# Μέσα στο container
python3.6 executor.py   #Τρέχει τις προσομοιώσεις (αποτελέσματα στο results)
python3.6 analyzer.py   #Αναλύει τα αρχεία αποτελεσμάτων, τ΄ρέχει McPAT 
                        #και συσσωρεύει τα στατιστικά στο results.json

#Έξω από το container σε σύστημα με python και matplotlib
mkdir figures
python3 graphing.py     #Φτιάχνει διαγράμματα με βάση το results.json στο figures
```