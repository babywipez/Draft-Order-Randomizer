import random

# List that stores all members of the league.
leagueMembers = [
    'Katie',
    'Luke',
    'Jake',
    'Eric',
    'Justin',
    'Josh',
    'Dennis',
    'Avi',
    'Al',
    'Dillon',
    'Chris',
    'Regy'
]

# Empty list that will store the randomized draft order.
randomizedOrder = []

# Store draft position in an integer.
pos = 1

while leagueMembers:
    """Loop that runs while leagueMembers isn't empty."""
    # Find random index of current iteration of leagueMembers.
    randomIndex = random.randint(0, (len(leagueMembers) - 1))
    # Add random league member into randomizedOrder list.
    randomizedOrder.append(leagueMembers[randomIndex])
    # Remove the member from the original list.
    leagueMembers.pop(randomIndex)

# Display the new list.
print("The draft order is set!")
for member in randomizedOrder:
    print(f"{pos}. {member}")
    pos += 1