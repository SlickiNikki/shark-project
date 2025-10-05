sharks = {
    "great white": {
    "description":"Great White Shark, often seen hunting alone, and referred to as the 'King of the Ocean' in pop culture.",
    "size": "juveniles: ranges from 1.2-2.5 meters or 4-8 feet; adults: range from 3.5-4.5 meters or 11-15 feet with weight ranging from 700-1100 kg or 1500-2400 lbs; certain large individuals can reach 5-6 meters or 16-20 feet, with weight up to 2200 kg or 4900 lbs",
    "habitat": "The white shark occurs worldwide in temperate and subtropical waters, often migrating seasonally to follow its preferred temperature range (approximately 10-26°C or 50-80 °F). They are most common in coastal areas near the surface of the water but can also be found at depths of up to 250 meters.",
    "diet": "One of the main food sources for great white sharks is marine mammals such as seals, sea lions, and occasionally small whales. These animals provide a high amount of fat and energy, making them attractive prey. It's important to note that the diet of great white sharks can vary based on their geographical location, seasonal changes, and availability of prey.",
    "behavior": {
        "hunting":"The most common attack method used by great white sharks involves the shark positioning itself directly below its prey and then swimming vertically into an attack. These sharks collide into their prey and then bite them. Prey often die from blood loss, decapitation or severance of vital appendages such as fins.",
        "social": "Great Whites typically act as lone wolves or outsiders. When an individual joins a group, they usually try to avoid conflict or competition for power.",
        "migration": "Great whites follow regular migration patterns. They feed on seals and elephant seals in breeding areas. When the seals leaves to hunt in the open sea, the great whites also leave. Their migrations aren't neat, like a bird's or a butterfly's. They're messy, with one hugging the coast while another zigzags hundreds of miles out to sea. Many, but not all, seem to seasonally move between warm and cold water. And the paths seem different for males, females, and juveniles."},
    }
}

print("Welcome to Sharkster!")
print("Type the name of the shark you would like to find information on, or type quit to exit.")

while True:
    shark_name = input("Enter a shark name: ").lower().strip()

    if shark_name == "quit":
        print("Exiting Sharkster. Goodbye!")
        break

    if len(user_input) < 3:
        print ("Please enter a more specific name")
    if user_input in ("shark", "fish", "animal", "underwater"):
        print("That's too general, try typing or selecting part of the shark's name instead.")
        continue

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
