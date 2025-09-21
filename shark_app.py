sharks = {
    "great_white_shark": "Great White Shark, often seen hunting alone, and referred to as the 'King of the Ocean' in pop culture.",
    "whale_shark": "By a significant margin, the largest fish in the sea, known for its gentle nature and filter-feeding habits.",
    "hammerhead_shark": "Easily recognizable by its unique head shape, which provides enhanced sensory capabilities.",
    "tiger_shark": "Known for the dark vertical stripes on its body that resemble a tiger's patterns, the tiger shark is another large predator and is often grouped with the great white and bull shark as 'The Big Three' in discussions of shark attacks."
}

while True:
    shark_name = input("enter a shark name").lower()
    if shark_name == "quit":
        break

    if shark_name in sharks:
        user_input = input("Would you like to get more information about this shark? (yes/no): ").lower()

        if user_input == "yes":
            print (f"{sharks[shark_name]}")
    else:
            print("Sorry, I'm not yet familiar with that shark. :(")            
    
            
