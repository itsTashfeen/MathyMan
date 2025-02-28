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
            "problem": "f(x) = sin(x)/x",
            "problem_latex": r"f(x) = \frac{\sin(x)}{x}",
            "solution": "f'(x) = (xcos(x) - sin(x))/x^2",
            "solution_latex": r"f'(x) = \frac{x\cos(x) - \sin(x)}{x^2}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 32,
            "problem": "f(x) = sqrt(x^2 + 1)",
            "problem_latex": r"f(x) = \sqrt{x^2 + 1}",
            "solution": "f'(x) = x/sqrt(x^2 + 1)",
            "solution_latex": r"f'(x) = \frac{x}{\sqrt{x^2 + 1}}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 33,
            "problem": "f(x) = ln(sin(x))",
            "problem_latex": r"f(x) = \ln(\sin(x))",
            "solution": "f'(x) = cot(x)",
            "solution_latex": r"f'(x) = \cot(x)",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 34,
            "problem": "f(x) = arcsin(x^2)",
            "problem_latex": r"f(x) = \arcsin(x^2)",
            "solution": "f'(x) = 2x/sqrt(1 - x^4)",
            "solution_latex": r"f'(x) = \frac{2x}{\sqrt{1 - x^4}}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 35,
            "problem": "f(x) = arccos(sqrt(x))",
            "problem_latex": r"f(x) = \arccos(\sqrt{x})",
            "solution": "f'(x) = -1/(2sqrt(x)sqrt(1 - x))",
            "solution_latex": r"f'(x) = -\frac{1}{2\sqrt{x}\sqrt{1 - x}}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 36,
            "problem": "f(x) = arctan(e^x)",
            "problem_latex": r"f(x) = \arctan(e^x)",
            "solution": "f'(x) = e^x/(1 + e^{2x})",
            "solution_latex": r"f'(x) = \frac{e^x}{1 + e^{2x}}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 37,
            "problem": "f(x) = ln(1 + x^2)",
            "problem_latex": r"f(x) = \ln(1 + x^2)",
            "solution": "f'(x) = 2x/(1 + x^2)",
            "solution_latex": r"f'(x) = \frac{2x}{1 + x^2}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 38,
            "problem": "f(x) = e^x sin(2x)",
            "problem_latex": r"f(x) = e^x \sin(2x)",
            "solution": "f'(x) = e^x(2cos(2x) + sin(2x))",
            "solution_latex": r"f'(x) = e^x(2\cos(2x) + \sin(2x))",
            "topic": "differentiation",
            "difficulty": "medium"
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
            "problem": "f(x) = ln(x + sqrt(x^2 + 1))",
            "problem_latex": r"f(x) = \ln(x + \sqrt{x^2 + 1})",
            "solution": "f'(x) = 1/sqrt(x^2 + 1)",
            "solution_latex": r"f'(x) = \frac{1}{\sqrt{x^2 + 1}}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 41,
            "problem": "f(x) = tan^2(x)",
            "problem_latex": r"f(x) = \tan^2(x)",
            "solution": "f'(x) = 2tan(x)sec^2(x)",
            "solution_latex": r"f'(x) = 2\tan(x)\sec^2(x)",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 42,
            "problem": "f(x) = e^{x^3}",
            "problem_latex": r"f(x) = e^{x^3}",
            "solution": "f'(x) = 3x^2e^{x^3}",
            "solution_latex": r"f'(x) = 3x^2 e^{x^3}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 43,
            "problem": "f(x) = cos^3(x)",
            "problem_latex": r"f(x) = \cos^3(x)",
            "solution": "f'(x) = -3cos^2(x)sin(x)",
            "solution_latex": r"f'(x) = -3\cos^2(x)\sin(x)",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 44,
            "problem": "f(x) = ln(x)/sqrt(x)",
            "problem_latex": r"f(x) = \frac{\ln(x)}{\sqrt{x}}",
            "solution": "f'(x) = (1 - 2ln(x))/(2x^(3/2))",
            "solution_latex": r"f'(x) = \frac{1 - 2\ln(x)}{2x^{3/2}}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 45,
            "problem": "f(x) = sin(x)/x^2",
            "problem_latex": r"f(x) = \frac{\sin(x)}{x^2}",
            "solution": "f'(x) = (xcos(x) - 2sin(x))/x^3",
            "solution_latex": r"f'(x) = \frac{x\cos(x) - 2\sin(x)}{x^3}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 46,
            "problem": "f(x) = arctan(x^2)",
            "problem_latex": r"f(x) = \arctan(x^2)",
            "solution": "f'(x) = 2x/(1 + x^4)",
            "solution_latex": r"f'(x) = \frac{2x}{1 + x^4}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 47,
            "problem": "f(x) = ln(x^2 + 1) sin(x)",
            "problem_latex": r"f(x) = \ln(x^2 + 1) \sin(x)",
            "solution": "f'(x) = cos(x)ln(x^2 + 1) + 2xsin(x)/(x^2 + 1)",
            "solution_latex": r"f'(x) = \cos(x)\ln(x^2 + 1) + \frac{2x\sin(x)}{x^2 + 1}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 48,
            "problem": "f(x) = x^3 ln(x)",
            "problem_latex": r"f(x) = x^3 \ln(x)",
            "solution": "f'(x) = 3x^2ln(x) + x^2",
            "solution_latex": r"f'(x) = 3x^2\ln(x) + x^2",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 49,
            "problem": "f(x) = tan(x)/x^2",
            "problem_latex": r"f(x) = \frac{\tan(x)}{x^2}",
            "solution": "f'(x) = (x^2sec^2(x) - 2xtan(x))/x^4",
            "solution_latex": r"f'(x) = \frac{x^2\sec^2(x) - 2x\tan(x)}{x^4}",
            "topic": "differentiation",
            "difficulty": "medium"
        },
        {
            "id": 50,
            "problem": "f(x) = ln(2x)/x^2",
            "problem_latex": r"f(x) = \frac{\ln(2x)}{x^2}",
            "solution": "f'(x) = (1 - 2ln(2x))/x^3",
            "solution_latex": r"f'(x) = \frac{1 - 2\ln(2x)}{x^3}",
            "topic": "differentiation",
            "difficulty": "medium"
        }
    ],
    "hard": [
        {
            "id": 51,
            "problem": "f(x) = x^{sin(x)}",
            "problem_latex": r"f(x) = x^{\sin(x)}",
            "solution": "f'(x) = x^{sin(x)}(cos(x)ln(x) + sin(x)/x)",
            "solution_latex": r"f'(x) = x^{\sin(x)}\left(\cos(x)\ln(x) + \frac{\sin(x)}{x}\right)",
            "topic": "differentiation",
            "difficulty": "hard"
        },
        {
            "id": 52,
            "problem": "f(x) = ln(ln(x))",
            "problem_latex": r"f(x) = \ln(\ln(x))",
            "solution": "f'(x) = 1/(xln(x))",
            "solution_latex": r"f'(x) = \frac{1}{x\ln(x)}",
            "topic": "differentiation",
            "difficulty": "hard"
        },
        {
            "id": 53,
            "problem": "f(x) = e^{arctan(x)}",
            "problem_latex": r"f(x) = e^{\arctan(x)}",
            "solution": "f'(x) = e^{arctan(x)}/(1 + x^2)",
            "solution_latex": r"f'(x) = \frac{e^{\arctan(x)}}{1 + x^2}",
            "topic": "differentiation",
            "difficulty": "hard"
        },
        {
            "id": 54,
            "problem": "f(x) = sin(x)/ln(x)",
            "problem_latex": r"f(x) = \frac{\sin(x)}{\ln(x)}",
            "solution": "f'(x) = (cos(x)ln(x) - sin(x)/x)/(ln(x))^2",
            "solution_latex": r"f'(x) = \frac{\cos(x)\ln(x) - \sin(x)/x}{(\ln(x))^2}",
            "topic": "differentiation",
            "difficulty": "hard"
        },
        {
            "id": 55,
            "problem": "f(x) = ln(sqrt(x^2 + 1) + x)",
            "problem_latex": r"f(x) = \ln\left(\sqrt{x^2 + 1} + x\right)",
            "solution": "f'(x) = 1/sqrt(x^2 + 1)",
            "solution_latex": r"f'(x) = \frac{1}{\sqrt{x^2 + 1}}",
            "topic": "differentiation",
            "difficulty": "hard"
        },
        {
            "id": 56,
            "problem": "f(x) = ln(x)/(x^2 + 1)",
            "problem_latex": r"f(x) = \frac{\ln(x)}{x^2 + 1}",
            "solution": "f'(x) = (1 - 2xln(x))/(x^2 + 1)^2",
            "solution_latex": r"f'(x) = \frac{1 - 2x\ln(x)}{(x^2 + 1)^2}",
            "topic": "differentiation",
            "difficulty": "hard"
        },
        {
            "id": 57,
            "problem": "f(x) = x^2 e^{1/x}",
            "problem_latex": r"f(x) = x^2 e^{1/x}",
            "solution": "f'(x) = 2x e^{1/x} - e^{1/x}/x",
            "solution_latex": r"f'(x) = 2x e^{1/x} - e^{1/x}/x",
            "topic": "differentiation",
            "difficulty": "hard"
        },
        {
            "id": 58,
            "problem": "f(x) = e^{xsin(x)}",
            "problem_latex": r"f(x) = e^{x\sin(x)}",
            "solution": "f'(x) = e^{xsin(x)}(sin(x) + xcos(x))",
            "solution_latex": r"f'(x) = e^{x\sin(x)}(\sin(x) + x\cos(x))",
            "topic": "differentiation",
            "difficulty": "hard"
        },
        {
            "id": 59,
            "problem": "f(x) = ln(sin(x) + cos(x))",
            "problem_latex": r"f(x) = \ln(\sin(x) + \cos(x))",
            "solution": "f'(x) = (cos(x) - sin(x))/(sin(x) + cos(x))",
            "solution_latex": r"f'(x) = \frac{\cos(x) - \sin(x)}{\sin(x) + \cos(x)}",
            "topic": "differentiation",
            "difficulty": "hard"
        },
        {
            "id": 60,
            "problem": "f(x) = tan^{-1}(1/x)",
            "problem_latex": r"f(x) = \tan^{-1}\left(\frac{1}{x}\right)",
            "solution": "f'(x) = -1/(x^2 + 1)",
            "solution_latex": r"f'(x) = -\frac{1}{x^2 + 1}",
            "topic": "differentiation",
            "difficulty": "hard"
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
            "difficulty": "ultimate"
        },
        {
            "id": 62,
            "problem": "f(x) = e^{x^3 ln(x)}",
            "problem_latex": r"f(x) = e^{x^3 \ln(x)}",
            "solution": "f'(x) = e^{x^3 ln(x)}(3x^2 ln(x) + x^2)",
            "solution_latex": r"f'(x) = e^{x^3 \ln(x)} \left(3x^2 \ln(x) + x^2\right)",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 63,
            "problem": "f(x) = arctan(e^{x^2})",
            "problem_latex": r"f(x) = \arctan(e^{x^2})",
            "solution": "f'(x) = 2x e^{x^2}/(1 + e^{2x^2})",
            "solution_latex": r"f'(x) = \frac{2x e^{x^2}}{1 + e^{2x^2}}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 64,
            "problem": "f(x) = ln(sin(x^2))",
            "problem_latex": r"f(x) = \ln(\sin(x^2))",
            "solution": "f'(x) = 2xcos(x^2)/sin(x^2)",
            "solution_latex": r"f'(x) = \frac{2x\cos(x^2)}{\sin(x^2)}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 65,
            "problem": "f(x) = x^{x^2}",
            "problem_latex": r"f(x) = x^{x^2}",
            "solution": "f'(x) = x^{x^2}(2xln(x) + 1)",
            "solution_latex": r"f'(x) = x^{x^2}(2x\ln(x) + 1)",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 66,
            "problem": "f(x) = tan^{-1}(ln(x))",
            "problem_latex": r"f(x) = \tan^{-1}\left(\ln(x)\right)",
            "solution": "f'(x) = 1/(x(1 + (ln(x))^2))",
            "solution_latex": r"f'(x) = \frac{1}{x(1 + (\ln(x))^2)}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 67,
            "problem": "f(x) = ln(e^x + e^{-x})",
            "problem_latex": r"f(x) = \ln\left(e^x + e^{-x}\right)",
            "solution": "f'(x) = tanh(x)",
            "solution_latex": r"f'(x) = \tanh(x)",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 68,
            "problem": "f(x) = sqrt(ln(x^2 + 1))",
            "problem_latex": r"f(x) = \sqrt{\ln(x^2 + 1)}",
            "solution": "f'(x) = x/(sqrt(ln(x^2 + 1))(x^2 + 1))",
            "solution_latex": r"f'(x) = \frac{x}{\sqrt{\ln(x^2 + 1)}(x^2 + 1)}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 69,
            "problem": "f(x) = e^{sin(x^2)}",
            "problem_latex": r"f(x) = e^{\sin(x^2)}",
            "solution": "f'(x) = 2xcos(x^2)e^{sin(x^2)}",
            "solution_latex": r"f'(x) = 2x\cos(x^2)e^{\sin(x^2)}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 70,
            "problem": "f(x) = ln(arctan(x^2))",
            "problem_latex": r"f(x) = \ln\left(\tan^{-1}(x^2)\right)",
            "solution": "f'(x) = 4x/(1 + x^4)",
            "solution_latex": r"f'(x) = \frac{4x}{1 + x^4}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 71,
            "problem": "f(x) = x^x sin(x)",
            "problem_latex": r"f(x) = x^x \sin(x)",
            "solution": "f'(x) = x^x(ln(x) + 1)sin(x) + x^x cos(x)",
            "solution_latex": r"f'(x) = x^x (\ln(x) + 1)\sin(x) + x^x \cos(x)",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 72,
            "problem": "f(x) = e^{x cos(x)}",
            "problem_latex": r"f(x) = e^{x \cos(x)}",
            "solution": "f'(x) = e^{x cos(x)}(-x sin(x) + cos(x))",
            "solution_latex": r"f'(x) = e^{x \cos(x)}(-x \sin(x) + \cos(x))",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 73,
            "problem": "f(x) = sin(x^2)/sqrt(x)",
            "problem_latex": r"f(x) = \frac{\sin(x^2)}{\sqrt{x}}",
            "solution": "f'(x) = 2xcos(x^2)/sqrt(x) - sin(x^2)/(2x^(3/2))",
            "solution_latex": r"f'(x) = \frac{2x \cos(x^2)}{\sqrt{x}} - \frac{\sin(x^2)}{2x^{3/2}}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 74,
            "problem": "f(x) = tan^{-1}(e^x + e^{-x})",
            "problem_latex": r"f(x) = \tan^{-1}\left(e^x + e^{-x}\right)",
            "solution": "f'(x) = (e^x - e^{-x})/(1 + (e^x + e^{-x})^2)",
            "solution_latex": r"f'(x) = \frac{e^x - e^{-x}}{1 + (e^x + e^{-x})^2}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 75,
            "problem": "f(x) = ln(x + sqrt(x^2 - 1))",
            "problem_latex": r"f(x) = \ln\left(x + \sqrt{x^2 - 1}\right)",
            "solution": "f'(x) = 1/sqrt(x^2 - 1)",
            "solution_latex": r"f'(x) = \frac{1}{\sqrt{x^2 - 1}}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 76,
            "problem": "f(x) = x^{tan(x)}",
            "problem_latex": r"f(x) = x^{\tan(x)}",
            "solution": "f'(x) = x^{tan(x)}(tan(x)ln(x) + sec^2(x)ln(x))",
            "solution_latex": r"f'(x) = x^{\tan(x)} \left(\tan(x)\ln(x) + \sec^2(x)\ln(x)\right)",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 77,
            "problem": "f(x) = e^{ln(x^2 + 1)}",
            "problem_latex": r"f(x) = e^{\ln(x^2 + 1)}",
            "solution": "f'(x) = 2x e^{ln(x^2 + 1)}/(x^2 + 1)",
            "solution_latex": r"f'(x) = \frac{2x e^{\ln(x^2 + 1)}}{x^2 + 1}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 78,
            "problem": "f(x) = sqrt(x^2 + 2x + 1) ln(x)",
            "problem_latex": r"f(x) = \sqrt{x^2 + 2x + 1} \ln(x)",
            "solution": "(x+1)ln(x)/sqrt(x^2 + 2x + 1) + sqrt(x^2 + 2x + 1)/x",
            "solution_latex": r"\frac{(x+1)\ln(x)}{\sqrt{x^2 + 2x + 1}} + \frac{\sqrt{x^2 + 2x + 1}}{x}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 79,
            "problem": "f(x) = e^x/(x^2 + 1)",
            "problem_latex": r"f(x) = \frac{e^x}{x^2 + 1}",
            "solution": "f'(x) = (e^x(x^2 + 1) - 2xe^x)/(x^2 + 1)^2",
            "solution_latex": r"f'(x) = \frac{e^x(x^2 + 1) - 2xe^x}{(x^2 + 1)^2}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 80,
            "problem": "f(x) = ln(x^2 + 2x + 1)",
            "problem_latex": r"f(x) = \ln(x^2 + 2x + 1)",
            "solution": "f'(x) = (2x + 2)/(x^2 + 2x + 1)",
            "solution_latex": r"f'(x) = \frac{2x + 2}{x^2 + 2x + 1}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 81,
            "problem": "f(x) = x^{x^3}",
            "problem_latex": r"f(x) = x^{x^3}",
            "solution": "f'(x) = x^{x^3}(3x^2 ln(x) + x^2)",
            "solution_latex": r"f'(x) = x^{x^3} \left(3x^2 \ln(x) + x^2\right)",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 82,
            "problem": "f(x) = arctan(ln(x)/sqrt(x))",
            "problem_latex": r"f(x) = \arctan\left(\frac{\ln(x)}{\sqrt{x}}\right)",
            "solution": "f'(x) = ((ln(x) + 2) / (x^(3/2))) / (1 + (ln(x)/sqrt(x))^2)",
            "solution_latex": r"f'(x) = \frac{\ln(x) + 2}{x\sqrt{x}(1 + (\ln(x)/\sqrt{x})^2)}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 83,
            "problem": "f(x) = ln(cos(x))^2",
            "problem_latex": r"f(x) = \ln(\cos(x))^2",
            "solution": "-2tan(x)",
            "solution_latex": r"-2\tan(x)",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 84,
            "problem": "f(x) = e^{sin(x)}ln(x)",
            "problem_latex": r"f(x) = e^{\sin(x)}\ln(x)",
            "solution": "f'(x) = e^{sin(x)}ln(x)cos(x) + e^{sin(x)}/x",
            "solution_latex": r"f'(x) = e^{\sin(x)}\ln(x)\cos(x) + \frac{e^{\sin(x)}}{x}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 85,
            "problem": "f(x) = arctan(e^{x ln(x)})",
            "problem_latex": r"f(x) = \arctan(e^{x \ln(x)})",
            "solution": "f'(x) = e^{x ln(x)}(ln(x) + 1) / (1 + e^{2x ln(x)})",
            "solution_latex": r"f'(x) = \frac{e^{x \ln(x)}(\ln(x) + 1)}{1 + e^{2x \ln(x)}}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 86,
            "problem": "f(x) = ln(sin(x^3))",
            "problem_latex": r"f(x) = \ln(\sin(x^3))",
            "solution": "f'(x) = 3x^2cos(x^3)/sin(x^3)",
            "solution_latex": r"f'(x) = \frac{3x^2 \cos(x^3)}{\sin(x^3)}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 87,
            "problem": "f(x) = x^{e^x}",
            "problem_latex": r"f(x) = x^{e^x}",
            "solution": "f'(x) = x^{e^x}(e^x ln(x) + 1/x)",
            "solution_latex": r"f'(x) = x^{e^x}\left(e^x \ln(x) + \frac{1}{x}\right)",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 88,
            "problem": "f(x) = ln(sqrt(tan(x)))",
            "problem_latex": r"f(x) = \ln\left(\sqrt{\tan(x)}\right)",
            "solution": "f'(x) = 1/(2tan(x)cos^2(x))",
            "solution_latex": r"f'(x) = \frac{1}{2 \tan(x)\cos^2(x)}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 89,
            "problem": "f(x) = e^{x^x ln(x)}",
            "problem_latex": r"f(x) = e^{x^x \ln(x)}",
            "solution": "f'(x) = e^{x^x ln(x)}(x^{x-1}(ln(x) + 1) + x^x/x)",
            "solution_latex": r"f'(x) = e^{x^x \ln(x)}\left(x^{x-1}(\ln(x) + 1) + \ln(x)\right)",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 90,
            "problem": "f(x) = ln(ln(sin(x)))",
            "problem_latex": r"f(x) = \ln\left(\ln(\sin(x))\right)",
            "solution": "f'(x) = cot(x)/ln(sin(x))",
            "solution_latex": r"f'(x) = \frac{\cot(x)}{\ln(\sin(x))}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 91,
            "problem": "f(x) = arcsin(e^{x^2})",
            "problem_latex": r"f(x) = \arcsin(e^{x^2})",
            "solution": "f'(x) = 2x e^{x^2}/sqrt(1 - e^{2x^2})",
            "solution_latex": r"f'(x) = \frac{2x e^{x^2}}{\sqrt{1 - e^{2x^2}}}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 92,
            "problem": "f(x) = tan^{-1}(sin(x)/cos(x))",
            "problem_latex": r"f(x) = \tan^{-1}\left(\frac{\sin(x)}{\cos(x)}\right)",
            "solution": "1",
            "solution_latex": r"1",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 93,
            "problem": "f(x) = x^{e^{ln(x)}}",
            "problem_latex": r"f(x) = x^{e^{\ln(x)}}",
            "solution": "f'(x) = x^x(ln(x) + 1)",
            "solution_latex": r"f'(x) = x^x(\ln(x) + 1)",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 94,
            "problem": "f(x) = ln(x^x + x^{2x})",
            "problem_latex": r"f(x) = \ln(x^x + x^{2x})",
            "solution": "f'(x) = (x^{x-1}(ln(x) + 1) + 2x^{2x-1}(ln(x) + 1))/(x^x + x^{2x})",
            "solution_latex": r"f'(x) = \frac{x^{x-1}(\ln(x) + 1) + 2x^{2x-1}(\ln(x) + 1)}{x^x + x^{2x}}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 95,
            "problem": "f(x) = tan(x^2)/ln(x)",
            "problem_latex": r"f(x) = \frac{\tan(x^2)}{\ln(x)}",
            "solution": "(2x sec^2(x^2)ln(x) - tan(x^2)/x)/(ln(x))^2",
            "solution_latex": r"\frac{2x \sec^2(x^2)\ln(x) - \tan(x^2)/x}{(\ln(x))^2}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 96,
            "problem": "f(x) = sqrt(arctan(x^2))",
            "problem_latex": r"f(x) = \sqrt{\tan^{-1}(x^2)}",
            "solution": "2x/((1 + x^4)sqrt(arctan(x^2)))",
            "solution_latex": r"\frac{2x}{\sqrt{\tan^{-1}(x^2)}(1 + x^4)}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 97,
            "problem": "f(x) = ln(arctan(x^3))",
            "problem_latex": r"f(x) = \ln\left(\arctan(x^3)\right)",
            "solution": "f'(x) = 3x^2/(x^6 + 1)",
            "solution_latex": r"f'(x) = \frac{3x^2}{x^6 + 1}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 98,
            "problem": "f(x) = e^{sin(x^2 + 1)}",
            "problem_latex": r"f(x) = e^{\sin(x^2 + 1)}",
            "solution": "f'(x) = 2x cos(x^2 + 1) e^{sin(x^2 + 1)}",
            "solution_latex": r"f'(x) = 2x \cos(x^2 + 1) e^{\sin(x^2 + 1)}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 99,
            "problem": "f(x) = arctan(e^{sin(x)})",
            "problem_latex": r"f(x) = \arctan\left(e^{\sin(x)}\right)",
            "solution": "f'(x) = cos(x)e^{sin(x)}/(1 + e^{2sin(x)})",
            "solution_latex": r"f'(x) = \frac{\cos(x)e^{\sin(x)}}{1 + e^{2\sin(x)}}",
            "topic": "differentiation",
            "difficulty": "ultimate"
        },
        {
            "id": 100,
            "problem": "f(x) = ln(x^{x^x})",
            "problem_latex": r"f(x) = \ln(x^{x^x})",
            "solution": "(x^x(ln(x)+1)/x^x)*ln(x) + x^x(ln(x) + 1)",
            "solution_latex": r"x^x(\ln(x) + 1)\ln(x) + x^{x-1}(\ln(x) + 1)",
            "topic": "differentiation",
            "difficulty": "ultimate"
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