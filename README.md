![Build](https://github.com/kzborisov/MedPall/actions/workflows/ci.yml/badge.svg)
![Coverage](coverage-badge.svg)
![Flake8](flake8-badge.svg)

# MedPall
The goal of the **MedPall** project is to aid medical students
develop their knowledge of diseases and learn to better diagnose patients by creating and learning
flashcards by their liking and looking through a database of diseases with the corresponding symptoms.

## Project Structure
The project consists of several applications:
1. **Home app** - Showing the basic templates (home page, about page, contacts page).
2. **Flashcards app** - The users can create and learn Flashcards created by themselves to best suit their needs.
3. **Disease app** - The users can look through and learn the symptoms of a large database of predefined diseases.
4. **Profiles app** - The users can log in/ sign up for the project.

## Medpall project endpoints

|      **Page**       |                     **Path**                      |
|:-------------------:|:-------------------------------------------------:|
|        Home         |              http://localhost:8000/               |
|        About        |            http://localhost:8000/about            |
|      Contacts       |          http://localhost:8000/contacts           |
|       Sign up       |           http://localhost:8000/sign-up           |
|       Sign in       |           http://localhost:8000/sign-in           |
|      Sign out       |          http://localhost:8000/sign-out           |
|     Flashcards      |         http://localhost:8000/flashcards          |
|  Create flashcards  | http://localhost:8000/flashcards/create-flashcard |
| Practise flashcards |     http://localhost:8000/flashcards/practise     |
| Diseases categories |          http://localhost:8000/diseases           |
| Disease by category |   http://localhost:8000/diseases/category/<pk>    |
|       Disease       |    http://localhost:8000/diseases/disease/<pk>    |
