while True:
    print("=" * 14, "REGISTER PATIENT", "=" * 14)

    name = str(input("Name: "))
    age = int(input("Age: "))
    temperature = float(input("Body temperature (ºC): "))
    cough_duration = int(input("Duration of cough symptoms (days): "))
    headache_duration = int(input("Duration of headache (days): "))

    print('Have you visited any of these countries? ')

    countries_visited = ['USA', 'Italy', 'Indonesia', 'China', 'Portugal']

    for idx, country in enumerate(countries_visited, start=1):
        print(f"{idx}. {country}")

    response = input("(Enter the country number or 0 if not applicable): ")

    if temperature >= 37.5 or cough_duration >= 14 or headache_duration >= 3 or response != '0':
        print("Status: Quarantine")
    else:
        print("Status: Released")
