from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Chat Bot')

conversa = ['Oi', 'Olá', 
            'Tudo bem?', 'Tudo ótimo', 
            'Você gosta de programar?', 'Sim, eu programo em Python',
            'Quantos anos você tem?', '21',
            'Onde você mora?', 'Sorocaba']

trainer = ListTrainer(bot) 
trainer.train(conversa)

while True:
    pergunta = input("Você: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Bot: ', resposta)
    else:
        print('Bot: Ainda não sei responder esta pergunta')