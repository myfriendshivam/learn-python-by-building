# Emoji Enhancer for Messages

# get a dictionary
emoji_map_fun = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "☕️",
    "music": "🎸",
    "food": "🌭"
}

# get user message
message = input("Enter your message: ")
update_words = []

# process each word
for word in message.split():
    cleaned = word.lower().strip(".,!?")
    emoji = emoji_map_fun.get(cleaned, "")
    if emoji:
        update_words.append(f"{word} {emoji}")
    else:
        update_words.append(word)

updated_message = " ".join(update_words)
print("\n Enchanced message: \n")
print(updated_message)
