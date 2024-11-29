def newState(thatInput, state):
    nextState = None
    match state:
        case 'A':
            if thatInput == 1:
                nextState = 'B'
            else:
                nextState = 'A'
        case 'B':
            if thatInput == 1:
                nextState = 'C'
            else:
                nextState = 'A'
        case 'C':
            if thatInput == 1:
                nextState = 'C'
            else:
                nextState = 'D'
        case 'D':
            if thatInput == 1:
                nextState = 'B'
            else:
                nextState = 'A'
    return nextState

def output(state):
    outputNum = -1
    match state:
        case 'A':
            outputNum = 0
        case 'B':
            outputNum = 0
        case 'C':
            outputNum = 0
        case 'D':
            outputNum = 1
    return outputNum

def stateMachine(thisInput):
    state = 'A'
    outputString = ''
    for num in range(len(thisInput)):
        outputString += str(output(state))
        print(output(state))
        state = newState(int(thisInput[num]),state)
    return outputString

def main():
    inputString = input('Enter a binary string: ')
    fullOutput = stateMachine(inputString)
    print('The output from this SM is:',fullOutput)

def assertions():
    assert stateMachine('1101') == '0001'
    assert stateMachine('1010') == '0000'
    assert stateMachine('1111') == '0000'
    assert stateMachine('1000') == '0000'
    assert stateMachine('0000') == '0000'
    assert stateMachine('0001') == '0000'
    assert stateMachine('0010') == '0000'
    assert stateMachine('0011') == '0000'
    assert stateMachine('0100') == '0000'
    assert stateMachine('0101') == '0000'
    assert stateMachine('0110') == '0000'
    assert stateMachine('0111') == '0000'
    print('All assertions passed')

if __name__ == "__main__":
    assertions()
    main()

