import spacy
nlp = spacy.load("pt_core_news_sm")

def word_frequency(text):
    text = nlp(text)
    token_list = [token.text for token in text if not token.is_punct]
    unique_list = {}


    for item in token_list:
        if item not in unique_list:
            unique_list.update({item: 1})
        else:
            unique_list[item] += 1

    return unique_list

if __name__ == "__main__":
    text = input("Your text: ")
    print(word_frequency(text))
