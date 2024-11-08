# AI powered translator

# Import the NLTK library
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
instruction_synonyms = {"INPUT": ['enter', 'type', 'key', 'typeset', 'set' 'keyboard', 'key in', 'record',
                                  'log', 'register', 'write', 'index', 'post', 'insert', 'copy', 'put in',
                                  'list', 'catalog', 'catalogue', 'note', 'document', 'inscribe', 'docket',
                                  'file', 'schedule', 'report', 'chronicle', 'tabulate', 'make an inventory of',
                                  'transcribe', 'mark down', 'commit to paper', 'slate', 'jot down',
                                  'put in writing' 'put on record', 'put down', 'diarize', 'note down',
                                  'detail', 'enroll', 'put down on paper', 'set down', 'take down', 'enrol',
                                  'book', 'show', 'put on file', 'write down', 'enumerate', 'indicate',
                                  'introduce', 'put on paper', 'make a note of', 'minute', 'write in chart',
                                  'inject', 'mark', 'load', 'store', 'capture', 'submit', 'commit', 'feed in code',
                                  'enter data', 'table', 'process', 'type in', 'lodge'],
                        "MULTIPLY": ["multiply", "times"], "OUTPUT": ["output", "print"],
                        "SET": ["set", "assign"], "IF": ["if", "when"], "THEN": ["then", "next"], "ELSE": ["else", "otherwise"],
                        "SELECT": ["select", "choose"], "END": ["end", "finish"], "FOR": ["for", "each"], "REPEAT": ["repeat", "again"],
                        "READ": ["read", "get"], "DO": ["do", "perform"], "WHILE": ["while", "until"]}

def get_synonyms(word):
    synonyms = instruction_synonyms.values()

    return synonyms

def check_synonyms(instruction):
    words = word_tokenize(instruction)
    words = [lemmatizer.lemmatize(word) for word in words]
    code = ""
    for word in words:
        if word in instruction_to_code2:
            code += instruction_to_code2[word] + "\n"
        else:
            synonyms = get_synonyms(word)
            for synonym in synonyms:
                if synonym in instruction_to_code2:
                    code += instruction_to_code2[synonym] + "\n"
    print(code)
    return code

# nltk.download('punkt')

# Read the English instructions from a file
def read_file(file):
    with open(file, 'r') as f:
        data = f.readlines()
    thisQuery = ''
    for i in range(len(data)):
        thisQuery += data[i]
    queries = thisQuery.split("\n\n")
    return queries


# Mapping from English instructions to Python code snippets
instruction_to_code = {
    "INPUT hours worked": "hours = int(input('Enter hours: '))",
    "MULTIPLY hours worked by rate of pay": "pay = hours * rate",
    "OUTPUT pay": "print('Pay:', pay)",
    "SET hours worked to 40": "hours = 40",
    "IF error found": "if error:",
    'THEN OUTPUT "Error"': 'print("Error")',
    'ELSE OUTPUT "All Fine"': 'else:\n\tprint("All Fine")',
    "SELECT VALUE errorNumber": "match errorNumber:",
    '1: OUTPUT "Error Number 1"': 'case 1: print("Error Number 1")',
    '3: OUTPUT "Error Number 3"': 'case 3: print("Error Number 3")',
    '5: OUTPUT "That\'s a bad miss"': 'case 5: print("That\'s a bad miss")',
    "END SELECT": "\n",
    "FOR EACH employee": "for employee in employees:",
    "REPEAT UNTIL no more employee records": "while count < len(Employees):",
    "READ next employee record": "employee = Employees[count]\n\tcount += 1",
    "READ hours worked": "hours = employee.hours",
    "READ pay rate": "rate = employee.rate",
    "MULTIPLY pay rate by hours worked": "pay = hours * rate",
    "DO WHILE more employee records to process": "while count < len(Employees):",
}


# Translate English instructions to Python code
def translate_instructions_to_code(instructions):
    codeCollection = []
    for instruction in instructions:
        # Tokenize the instruction into sentences
        sentences = nltk.sent_tokenize(instruction)
        # Translate each sentence to code
        code = ""
        for sentence in sentences:
            sentence = sentence.split("\n")
            for thisSentence in sentence:
                indented = False
                if thisSentence[:4] == "    ":
                    thisSentence = thisSentence[4:]
                    indented = True
                if thisSentence in instruction_to_code:
                    if indented:
                        code += "\t" + instruction_to_code[thisSentence] + "\n"
                    else:
                        code += instruction_to_code[thisSentence] + "\n"
                else:
                    print(f"Warning: Could not translate instruction: {thisSentence}")

        codeCollection.append(code)
    return codeCollection


def translation_main():
    # Read English instructions from a file using the function read_file()
    data = read_file('Code.txt')

    # Translate instructions to code
    code = translate_instructions_to_code(data)

    # Write the translated code to a new file
    with open("translated_code.py", "w") as file:
        for line in code:
            file.write(line)


if __name__ == "__main__":
    # Read English instructions from a file using the function read_file()
    data = read_file('Code.txt')
    print(data)

    # Translate instructions to code
    code = translate_instructions_to_code(data)
    print("Code:", code)
    for instruction in data:
        code = map_instructions_to_code(instruction)
        print("Code 2:", code)

    # Write the translated code to a new file
    with open("translated_code.py", "w") as file:
        for line in code:
            file.write(line)
