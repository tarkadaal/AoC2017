use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").unwrap();
    let maze: Vec<i32> = contents
        .lines()
        .map(|line| line.trim().parse())
        .filter(|result| result.is_ok())
        .map(|some| some.unwrap())
        .collect();

    
    // print step count
    println!("Completed in {} steps.", solve_maze( maze.clone(), |x| x + 1));
    println!("Completed in {} steps.", solve_maze( maze.clone(), |x| if x>2 {x-1} else {x+1}));
}

fn solve_maze<F>(mut maze: Vec<i32>, alter_instruction: F) -> u32 where
    F: Fn(i32) -> i32
{
    let mut instruction_pointer = 0;
    let mut step_count = 0;
    // while in maze
    while instruction_pointer < maze.len() as i32 {
        step_count += 1;
        let instruction = maze[instruction_pointer as usize];
        let new_instruction = alter_instruction(instruction);
        maze[instruction_pointer as usize] = new_instruction;
        instruction_pointer += instruction as i32;
    }
    step_count
}