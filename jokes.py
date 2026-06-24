import random

jokes = [
    {
        "joke": "Why don't scientists trust atoms?",
        "punchline": "Because they make up everything."
    },
    {
        "joke": "Why did the scarecrow win an award?",
        "punchline": "Because he was outstanding in his field."
    },
    {
        "joke": "Why don't skeletons fight each other?",
        "punchline": "They don't have the guts."
    },
    {
        "joke": "What do you call fake spaghetti?",
        "punchline": "An impasta."
    },
    {
        "joke": "Why did the bicycle fall over?",
        "punchline": "Because it was two-tired."
    },
    {
        "joke": "What do you call cheese that isn't yours?",
        "punchline": "Nacho cheese."
    },
    {
        "joke": "Why did the math book look sad?",
        "punchline": "Because it had too many problems."
    },
    {
        "joke": "What do you call a bear with no teeth?",
        "punchline": "A gummy bear."
    },
    {
        "joke": "Why can't your nose be 12 inches long?",
        "punchline": "Because then it would be a foot."
    },
    {
        "joke": "Why did the coffee file a police report?",
        "punchline": "It got mugged."
    }
];
comedian = random.choice(jokes);
print(comedian["joke"]);
print(comedian["punchline"]);