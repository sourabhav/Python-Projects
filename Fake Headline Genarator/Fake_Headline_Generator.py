import random

subjects= [
    "Yash",
    "Sudeep",
    "Modi",
    "Meloni",
    "Rukmini_vasanth",
    "Bangalore_dogs",
    "America_dogs"
]

actions=[
    "Dance",
    "Celebrates",
    "Shooting",
    "Ruling",
    "Acting",
    "Sleeping",
    "Running",
    "Talking"
]

places_things=[
    "Bangalore",
    "chandapura",
    "mumbai",
    "delhi parliament",
    "Film shooting",
    "Movie Theatre",
    "Temple",
    "America",
    "Melody_chocolate"
]

while True:
    subject= random.choice(subjects)
    action= random.choice(actions)
    place_thing= random.choice(places_things)

    headline=f"BREAKING NEWS!!-- {subject} {action} {place_thing}"
    print(headline)
    print()

    user= input("Do you want to generate another headline like this?? (yes/no): ")
    if user=="no":
        break

print("Thank you for using Fake News Generator!")    
print()