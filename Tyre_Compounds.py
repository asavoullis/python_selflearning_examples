"""  Tyre Compounds Leetcode Exercise """

"""

For and F1 race, there are multiple tyre compounds available 
These compounds vary in their initial grip level, and the rate at which their performance degrades.

Given the following information:
- The number of laps in the race
- The number of available compounds
- The initial compound name
- The initial lap time for each compound in seconds
- The lap time degradation in seconds/lap
    - If the tyre deg is 0.1s / l lap, and the initial lap time is 90s, the lap 1 will take 90s and lap 2 will take 90.1 seconds

Print the following:
- Optimal lap to stop at the end of minimise race time.
- The name of the tyre compound for the last stint.

You must use exactly 2 compounds of tyre
You must change tyres before the start of the last lap
There is only a single stop ( and therefore 2 stints)

"""




# n_laps = int(input())
# compound_names = input().split()
# starting_compound = input()
# initial_lap_times = [float(x) for x in input().split()]
# degradation = [float(x) for x in input().split()]
# Initialize variables to store the optimal lap and compound
optimal_lap = 0
last_stint_compound = ""


def race_time(n_laps, compound_names, starting_compound, initial_lap_times, degradation):
    min_race_time = float('inf')
    
    # Iterate over each lap as a potential pit stop lap
    for lap in range(1, n_laps):  # Exclude the last lap
        for compound_index, compound in enumerate(compound_names):
            if compound != starting_compound:
                # Calculate time for the first stint with the starting compound
                first_stint_time = calculate_stint_time(
                    initial_lap_times[starting_compound],
                    degradation[starting_compound],
                    lap
                )
                # Calculate time for the second stint with the current compound
                second_stint_time = calculate_stint_time(
                    initial_lap_times[compound],
                    degradation[compound],
                    n_laps - lap
                )
                # Total race time
                total_time = first_stint_time + second_stint_time

                # Check if this is the minimum time found so far
                if total_time < min_race_time:
                    min_race_time = total_time
                    global optimal_lap, last_stint_compound  # Declare these as global as well
                    optimal_lap = lap
                    last_stint_compound = compound

# Function to calculate stint time
def calculate_stint_time(initial_time, degradation, laps):
    return initial_time + degradation * (laps - 1)

# Example data
laps = 50
compounds = ["soft", "medium", "hard"]
initial_compound = "soft"
initial_lap_times = {"soft": 90, "medium": 95, "hard": 100}
lap_time_degradation = {"soft": 0.1, "medium": 0.08, "hard": 0.05}

# Call the function
race_time(laps, compounds, initial_compound, initial_lap_times, lap_time_degradation)
print("Optimal lap to stop at:", optimal_lap)
print("Last stint compound:", last_stint_compound)



def race_time(laps, compounds, initial_compound, initial_lap_times, lap_time_degradation):
    min_race_time = float('inf')
    optimal_stop_lap = 0
    last_stint_compound = ""

    for i in range(len(compounds)):
        for j in range(len(compounds)):
            if i != j:  # Ensure different compounds are used for each stint
                compound1 = compounds[i]
                compound2 = compounds[j]

                # Simulate race for current compound combination
                current_lap = 1
                total_time = 0
                for lap in range(1, laps + 1):
                    if lap == laps:  # Last lap, must stop before starting it
                        break
                    if current_lap % 2 == 1:
                        total_time += initial_lap_times[compound1]
                        current_lap_time = initial_lap_times[compound1] + lap_time_degradation[compound1] * (lap - 1)
                        current_lap += 1
                    else:
                        total_time += initial_lap_times[compound2]
                        current_lap_time = initial_lap_times[compound2] + lap_time_degradation[compound2] * (lap - 1)
                        current_lap += 1

                # Check if current combination yields minimum race time
                if total_time < min_race_time:
                    min_race_time = total_time
                    optimal_stop_lap = lap
                    last_stint_compound = compound2 if current_lap % 2 == 0 else compound1

    return optimal_stop_lap, last_stint_compound


# Example data
laps = 50
compounds = ["soft", "medium", "hard"]
initial_compound = "soft"
initial_lap_times = {"soft": 90, "medium": 95, "hard": 100}
lap_time_degradation = {"soft": 0.1, "medium": 0.08, "hard": 0.05}

# Solve and print results
optimal_stop_lap, last_stint_compound = race_time(laps, compounds, initial_compound, initial_lap_times, lap_time_degradation)
print("\nOptimal lap to stop at:", optimal_stop_lap)
print("Last stint compound:", last_stint_compound)
