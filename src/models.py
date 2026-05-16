Module containing the core object models for tracking workout volume.

import math

class Exercise:
    Represents a single exercise performed in a workout session.

    def __init__(self, name: str, sets: int, reps: int, weight: float):
        Initializes an Exercise instance.

        Args:
            name (str): The name of the exercise (e.g., 'Bench Press').
            sets (int): Total number of sets completed.
            reps (int): Repetitions completed per set.
            weight (float): Weight lifted in kilograms or pounds.
        
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight

    property
    def total_volume(self) -> float:
        Calculates the total volume for the exercise.

        Returns:
            float: Total volume calculated as sets * reps * weight.
      
        return float(self.sets * self.reps * self.weight)

    def estimate_1rm(self) -> float:
        Estimates the 1-Repetition Maximum (1RM) using the Epley formula.

        Returns:
            float: Estimated 1RM value.
        
        if self.reps == 1:
            return self.weight
        return self.weight * (1 + self.reps / 30)


class WorkoutSession:
    Manages a collection of exercises performed during a single gym visit.

    def __init__(self, date_str: str):
       Initializes a WorkoutSession instance.

        Args:
            date_str (str): The date of the session (YYYY-MM-DD).
 
        self.date_str = date_str
        self.exercises = []

    def add_exercise(self, exercise: Exercise) -> None:
        Appends a completed exercise to the workout session.
        self.exercises.append(exercise)

    def get_session_volume(self) -> float:
        Calculates the combined volume of all exercises using a comprehension.

        Returns:
            float: Combined session volume.
      
      
        return sum([ex.total_volume for ex in self.exercises])
