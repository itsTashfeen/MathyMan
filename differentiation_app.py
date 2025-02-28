import streamlit as st
import sqlite3
import random
import re
import math
import hashlib
import os
from typing import Tuple, Union
import json

# Database setup
DATABASE_FILE = 'math_problems.db'
USER_DB_FILE = 'user_data.db'

# Authentication functions (same as before)
def init_user_db():
    """Initialize the user database if it doesn't exist"""
    conn = sqlite3.connect(USER_DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL,
        preferences TEXT
    )
    ''')
    conn.commit()
    conn.close()

def hash_password(password, salt=None):
    """Hash a password with a salt for security"""
    if salt is None:
        salt = os.urandom(32).hex()
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return hash_obj.hex(), salt

def create_user(username, password):
    """Create a new user in the database"""
    conn = sqlite3.connect(USER_DB_FILE)
    cursor = conn.cursor()
    
    # Check if username already exists
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return False, "Username already exists"
    
    # Hash password and store user
    password_hash, salt = hash_password(password)
    default_preferences = json.dumps({
        "default_topic": "Basics of Differentiation",
        "default_difficulty": "easy",
        "default_num_questions": 5,
        "dark_mode": False,
        "theme": "light"  # New theme preference
    })
    
    cursor.execute(
        "INSERT INTO users (username, password_hash, salt, preferences) VALUES (?, ?, ?, ?)",
        (username, password_hash, salt, default_preferences)
    )
    conn.commit()
    conn.close()
    return True, "User created successfully"

def verify_user(username, password):
    """Verify user credentials"""
    conn = sqlite3.connect(USER_DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        stored_hash, salt = result
        calculated_hash, _ = hash_password(password, salt)
        if calculated_hash == stored_hash:
            return True
    return False

def get_user_preferences(username):
    """Get user preferences from the database"""
    conn = sqlite3.connect(USER_DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT preferences FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    
    if result and result[0]:
        return json.loads(result[0])
    return None

def save_user_preferences(username, preferences):
    """Save user preferences to the database"""
    conn = sqlite3.connect(USER_DB_FILE)
    cursor = conn.cursor()
    preferences_json = json.dumps(preferences)
    cursor.execute("UPDATE users SET preferences = ? WHERE username = ?", (preferences_json, username))
    conn.commit()
    conn.close()

# Original math problem functions (same as before)
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
    # Include all the other variable type cases here (unchanged from original)
    # ... (keeping original substitution logic)
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

# Helper function to apply a theme (based on your original code's intended functionality)
def apply_theme(theme: str):
    """Applies a Streamlit theme based on the given theme name."""
    if theme == "dark":
        return """
            <style>
            body {
                color: #fff;
                background-color: #222;
            }
            .st-emotion-cache-1y4068c { /* Streamlit default elements, can vary */
                background-color: #333;
                color: #fff;
                border: 1px solid #444;
            }
            .st-emotion-cache-fzvqzx { /* Expanders */
                background-color: #333;
                color: #fff;
                border: 1px solid #444;
            }
            .st-emotion-cache-162wq40 { /* Select boxes */
                background-color: #333;
                color: #fff;
            }
            .st-emotion-cache-10o59y8 { /* Sliders */
                background-color: #333;
                color: #fff;
            }
            .st-emotion-cache-1kyxreq { /* Buttons */
                background-color: #4CAF50; /* Green */
                color: white;
            }
            .st-emotion-cache-162wq40 select {  /*Fix for select boxes */
                 color: black !important;
            }

            </style>
        """
    elif theme == "light":
        return """
            <style>
            body {
                color: #222;
                background-color: #fff;
            }
            .st-emotion-cache-1y4068c {
                background-color: #f8f9fa;
                color: #222;
                border: 1px solid #ccc;
            }
            .st-emotion-cache-fzvqzx {
                background-color: #f8f9fa;
                color: #222;
                border: 1px solid #ccc;
            }
            .st-emotion-cache-162wq40 {
                background-color: #f8f9fa;
                color: #222;
            }
            .st-emotion-cache-10o59y8 {
                background-color: #f8f9fa;
                color: #222;
            }
            .st-emotion-cache-1kyxreq {
                background-color: #4CAF50; /* Green */
                color: white;
            }
             .st-emotion-cache-162wq40 select {  /*Fix for select boxes */
                 color: black !important;
            }
            </style>
        """
    elif theme == "blue":
        return """
            <style>
            body {
                color: #fff;
                background-color: #3498db; /* A nice blue */
            }
            .st-emotion-cache-1y4068c {
                background-color: #2980b9;
                color: #fff;
                border: 1px solid #2980b9;
            }
            .st-emotion-cache-fzvqzx {
                background-color: #2980b9;
                color: #fff;
                border: 1px solid #2980b9;
            }
            .st-emotion-cache-162wq40 {
                background-color: #2980b9;
                color: #fff;
            }
            .st-emotion-cache-10o59y8 {
                background-color: #2980b9;
                color: #fff;
            }
             .st-emotion-cache-1kyxreq {
                background-color: #27ae60; /* Green */
                color: white;
            }
             .st-emotion-cache-162wq40 select {  /*Fix for select boxes */
                 color: black !important;
            }

            </style>
        """

    # More themes can be added here

    else: # Default fallback
        return apply_theme("light")  # Or any other default theme


def main():
    st.set_page_config(page_title="Advanced Math Problem Generator", layout="wide")

    # Initialize user database
    init_user_db()

    # Custom CSS (including the auth-container from before, and the theme application)
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            padding: 0;
        }}
        .main .block-container {{
            padding: 2rem;
        }}
        .auth-container {{
            max-width: 500px;
            margin: 0 auto;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            background-color: #f8f9fa;
        }}
        /*  Apply the theme dynamically, note the usage of the apply_theme method */
        {apply_theme(st.session_state.get('preferences', {}).get('theme', 'light'))}

        </style>
        """,
        unsafe_allow_html=True,
    )


    # Initialize session state for storing login status and user data
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'preferences' not in st.session_state:
        st.session_state.preferences = None
    if 'show_register' not in st.session_state:
        st.session_state.show_register = False


    # App title
    st.title("Advanced Math Problem Generator")
    st.markdown("<hr>", unsafe_allow_html=True)


    # Authentication Section
    if not st.session_state.logged_in:
        # Toggle between login and register
        toggle_col1, toggle_col2 = st.columns([3, 1])
        with toggle_col1:
            st.subheader("User Authentication")
        with toggle_col2:
            if st.button("Switch to Register" if not st.session_state.show_register else "Switch to Login"):
                st.session_state.show_register = not st.session_state.show_register

        # Create the login/register container
        with st.container():
            st.markdown('<div class="auth-container">', unsafe_allow_html=True)

            if not st.session_state.show_register:
                # Login form
                st.subheader("Login")
                login_username = st.text_input("Username", key="login_username")
                login_password = st.text_input("Password", type="password", key="login_password")

                if st.button("Login", key="login_button"):
                    if login_username and login_password:
                        if verify_user(login_username, login_password):
                            st.session_state.logged_in = True
                            st.session_state.username = login_username
                            st.session_state.preferences = get_user_preferences(login_username)
                            st.success("Login successful!")
                            st.rerun()  # Updated from experimental_rerun
                        else:
                            st.error("Invalid username or password")
                    else:
                        st.warning("Please enter both username and password")
            else:
                # Registration form
                st.subheader("Register")
                reg_username = st.text_input("Username", key="reg_username")
                reg_password = st.text_input("Password", type="password", key="reg_password")
                reg_password_confirm = st.text_input("Confirm Password", type="password", key="reg_password_confirm")

                if st.button("Register", key="register_button"):
                    if reg_username and reg_password:
                        if reg_password != reg_password_confirm:
                            st.error("Passwords do not match")
                        elif len(reg_password) < 6:
                            st.error("Password must be at least 6 characters long")
                        else:
                            success, message = create_user(reg_username, reg_password)
                            if success:
                                st.success(message)
                                st.session_state.show_register = False
                                st.rerun()  # Updated from experimental_rerun
                            else:
                                st.error(message)
                    else:
                        st.warning("Please fill out all fields")

            st.markdown('</div>', unsafe_allow_html=True)

    # Main Application (when logged in)
    else:
        # User welcome and logout option
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"Welcome, {st.session_state.username}!")
        with col2:
            if st.button("Logout"):
                # Save current preferences before logging out
                if st.session_state.preferences:
                    save_user_preferences(st.session_state.username, st.session_state.preferences)
                # Reset session state
                st.session_state.logged_in = False
                st.session_state.username = None
                st.session_state.preferences = None
                st.rerun()  # Updated from experimental_rerun

        # Load user preferences
        user_prefs = st.session_state.preferences
        default_topic = user_prefs.get("default_topic") if user_prefs else "Basics of Differentiation"
        default_difficulty = user_prefs.get("default_difficulty") if user_prefs else "easy"
        default_num_questions = user_prefs.get("default_num_questions") if user_prefs else 5
        current_theme = user_prefs.get("theme", "light")  # Load theme

        # Problem Generation Section with tabs
        tabs = st.tabs(["Generate Problems", "User Preferences"])

        # Tab 1: Problem Generation
        with tabs[0]:
            col1, col2, col3 = st.columns(3)

            topics = get_topics_from_db()
            topic_index = topics.index(default_topic) if default_topic in topics else 0

            with col1:
                topic = st.selectbox("Problem Type", topics, index=topic_index)
            with col2:
                difficulty_options = ["easy", "medium", "hard", "ultimate"]
                difficulty_index = difficulty_options.index(default_difficulty) if default_difficulty in difficulty_options else 0
                difficulty = st.selectbox("Difficulty", difficulty_options, index=difficulty_index)
            with col3:
                num_questions = st.slider("Number of Problems", 1, 20, default_num_questions)

            if st.button("Generate Problems"):
                # Save current selections as preferences
                if not st.session_state.preferences:
                    st.session_state.preferences = {}
                st.session_state.preferences["default_topic"] = topic
                st.session_state.preferences["default_difficulty"] = difficulty
                st.session_state.preferences["default_num_questions"] = num_questions
                save_user_preferences(st.session_state.username, st.session_state.preferences)

                # Generate and display problems
                problem_set = generate_problem_set(topic, difficulty, num_questions)

                for i, problem in enumerate(problem_set):
                    st.subheader(f"Question {i+1}")
                    st.latex(problem["problem_latex"])
                    if problem["substitutions"]:
                        st.write(f"Variable Substitutions: {problem['substitutions']}")

                    with st.expander("Show Solution"):
                        st.latex(problem["solution_latex"])
                    st.write("---")

        # Tab 2: User Preferences
        with tabs[1]:
            st.subheader("User Preferences")

            # Load current preferences
            current_prefs = st.session_state.preferences or {}

            # Default topic preference
            topics = get_topics_from_db()
            default_topic = current_prefs.get("default_topic", "Basics of Differentiation")
            topic_index = topics.index(default_topic) if default_topic in topics else 0
            new_default_topic = st.selectbox("Default Problem Type", topics, index=topic_index)

            # Default difficulty preference
            difficulty_options = ["easy", "medium", "hard", "ultimate"]
            default_difficulty = current_prefs.get("default_difficulty", "easy")
            difficulty_index = difficulty_options.index(default_difficulty) if default_difficulty in difficulty_options else 0
            new_default_difficulty = st.selectbox("Default Difficulty", difficulty_options, index=difficulty_index)

            # Default number of questions
            default_num = current_prefs.get("default_num_questions", 5)
            new_default_num = st.slider("Default Number of Problems", 1, 20, default_num)

            # Theme Selection
            theme_options = ["light", "dark", "blue"] # add more themes
            current_theme = current_prefs.get("theme", "light")
            new_theme = st.selectbox("Theme", theme_options, index=theme_options.index(current_theme))

            # Save preferences button
            if st.button("Save Preferences"):
                # Update preferences
                if not st.session_state.preferences:
                    st.session_state.preferences = {}

                st.session_state.preferences["default_topic"] = new_default_topic
                st.session_state.preferences["default_difficulty"] = new_default_difficulty
                st.session_state.preferences["default_num_questions"] = new_default_num
                st.session_state.preferences["theme"] = new_theme # Save the theme

                # Save to database
                save_user_preferences(st.session_state.username, st.session_state.preferences)
                st.success("Preferences saved successfully!")
                #  Force a rerun to update the theme immediately.
                st.rerun() # or st.experimental_rerun()

if __name__ == "__main__":
    main()
