const fs = require('fs')

const solve_maze = (maze, fn) => {
    let instruction_pointer = 0
    let step_count = 0
    while (instruction_pointer >= 0 && instruction_pointer < maze.length) {
        step_count++
        const instruction = maze[instruction_pointer]
        const new_instruction = fn(instruction)
        maze[instruction_pointer] = new_instruction
        instruction_pointer += instruction
    }
    return step_count
}

const filedata = fs.readFileSync("input.txt", "utf-8")
const maze = filedata.split('\n').map(x => parseInt(x.trim()))

console.log(solve_maze([...maze], x => x + 1))
console.log(solve_maze([...maze], x => x > 2 ? x - 1 : x + 1))