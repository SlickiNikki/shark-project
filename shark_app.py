sharks = {
    "great white": "Great White Shark, often seen hunting alone, and referred to as the 'King of the Ocean' in pop culture.",
    "whale": "By a significant margin, the largest fish in the sea, known for its gentle nature and filter-feeding habits.",
    "hammerhead": "Easily recognizable by its unique head shape, which provides enhanced sensory capabilities.",
    "tiger": "Known for the dark vertical stripes on its body that resemble a tiger's patterns, the tiger shark is another large predator and is often grouped with the great white and bull shark as 'The Big Three' in discussions of shark attacks."
}

print("Welcome to the SharkNet App!")
print("Type the name of the shark you would like to find information on, or type quit to exit.")

while True:
    shark_name = input("Enter a shark name: ").lower().strip()

    if shark_name == "quit":
        print("Exiting SharkNet. Goodbye!")
        break

    partial_match = []

    for match in sharks:
        if shark_name.lower() in match.lower():
            partial_match.append(match)
        
    if not partial_match:
        print ("Sorry, this shark is not in our database yet.")
    else:
        user_input = input("Would you like to get more information about this shark? (Yes/No): ").lower().strip()
        if user_input == "yes":
            print(f"\n{sharks[partial_match[0]]}\n")
