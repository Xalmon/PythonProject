def find_geopolitical_zone():
    geopolitical_zones = {
        "NORTH_WEST": "JIGAWA, KADUNA, KANO, KASTINA, KEBBI, SOKOTA, ZAMFARA",
        "NORTH_EAST": "ADAMAWA, BAUCHI, BORNO, GOMBE, TARABA, YOBE",
        "NORTH_CENTRAL": "BENUE, KOGI, KWARA, NASARAWA, NIGER, PLATEAU",
        "SOUTH_SOUTH": "AKWAIBOM, BAYELSA, CROSS RIVER, DELTA, EDO, RIVERS",
        "SOUTH_EAST": "ABIA, ANAMBRA, EBONYI, ENUGU, IMO",
        "SOUTH_WEST": "EKITI, LAGOS, OGUN, ONDO, OSUN, OYO"
    }

    input_state = input("Enter a state: ").strip().upper()

    found_zone = None

    for zone, states in geopolitical_zones.items():
        if input_state in states:
            found_zone = zone
            break

    if found_zone:
        print("Geopolitical Zone:", found_zone)
        print("States:", geopolitical_zones[found_zone])
    else:
        print("State not found in any geopolitical zone.")


