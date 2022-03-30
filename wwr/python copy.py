max_life = 0
max_country = "abc"
min_life = 50
total = 0
num = 0

chosen_volume = input("Which year would you like to learn about? ")
with open ("life-expectancy.csv") as file:
    next(file)
    for line in file:
        line_split = line.split(",")
        country =  line_split[0].strip()
        year = line_split[2].split()
        life = float(line_split[3])
        if life > max_life:
            max_life = life
            max_country = country
            max_year = year
        if life < min_life:
            min_life = life
            min_country = country
            min_year = year
       

    print(f"The Maximun life expectancy was {max_country} with {max_life} in {max_year}")
    print(f"The Minimun expectancy was {min_country} with {min_life} in {min_year}")

