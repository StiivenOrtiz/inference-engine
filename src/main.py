from inference.refutation import refutation

import sys

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        first_line = file.readline().strip()
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return first_line, lines

def main():
    if len(sys.argv) < 2:
        print("Please provide a file as an argument.")
        print("Use: python main.py file.txt")
        return
    file_name = sys.argv[1]

    question, axioms = read_file(file_name)
    
    print("_______________________________________   _______________________________________")
    print(" |                        |            \\|/            |                        |")
    print(" |->->->->->->->->->->->->|WELCOME TO INFERENCE ENGINE|<-<-<-<-<-<-<-<-<-<-<-<-|")
    print("_|________________________|____________/|\\____________|________________________|_\n\n")

    print("|---------------------------------\\/---/\\---\\/---------------------------------|")
    print("|---------------------------------\\/|Axioms|\\/---------------------------------|")
    print("|---------------------------------\\/---\\/---\\/---------------------------------|\n")
    for i in range(len(axioms)):
        print(str(i + 1) + ". " + axioms[i])
    print("\n|--------------------------------\\/----/\\----\\/--------------------------------|")
    print("|--------------------------------\\/|Question|\\/--------------------------------|")
    print("|--------------------------------\\/----\\/----\\/--------------------------------|\n")
    print(f"-> ¿{question}?\n")
    print("\n|---------------------------------\\/---/\\---\\/---------------------------------|")
    print("|---------------------------------\\/|Result|\\/---------------------------------|")
    print("|---------------------------------\\/---\\/---\\/---------------------------------|\n")

    if (refutation(axioms, question)):
        print("\n-> The sentence is true\n")
    else:
        print("\n-> The sentence is false\n")

    print("|---------------------------------\\/---\\/---\\/---------------------------------|\n")

if __name__ == "__main__":
    main()
