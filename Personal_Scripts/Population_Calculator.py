import matplotlib.pyplot as plt

def get_user_input():
    """Prompt the user for necessary variables and return them."""
    print("Welcome to the Population Growth Simulator!")
    print("This program simulates population growth over a specified number of years, considering various factors such as birth rate, survival rate, and life expectancy.")
    print("You will be prompted to enter several parameters to customize the simulation.")

    years = int(input("Enter the number of years to simulate: "))
    total_initial_population = int(input("Enter the total initial population (including children and adults): "))
    initial_adults = int(input("Enter the initial number of adults: "))
    initial_births = int(input("Enter the initial number of births on day 1: "))
    age_of_fertility = int(input("Enter the age of fertility: "))
    age_of_menopause = int(input("Enter the age of menopause: "))
    reproduction_interval = float(input("Enter the reproduction interval in years (e.g., 0.5 for twice a year): "))
    life_expectancy = int(input("Enter the life expectancy in years: "))
    
    develop_intelligence = input("Do you want the species to develop intelligence? (yes/no): ").strip().lower()
    if develop_intelligence == 'yes':
        initial_survival_rate = float(input("Enter the initial birth survival rate (as a decimal): "))
        final_survival_rate = float(input("Enter the final birth survival rate (as a decimal): "))
        initial_reproduction_percentage = float(input("Enter the initial reproduction percentage (as a decimal): "))
        final_reproduction_percentage = float(input("Enter the final reproduction percentage (as a decimal): "))
    else:
        survival_rate = float(input("Enter the birth survival rate (as a decimal): "))
        initial_survival_rate = final_survival_rate = survival_rate
        reproduction_percentage = float(input("Enter the reproduction percentage (as a decimal): "))
        initial_reproduction_percentage = final_reproduction_percentage = reproduction_percentage

    return (years, total_initial_population, initial_adults, initial_births, age_of_fertility, age_of_menopause, reproduction_interval, life_expectancy, initial_survival_rate, final_survival_rate, initial_reproduction_percentage, final_reproduction_percentage)

def initialize_population(total_initial_population, initial_adults, initial_births, age_of_fertility, life_expectancy):
    """Initialize the population with given parameters."""
    age_groups = [0] * (life_expectancy + 1)  # Age groups from 0 to life expectancy
    children = total_initial_population - initial_adults
    age_groups[age_of_fertility] = initial_adults
    age_groups[0] = initial_births
    if children > 0:
        # Distribute children in the age groups before fertility age
        for i in range(1, age_of_fertility):
            if children <= 0:
                break
            age_groups[i] += 1
            children -= 1
    return age_groups

def simulate_population(years, total_initial_population, initial_adults, initial_births, age_of_fertility, age_of_menopause, reproduction_interval, life_expectancy, initial_survival_rate, final_survival_rate, initial_reproduction_percentage, final_reproduction_percentage):
    """Simulate population growth over a specified number of years."""
    age_groups = initialize_population(total_initial_population, initial_adults, initial_births, age_of_fertility, life_expectancy)
    previous_children, previous_adults, previous_total = calculate_population(age_groups, age_of_fertility)
    generation = 0

    generations = []
    population_stats = {'children': [], 'adults': [], 'total': []}
    change_stats = {'more_children': [], 'more_adults': [], 'more_total': []}

    total_intervals = int(years / reproduction_interval)

    if initial_survival_rate != final_survival_rate:
        survival_rate_increment = (final_survival_rate - initial_survival_rate) / total_intervals
    else:
        survival_rate_increment = 0

    if initial_reproduction_percentage != final_reproduction_percentage:
        reproduction_percentage_increment = (final_reproduction_percentage - initial_reproduction_percentage) / total_intervals
    else:
        reproduction_percentage_increment = 0

    for interval in range(1, total_intervals + 1):
        year = interval * reproduction_interval

        # Calculate new births
        generation += 1
        fertile_women = sum(age_groups[age_of_fertility:age_of_menopause + 1])
        men_after_menopause = sum(age_groups[age_of_menopause + 1:]) / 2

        if initial_survival_rate != final_survival_rate:
            survival_rate = initial_survival_rate + (generation - 1) * survival_rate_increment
        else:
            survival_rate = initial_survival_rate

        if initial_reproduction_percentage != final_reproduction_percentage:
            reproduction_percentage = initial_reproduction_percentage + (generation - 1) * reproduction_percentage_increment
        else:
            reproduction_percentage = initial_reproduction_percentage

        reproducing_population = (fertile_women + men_after_menopause) * reproduction_percentage
        new_births = int(reproducing_population * 0.50 * survival_rate)  # 50% of reproducing adults
        age_groups[0] += new_births

        # Calculate and display population details at reproduction interval
        children, adults, total_population = calculate_population(age_groups, age_of_fertility)
        more_children = children - previous_children
        more_adults = adults - previous_adults
        more_total = total_population - previous_total
        
        print(f"Generation {generation}, Year {year:.1f}:")
        display_population(children, adults, total_population)
        print(f"\nChange since last interval:")
        print(f"More Children: {more_children}")
        print(f"More Adults: {more_adults}")
        print(f"More Total Population: {more_total}\n\n")

        # Update previous population counts
        previous_children, previous_adults, previous_total = children, adults, total_population

        # Record stats for plotting
        generations.append(generation)
        population_stats['children'].append(children)
        population_stats['adults'].append(adults)
        population_stats['total'].append(total_population)
        change_stats['more_children'].append(more_children)
        change_stats['more_adults'].append(more_adults)
        change_stats['more_total'].append(more_total)

        # Age the population
        new_age_groups = [0] * (life_expectancy + 1)
        for age in range(life_expectancy, 0, -1):
            new_age_groups[age] = age_groups[age - 1]

        # Update the population with the aged groups
        age_groups = new_age_groups

    # Plot the stats
    plot_stats(generations, population_stats, change_stats)

    return age_groups

def calculate_population(age_groups, age_of_fertility):
    """Calculate the total population, children, and adults."""
    children = sum(age_groups[:age_of_fertility])
    adults = sum(age_groups[age_of_fertility:])
    total_population = children + adults
    return children, adults, total_population

def display_population(children, adults, total_population):
    """Display the population details."""
    print(f"Children: {children}")
    print(f"Adults: {adults}")
    print(f"Total Population: {total_population}")

def plot_stats(generations, population_stats, change_stats):
    """Plot population and change stats over generations."""
    plt.figure(figsize=(14, 7))

    # Population Stats
    plt.subplot(1, 2, 1)
    plt.plot(generations, population_stats['children'], label='Children')
    plt.plot(generations, population_stats['adults'], label='Adults')
    plt.plot(generations, population_stats['total'], label='Total Population')
    plt.xlabel('Generation')
    plt.ylabel('Population')
    plt.title('Population Stats by Generation')
    plt.legend()

    # Change Stats
    plt.subplot(1, 2, 2)
    plt.plot(generations, change_stats['more_children'], label='More Children')
    plt.plot(generations, change_stats['more_adults'], label='More Adults')
    plt.plot(generations, change_stats['more_total'], label='More Total Population')
    plt.xlabel('Generation')
    plt.ylabel('Change in Population')
    plt.title('Change in Population by Generation')
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    # Get user input
    (years, total_initial_population, initial_adults, initial_births, age_of_fertility, age_of_menopause, reproduction_interval, life_expectancy, initial_survival_rate, final_survival_rate, initial_reproduction_percentage, final_reproduction_percentage) = get_user_input()

    # Simulate population growth
    age_groups = simulate_population(years, total_initial_population, initial_adults, initial_births, age_of_fertility, age_of_menopause, reproduction_interval, life_expectancy, initial_survival_rate, final_survival_rate, initial_reproduction_percentage, final_reproduction_percentage)

    # Calculate final population details
    children, adults, total_population = calculate_population(age_groups, age_of_fertility)

    # Display final population details
    print(f"Final Year {years}:")
    display_population(children, adults, total_population)

if __name__ == "__main__":
    main()
