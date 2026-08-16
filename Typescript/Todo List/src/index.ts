import { TodoItem } from "./TodoItem";
import { TodoCollection } from "./TodoCollection";
import inquirer from "inquirer";

let todos: TodoItem[] = [
    new TodoItem(1, "Wash Your clothes"),
    new TodoItem(2, "Make sure to write Typescript and Practice Frontend"),
];

let collections = new TodoCollection("Amot the Dev", todos)
console.log(collections.username, "Todo List")
let newTodo: number = collections.addTodo("Flush the Toilet")

enum Commands {
    Quit = "Quit",
    Add = "Add Task",
    ShowTasks = "Show all Task",
    Toggle = "Show/Hide Completed",
    MarkComplete = "Mark Completed Task",
    RemoveCompleted = "Remove Completed Task"
}

let showCompletedTask: boolean = false


function promptComplete(){
    inquirer.prompt({type:'checkbox', name:'completed tasks', message:"Mark complete Tasks", choices:collections.getTodoItems(false).map(item => ({name:item.task, value:item.id, checked:item.isCompleted})
    )}).then(answer => {
        let completedTasks = answer['completed tasks'] as number[];
        collections.getTodoItems(true).forEach(task => completedTasks.includes(task.id) ? collections.markComplete(task.id) : null)
        promptUser()
    })
}


console.clear()
function promptUser(): void{
    console.log(collections.username, "Todo List")

    inquirer.prompt([{
        type:'select', name:'command', message:`Welcome ${collections.username}, What will you like to do today?:`, choices:Object.values(Commands)
    }]).then(answer => {
        switch(answer["command"]){
            case Commands.Quit:
                promptUser()
                break;
            case Commands.Toggle:
                showCompletedTask = !showCompletedTask;
                promptUser();
                break;
            case Commands.ShowTasks:
                collections.printTasks(showCompletedTask);
                promptUser();
                break;
            case Commands.Add:
                inquirer.prompt({type:'input', name:'Task added', message:"Enter new task:"}).then(answer => {
                    let newTask = answer['Task added']
                    let taskId: number = collections.addTodo(newTask);
                    console.log(`[${taskId}] Task ${newTask} added...!!\n`)
                    promptUser();
                })
                break;
            case Commands.MarkComplete:
                if( collections.getTodoItems(false)){
                    promptComplete()
                }else{
                    promptUser()
                    break;
                }
            case Commands.RemoveCompleted:
                collections.removeCompleted()
                promptUser()
                break;
            default:
                promptUser()

        }
    })
}

promptUser()

// collections.addTodo(5050)   this will cause an error as the data type that is expected by Type script compiler is a string and 
// a number is passed


