import streamlit as st
import sqlite3
import random
import re
import math
from typing import Tuple, Union

# Database setup (assuming the database is in the same directory as the script)
DATABASE_FILE = 'math_problems.db'

def connect_to_db():
    """Connects to the SQLite database."""
    conn = sqlite3.connect(DATABASE_FILE)
    return conn

def get_topics_from_db():
    """Fetches the unique topics from the database."""
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT topic FROM problems")
    topics = [row[0] for row in cursor.fetchall()]
    conn.close()
    return topics


def fetch_problems(topic: str, difficulty: str, num_questions: int) -> list:
    """Fetches a specified number of problems of a given difficulty and topic from the database."""
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM problems WHERE topic = ? AND difficulty = ? ORDER BY RANDOM() LIMIT ?", (topic, difficulty, num_questions))
    problems = cursor.fetchall()
    conn.close()
    return problems


def generate_random_value(variable_type: str = None) -> Union[int, float]:
    """Generates a random value based on variable type."""
    if variable_type in ("power_rule", "e_rule", "ln_coeff", "power_rule_coeff", "general_coeff_sqrt", "chain_rule_trig_ln", "arccos_sqrt_coeff", "arctan_e_coeff", "ln_coeff_plus_x2", "product_rule_coeff_trig", "ln_sqrt_coeff", "power_rule_trig", "power_rule_chain_exp", "quotient_rule_sqrt_coeff", "power_rule_chain_arctan", "product_rule_ln_coeff", "power_rule_product", "quotient_rule_ln_coeff","quotient_rule_power_denom", "ln_ln_ax", "sin_x_ln_ax","power_e_x","e_ax_sin_x","ln_sin_x_a_cos_x", "ln_x_a_x2", "power_rule_x_xa", "arctan_ln_ax","ln_exp_coeff", "sqrt_ln_x2_coeff", "e_sin_ax2", "ln_arctan_ax2", "product_rule_x_sin_ax", "e_x_cos_ax", "quotient_rule_sin_ax2", "arctan_exp_ax", "ln_ax_sqrt", "ln_x2_ax", "arctan_ln_ax_x", "power_rule_ln_cos", "product_rule_e_sin_ln_ax", "arctan_e_ax_ln_x", "ln_sin_ax3", "ln_sqrt_tan_ax", "e_x_x_ln_ax", "ln_ln_sin_ax", "arcsin_e_ax2", "power_rule_exp_a_ln_x", "ln_x_ax", "quotient_rule_tan_ax2", "sqrt_arctan_ax2", "ln_arctan_ax3", "e_sin_ax2_a", "arctan_e_a_sin_x", "ln_x_xa"):
        return random.randint(1, 5)  # Coefficients and powers
    elif variable_type == "x_sin_ax":
        return random.uniform(0.1, 0.9) # Between 0.1 and 0.9 for better results
    elif variable_type == 'none':
        return None # No variables to substitute
    elif variable_type == "arctan_a_x":
        return random.randint(1, 3)
    elif variable_type == 'arcsin':
        return random.uniform(0.1, 0.9)
    else:
        return random.randint(1, 5) # Default integer


def substitute_variables(problem_latex: str, variable_type: str = None) -> Tuple[str, str]:
    """Substitutes variables in a problem using the variable_type to determine substitution."""
    if variable_type is None:
        return problem_latex, ""

    # Define substitution rules for different variable types
    if variable_type == "power_rule":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "e_rule":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_coeff":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "power_rule_coeff":
        a = generate_random_value(variable_type)
        b = generate_random_value(variable_type)
        c = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a)).replace("b", str(b)).replace("c", str(c))
        return problem_latex, f"a = {a}, b = {b}, c = {c}"
    elif variable_type == "general_coeff_sqrt":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "chain_rule_trig_ln":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "arccos_sqrt_coeff":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "arctan_e_coeff":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_coeff_plus_x2":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "product_rule_coeff_trig":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_sqrt_coeff":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "power_rule_trig":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "power_rule_chain_exp":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "quotient_rule_sqrt_coeff":
         a = generate_random_value(variable_type)
         problem_latex = problem_latex.replace("a", str(a))
         return problem_latex, f"a = {a}"
    elif variable_type == "power_rule_chain_arctan":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "product_rule_ln_coeff":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "power_rule_product":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "quotient_rule_ln_coeff":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "arctan_a_x":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "quotient_rule_power_denom":
         a = generate_random_value(variable_type)
         problem_latex = problem_latex.replace("a", str(a))
         return problem_latex, f"a = {a}"
    elif variable_type == "ln_ln_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "sin_x_ln_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "power_e_x":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "e_ax_sin_x":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_sin_x_a_cos_x":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_x_a_x2":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "power_rule_x_xa":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "arctan_ln_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_exp_coeff":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "sqrt_ln_x2_coeff":
         a = generate_random_value(variable_type)
         problem_latex = problem_latex.replace("a", str(a))
         return problem_latex, f"a = {a}"
    elif variable_type == "e_sin_ax2":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_arctan_ax2":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "product_rule_x_sin_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "e_x_cos_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "quotient_rule_sin_ax2":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "arctan_exp_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_ax_sqrt":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_x2_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "arctan_ln_ax_x":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "power_rule_ln_cos":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "product_rule_e_sin_ln_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "arctan_e_ax_ln_x":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_sin_ax3":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_sqrt_tan_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "e_x_x_ln_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_ln_sin_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "arcsin_e_ax2":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "power_rule_exp_a_ln_x":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_x_ax":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "quotient_rule_tan_ax2":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "sqrt_arctan_ax2":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_arctan_ax3":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "e_sin_ax2_a":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "arctan_e_a_sin_x":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"
    elif variable_type == "ln_x_xa":
        a = generate_random_value(variable_type)
        problem_latex = problem_latex.replace("a", str(a))
        return problem_latex, f"a = {a}"

    return problem_latex, ""


def generate_problem_set(topic: str, difficulty: str, num_questions: int) -> list:
    """Generates a list of problems with substituted variables."""
    problem_set = []
    problems = fetch_problems(topic, difficulty, num_questions)

    for problem in problems:
        # problem[1] is the problem, problem[6] is the variable_type
        if problem[6]:  # if there is a variable type
            substituted_problem, substitutions = substitute_variables(problem[2], problem[6])
            substituted_solution, _ = substitute_variables(problem[3], problem[6])  # Substitute also in solution
        else:
            substituted_problem = problem[2]
            substituted_solution = problem[3]
            substitutions = ""

        problem_set.append({
            "problem_latex": substituted_problem,
            "solution_latex": substituted_solution,
            "substitutions": substitutions
        })

    return problem_set


def main():
    st.set_page_config(page_title="Advanced Math Problem Generator", layout="wide")

    # Custom CSS for layout (optional, but makes it cleaner)
    st.markdown(
        """
        <style>
        .reportview-container {
            padding: 0;
        }
        .main .block-container {
            padding: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


    st.title("Advanced Math Problem Generator") # Changed title to match the image
    st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

    # Problem Generation Section
    with st.container():
        col1, col2, col3 = st.columns(3)  # Create three columns for layout

        with col1:
            topics = get_topics_from_db()
            topic = st.selectbox("Problem Type", topics, index=0) # Use topics from DB
        with col2:
            difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard", "ultimate"], index=0)
        with col3:
            num_questions = st.slider("Number of Problems", 1, 20, 5)  # Slider for number of questions

        if st.button("Generate Problems"):  # Generate button
            problem_set = generate_problem_set(topic, difficulty, num_questions)

            # Display Problems Section
            for i, problem in enumerate(problem_set):
                st.subheader(f"Question {i+1}")
                st.latex(problem["problem_latex"])
                if problem["substitutions"]:
                    st.write(f"Variable Substitutions: {problem['substitutions']}")

                with st.expander("Show Solution"):
                    st.latex(problem["solution_latex"])
                st.write("---")  # Separator


if __name__ == "__main__":
    main()
