from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = Ollama(model="mistral")
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

def ask_tutor(query):
    return conversation.run(query)
