import json
import random

# Define templates for news generation
templates = [
    {
        "title": "{} Legislature Passes Law Requiring Dogs to Wear Sunglasses on Sunny Days",
        "content": "In a groundbreaking move for pet safety, lawmakers in {} have passed a law mandating that all dogs wear UV-rated sunglasses during sunny weather."
    },
    {
        "title": "{} City Introduces Traffic Lanes for Pedestrians Texting While Walking",
        "content": "To improve sidewalk traffic flow, {} has introduced dedicated lanes for pedestrians who are texting, to prevent collisions and keep foot traffic moving smoothly."
    },
    {
        "title": "{} Town Elects Its First Ever Cat as Mayor, Promises a 'Purrfect' Future",
        "content": "The small town of Meowville, {}, has made history by electing a cat as its mayor, with campaign promises to improve local bird watching and fish markets."
    },
    {
        "title": "{} Man Uses Drone to Walk Dog, Never Leaves His Couch Again",
        "content": "A man in {} has developed a new way to walk his dog using a drone, creating a buzz about pet care innovation."
    },
    {
        "title": "{} to Implement Slot Machines at Airport Security Lines to Kill Time",
        "content": "In a novel approach to making airport security more enjoyable, {} airport will introduce slot machines in security lines."
    },
    {
        "title": "Scientists Discover Water on Mars; Turns Out It's Just a Leaky Faucet from {}",
        "content": "NASA scientists were excited to discover water on Mars, only to find out later it was caused by a faulty faucet installed by a previous rover from {}."
    },
    {
        "title": "{} Bans All Forms of Paper to Prevent Paper Cuts",
        "content": "In a health and safety move, officials in {} have declared a ban on all paper products to prevent paper cuts, shifting entirely to digital communication."
    },
    {
        "title": "Farmers in {} Claim Corn Crop Circles Were Just Bored Teens Not Aliens",
        "content": "Farmers in {} debunk myths about alien crop circles, blaming local teens looking for entertainment."
    },
    {
        "title": "{} Offers Free Heating Bills for Residents Who Can Ice Fish with Their Bare Hands",
        "content": "Alaska introduces a new policy offering to pay the heating bills of any resident who can catch a fish in icy waters using only their hands."
    },
    {
        "title": "Hollywood Announces All Future Movies Will Be Directed by AI, Actors in {} Not So Sure",
        "content": "The film industry is set to embrace AI as directors for all upcoming movies, sparking debates among actors over the future of filmmaking in {}."
    }
]

states = ["California", "New York", "Texas", "Florida", "Nevada", "Iowa", "Alaska", "Washington D.C."]

# Generate a list of 1000 fake news items
news_list = []
for _ in range(1000):
    template = random.choice(templates)
    state = random.choice(states)
    news_list.append({
        "title": template["title"].format(state),
        "fake": True,
        "content": template["content"].format(state)
    })

# Save the news items to a JSON file
with open('newsData.json', 'w') as f:
    json.dump({"news": news_list}, f, indent=4)
