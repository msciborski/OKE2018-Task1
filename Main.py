import nltk
import rdflib
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import argparse
import json
import unidecode


nltk.download('stopwords')

graph = rdflib.Graph()




def get_argparse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input text')
    parser.add_argument('--output')
    return vars(parser.parse_args())


def tokenize_input(input):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(input)


def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return list(filter(lambda x: x not in stop_words, tokens))


def get_series(tokens):
    serie = ''
    series = []
    for token in tokens:
        if token[0].isupper():
            if serie == '':
                serie = serie + token
            else:
                serie = serie + '_' + token
        else:
            if serie != '':
                series += [serie]
            series += [token]
            serie = ''

    if serie != '':
        series.append(serie)

    return series


def check_dbpedia(classified_input):
    results = []
    person = rdflib.URIRef('http://dbpedia.org/ontology/Person')
    place = rdflib.URIRef('http://dbpedia.org/ontology/Place')
    organisation = rdflib.URIRef('http://dbpedia.org/ontology/Organisation')

    for word in classified_input:
        resource = rdflib.URIRef(f"http://dbpedia.org/resource/{word}")
        graph.value(resource, rdflib.RDFS.label)
        graph.load(resource)
        word_results = []
        for subject, predicate, object_ in graph:
            if subject == resource and object_ in [person, place, organisation]:
                word_results.append((subject, predicate, object_))
        results.append((word, word_results))

    return results


def save_to_file_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def main():
    args = get_argparse_arguments()
    input = unidecode.unidecode(args["input"])
    output_path = args["output"]

    tokenized_input = tokenize_input(input)
    series = get_series(tokenized_input)
    dbpedia_results = check_dbpedia(series)

    if output_path != '':
        save_to_file_json(dbpedia_results, output_path)


if __name__ == '__main__':
    main()
