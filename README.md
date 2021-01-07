# Yatzy

> In this repository you'll wind the refactor of a **Christamas Kata** called Yatzy. This project has been designed for the Web _Development students_ of the first year. The goal of thsi Christmas kata is try to detect different code smells and try to make an effective and powerful refactoring.

## Table of Contents

1. [Motivation](#motivation)
1. [Used Technologies](#used-technologies)
1. [Content](#Content)
1. [Reflections](#reflections)
1. [License](#license)

---

## Motivation

This project motivation is try to test all the learning that we have done since we started the course of _Web Development_. In this we will find non conventional and bad coding routines that we should be able to detect and correct.

---

**[⬆ back to top](#table-of-contents)**

## Used Technologies

- Python
- Pytest
- MarkDown
- Github

---

**[⬆ back to top](#table-of-contents)**

## Content

> The content of this project it's separed into two different directories **Domain** and **Resources**.

### Domain

In this direcotry we will find that it's subdivided into another two, **src** and **test**.

- **src**

Inside _src_ we have the main program that alredy has been refactorized and is the completely functional.

---

- **test**

Inside _test_ we have all the test cases that have been built to check the functionality of the program and if it runs correctly following the rules of the Yatzy.

### Resources

The directory of _resources_ how it tells the name has been built to keep all the external resources to the Yatzy program, in it we will find:

---

###### How to play Yatzy

In this document we have the rules of Yatzy in case we have never played before and we don't know how it works the logic of the game. It will have a clear explanation relationed with the program we built to help the user to understand how the program and test cases works.

---

###### Yatzy Code Smells

In this docuemnt we will find an original copy of the program of the game of Yatzy. We keep it to give the user a clue about how this kata should be resolved and because our teacher has asked if we can write down somwhere all the code smells we have been able to find in the original program. In this document we wrote all the code smells that we could find on the top of each function that conforms the yatzy program.

---

###### Yatzy Explained

This document have all the functions explained minutely one by one, in case any user is not able to understand the code that conforms the yatzy program game.

**[⬆ back to top](#table-of-contents)**

## Reflections

> Now we proceed to explain the reflections we went writing down through while we were solving the kata.

###### How much duplicated code is in your solution ? And in your test cases ?

The code of my solution i think is well implemented, is true that most of the functions makes it's purpose but the functions that try to get just the sumative of the count of the dice number could be implemented in just one function because the code has been duplicated to each function that operates for each number that could be in a dice face. And comeback to happen the same on the functions that are similar to each other like _two_pair_, _three_of_a_kind_ or _four_of_a_kind_. We kept it separated because following the rules of Yatzy i think should be differenciated from the others acting like separated actions that a user can choose depending of the result of the dices and the elections that has left and him/her has made before.

Respect to the test cases, we refactor them until we didn't had duplicated long code and finally we added a few more that we thought could break the game program.

---

###### Did you write a list of test cases before start ?

Yes. For this kata we followed the methodology of TDD (Test-Drive-Development) first of all we refactor the actual test cases we have and we added a few more trying to break the program or trying to find a bug in it. After that we proceed to refactor and improve the Yatzy game program.

---

###### How did you decide the order in wich to implement the test cases ?

We decide to follow the order of the functions to implement the different test cases and an organization on them. The game program starts checking for a chance and a Yatzy, followed the account of the numbers that we can find in the six faces of a dice, this ones will be our first functions to test and therefore this ones will be our first test cases. We continue with the next more difficult rules to the most sophisticated rules like could be the _full_house_ function.

---

**[⬆ back to top](#table-of-contents)**

## License

MIT License

Copyright (c) 2020 AntoniPizarro and Pau Llinàs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

**[⬆ back to top](#table-of-contents)**
