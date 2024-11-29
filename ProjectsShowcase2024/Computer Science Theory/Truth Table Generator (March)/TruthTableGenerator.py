#Truth table generator for boolean circuits [1 gate only]
class TruthTableGenerator:
    def __init__(self):
        self.gates = ["AND", "OR", "XOR", "NOR", "NAND"]
        self.inputs = [0, 1]
        self.inputVariables = []
        self.truthTableInputs = [[0,0], [0,1], [1,0], [1,1]]
        self.truthTableResults = []
        self.gate = ""

    def getInputVariables(self):
        moreVariables = True
        while moreVariables:
            variable = input("Enter an input variable name: ")
            self.inputVariables.append(variable)
            continueLoop = input("Are there more variables (Y/N)? ")
            if continueLoop.upper() == "Y":
                moreVariables = True
            else:
                moreVariables = False

    def getGateInput(self):
        gateInput = ""
        while gateInput.upper() not in self.gates:
            gateInput = input("Enter gate: ")
            if gateInput.upper() == "NOT":
                break
        return gateInput.upper()

    def generate_truth_table(self, num_variables):
        # Initialize the truth table
        truth_table = []

        # Generate all possible combinations of inputs
        for i in range(2**num_variables):
            # Convert the current combination to binary and pad it with zeros to get the full number of variables
            row = list(bin(i)[2:].zfill(num_variables))
            # Convert the binary string to a list of integers
            row = [int(bit) for bit in row]
            # Append the row to the truth table
            truth_table.append(row)

        return truth_table

    def calculate_gate_output(self, gate, truth_table):
        output = []
        for row in truth_table:
            if gate == "AND":
                result = all(row)
            elif gate == "OR":
                result = any(row)
            elif gate == "XOR":
                result = row.count(1) % 2 == 1
            elif gate == "NOR":
                result = not any(row)
            elif gate == "NAND":
                result = not all(row)
            else:
                if row[0] == 0:
                    result = 1
                else:
                    result = 0
            output.append(int(result))
        return output

    def displayTruthTable(self):
        print("-"*30)
        print("\nTruth Table for", self.gate, "gate: \n")
        truthTable = []
        for row in self.truthTableInputs:
            truthTable.append(row + [self.truthTableResults[self.truthTableInputs.index(row)]])
        for item in self.inputVariables:
            print(item, end="|")
        print("R|")
        print("--"*len(self.inputVariables)+"-")
        for item in truthTable:
            for i in item:
                print(i, end="|")
            print("")
    
    def main(self):
        self.gate = self.getGateInput()
        self.getInputVariables()
        while self.gate.upper() != "NOT" and len(self.inputVariables) < 2:
            print("You need at least 2 input variables for this gate")
            self.inputVariables = []
            self.getInputVariables()
        self.truthTableInputs = self.generate_truth_table(len(self.inputVariables))
        self.truthTableResults = self.calculate_gate_output(self.gate, self.truthTableInputs)
        self.displayTruthTable()

if __name__ == "__main__":
    ttg = TruthTableGenerator()
    ttg.main()
		
