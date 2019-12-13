import nltk
from nltk.tag import StanfordNERTagger
from nltk.internals import find_jars_within_path
from nltk.tokenize import word_tokenize


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


def main():
    input = 'Florence May Harding studied at a school in Sydney, and with Douglas Robert Dundas, but in effect had no formal training in either botany or art.'
    st = initialize_stanford_ner_tagger()
    tokenized_input = tokenize_input(input)
    print('Tokenized', tokenized_input)
    classified_input = list(st.tag(tokenized_input))
    print('Classified input:', classified_input)
    print(type(classified_input[0]))
    filtered_classified_input = list(filter(lambda tup: tup[1] == 'LOCATION' or tup[1] == 'PERSON' or tup[1] == 'LOCATION', classified_input))
    print('Filtered input:', filtered_classified_input)


if __name__ == '__main__':
    main()
# tagged = st.tag('Rami Eid is studying at Stony Brook University in NY'.split())
# print(tagged)
