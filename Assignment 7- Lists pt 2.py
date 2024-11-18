def calculate_death_confirmed(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    header = lines[0].strip().split(',')
    state_index = header.index('state')
    death_confirmed_index = header.index('deathConfirmed')

    death_confirmed_totals = {}

    for line in lines[1:]:
        columns = line.strip().split(',')
        state = columns[state_index]
        death_confirmed = columns[death_confirmed_index]

        if death_confirmed:
            death_confirmed = int(death_confirmed)
            if state in death_confirmed_totals:
                death_confirmed_totals[state] += death_confirmed
            else:
                death_confirmed_totals[state] = death_confirmed

    with open(output_file, 'w') as file:
        file.write('state,deathConfirmed\n')
        for state, total in death_confirmed_totals.items():
            file.write(f'{state},{total}\n')

# Example usage
file_path = "/Users/tawfiqabulail/Downloads/Information Infrastructure I /covid_data_set.csv"
calculate_death_confirmed(file_path, 'death_confirmed_totals.csv')