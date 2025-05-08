print("hello, I am a chatbot , whats your name:?")
name=input()
print("nice to meet you",name)
print("how are you feeling today? (good/bad)")
mood=input().lower()
if mood=='good':
    print("Iam glad to hear that")
elif mood=='bad':
    print("I am so sorry, I hope things get better")
else:
    print("I see, sometimes its difficult to describe ones feeling")
print("it was ice chattong with you, good bye", name)


