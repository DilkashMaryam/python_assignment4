def main():
    """Calculate and display a user's weight on different planets in the solar system."""
    print("🌌 Welcome to the Interplanetary Weight Calculator! 🌍")

    # Get user input
    earth_weight = float(input("Enter your weight on Earth (in kg): "))
    planet = input("Enter the name of a planet: ")

    # Gravity conversion factors
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    if planet in gravity_factors:
        planet_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"Your weight on {planet} would be {planet_weight} kg.")
    else:
        print("Oops! That planet isn't in our solar system list.")

if __name__ == "__main__":
    main()
