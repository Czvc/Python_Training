# Python Functions
print("This is for defining and calling a function:")

def greet_player(name):
    # Simple function that prints a message.
    print(f"Welcome to the court, {name}!")

greet_player("LeBron James")
greet_player("Stephen Curry")

# Python Arguments
print("\nThis is for positional arguments:")

def player_info(name, team):
    # Arguments let you pass data into a function.
    print(f"{name} plays for {team}.")

player_info("Kevin Durant", "Thunder")
player_info("Kawhi Leonard", "Spurs")

print("\nThis is for keyword arguments:")

def jersey_info(name, number):
    print(f"{name} wears jersey #{number}.")

jersey_info(name="Chris Paul", number=3)
jersey_info(number=13, name="James Harden")

print("\nThis is for default parameter values:")

def points_per_game(name, ppg=10):
    # If ppg is not given, default is used.
    print(f"{name} averages {ppg} points per game.")

points_per_game("Draymond Green")
points_per_game("Kobe Bryant", 27)

print("\nThis is for returning values:")

def total_points(points_per_game, games):
    return points_per_game * games

print(total_points(30, 82))  # some superstar season


# Python *args / **kwargs
print("\nThis is for *args (arbitrary positional arguments):")

def list_scorers(*players):
    # *players becomes a tuple of all arguments.
    print("Top scorers this game:")
    for p in players:
        print("-", p)

list_scorers("LeBron", "Curry", "Durant")

print("\nThis is for **kwargs (arbitrary keyword arguments):")

def player_stats(**stats):
    # **stats becomes a dictionary of key:value pairs.
    for key, value in stats.items():
        print(key, "=", value)

player_stats(name="Russell Westbrook", triple_doubles=34, season="2016-2017")


# Python Scope
print("\nThis is for local and global scope:")

league = "NBA"  # global variable

def show_scope():
    team = "Heat"   # local variable
    print("Inside function:", league, team)

show_scope()
print("Outside function:", league)

print("\nThis is for modifying a global variable inside a function:")

score = 0

def add_points():
    global score
    score += 3  # like hitting a three-pointer

add_points()
print("Score after function:", score)


# Python Decorators
print("\nThis is for a simple decorator:")

def cheer_decorator(func):
    # Decorator adds extra behavior before or after a function.
    def wrapper(name):
        print("Crowd: *cheers loudly*")
        func(name)
        print("Crowd: MVP! MVP!")
    return wrapper

@cheer_decorator
def announce_player(name):
    print(f"Now entering the game: {name}")

announce_player("Giannis Antetokounmpo")


# Python Lambda
print("\nThis is for lambda (small anonymous function):")

# A lambda to compute efficiency rating in a silly way.
efficiency = lambda points, assists: points * 2 + assists
print(efficiency(30, 8))

# Using lambda with sort() to sort players by points.
players = [
    ("LeBron", 27),
    ("Curry", 24),
    ("Harden", 25),
]
players.sort(key=lambda p: p[1], reverse=True)
print(players)


# Python Recursion
print("\nThis is for recursion (function calling itself):")

def countdown_games(n):
    # Simulate counting down playoff games remaining.
    if n == 0:
        print("Season over, time for free agency.")
    else:
        print(f"{n} games left.")
        countdown_games(n - 1)

countdown_games(3)


# Python Generators
print("\nThis is for generators (yield values one by one):")

def season_points(points_list):
    # Generator that yields points each game.
    for pts in points_list:
        yield pts

games_points = season_points([25, 30, 18, 40])

for pts in games_points:
    print("Game points:", pts)
