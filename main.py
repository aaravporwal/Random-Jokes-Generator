import random


print("Hey, Welcome to Random Jokes Generator!")
print()
print("Here is a joke to Enlighten your Mood:")
print()
jokes = (
  "Why don't scientists trust atoms? Because they make up everything.",
  "How do you organize a space party? You planet.",
  "Why do elephants never use computers? They're afraid of the mouse.",
  "Why did the scarecrow win an award? Because he was outstanding in his field!",
  "What do you call an alligator in a vest? An investigator",
)
print(random.choice(jokes))
print()
print("Hope you are happy now :)")
print("Press Run to get another joke.")
