"""Python program that will simulate a state machine,
by taking the input sequence (max 5 length)
and creating the states based on the input sequence.
The output will be the output sequence of the state machine."""

stateNames = ['A', 'B', 'C', 'D', 'E', 'F']

class State:
    def __init__(self, name):
        self.name = name
        self.zero_pointer = None
        self.one_pointer = None

    def printInfo(self):
        print(f"State: {self.name}, 0 -> {self.zero_pointer}, 1 -> {self.one_pointer}")

    def getFromName(self, name):
        if self.name == name:
            return self
        else:
            return None

def newState(thatInput, thisState):
    nextState = None
    stateName = thisState.name
    match stateName:
        case 'A':
            if thatInput == 1:
                nextState = thisState.one_pointer
            else:
                nextState = thisState.zero_pointer
        case 'B':
            if thatInput == 1:
                nextState = thisState.one_pointer
            else:
                nextState = thisState.zero_pointer
        case 'C':
            if thatInput == 1:
                nextState = thisState.one_pointer
            else:
                nextState = thisState.zero_pointer
        case 'D':
            if thatInput == 1:
                nextState = thisState.one_pointer
            else:
                nextState = thisState.zero_pointer
        case 'E':
            if thatInput == 1:
                nextState = thisState.one_pointer
            else:
                nextState = thisState.zero_pointer
        case 'F':
            if thatInput == 1:
                nextState = thisState.one_pointer
            else:
                nextState = thisState.zero_pointer
    return nextState

def output(stateName, inputSequence):
    outputNum = -1
    match stateName:
        case 'A':
            outputNum = 0
        case 'B':
            outputNum = 0 if len(inputSequence) > 1 else 1
        case 'C':
            outputNum = 0 if len(inputSequence) > 2 else 1
        case 'D':
            outputNum = 0 if len(inputSequence) > 3 else 1
        case 'E':
            outputNum = 0 if len(inputSequence) > 4 else 1
        case 'F':
            outputNum = 1
    return outputNum

def traceBackStateZeros(inputSequence, states, currentState):
    nextState = None
    inputs = []
    for i in range(len(inputSequence)):
        inputs.append(inputSequence[i])
    if currentState.name == states[1].name:
        inputs = inputs[:2]
        inputs = inputs[::-1]
        match inputs:
            case ['1', '0']:
                nextState = states[1].name
            case ['1', '1']:
                nextState = states[0].name
            case _:
                nextState = states[0].name
    elif currentState.name == states[2].name:
        inputs = inputs[:3]
        inputs = inputs[::-1]
        match inputs:
            case['1', '0', '0']:
                nextState = states[2].name
            case['1', '0', '1']:
                nextState = states[0].name
            case['1', '1', '0']:
                nextState = states[1].name
            case['1', '1', '1']:
                nextState = states[0].name
            case _:
                nextState = states[1].name
    elif currentState.name == states[3].name:
        inputs = inputs[:4]
        inputs = inputs[::-1]
        match inputs:
            case['1', '0', '0', '0']:
                nextState = states[3].name
            case['1', '0', '0', '1']:
                nextState = states[0].name
            case['1', '0', '1', '0']:
                nextState = states[1].name
            case['1', '0', '1', '1']:
                nextState = states[0].name
            case['1', '1', '0', '0']:
                nextState = states[1].name
            case['1', '1', '0', '1']:
                nextState = states[2].name
            case['1', '1', '1', '0']:
                nextState = states[1].name
            case['1', '1', '1', '1']:
                nextState = states[0].name
            case _:
                nextState = states[2].name
    elif currentState.name == states[4].name:
        inputs = inputs[:5]
        inputs = inputs[::-1]
        match inputs:
            case['1', '0', '0', '0', '0']:
                nextState = states[4].name
            case['1', '0', '0', '0', '1']:
                nextState = states[0].name
            case['1', '0', '0', '1', '0']:
                nextState = states[1].name
            case['1', '0', '0', '1', '1']:
                nextState = states[0].name
            case['1', '0', '1', '0', '0']:
                nextState = states[2].name
            case['1', '0', '1', '0', '1']:
                nextState = states[0].name
            case['1', '0', '1', '1', '0']:
                nextState = states[1].name
            case['1', '0', '1', '1', '1']:
                nextState = states[0].name
            case['1', '1', '0', '0', '0']:
                nextState = states[1].name
            case['1', '1', '0', '0', '1']:
                nextState = states[2].name
            case['1', '1', '0', '1', '0']:
                nextState = states[3].name
            case['1', '0', '0', '0', '1']:
                nextState = states[0].name
            case['1', '1', '1', '0', '0']:
                nextState = states[1].name
            case['1', '1', '1', '0', '1']:
                nextState = states[2].name
            case['1', '1', '1', '1', '0']:
                nextState = states[1].name
            case['1', '1', '1', '1', '1']:
                nextState = states[0].name
            case _:
                nextState = states[3].name
    else:
        nextState = states[0].name
    return nextState

def traceBackStateOnes(inputSequence, states, currentState):
    nextState = None
    inputs = []
    for i in range(len(inputSequence)):
        inputs.append(inputSequence[i])
    if currentState.name == states[1].name:
        inputs = inputs[:2]
        inputs = inputs[::-1]
        match inputs:
            case['0', '1']:
                nextState = states[1].name
            case['0', '0']:
                nextState = states[0].name
            case _:
                nextState = states[0].name
    elif currentState.name == states[2].name:
        inputs = inputs[:3]
        inputs = inputs[::-1]
        match inputs:
            case['0', '1', '1']:
                nextState = states[2].name
            case['0', '1', '0']:
                nextState = states[0].name
            case['0', '0', '1']:
                nextState = states[1].name
            case['0', '0', '0']:
                nextState = states[0].name
            case _:
                nextState = states[1].name
    elif currentState.name == states[3].name:
        inputs = inputs[:4]
        inputs = inputs[::-1]
        match inputs:
            case['0', '1', '1' ,'1']:
                nextState = states[3].name
            case['0', '1', '1', '0']:
                nextState = states[0].name
            case['0', '1', '0' ,'1']:
                nextState = states[1].name
            case['0', '1', '0', '0']:
                nextState = states[0].name
            case['0', '0', '1', '1']:
                nextState = states[1].name
            case['0', '0', '1', '0']:
                nextState = states[2].name
            case['0', '0', '0', '1']:
                nextState = states[1].name
            case['0', '0', '0', '0']:
                nextState = states[0].name
            case _:
                nextState = states[2].name
    elif currentState.name == states[4].name:
        inputs = inputs[:5]
        inputs = inputs[::-1]
        match inputs:
            case['0', '1', '1', '1', '1']:
                nextState = states[4].name
            case['0', '1', '1', '1', '0']:
                nextState = states[0].name
            case['0', '1', '1', '0', '1']:
                nextState = states[1].name
            case['0', '1', '1', '0', '0']:
                nextState = states[0].name
            case['0', '1', '0', '1', '1']:
                nextState = states[2].name
            case['0', '1', '0', '1', '0']:
                nextState = states[0].name
            case['0', '1', '0', '0', '1']:
                nextState = states[1].name
            case['0', '1', '0', '0', '0']:
                nextState = states[0].name
            case['0', '0', '1', '1', '1']:
                nextState = states[1].name
            case['0', '0', '1', '1', '0']:
                nextState = states[2].name
            case['0', '0', '1', '0', '1']:
                nextState = states[3].name
            case['0', '0', '1', '0', '0']:
                nextState = states[0].name
            case['0', '0', '0', '1', '1']:
                nextState = states[1].name
            case['0', '0', '0', '1', '0']:
                nextState = states[2].name
            case['0', '0', '0', '0', '1']:
                nextState = states[1].name
            case['0', '0', '0', '0', '0']:
                nextState = states[0].name
            case _:
                nextState = states[3].name
    else:
        nextState = states[0].name
    return nextState

"""def setFinalStatePointers(inputSequence, states, state):
    newInputZero = inputSequence[1:] + ['0']
    newInputOne = inputSequence[1:] + ['1']
    if len(inputSequence) == 2:
        match inputSequence:
            case '00':
                state.zero_pointer = states[2].name
                state.one_pointer = states[0].name
            case '01':
                state.zero_pointer = states[1].name
                state.one_pointer = states[0].name
            case '10':
                state.zero_pointer = states[0].name
                state.one_pointer = states[1].name
            case '11':
                state.zero_pointer = states[0].name
                state.one_pointer = states[2].name
    elif len(inputSequence) == 3:
        match inputSequence:
            case '000':
                state.zero_pointer = states[3].name
                state.one_pointer = states[0].name
            case '001':
                state.zero_pointer = states[1].name
                state.one_pointer = states[0].name
            case '010':
                state.zero_pointer = states[1].name
                state.one_pointer = states[2].name
            case '011':
                state.zero_pointer = states[1].name
                state.one_pointer = states[0].name
            case '100':
                state.zero_pointer = states[0].name
                state.one_pointer = states[1].name
            case '101':
                state.zero_pointer = states[2].name
                state.one_pointer = states[1].name
            case '110':
                state.zero_pointer = states[0].name
                state.one_pointer = states[1].name
            case '111':
                state.zero_pointer = states[0].name
                state.one_pointer = states[3].name"""

def setFinalStatePointers(inputSequence, states, state):
    zero_pointer = states[0].name
    one_pointer = states[0].name
    if len(inputSequence) == 2:
        if inputSequence == '00':
            zero_pointer = states[2].name
            one_pointer = states[0].name
        elif inputSequence == '01':
            zero_pointer = states[1].name
            one_pointer = states[0].name
        elif inputSequence == '10':
            zero_pointer = states[0].name
            one_pointer = states[1].name
        else:
            zero_pointer = states[0].name
            one_pointer = states[2].name
    else:
        for i in range(len(inputSequence)):
            if inputSequence[i] == '0':
                zero_pointer = states[i+1].name
            else:
                one_pointer = states[i+1].name
    state.zero_pointer = zero_pointer
    state.one_pointer = one_pointer

def finishStates(inputSequence, states):
    for i in range(len(states)-1):
        state = states[i]
        if i == 0:
            state.zero_pointer = states[i+1].name if inputSequence[i] == '0' else states[i].name
            state.one_pointer = states[i+1].name if inputSequence[i] == '1' else states[i].name
        elif i < len(states)-1:
            state.zero_pointer = states[i+1].name if inputSequence[i] == '0' else traceBackStateZeros(inputSequence, states, state)
            state.one_pointer = states[i+1].name if inputSequence[i] == '1' else traceBackStateOnes(inputSequence, states, state)
        else:
            setFinalStatePointers(inputSequence, states, state)
        states[i] = state
    return states

def createState(inputSequence, stateNum, states):
    state = State(stateNames[stateNum])
    for i in range(stateNum):
        if inputSequence[i] == '0':
            state.zero_pointer = states[i + 1].name
            state.one_pointer = states[i].name
        else:
            state.zero_pointer = states[i].name
            state.one_pointer = states[i + 1].name
    state.printInfo()
    return state

def stateMachine(inputString, inputSequence):
    state = State('A')
    outputString = ''
    states = [State('')]*(len(inputSequence)+1)
    for i in range(len(inputSequence)+1):
        state = createState(inputSequence, i, states)
        states[i] = state
    states = finishStates(inputSequence,states)
    stateName = states[0].name
    for num in range(len(inputString)):
        outputString += str(output(stateName, inputSequence))
        thisState = None
        for h in range(len(states)):
            if states[h].name == stateName:
                thisState = states[h]
                break
        stateName = newState(int(inputString[num]),thisState)
    return outputString

def assertions():
    assert stateMachine('1001010010', '10') == '0010010100'
    assert stateMachine('101010', '110') == '000000'
    assert stateMachine('101010', '101') == '000101'
    assert stateMachine('101010', '111') == '000000'
    assert stateMachine('101010100010001', '1000') == '000000000010001'
    assert stateMachine('101010010101', '10101') == '000001000000'
    assert stateMachine('101010010101', '10100') == '000000010000'
    print('All assertions passed')

if __name__ == "__main__":
    inputSequence = ''
    while True:
        inputSequence = input("Enter the input sequence for the state machine (max length 5): ")
        if len(inputSequence) > 5:
            print("Input sequence is too long, please enter a sequence with a maximum length of 5")
        elif len(inputSequence) == 0:
            print("Input sequence is too short, please enter a sequence with a minimum length of 1")
        elif all(c in '01' for c in inputSequence):
            print("Input sequence is valid")
            break
        else:
            print("Please enter a valid input sequence [only 0s and 1s]")
    while True:
        inputString = input("Enter the input string for the state machine: ")
        if all(c in '01' for c in inputString):
            print("Input string is valid")
            break
        else:
            print("Please enter a valid input string [only 0s and 1s]")
    output = stateMachine(inputString, inputSequence)
    print(f"The output sequence of the state machine is: {output}")

