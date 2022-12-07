{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNXltYRJG1meDSYOtKLpRWd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MullapudiHarshitha/CD-lab/blob/main/ex10.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "26TaVubzwtxZ",
        "outputId": "71953fd7-3140-4df5-bd22-645e22b6be3a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "INPUT THE EXPRESSION: x=a*b+c\n",
            "PREFIX: +*abc\n",
            "POSTFIX: x=ab*c+\n",
            "### THREE ADDRESS CODE GENERATION ###\n",
            "t1 := a * b\n",
            "t2 := t1 + c\n"
          ]
        }
      ],
      "source": [
        "OPERATORS = set(['+', '-', '*', '/', '(', ')'])\n",
        "PRI = {'+':1, '-':1, '*':2, '/':2}\n",
        "\n",
        "### INFIX ===> POSTFIX ###\n",
        "def infix_to_postfix(formula):\n",
        "    stack = [] # only pop when the coming op has priority \n",
        "    output = ''\n",
        "    for ch in formula:\n",
        "        if ch not in OPERATORS:\n",
        "            output += ch\n",
        "        elif ch == '(':\n",
        "            stack.append('(')\n",
        "        elif ch == ')':\n",
        "            while stack and stack[-1] != '(':\n",
        "                output += stack.pop()\n",
        "            stack.pop() # pop '('\n",
        "        else:\n",
        "            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:\n",
        "                output += stack.pop()\n",
        "            stack.append(ch)\n",
        "    # leftover\n",
        "    while stack: \n",
        "    \toutput += stack.pop()\n",
        "    print(f'POSTFIX: {output}')\n",
        "    return output\n",
        "\n",
        "### INFIX ===> PREFIX ###\n",
        "def infix_to_prefix(formula):\n",
        "    op_stack = []\n",
        "    exp_stack = []\n",
        "    for ch in formula:\n",
        "        if not ch in OPERATORS:\n",
        "            exp_stack.append(ch)\n",
        "        elif ch == '(':\n",
        "            op_stack.append(ch)\n",
        "        elif ch == ')':\n",
        "            while op_stack[-1] != '(':\n",
        "                op = op_stack.pop()\n",
        "                a = exp_stack.pop()\n",
        "                b = exp_stack.pop()\n",
        "                exp_stack.append( op+b+a )\n",
        "            op_stack.pop() # pop '('\n",
        "        else:\n",
        "            while op_stack and op_stack[-1] != '(' and PRI[ch] <= PRI[op_stack[-1]]:\n",
        "                op = op_stack.pop()\n",
        "                a = exp_stack.pop()\n",
        "                b = exp_stack.pop()\n",
        "                exp_stack.append( op+b+a )\n",
        "            op_stack.append(ch)\n",
        "    \n",
        "    # leftover\n",
        "    while op_stack:\n",
        "        op = op_stack.pop()\n",
        "        a = exp_stack.pop()\n",
        "        b = exp_stack.pop()\n",
        "        exp_stack.append( op+b+a )\n",
        "    print(f'PREFIX: {exp_stack[-1]}')\n",
        "    return exp_stack[-1]\n",
        "\n",
        "### THREE ADDRESS CODE GENERATION ###\n",
        "def generate3AC(pos):\n",
        "\tprint(\"### THREE ADDRESS CODE GENERATION ###\")\n",
        "\texp_stack = []\n",
        "\tt = 1\n",
        "\t\n",
        "\tfor i in pos:\n",
        "\t\tif i not in OPERATORS:\n",
        "\t\t\texp_stack.append(i)\n",
        "\t\telse:\n",
        "\t\t\tprint(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')\n",
        "\t\t\texp_stack=exp_stack[:-2]\n",
        "\t\t\texp_stack.append(f't{t}')\n",
        "\t\t\tt+=1\n",
        "\n",
        "expres = input(\"INPUT THE EXPRESSION: \")\n",
        "pre = infix_to_prefix(expres)\n",
        "pos = infix_to_postfix(expres)\n",
        "generate3AC(pos)"
      ]
    }
  ]
}