from app import GoogleGemini

llm=GoogleGemini()

print("Ask me anything:")
user=input()
print(llm.invoke(user))