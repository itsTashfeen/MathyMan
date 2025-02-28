import json
import random
import streamlit as st

# Load the problem data from the JSON file.  Assume the file is in the same directory.
try:
    with open('differentiation_problems.json', 'r') as f:
        differentiation_problems = json.load(f)
except FileNotFoundError:
    st.error("Error: differentiation_problems.json not found. Make sure it's in the same directory as the script.")
    st.stop()

# Function to generate a variation of a problem
def generate_variation(problem, seed=None):
    """Generates a variation of a differentiation problem by replacing variables.
       This is a simplified example and can be expanded to handle more cases.
    """
    if seed is not None:
        random.seed(seed)  # for reproducibility
    problem_str = problem["problem"]
    solution_str = problem["solution"]
    problem_latex_str = problem["problem_latex"]
    solution_latex_str = problem["solution_latex"]


    # Simple variable replacement (x with a random integer or expression)
    if "x" in problem_str:

        #replace only x with simple intergers for now
        new_x = random.randint(2, 10) # Generate random value
        new_problem_str = problem_str.replace("x", f"{new_x}")
        new_solution_str = solution_str.replace("x", f"{new_x}")

        #latex
        new_problem_latex_str = problem_latex_str.replace("x", f"{new_x}")
        new_solution_latex_str = solution_latex_str.replace("x", f"{new_x}")

        return {
            "problem": new_problem_str,
            "problem_latex": new_problem_latex_str,
            "solution": new_solution_str,
            "solution_latex": new_solution_latex_str
        }

    return problem  # Return original if no suitable variable for replacement

# Streamlit app
st.title("Differentiation Problem Generator")

# User input for difficulty and number of problems
difficulty = st.selectbox("Select Difficulty:", ["ultimate"], index=0) # limiting to ultimate for now
num_problems = st.number_input("Enter Number of Problems to Generate:", min_value=1, max_value=20, value=1)

# Generate and display problems
if st.button("Generate Problems"):
    if difficulty in differentiation_problems:
        problems = differentiation_problems[difficulty]
        if problems: # Check if there are problems for the chosen difficulty

            for i in range(num_problems):
                # Select a random problem from the chosen difficulty
                selected_problem = random.choice(problems)

                # Generate a variation
                varied_problem = generate_variation(selected_problem, seed=i) # using seed for reproducibility

                st.subheader(f"Problem {i+1}:")
                st.latex(varied_problem["problem_latex"]) # Display using LaTeX

                st.subheader("Solution:")
                st.latex(varied_problem["solution_latex"])  # Display using LaTeX
        else:
            st.warning(f"No problems found for difficulty: {difficulty}")
    else:
        st.error("Invalid difficulty level selected.")
