from django.shortcuts import render

def home(request):
    user_message = request.GET.get("message", "").lower()

    responses = {
        "hello": "Hi! How are you?",
        "hi": "Hello! Welcome.",
        "bye": "Goodbye! Have a nice day.",
        "what is your name": "I am a Django Chatbot.",
        "how are you": "I am fine. Thank you!",
        "who created you": "I was created using Python and Django.",

        "apple": "Apple is a healthy fruit.",
        "mango": "Mango is the king of fruits.",
        "banana": "Banana is rich in potassium.",
        "orange": "Orange is rich in Vitamin C.",
        "grapes": "Grapes grow in bunches.",
        "pineapple": "Pineapple is a tropical fruit.",
        "papaya": "Papaya helps digestion.",
        "guava": "Guava is rich in fiber.",
        "watermelon": "Watermelon contains lots of water.",
        "pomegranate": "Pomegranate is rich in antioxidants.",

        "lion": "Lion is the king of the jungle.",
        "tiger": "Tiger is the national animal of India.",
        "elephant": "Elephant is the largest land animal.",
        "dog": "Dog is a loyal animal.",
        "cat": "Cat is a popular pet animal.",
        "horse": "Horse is a fast-running animal.",
        "cow": "Cow gives milk.",
        "goat": "Goat is a domestic animal.",
        "monkey": "Monkey likes climbing trees.",
        "rabbit": "Rabbit loves carrots.",

        "india": "New Delhi is the capital of India.",
        "usa": "Washington D.C. is the capital of USA.",
        "japan": "Tokyo is the capital of Japan.",
        "china": "Beijing is the capital of China.",
        "australia": "Canberra is the capital of Australia.",
        "france": "Paris is the capital of France.",
        "germany": "Berlin is the capital of Germany.",
        "russia": "Moscow is the capital of Russia.",
        "canada": "Ottawa is the capital of Canada.",
        "brazil": "Brasilia is the capital of Brazil.",

        "national animal of india": "Tiger",
        "national bird of india": "Peacock",
        "national flower of india": "Lotus",
        "national fruit of india": "Mango",
        "national tree of india": "Banyan Tree",

        "python": "Python is a popular programming language.",
        "django": "Django is a Python web framework.",
        "html": "HTML is used to create web pages.",
        "css": "CSS is used to style web pages.",
        "javascript": "JavaScript makes web pages interactive.",

        "sun": "The Sun is a star.",
        "moon": "The Moon is Earth's natural satellite.",
        "earth": "Earth is the third planet from the Sun.",
        "mars": "Mars is known as the Red Planet.",
        "jupiter": "Jupiter is the largest planet."
    }

    reply = responses.get(
        user_message,
        "Sorry, I don't understand. Please try another question."
    )

    return render(request, "chat.html", {"reply": reply})

