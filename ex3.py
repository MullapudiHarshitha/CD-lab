{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOvUOHWDb3ax0aNqEkRsXKd",
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
        "<a href=\"https://colab.research.google.com/github/MullapudiHarshitha/CD-lab/blob/main/ex3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##Note : This code is direct and indirect left recursion\n",
        "##Some point to notedown for understanding output\n",
        "##  'e' means ϵ (epsalion)\n",
        "## A->[[‘t’,’A'’],[‘b’]] means  A -> tA' | b              \n",
        "##This above note for understanding output \n",
        "\n",
        "\n",
        "gram = {}\n",
        "\n",
        "def add(str):                               #to rules together\n",
        "    str = str.replace(\" \", \"\").replace(\"\t\", \"\").replace(\"\\n\", \"\")\n",
        "    x = str.split(\"->\")\n",
        "    y = x[1]\n",
        "    x.pop()\n",
        "    z = y.split(\"|\")\n",
        "    x.append(z)\n",
        "    gram[x[0]]=x[1]\n",
        "\n",
        "def removeDirectLR(gramA, A):        \n",
        "\t\"\"\"gramA is dictonary\"\"\"\n",
        "\ttemp = gramA[A]\n",
        "\ttempCr = []\n",
        "\ttempInCr = []\n",
        "\tfor i in temp:\n",
        "\t\tif i[0] == A:\n",
        "\t\t\t#tempInCr.append(i[1:])\n",
        "\t\t\ttempInCr.append(i[1:]+[A+\"'\"])\n",
        "\t\telse:\n",
        "\t\t\t#tempCr.append(i)\n",
        "\t\t\ttempCr.append(i+[A+\"'\"])\n",
        "\ttempInCr.append([\"e\"])\n",
        "\tgramA[A] = tempCr\n",
        "\tgramA[A+\"'\"] = tempInCr\n",
        "\treturn gramA\n",
        "\n",
        "\n",
        "def checkForIndirect(gramA, a, ai):\n",
        "\tif ai not in gramA:\n",
        "\t\treturn False \n",
        "\tif a == ai:\n",
        "\t\treturn True\n",
        "\tfor i in gramA[ai]:\n",
        "\t\tif i[0] == ai:\n",
        "\t\t\treturn False\n",
        "\t\tif i[0] in gramA:\n",
        "\t\t\treturn checkForIndirect(gramA, a, i[0])\n",
        "\treturn False\n",
        "\n",
        "def rep(gramA, A):\n",
        "\ttemp = gramA[A]\n",
        "\tnewTemp = []\n",
        "\tfor i in temp:\n",
        "\t\tif checkForIndirect(gramA, A, i[0]):\n",
        "\t\t\tt = []\n",
        "\t\t\tfor k in gramA[i[0]]:\n",
        "\t\t\t\tt=[]\n",
        "\t\t\t\tt+=k\n",
        "\t\t\t\tt+=i[1:]\n",
        "\t\t\t\tnewTemp.append(t)\n",
        "\n",
        "\t\telse:\n",
        "\t\t\tnewTemp.append(i)\n",
        "\tgramA[A] = newTemp\n",
        "\treturn gramA\n",
        "\n",
        "def rem(gram):\n",
        "\tc = 1\n",
        "\tconv = {}\n",
        "\tgramA = {}\n",
        "\trevconv = {}\n",
        "\tfor j in gram:\n",
        "\t\tconv[j] = \"A\"+str(c)\n",
        "\t\tgramA[\"A\"+str(c)] = []\n",
        "\t\tc+=1\n",
        "\n",
        "\tfor i in gram:\n",
        "\t\tfor j in gram[i]:\n",
        "\t\t\ttemp = []\t\n",
        "\t\t\tfor k in j:\n",
        "\t\t\t\tif k in conv:\n",
        "\t\t\t\t\ttemp.append(conv[k])\n",
        "\t\t\t\telse:\n",
        "\t\t\t\t\ttemp.append(k)\n",
        "\t\t\tgramA[conv[i]].append(temp)\n",
        "\n",
        "\n",
        "\t#print(gramA)\n",
        "\tfor i in range(c-1,0,-1):\n",
        "\t\tai = \"A\"+str(i)\n",
        "\t\tfor j in range(0,i):\n",
        "\t\t\taj = gramA[ai][0][0]\n",
        "\t\t\tif ai!=aj :\n",
        "\t\t\t\tif aj in gramA and checkForIndirect(gramA,ai,aj):\n",
        "\t\t\t\t\tgramA = rep(gramA, ai)\n",
        "\n",
        "\tfor i in range(1,c):\n",
        "\t\tai = \"A\"+str(i)\n",
        "\t\tfor j in gramA[ai]:\n",
        "\t\t\tif ai==j[0]:\n",
        "\t\t\t\tgramA = removeDirectLR(gramA, ai)\n",
        "\t\t\t\tbreak\n",
        "\n",
        "\top = {}\n",
        "\tfor i in gramA:\n",
        "\t\ta = str(i)\n",
        "\t\tfor j in conv:\n",
        "\t\t\ta = a.replace(conv[j],j)\n",
        "\t\trevconv[i] = a\n",
        "\n",
        "\tfor i in gramA:\n",
        "\t\tl = []\n",
        "\t\tfor j in gramA[i]:\n",
        "\t\t\tk = []\n",
        "\t\t\tfor m in j:\n",
        "\t\t\t\tif m in revconv:\n",
        "\t\t\t\t\tk.append(m.replace(m,revconv[m]))\n",
        "\t\t\t\telse:\n",
        "\t\t\t\t\tk.append(m)\n",
        "\t\t\tl.append(k)\n",
        "\t\top[revconv[i]] = l\n",
        "\n",
        "\treturn op\n",
        "\n",
        "n = int(input(\"Enter No of Production: \"))\n",
        "for i in range(n):\n",
        "    txt=input()\n",
        "    add(txt)\n",
        "   \n",
        "result = rem(gram)\n",
        "\n",
        "for x,y in result.items():\n",
        "    print(f'{x} -> ', end=\"\")\n",
        "    for index, i in enumerate(y):\n",
        "        for j in i:\n",
        "            print(j, end=\"\")\n",
        "            if (index != len(y) - 1):\n",
        "                print(\" | \", end=\"\")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lIErSdFWrzbV",
        "outputId": "c76b5394-02b1-4e9e-e7d6-9aa78e23002d"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter No of Production: 6\n",
            "E->E+T\n",
            "E->T\n",
            "T->T*F\n",
            "T->F\n",
            "F->(E)\n",
            "F->id\n",
            "E -> T\n",
            "T -> F\n",
            "F -> id\n"
          ]
        }
      ]
    }
  ]
}