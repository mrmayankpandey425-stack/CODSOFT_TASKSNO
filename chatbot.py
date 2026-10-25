
# CODSOFT AI Internship - Task 1
# Rule-Based Chatbot

print("=" * 40)
print("       CODSOFT CHATBOT")
print("=" * 40)
print("Hello! Main ek simple chatbot hoon.")
print("Tum mujhse baat kar sakte ho.")
print("Band karne ke liye 'bye' type karo.")

while True:
    user_input = input("\nYou: ").strip().lower()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! Kaise ho?")

    elif "your name" in user_input or "naam" in user_input:
        print("Bot: Mera naam CodBot hai.")

    elif "how are you" in user_input or "kaise ho" in user_input:
        print("Bot: Main badhiya hoon! Tum batao.")

    elif "help" in user_input:
        print("Bot: Main greeting, naam aur basic "
              "questions ka jawab de sakta hoon.")

    elif "thank" in user_input:
        print("Bot: You're welcome!")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Bye! Have a nice day.")
        break

    elif user_input == "":
        print("Bot: Kuch type toh karo!")

    else:
        print("Bot: Sorry, mujhe samajh nahi aaya.")
        print("Bot: Hello, help ya naam pooch kar dekho.")
