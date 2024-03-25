from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


def criar_bot():
    """Cria uma instância do chatbot Rose.

    Returns:
        ChatBot: Instância do chatbot Rose configurado.
    """
    bot = ChatBot(
        'Rose',
        logic_adapters=['chatterbot.logic.BestMatch'],
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3?check_same_thread=False',
        preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html']
        )
    return bot


def treinar_bot(bot):
    """Treina o chatbot com corpus em português e dados personalizados.

    Args:
        bot (ChatBot): Instância do chatbot Rose.
    """
    # Treinamento do corpus em português
    conversa_corpus = ChatterBotCorpusTrainer(bot)
    conversa_corpus.train('chatterbot.corpus.portuguese')
    conversa = []
    # Treinamento personalizado com mensagens de vendas de curso
    conversa_lista = ListTrainer(bot)
    conversa_lista.train(conversa)


def executar_chat(bot):
    """Executa um loop de interações com o usuário.

    Args:
        bot (ChatBot): Instância do chatbot Rose.
    """
    print("Bem-vindo à assistente PetShop! Como posso ajudar?")
    while True:
        try:
            resposta = bot.get_response(input("Cliente: "))
            if resposta.confidence > 0.2:
                print("PetShop:", resposta)
            else:
                print("Desculpe, não entendi. Pode reformular a pergunta?")
        except (KeyboardInterrupt, EOFError, SystemExit):
            print("Até logo!")
            break

if __name__ == "__main__":
    bot = criar_bot()
    treinar_bot(bot)
    executar_chat(bot)