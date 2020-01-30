# OKE2018-Task1
## Focused Named Entity Identification and Linking
The task comprises the identification of named entities in sentences and the disambiguation of the identified entities to the DBpedia knowledge base.
This task is limited to three DBpedia ontology classes (Person, Place, Organisation) and their associated sub classes.

## Our algorithm:
For our solution we used python with nltk and rdflib library. We are tokenizing sentence, then remove punctunation. Next step is to concantante words into series. Series contains words which starts from capital letter, for example: 
- Michal Sciborski lives in Poznan -> ['Michal_Sciborski', 'lives', 'in', 'Poznan']. 
After creating series, we are doing request to dbpedia using rdflib library. 

# Team Responsibilities
- Michał Ściborski - nltk, rdflib
- Bartosz Więckowski - algorithm for creating series
- Agata Błachowiak - CLI, nltk

# CLI
pyton Main.py input "text" --output "path"

## Arguments:
- input - text for parsing and checking in dbpedia
- output - optional parametr. If not provided, result is printed in console. 
