"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const TodoItem_1 = require("./TodoItem");
const TodoCollection_1 = require("./TodoCollection");
const inquirer_1 = require("inquirer");
let todos = [
    new TodoItem_1.TodoItem(1, "Wash Your clothes"),
    new TodoItem_1.TodoItem(2, "Make sure to write Typescript and Practice Frontend"),
];
let collections = new TodoCollection_1.TodoCollection("Amot the Dev", todos);
console.log(collections.username, "Todo List");
let newTodo = collections.addTodo("Flush the Toilet");
var Commands;
(function (Commands) {
    Commands["Quit"] = "Quit";
    Commands["Add"] = "Add Task";
    Commands["ShowTasks"] = "Show all Task";
    Commands["Toggle"] = "Show/Hide Completed";
    Commands["MarkComplete"] = "Mark Completed Task";
    Commands["RemoveCompleted"] = "Remove Completed Task";
})(Commands || (Commands = {}));
let showCompletedTask = false;
function promptComplete() {
    inquirer_1.default.prompt({ type: 'checkbox', name: 'completed tasks', message: "Mark complete Tasks", choices: collections.getTodoItems(false).map(item => ({ name: item.task, value: item.id, checked: item.isCompleted })) }).then(answer => {
        let completedTasks = answer['completed tasks'];
        collections.getTodoItems(true).forEach(task => completedTasks.includes(task.id) ? collections.markComplete(task.id) : null);
        promptUser();
    });
}
console.clear();
function promptUser() {
    console.log(collections.username, "Todo List");
    inquirer_1.default.prompt([{
            type: 'select', name: 'command', message: `Welcome ${collections.username}, What will you like to do today?:`, choices: Object.values(Commands)
        }]).then(answer => {
        switch (answer["command"]) {
            case Commands.Quit:
                promptUser();
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
                inquirer_1.default.prompt({ type: 'input', name: 'Task added', message: "Enter new task:" }).then(answer => {
                    let newTask = answer['Task added'];
                    let taskId = collections.addTodo(newTask);
                    console.log(`[${taskId}] Task ${newTask} added...!!\n`);
                    promptUser();
                });
                break;
            case Commands.MarkComplete:
                if (collections.getTodoItems(false)) {
                    promptComplete();
                }
                else {
                    promptUser();
                    break;
                }
            case Commands.RemoveCompleted:
                collections.removeCompleted();
                promptUser();
                break;
            default:
                promptUser();
        }
    });
}
promptUser();
// collections.addTodo(5050)   this will cause an error as the data type that is expected by Type script compiler is a string and 
// a number is passed
