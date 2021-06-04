data = {
    "start": {
        "text": "You are at a junction in the road, you have two choices, which way do you want to go?",
        "choices" : {
            "left" : "hole",
            "right" : "wonderland"
        }
    },
    "hole": {
        "text": "You fell down a hole and knocked yourself out!",
        "choices" : {
            "next" : "end"
        }
    },
    "wonderland": {
        "text": "You have found the paradise of wonderland, congratulations!",
        "choices" : {
            "next" : "end"
        }
    },
    "end": {
        "text": "Your adventure is over :(",
        "choices" : {
            "Try again" : "start"
        }
    }
}