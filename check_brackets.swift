import Foundation

func checkBrackets(string: String) -> Int {
    let length: Int = string.count
    if length == 0 {return -1}
    
    let brackets: [Character: Character] = ["]":"[",")":"(","}":"{"]
    var stack: [stackElement] = []
    struct stackElement {
        var char: Character
        var index: Int 
    }

    for index in 1...length {
        var char = string[string.index(string.startIndex, offsetBy: index-1)]
        if brackets.values.contains(char) {stack.append(stackElement(char: char,index: index))}
        if brackets.keys.contains(char) {
            if stack.isEmpty {return index}
            if brackets[char] != stack.removeLast().char {return index}
        }
    }
    
    if !stack.isEmpty {return(stack.removeLast().index)}
    return -1
}
