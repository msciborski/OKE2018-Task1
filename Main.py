import nltk
import rdflib
from nltk.tag import StanfordNERTagger
from nltk.internals import find_jars_within_path
from nltk.tokenize import word_tokenize

graph = rdflib.Graph()


def initialize_stanford_ner_tagger():
    st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
    print(st._stanford_jar)
    stanford_dir = st._stanford_jar.rpartition('/')[0]
    stanford_jars = find_jars_within_path(stanford_dir)
    print(":".join(stanford_jars))
    st._stanford_jar = ':'.join(stanford_jars)
    print(st._stanford_jar)

    return st


def tokenize_input(input):
    return word_tokenize(input)


def get_persons_places_organizations(input):
    st = initialize_stanford_ner_tagger()
    tokenized_input = tokenize_input(input)
    classified_input = list(st.tag(tokenized_input))
    return list(filter(lambda tup: tup[1] == 'LOCATION' or tup[1] == 'PERSON' or tup[1] == 'LOCATION', classified_input))


def check_dbpedia(classified_input):
    result = []
    person = rdflib.URIRef('http://dbpedia.org/ontology/Person')
    place = rdflib.URIRef('http://dbpedia.org/ontology/Place')
    organisation = rdflib.URIRef('http://dbpedia.org/ontology/Organisation')

    for word in classified_input:
        resource = rdflib.URIRef(f"http://dbpedia.org/resource/Robert")
        graph.value(resource, rdflib.RDFS.label)
        graph.load(resource)
        for subject, predicate, object_ in graph:
            if subject == resource and object_ in [person, place, organisation]:
                result.append((word, subject, predicate, object_))
    return result


def main():
    input = 'Florence May Harding studied at a school in Sydney, and with Douglas Robert Dundas, but in effect had no formal training in either botany or art.'
    result = get_persons_places_organizations(input)
    dbpedia_result = check_dbpedia(result)
    print(dbpedia_result)
    # st = initialize_stanford_ner_tagger()
    # tokenized_input = tokenize_input(input)
    # print('Tokenized', tokenized_input)
    # classified_input = list(st.tag(tokenized_input))
    # print('Classified input:', classified_input)
    # print(type(classified_input[0]))
    # print('Filtered input:', filtered_classified_input)
    # filtered_classified_input = list(filter(lambda tup: tup[1] == 'LOCATION' or tup[1] == 'PERSON' or tup[1] == 'LOCATION', classified_input))


if __name__ == '__main__':
    main()
