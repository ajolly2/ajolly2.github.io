import json

# Read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Define your custom emoji mappings
emoji_mapping = {
    '•': '⚾️',  # Replace bullet point with desired emoji
    '◦': '🔸',  # Replace bullet point with desired emoji
    '▪': '🔘',  # Replace bullet point with desired emoji
    '▫': '◽️',  # Replace bullet point with desired emoji
    '■': '⬛️',  # Replace bullet point with desired emoji
    '□': '⬜️'   # Replace bullet point with desired emoji
}

# Replace bullet points with emoji in the JSON data
for item in data:
    if 'text' in item:
        for bullet_point, emoji in emoji_mapping.items():
            item['text'] = item['text'].replace(bullet_point, emoji)

# Write the modified data back to the JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)
