import spacy
nlp = spacy.load("pt_core_news_sm")


text = input("Your text: ")
text = nlp(text)

token_list = [token.text for token in text if not token.is_punct]
unique_list = {}


for item in token_list:
    if item not in unique_list:
        unique_list.update({item: 1})
    else:
        unique_list[item] += 1

print(unique_list)