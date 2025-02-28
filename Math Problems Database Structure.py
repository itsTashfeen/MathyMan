import json
import sqlite3

# Create a dictionary structure for all problems
differentiation_problems = {
    "easy": [
        {
            "id": 1,
            "problem": "f(x) = x^a",
            "problem_latex": r"f(x) = x^a",
            "solution": "f'(x) = a*x^(a-1)",
            "solution_latex": r"f'(x) = a*x^(a-1)",
            "topic": "differentiation",
            "difficulty": "easy",
            "variable_type": "power_rule"
        },
        {
            "id": 2,
            "problem": "f(x) = cos(x)",
            "problem_latex": r"f(x) = \cos(x)",
            "solution": "f'(x) = -sin(x)",
            "solution_latex": r"f'(x) = -\sin(x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 3,
            "problem": "f(x) = e^{ax}",
            "problem_latex": r"f(x) = e^{ax}",
            "solution": "f'(x) = a*e^{ax}",
            "solution_latex": r"f'(x) = a*e^{ax}",
            "topic": "differentiation",
            "difficulty": "easy",
            "variable_type": "e_rule"
        },
        {
            "id": 4,
            "problem": "f(x) = ln(ax)",
            "problem_latex": r"f(x) = \ln(ax)",
            "solution": "f'(x) = 1/x",
            "solution_latex": r"f'(x) = \frac{1}{x}",
            "topic": "differentiation",
            "difficulty": "easy",
            "variable_type": "ln_coeff"
        },
        {
            "id": 5,
            "problem": "f(x) = ax^3 - bx + c",
            "problem_latex": r"f(x) = ax^3 - bx + c",
            "solution": "f'(x) = 3ax^2 - b",
            "solution_latex": r"f'(x) = 3ax^2 - b",
            "topic": "differentiation",
            "difficulty": "easy",
            "variable_type": "power_rule_coeff"
        },
        {
            "id": 6,
            "problem": "f(x) = tan(x)",
            "problem_latex": r"f(x) = \tan(x)",
            "solution": "f'(x) = sec^2(x)",
            "solution_latex": r"f'(x) = \sec^2(x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 7,
            "problem": "f(x) = arctan(x)",
            "problem_latex": r"f(x) = \arctan(x)",
            "solution": "f'(x) = 1/(1 + x^2)",
            "solution_latex": r"f'(x) = \frac{1}{1 + x^2}",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 8,
            "problem": "f(x) = sqrt(x)",
            "problem_latex": r"f(x) = \sqrt{x}",
            "solution": "f'(x) = 1/(2sqrt(x))",
            "solution_latex": r"f'(x) = \frac{1}{2\sqrt{x}}",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 9,
            "problem": "f(x) = 1/x",
            "problem_latex": r"f(x) = \frac{1}{x}",
            "solution": "f'(x) = -1/x^2",
            "solution_latex": r"f'(x) = -\frac{1}{x^2}",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 10,
            "problem": "f(x) = sin^2(x)",
            "problem_latex": r"f(x) = \sin^2(x)",
            "solution": "f'(x) = 2sin(x)cos(x) = sin(2x)",
            "solution_latex": r"f'(x) = 2\sin(x)\cos(x) = \sin(2x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 11,
            "problem": "f(x) = cos^2(x)",
            "problem_latex": r"f(x) = \cos^2(x)",
            "solution": "f'(x) = -2cos(x)sin(x) = -sin(2x)",
            "solution_latex": r"f'(x) = -2\cos(x)\sin(x) = -\sin(2x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 12,
            "problem": "f(x) = arcsin(x)",
            "problem_latex": r"f(x) = \arcsin(x)",
            "solution": "f'(x) = 1/sqrt(1 - x^2)",
            "solution_latex": r"f'(x) = \frac{1}{\sqrt{1 - x^2}}",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 13,
            "problem": "f(x) = arccos(x)",
            "problem_latex": r"f(x) = \arccos(x)",
            "solution": "f'(x) = -1/sqrt(1 - x^2)",
            "solution_latex": r"f'(x) = -\frac{1}{\sqrt{1 - x^2}}",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 14,
            "problem": "f(x) = arctan(ax)",
            "problem_latex": r"f(x) = \arctan(ax)",
            "solution": "f'(x) = a/(1 + (ax)^2)",
            "solution_latex": r"f'(x) = \frac{a}{1 + (ax)^2}",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 15,
            "problem": "f(x) = ln|x|",
            "problem_latex": r"f(x) = \ln|x|",
            "solution": "f'(x) = 1/x",
            "solution_latex": r"f'(x) = \frac{1}{x}",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 16,
            "problem": "f(x) = e^{-ax}",
            "problem_latex": r"f(x) = e^{-ax}",
            "solution": "f'(x) = -a*e^{-ax}",
            "solution_latex": r"f'(x) = -a*e^{-ax}",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 17,
            "problem": "f(x) = sec(x)",
            "problem_latex": r"f(x) = \sec(x)",
            "solution": "f'(x) = sec(x)tan(x)",
            "solution_latex": r"f'(x) = \sec(x)\tan(x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 18,
            "problem": "f(x) = csc(x)",
            "problem_latex": r"f(x) = \csc(x)",
            "solution": "f'(x) = -csc(x)cot(x)",
            "solution_latex": r"f'(x) = -\csc(x)\cot(x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 19,
            "problem": "f(x) = cot(x)",
            "problem_latex": r"f(x) = \cot(x)",
            "solution": "f'(x) = -csc^2(x)",
            "solution_latex": r"f'(x) = -\csc^2(x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 20,
            "problem": "f(x) = sinh(x)",
            "problem_latex": r"f(x) = \sinh(x)",
            "solution": "f'(x) = cosh(x)",
            "solution_latex": r"f'(x) = \cosh(x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 21,
            "problem": "f(x) = cosh(x)",
            "problem_latex": r"f(x) = \cosh(x)",
            "solution": "f'(x) = sinh(x)",
            "solution_latex": r"f'(x) = \sinh(x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 22,
            "problem": "f(x) = tanh(x)",
            "problem_latex": r"f(x) = \tanh(x)",
            "solution": "f'(x) = sech^2(x)",
            "solution_latex": r"f'(x) = \text{sech}^2(x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 23,
            "problem": "f(x) = sech(x)",
            "problem_latex": r"f(x) = \text{sech}(x)",
            "solution": "f'(x) = -sech(x)tanh(x)",
            "solution_latex": r"f'(x) = -\text{sech}(x)\tanh(x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 24,
            "problem": "f(x) = csch(x)",
            "problem_latex": r"f(x) = \text{csch}(x)",
            "solution": "f'(x) = -csch(x)coth(x)",
            "solution_latex": r"f'(x) = -\text{csch}(x)\coth(x)",
            "topic": "differentiation",
            "difficulty": "easy"
        },
        {
            "id": 25,
            "problem": "f(x) = coth(x)",
            "problem_latex": r"f(x) = \coth(x)",
            "solution": "f'(x) = -csch^2(x)",
            "solution_latex": r"f'(x) = -\text{csch}^2(x)",
            "topic": "differentiation",
            "difficulty": "easy"
        }
    ],
    "medium": [
        {
            "id": 26,
            "problem": "f(x) = x^a sin(x)",
            "problem_latex": r"f(x) = x^a \sin(x)",
            "solution": "f'(x) = a*x^(a-1)sin(x) + x^a*cos(x)",
            "solution_latex": r"f'(x) = a*x^(a-1)\sin(x) + x^a\cos(x)",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "power_rule"
        },
        {
            "id": 27,
            "problem": "f(x) = e^x cos(x)",
            "problem_latex": r"f(x) = e^x \cos(x)",
            "solution": "f'(x) = e^x(cos(x) - sin(x))",
            "solution_latex": r"f'(x) = e^x (\cos(x) - \sin(x))",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 28,
            "problem": "f(x) = ln(x^a + 1)",
            "problem_latex": r"f(x) = \ln(x^a + 1)",
            "solution": "f'(x) = a*x^(a-1)/(x^a + 1)",
            "solution_latex": r"f'(x) = \frac{a*x^(a-1)}{x^a + 1}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "power_rule"
        },
        {
            "id": 29,
            "problem": "f(x) = arctan(x/a)",
            "problem_latex": r"f(x) = \arctan\left(\frac{x}{a}\right)",
            "solution": "f'(x) = a/(a^2 + x^2)",
            "solution_latex": r"f'(x) = \frac{a}{a^2 + x^2}",
            "topic": "differentiation",
            "difficulty": "medium",
             "variable_type": "ln_coeff"
        },
        {
            "id": 30,
            "problem": "f(x) = x e^{ax}",
            "problem_latex": r"f(x) = x e^{ax}",
            "solution": "f'(x) = (1 + ax)e^{ax}",
            "solution_latex": r"f'(x) = (1 + ax) e^{ax}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "e_rule"
        },
        {
            "id": 31,
            "problem": "f(x) = sin(x)/x^a",
            "problem_latex": r"f(x) = \frac{\sin(x)}{x^a}",
            "solution": "f'(x) = (x*cos(x) - a*sin(x))/x^(a+1)",
            "solution_latex": r"f'(x) = \frac{x\cos(x) - a\sin(x)}{x^{a+1}}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "quotient_rule_power_denom"
        },
        {
            "id": 32,
            "problem": "f(x) = sqrt(x^2 + a)",
            "problem_latex": r"f(x) = \sqrt{x^2 + a}",
            "solution": "f'(x) = x/sqrt(x^2 + a)",
            "solution_latex": r"f'(x) = \frac{x}{\sqrt{x^2 + a}}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "general_coeff_sqrt"
        },
        {
            "id": 33,
            "problem": "f(x) = ln(sin(ax))",
            "problem_latex": r"f(x) = \ln(\sin(ax))",
            "solution": "f'(x) = a*cot(ax)",
            "solution_latex": r"f'(x) = a\cot(ax)",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "chain_rule_trig_ln"
        },
        {
            "id": 34,
            "problem": "f(x) = arcsin(x^a)",
            "problem_latex": r"f(x) = \arcsin(x^a)",
            "solution": "f'(x) = a*x^(a-1)/sqrt(1 - x^(2a))",
            "solution_latex": r"f'(x) = \frac{a x^{a-1}}{\sqrt{1 - x^{2a}}}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "power_rule_chain_arcsin"
        },
        {
            "id": 35,
            "problem": "f(x) = arccos(sqrt(ax))",
            "problem_latex": r"f(x) = \arccos(\sqrt{ax})",
            "solution": "f'(x) = -a/(2sqrt(ax)sqrt(1 - ax))",
            "solution_latex": r"f'(x) = -\frac{a}{2\sqrt{ax}\sqrt{1 - ax}}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "arccos_sqrt_coeff"
        },
        {
            "id": 36,
            "problem": "f(x) = arctan(e^{ax})",
            "problem_latex": r"f(x) = \arctan(e^{ax})",
            "solution": "f'(x) = a*e^{ax}/(1 + e^{2ax})",
            "solution_latex": r"f'(x) = \frac{a e^{ax}}{1 + e^{2ax}}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "arctan_e_coeff"
        },
        {
            "id": 37,
            "problem": "f(x) = ln(a + x^2)",
            "problem_latex": r"f(x) = \ln(a + x^2)",
            "solution": "f'(x) = 2x/(a + x^2)",
            "solution_latex": r"f'(x) = \frac{2x}{a + x^2}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "ln_coeff_plus_x2"
        },
        {
            "id": 38,
            "problem": "f(x) = e^x sin(ax)",
            "problem_latex": r"f(x) = e^x \sin(ax)",
            "solution": "f'(x) = e^x(acos(ax) + sin(ax))",
            "solution_latex": r"f'(x) = e^x(a\cos(ax) + \sin(ax))",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "product_rule_coeff_trig"
        },
        {
            "id": 39,
            "problem": "f(x) = x^x",
            "problem_latex": r"f(x) = x^x",
            "solution": "f'(x) = x^x(ln(x) + 1)",
            "solution_latex": r"f'(x) = x^x(\ln(x) + 1)",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 40,
            "problem": "f(x) = ln(x + sqrt(x^2 + a))",
            "problem_latex": r"f(x) = \ln(x + \sqrt{x^2 + a})",
            "solution": "f'(x) = 1/sqrt(x^2 + a)",
            "solution_latex": r"f'(x) = \frac{1}{\sqrt{x^2 + a}}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "ln_sqrt_coeff"
        },
        {
            "id": 41,
            "problem": "f(x) = tan^a(x)",
            "problem_latex": r"f(x) = \tan^a(x)",
            "solution": "f'(x) = a*tan^(a-1)(x)sec^2(x)",
            "solution_latex": r"f'(x) = a\tan^{a-1}(x)\sec^2(x)",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "power_rule_trig"
        },
        {
            "id": 42,
            "problem": "f(x) = e^{ax^3}",
            "problem_latex": r"f(x) = e^{ax^3}",
            "solution": "f'(x) = 3ax^2e^{ax^3}",
            "solution_latex": r"f'(x) = 3ax^2 e^{ax^3}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "power_rule_chain_exp"
        },
        {
            "id": 43,
            "problem": "f(x) = cos^a(x)",
            "problem_latex": r"f(x) = \cos^a(x)",
            "solution": "f'(x) = -a*cos^(a-1)(x)sin(x)",
            "solution_latex": r"f'(x) = -a\cos^{a-1}(x)\sin(x)",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "power_rule_trig"
        },
        {
            "id": 44,
            "problem": "f(x) = ln(x)/sqrt(ax)",
            "problem_latex": r"f(x) = \frac{\ln(x)}{\sqrt{ax}}",
            "solution": "f'(x) = (2ax - xln(x))/(2ax^(3/2))",
            "solution_latex": r"f'(x) = \frac{2a - \ln(x)}{2a x^{3/2}}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "quotient_rule_sqrt_coeff"
        },
        {
            "id": 45,
            "problem": "f(x) = sin(x)/x^a",
            "problem_latex": r"f(x) = \frac{\sin(x)}{x^a}",
            "solution": "f'(x) = (x^a*cos(x) - a*x^(a-1)sin(x))/x^(2a)",
            "solution_latex": r"f'(x) = \frac{x\cos(x) - a\sin(x)}{x^{a+1}}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "quotient_rule_power_denom"
        },
        {
            "id": 46,
            "problem": "f(x) = arctan(x^a)",
            "problem_latex": r"f(x) = \arctan(x^a)",
            "solution": "f'(x) = a*x^(a-1)/(1 + x^(2a))",
            "solution_latex": r"f'(x) = \frac{a x^{a-1}}{1 + x^{2a}}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "power_rule_chain_arctan"
        },
        {
            "id": 47,
            "problem": "f(x) = ln(x^2 + a) sin(x)",
            "problem_latex": r"f(x) = \ln(x^2 + a) \sin(x)",
            "solution": "f'(x) = cos(x)ln(x^2 + a) + (2xsin(x))/(x^2 + a)",
            "solution_latex": r"f'(x) = \cos(x)\ln(x^2 + a) + \frac{2x\sin(x)}{x^2 + a}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "product_rule_ln_coeff"
        },
        {
            "id": 48,
            "problem": "f(x) = x^a ln(x)",
            "problem_latex": r"f(x) = x^a \ln(x)",
            "solution": "f'(x) = a*x^(a-1)*ln(x) + x^(a-1)",
            "solution_latex": r"f'(x) = x^{a-1}(a\ln(x) + 1)",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "power_rule_product"
        },
        {
            "id": 49,
            "problem": "f(x) = tan(x)/x^a",
            "problem_latex": r"f(x) = \frac{\tan(x)}{x^a}",
            "solution": "f'(x) = (x^a*sec^2(x) - a*x^(a-1)tan(x))/x^(2a)",
            "solution_latex": r"f'(x) = \frac{x^a\sec^2(x) - a x^{a-1}\tan(x)}{x^{2a}}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "quotient_rule_power_denom"
        },
        {
            "id": 50,
            "problem": "f(x) = ln(ax)/x^2",
            "problem_latex": r"f(x) = \frac{\ln(ax)}{x^2}",
            "solution": "f'(x) = (1/x^2 - 2ln(ax)/x^3)",
            "solution_latex": r"f'(x) = \frac{1-2\ln(ax)}{x^3}",
            "topic": "differentiation",
            "difficulty": "medium",
            "variable_type": "quotient_rule_ln_coeff"
        }
    ],
    "hard": [
        {
            "id": 51,
            "problem": "f(x) = x^{sin(ax)}",
            "problem_latex": r"f(x) = x^{\sin(ax)}",
            "solution": "f'(x) = x^{sin(ax)}(acos(ax)ln(x) + sin(ax)/x)",
            "solution_latex": r"f'(x) = x^{\sin(ax)}(a\cos(ax)\ln(x) + \frac{\sin(ax)}{x})",
            "topic": "differentiation",
            "difficulty": "hard",
            "variable_type": "x_sin_ax"
        },
        {
            "id": 52,
            "problem": "f(x) = ln(ln(ax))",
            "problem_latex": r"f(x) = \ln(\ln(ax))",
            "solution": "f'(x) = 1/(xln(ax))",
            "solution_latex": r"f'(x) = \frac{1}{x\ln(ax)}",
            "topic": "differentiation",
            "difficulty": "hard",
            "variable_type": "ln_ln_ax"
        },
        {
            "id": 53,
            "problem": "f(x) = e^{arctan(ax)}",
            "problem_latex": r"f(x) = e^{\arctan(ax)}",
            "solution": "f'(x) = a*e^{arctan(ax)}/(1 + a^2 x^2)",
            "solution_latex": r"f'(x) = \frac{a e^{\arctan(ax)}}{1 + a^2 x^2}",
            "topic": "differentiation",
            "difficulty": "hard",
            "variable_type": "e_arctan_ax"
        },
        {
            "id": 54,
            "problem": "f(x) = sin(x)/ln(ax)",
            "problem_latex": r"f(x) = \frac{\sin(x)}{\ln(ax)}",
            "solution": "f'(x) = (cos(x)ln(ax) - sin(x)/x)/(ln(ax))^2",
            "solution_latex": r"f'(x) = \frac{\cos(x)\ln(ax) - \frac{\sin(x)}{x}}{(\ln(ax))^2}",
            "topic": "differentiation",
            "difficulty": "hard",
            "variable_type": "sin_x_ln_ax"
        },
        {
            "id": 55,
            "problem": "f(x) = ln(sqrt(x^2 + a) + x)",
            "problem_latex": r"f(x) = \ln\left(\sqrt{x^2 + a} + x\right)",
            "solution": "f'(x) = 1/sqrt(x^2 + a)",
            "solution_latex": r"f'(x) = \frac{1}{\sqrt{x^2 + a}}",
            "topic": "differentiation",
            "difficulty": "hard",
            "variable_type": "ln_sqrt_coeff"
        },
        {
            "id": 56,
            "problem": "f(x) = ln(x)/(ax^2 + 1)",
            "problem_latex": r"f(x) = \frac{\ln(x)}{ax^2 + 1}",
            "solution": "f'(x) = ((1 - 2axln(x))/((ax^2 + 1)^2)",
            "solution_latex": r"f'(x) = \frac{1 - 2a x\ln(x)}{(a x^2 + 1)^2}",
            "topic": "differentiation",
            "difficulty": "hard",
            "variable_type": "ln_x_a_x2"
        },
        {
            "id": 57,
            "problem": "f(x) = x^a e^{1/x}",
            "problem_latex": r"f(x) = x^a e^{1/x}",
            "solution": "f'(x) = a*x^(a-1) e^(1/x) - e^(1/x)/x^(2-a)",
            "solution_latex": r"f'(x) = a x^{a-1} e^{1/x} - \frac{e^{1/x}}{x^{2-a}}",
            "topic": "differentiation",
            "difficulty": "hard",
            "variable_type": "power_e_x"
        },
        {
            "id": 58,
            "problem": "f(x) = e^{axsin(x)}",
            "problem_latex": r"f(x) = e^{ax\sin(x)}",
            "solution": "f'(x) = e^{axsin(x)}(asin(x) + axcos(x))",
            "solution_latex": r"f'(x) = e^{ax\sin(x)}(a\sin(x) + ax\cos(x))",
            "topic": "differentiation",
            "difficulty": "hard",
            "variable_type": "e_ax_sin_x"
        },
        {
            "id": 59,
            "problem": "f(x) = ln(sin(x) + acos(x))",
            "problem_latex": r"f(x) = \ln(\sin(x) + a\cos(x))",
            "solution": "f'(x) = (cos(x) - asin(x))/(sin(x) + acos(x))",
            "solution_latex": r"f'(x) = \frac{\cos(x) - a\sin(x)}{\sin(x) + a\cos(x)}",
            "topic": "differentiation",
            "difficulty": "hard",
            "variable_type": "ln_sin_x_a_cos_x"
        },
        {
            "id": 60,
            "problem": "f(x) = tan^{-1}(a/x)",
            "problem_latex": r"f(x) = \tan^{-1}\left(\frac{a}{x}\right)",
            "solution": "f'(x) = -a/(x^2 + a^2)",
            "solution_latex": r"f'(x) = -\frac{a}{x^2 + a^2}",
            "topic": "differentiation",
            "difficulty": "hard",
            "variable_type": "arctan_a_x"
        }
    ],
    "ultimate": [
        {
            "id": 61,
            "problem": "f(x) = x^{x^x}",
            "problem_latex": r"f(x) = x^{x^x}",
            "solution": "f'(x) = x^{x^x}(ln(x^x) + x^{x-1}(ln(x) + 1))",
            "solution_latex": r"f'(x) = x^{x^x} \left( \ln(x^x) + x^{x-1}(\ln(x) + 1) \right)",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "none"
        },
        {
            "id": 62,
            "problem": "f(x) = e^{x^3 ln(x)}",
            "problem_latex": r"f(x) = e^{x^3 \ln(x)}",
            "solution": "f'(x) = e^{x^3 ln(x)}(3x^2 ln(x) + x^2)",
            "solution_latex": r"f'(x) = e^{x^3 \ln(x)} \left(3x^2 \ln(x) + x^2\right)",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "none"
        },
        {
            "id": 63,
            "problem": "f(x) = arctan(e^{x^2})",
            "problem_latex": r"f(x) = \arctan(e^{x^2})",
            "solution": "f'(x) = 2x e^{x^2}/(1 + e^{2x^2})",
            "solution_latex": r"f'(x) = \frac{2x e^{x^2}}{1 + e^{2x^2}}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "none"
        },
        {
            "id": 64,
            "problem": "f(x) = ln(sin(ax^2))",
            "problem_latex": r"f(x) = \ln(\sin(ax^2))",
            "solution": "f'(x) = 2axcos(ax^2)/sin(ax^2)",
            "solution_latex": r"f'(x) = \frac{2ax\cos(ax^2)}{\sin(ax^2)}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "chain_rule_sin_ax2"
        },
        {
            "id": 65,
            "problem": "f(x) = x^{x^a}",
            "problem_latex": r"f(x) = x^{x^a}",
            "solution": "f'(x) = x^(x^a)(ln(x^a) + x^(a-1)ln(x))",
            "solution_latex": r"f'(x) = x^{x^a}(x^a\ln(x) + x^{a-1}\ln(x))",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "power_rule_x_xa"
        },
        {
            "id": 66,
            "problem": "f(x) = tan^{-1}(ln(ax))",
            "problem_latex": r"f(x) = \tan^{-1}\left(\ln(ax)\right)",
            "solution": "f'(x) = 1/(x(1 + (ln(ax))^2))",
            "solution_latex": r"f'(x) = \frac{1}{x(1 + (\ln(ax))^2)}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "arctan_ln_ax"
        },
        {
            "id": 67,
            "problem": "f(x) = ln(e^{ax} + e^{-ax})",
            "problem_latex": r"f(x) = \ln\left(e^{ax} + e^{-ax}\right)",
            "solution": "f'(x) = (e^{ax} - e^{-ax})/(e^{ax} + e^{-ax})",
            "solution_latex": r"f'(x) = \frac{ae^{ax} - ae^{-ax}}{e^{ax} + e^{-ax}}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "ln_exp_coeff"
        },
        {
            "id": 68,
            "problem": "f(x) = sqrt(ln(x^2 + a))",
            "problem_latex": r"f(x) = \sqrt{\ln(x^2 + a)}",
            "solution": "f'(x) = x/((x^2 + a)sqrt(ln(x^2 + a)))",
            "solution_latex": r"f'(x) = \frac{x}{(x^2 + a)\sqrt{\ln(x^2 + a)}}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "sqrt_ln_x2_coeff"
        },
        {
            "id": 69,
            "problem": "f(x) = e^{sin(ax^2)}",
            "problem_latex": r"f(x) = e^{\sin(ax^2)}",
            "solution": "f'(x) = 2axcos(ax^2)e^{sin(ax^2)}",
            "solution_latex": r"f'(x) = 2ax\cos(ax^2)e^{\sin(ax^2)}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "e_sin_ax2"
        },
        {
            "id": 70,
            "problem": "f(x) = ln(arctan(ax^2))",
            "problem_latex": r"f(x) = \ln\left(\arctan(ax^2)\right)",
            "solution": "f'(x) = 2ax^3/(1 + a^2x^4)",
            "solution_latex": r"f'(x) = \frac{2ax}{1 + a^2x^4}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "ln_arctan_ax2"
        },
        {
            "id": 71,
            "problem": "f(x) = x^x sin(ax)",
            "problem_latex": r"f(x) = x^x \sin(ax)",
            "solution": "f'(x) = x^x(ln(x) + 1)sin(ax) + ax^x cos(ax)",
            "solution_latex": r"f'(x) = x^x (\ln(x) + 1)\sin(ax) + ax^x \cos(ax)",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "product_rule_x_sin_ax"
        },
        {
            "id": 72,
            "problem": "f(x) = e^{x cos(ax)}",
            "problem_latex": r"f(x) = e^{x \cos(ax)}",
            "solution": "f'(x) = e^{x cos(ax)}(-ax sin(ax) + cos(ax))",
            "solution_latex": r"f'(x) = e^{x \cos(ax)}(-ax \sin(ax) + \cos(ax))",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "e_x_cos_ax"
        },
        {
            "id": 73,
            "problem": "f(x) = sin(ax^2)/sqrt(x)",
            "problem_latex": r"f(x) = \frac{\sin(ax^2)}{\sqrt{x}}",
            "solution": "f'(x) = (2ax^2*cos(ax^2) - sin(ax^2))/(2x^(3/2))",
            "solution_latex": r"f'(x) = \frac{2ax^2\cos(ax^2) - \sin(ax^2)}{2x^{3/2}}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "quotient_rule_sin_ax2"
        },
        {
            "id": 74,
            "problem": "f(x) = tan^{-1}(e^{ax} + e^{-ax})",
            "problem_latex": r"f(x) = \tan^{-1}\left(e^{ax} + e^{-ax}\right)",
            "solution": "f'(x) = a(e^{ax} - e^{-ax})/(1 + (e^{ax} + e^{-ax})^2)",
            "solution_latex": r"f'(x) = \frac{a(e^{ax} - e^{-ax})}{1 + (e^{ax} + e^{-ax})^2}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "arctan_exp_ax"
        },
        {
            "id": 75,
            "problem": "f(x) = ln(ax + sqrt(x^2 - 1))",
            "problem_latex": r"f(x) = \ln\left(ax + \sqrt{x^2 - 1}\right)",
            "solution": "f'(x) = a/sqrt(x^2 - 1)",
            "solution_latex": r"f'(x) = \frac{a}{\sqrt{x^2 - 1}}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "ln_ax_sqrt"
        },
        {
            "id": 76,
            "problem": "f(x) = x^{tan(ax)}",
            "problem_latex": r"f(x) = x^{\tan(ax)}",
            "solution": "f'(x) = x^(tan(ax))(a*sec^2(ax)ln(x) + tan(ax)/x)",
            "solution_latex": r"f'(x) = x^{\tan(ax)}(a\sec^2(ax)\ln(x) + \frac{\tan(ax)}{x})",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "power_rule_tan_ax"
        },
        {
            "id": 77,
            "problem": "f(x) = e^{ln(ax^2 + 1)}",
            "problem_latex": r"f(x) = e^{\ln(ax^2 + 1)}",
            "solution": "f'(x) = 2ax e^{ln(ax^2 + 1)}/(ax^2 + 1)",
            "solution_latex": r"f'(x) = \frac{2ax e^{\ln(ax^2 + 1)}}{ax^2 + 1}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "e_ln_ax2"
        },
        {
            "id": 78,
            "problem": "f(x) = sqrt(x^2 + 2ax + a^2) ln(x)",
            "problem_latex": r"f(x) = \sqrt{x^2 + 2ax + a^2} \ln(x)",
            "solution": "((x+a)ln(x))/sqrt(x^2 + 2ax + a^2) + sqrt(x^2 + 2ax + a^2)/x",
            "solution_latex": r"\frac{(x+a)\ln(x)}{\sqrt{x^2 + 2ax + a^2}} + \frac{\sqrt{x^2 + 2ax + a^2}}{x}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "sqrt_x2_ax"
        },
        {
            "id": 79,
            "problem": "f(x) = e^{ax}/(x^2 + 1)",
            "problem_latex": r"f(x) = \frac{e^{ax}}{x^2 + 1}",
            "solution": "(e^(ax)(x^2 + 1) - 2x*e^(ax))/(x^2 + 1)^2",
            "solution_latex": r"\frac{e^{ax}(x^2 + 1) - 2axe^{ax}}{(x^2 + 1)^2}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "quotient_e_ax"
        },
        {
            "id": 80,
            "problem": "f(x) = ln(x^2 + 2ax + a^2)",
            "problem_latex": r"f(x) = \ln(x^2 + 2ax + a^2)",
            "solution": "f'(x) = (2x + 2a)/(x^2 + 2ax + a^2)",
            "solution_latex": r"f'(x) = \frac{2x + 2a}{x^2 + 2ax + a^2}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "ln_x2_ax"
        },
        {
            "id": 81,
            "problem": "f(x) = x^{x^a}",
            "problem_latex": r"f(x) = x^{x^a}",
            "solution": "f'(x) = x^{x^a}(a*x^(a-1)*ln(x) + x^(a-1))",
            "solution_latex": r"f'(x) = x^{x^a}(x^a\ln(x) + a x^{a-1})",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "power_rule_x_xa"
        },
        {
            "id": 82,
            "problem": "f(x) = arctan(ln(ax)/sqrt(x))",
            "problem_latex": r"f(x) = \arctan\left(\frac{\ln(ax)}{\sqrt{x}}\right)",
            "solution": "f'(x) = (x + ln(ax))/((x*sqrt(x)*(1 + (ln(ax)/sqrt(x))^2))",
            "solution_latex": r"f'(x) = \frac{a (1 + \ln(x))}{x\sqrt{x}(1 + (\ln(ax)/\sqrt{x})^2)}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "arctan_ln_ax_x"
        },
        {
            "id": 83,
            "problem": "f(x) = ln(cos(x))^a",
            "problem_latex": r"f(x) = \ln(\cos(x))^a",
            "solution": "f'(x) = -a*tan(x)ln(cos(x))^(a-1)",
            "solution_latex": r"f'(x) = -a\tan(x)\ln(\cos(x))^{a-1}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "power_rule_ln_cos"
        },
        {
            "id": 84,
            "problem": "f(x) = e^{sin(x)}ln(ax)",
            "problem_latex": r"f(x) = e^{\sin(x)}\ln(ax)",
            "solution": "f'(x) = e^(sin(x)ln(ax)cos(x) + e^(sin(x))/x",
            "solution_latex": r"f'(x) = e^{\sin(x)}\ln(ax)\cos(x) + \frac{e^{\sin(x)}}{x}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "product_rule_e_sin_ln_ax"
        },
        {
            "id": 85,
            "problem": "f(x) = arctan(e^{ax ln(x)})",
            "problem_latex": r"f(x) = \arctan(e^{ax \ln(x)})",
            "solution": "f'(x) = e^(axln(x))(a(ln(x) + 1))/(1 + e^(2axln(x)))",
            "solution_latex": r"f'(x) = \frac{e^{ax \ln(x)}(a(\ln(x) + 1))}{1 + e^{2ax \ln(x)}}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "arctan_e_ax_ln_x"
        },
        {
            "id": 86,
            "problem": "f(x) = ln(sin(ax^3))",
            "problem_latex": r"f(x) = \ln(\sin(ax^3))",
            "solution": "f'(x) = (3ax^2cos(ax^3)/sin(ax^3))",
            "solution_latex": r"f'(x) = \frac{3ax^2 \cos(ax^3)}{\sin(ax^3)}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "ln_sin_ax3"
        },
        {
            "id": 87,
            "problem": "f(x) = x^{e^{ax}}",
            "problem_latex": r"f(x) = x^{e^{ax}}",
            "solution": "f'(x) = x^(e^ax)(ae^xln(x) + 1/x)",
            "solution_latex": r"f'(x) = x^{e^{ax}}\left(a*e^{ax} \ln(x) + \frac{1}{x}\right)",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "x_exp_ax"
        },
        {
            "id": 88,
            "problem": "f(x) = ln(sqrt(tan(ax)))",
            "problem_latex": r"f(x) = \ln\left(\sqrt{\tan(ax)}\right)",
            "solution": "f'(x) = a/(2tan(ax)cos^2(ax))",
            "solution_latex": r"f'(x) = \frac{a}{2 \tan(ax)\cos^2(ax)}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "ln_sqrt_tan_ax"
        },
        {
            "id": 89,
            "problem": "f(x) = e^{x^x ln(ax)}",
            "problem_latex": r"f(x) = e^{x^x \ln(ax)}",
            "solution": "f'(x) = e^(x^xln(ax))(a*x^(x-1)(ln(ax) + 1) + x^x/(ax)",
            "solution_latex": r"f'(x) = e^{x^x \ln(ax)}\left(x^{x-1}(\ln(ax) + 1) + \frac{x^x}{x}\right)",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "e_x_x_ln_ax"
        },
        {
            "id": 90,
            "problem": "f(x) = ln(ln(sin(ax)))",
            "problem_latex": r"f(x) = \ln\left(\ln(\sin(ax))\right)",
            "solution": "f'(x) = a*cot(ax)/ln(sin(ax))",
            "solution_latex": r"f'(x) = \frac{a\cot(ax)}{\ln(\sin(ax))}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "ln_ln_sin_ax"
        },
        {
            "id": 91,
            "problem": "f(x) = arcsin(e^{ax^2})",
            "problem_latex": r"f(x) = \arcsin(e^{ax^2})",
            "solution": "f'(x) = 2axe^(ax^2)/sqrt(1 - e^(2ax^2))",
            "solution_latex": r"f'(x) = \frac{2ax e^{ax^2}}{\sqrt{1 - e^{2ax^2}}}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "arcsin_e_ax2"
        },
        {
            "id": 92,
            "problem": "f(x) = tan^{-1}(sin(ax)/cos(ax))",
            "problem_latex": r"f(x) = \tan^{-1}\left(\frac{\sin(ax)}{\cos(ax)}\right)",
            "solution": "a",
            "solution_latex": r"a",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "arctan_sin_ax"
        },
        {
            "id": 93,
            "problem": "f(x) = x^{e^{a ln(x)}}",
            "problem_latex": r"f(x) = x^{e^{a \ln(x)}}",
            "solution": "f'(x) = x^(e^(alnx))(a/x + (1/x)e^(alnx)ln(x))",
            "solution_latex": r"f'(x) = x^{e^{a\ln(x)}} a",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "power_rule_exp_a_ln_x"
        },
        {
            "id": 94,
            "problem": "f(x) = ln(x^x + x^{ax})",
            "problem_latex": r"f(x) = \ln(x^x + x^{ax})",
            "solution": "(x^(x-1)*(ln(x) + 1) + ax^(ax-1)ln(x))/(x^x + x^(ax)",
            "solution_latex": r"\frac{x^{x-1}(\ln(x) + 1) + ax^{ax-1}(\ln(x))}{x^x + x^{ax}}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "ln_x_ax"
        },
        {
            "id": 95,
            "problem": "f(x) = tan(ax^2)/ln(x)",
            "problem_latex": r"f(x) = \frac{\tan(ax^2)}{\ln(x)}",
            "solution": "(2axsec^2(ax^2)ln(x) - tan(ax^2)/x)/(ln(x))^2",
            "solution_latex": r"\frac{2ax \sec^2(ax^2)\ln(x) - \frac{\tan(ax^2)}{x}}{(\ln(x))^2}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "quotient_rule_tan_ax2"
        },
        {
            "id": 96,
            "problem": "f(x) = sqrt(arctan(ax^2))",
            "problem_latex": r"f(x) = \sqrt{\tan^{-1}(ax^2)}",
            "solution": "2ax/((1 + a^2x^4)sqrt(arctan(ax^2)))",
            "solution_latex": r"\frac{2ax}{\sqrt{\arctan(ax^2)}(1 + a^2x^4)}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "sqrt_arctan_ax2"
        },
        {
            "id": 97,
            "problem": "f(x) = ln(arctan(ax^3))",
            "problem_latex": r"f(x) = \ln\left(\arctan(ax^3)\right)",
            "solution": "f'(x) = 3ax^2/(1 + a^2x^6)",
            "solution_latex": r"f'(x) = \frac{3ax^2}{1 + a^2x^6}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "ln_arctan_ax3"
        },
        {
            "id": 98,
            "problem": "f(x) = e^{sin(ax^2 + a)}",
            "problem_latex": r"f(x) = e^{\sin(ax^2 + a)}",
            "solution": "f'(x) = 2ax*cos(ax^2 + a)e^(sin(ax^2 + a))",
            "solution_latex": r"f'(x) = 2ax \cos(ax^2 + a) e^{\sin(ax^2 + a)}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "e_sin_ax2_a"
        },
        {
            "id": 99,
            "problem": "f(x) = arctan(e^{a sin(x)})",
            "problem_latex": r"f(x) = \arctan\left(e^{a\sin(x)}\right)",
            "solution": "f'(x) = a*cos(x)e^{a sin(x)}/(1 + e^(2a sin(x)))",
            "solution_latex": r"f'(x) = \frac{a \cos(x)e^{a\sin(x)}}{1 + e^{2a\sin(x)}}",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "arctan_e_a_sin_x"
        },
        {
            "id": 100,
            "problem": "f(x) = ln(x^{x^a})",
            "problem_latex": r"f(x) = \ln(x^{x^a})",
            "solution": "a*x^(a-1)(ln(x)+1)ln(x) + x^(a)ln(x) + x^(a-1)ln(x)",
            "solution_latex": r"x^{a}(\ln(x) + 1)\ln(x) + x^{a-1}(\ln(x) + 1)",
            "topic": "differentiation",
            "difficulty": "ultimate",
            "variable_type": "ln_x_xa"
        }
    ]
}

# Save as JSON file
with open('differentiation_problems.json', 'w') as f:
    json.dump(differentiation_problems, f, indent=4)


# Create SQLite database
def create_problems_database():
    conn = sqlite3.connect('math_problems.db')
    cursor = conn.cursor()

    # Create problems table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS problems (
        id INTEGER PRIMARY KEY,
        problem TEXT NOT NULL,
        problem_latex TEXT NOT NULL,
        solution TEXT NOT NULL,
        solution_latex TEXT NOT NULL,
        topic TEXT NOT NULL,
        difficulty TEXT NOT NULL
    )
    ''')

    # Insert sample problems from each difficulty level
    for difficulty in differentiation_problems:
        for problem in differentiation_problems[difficulty]:
            cursor.execute('''
            INSERT OR REPLACE INTO problems (id, problem, problem_latex, solution, solution_latex, topic, difficulty)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                problem['id'],
                problem['problem'],
                problem['problem_latex'],
                problem['solution'],
                problem['solution_latex'],
                problem['topic'],
                problem['difficulty']
            ))

    conn.commit()
    conn.close()
    print("Database created successfully!")


if __name__ == "__main__":
    create_problems_database()