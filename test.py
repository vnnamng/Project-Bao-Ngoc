from transformers import pipeline, Conversation

chatbot = pipeline("conversational", model="vilm/vinallama-2.7b-chat")
# Conversation objects initialized with a string will treat it as a user message
conversation = Conversation("Tại sao chúng ta cần yêu thương nhau?")
conversation = chatbot(conversation)
conversation.messages[-1]["content"]
print(conversation.messages[-2]["content"])
print(conversation.messages[-1]["content"])

conversation.add_message({"role": "user", "content": "Thế sao?"})
conversation = chatbot(conversation)
conversation.messages[-1]["content"]
print(conversation.messages[-2]["content"])
print(conversation.messages[-1]["content"])