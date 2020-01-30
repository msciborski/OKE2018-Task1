# OKE2018-Task1
## Focused Named Entity Identification and Linking
The task comprises the identification of named entities in sentences and the disambiguation of the identified entities to the DBpedia knowledge base.
This task is limited to three DBpedia ontology classes (Person, Place, Organisation) and their associated sub classes.

## Our algorithm:
For our solution we used python with nltk and rdflib library. We are tokenizing sentence, then remove punctunation. Next step is to concantante words into series. Series contains words which starts from capital letter, for example: 
- Michal Sciborski lives in Poznan -> ['Michal_Sciborski', 'lives', 'in', 'Poznan'].
<!-- end of the list -->
After creating series, we are doing request to dbpedia using rdflib library. 

# Team Responsibilities
- Michał Ściborski - nltk, rdflib
- Bartosz Więckowski - algorithm for creating series
- Agata Błachowiak - CLI, nltk

# CLI:
pyton Main.py input "text" --output "path"

## Arguments:
- input - text for parsing and checking in dbpedia
- output - optional parametr. If not provided, result is printed in console. 

# Results:
Our solution worked for first quries, but doesn't work good for next. The biggest problem was to create series for sentences like:
'At University of Technology...', because our algorithm returns ['At_Univeristy', 'of', 'Technology'...]. We learned how to use nltk for parsing sentence. In first approach we used StanfordNER tagger for tagging words, but result was not satisfying.

>Michael Jackson and Donald Trump never met in New York.
 
[["Michael_Jackson", [["http://dbpedia.org/resource/Michael_Jackson", "http://www.w3.org/1999/02/22-rdf-syntax-ns#type", "http://dbpedia.org/ontology/Person"]]], ["and", []], ["Donald_Trump", [["http://dbpedia.org/resource/Donald_Trump", "http://www.w3.org/1999/02/22-rdf-syntax-ns#type", "http://dbpedia.org/ontology/Person"]]], ["never", []], ["met", []], ["in", []]]
 
>La Toya is an older sister of Michael Jackson.
 
 
[["La_Toya", []], ["is", []], ["an", []], ["older", []], ["sister", []], ["of", []], ["Michael_Jackson", [["http://dbpedia.org/resource/Michael_Jackson", "http://www.w3.org/1999/02/22-rdf-syntax-ns#type", "http://dbpedia.org/ontology/Person"]]]]
 
>At Poznan University of Technology a lot of nice people are working, especially Adam Małysz who is teaching ski jumps.
 
[["At_Poznan_University", []], ["of", []], ["Technology", []], ["a", []], ["lot", []], ["of", []], ["nice", []], ["people", []], ["are", []], ["working", []], ["especially", []], ["Adam_Malysz", []], ["who", []], ["is", []], ["teaching", []], ["ski", []], ["jumps", []]]
 
>Elvis married Priscilla in 1967 at the Aladdin Hotel in Las Vegas, Nevada. They had a daughter called Lisa and she was born in Memphis, >Tennessee.
 
[["Elvis", []], ["married", []], ["Priscilla", []], ["in", []], ["1967", []], ["at", []], ["the", []], ["Aladdin_Hotel", []], ["in", []], ["Las_Vegas_Nevada_They", []], ["had", []], ["a", []], ["daughter", []], ["called", []], ["Lisa", []], ["and", []], ["she", []], ["was", []], ["born", []], ["in", []], ["Memphis_Tennessee", []]]
 
>The Googleplex is the corporate headquarters complex of Google and its parent company Alphabet Inc.. It is located at 1600 Amphitheatre >Parkway in Mountain View, California, United States, near San Jose.
 
[["The_Googleplex", []], ["is", []], ["the", []], ["corporate", []], ["headquarters", []], ["complex", []], ["of", []], ["Google", [["http://dbpedia.org/resource/Google", "http://www.w3.org/1999/02/22-rdf-syntax-ns#type", "http://dbpedia.org/ontology/Organisation"]]], ["and", []], ["its", []], ["parent", []], ["company", []], ["Alphabet_Inc_It", []], ["is", []], ["located", []], ["at", []], ["1600", []], ["Amphitheatre_Parkway", []], ["in", []], ["Mountain_View_California_United_States", []], ["near", []], ["San_Jose", []]]
