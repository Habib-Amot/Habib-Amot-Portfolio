import { TodoItem } from "./TodoItem";
import * as inquirer from 'inquirer'

type itemsCount = {
    total: number,
    inCompleted: number
}

export class TodoCollection{
    private nextId: number = 1
    protected itemMap = new Map<number, TodoItem>();
    

    constructor(public username: string = "Unknown", public todoItems: TodoItem[] = []){
        todoItems.forEach(item => this.itemMap.set(item.id, item))
    }

    addTodo(task: string) : number{
        while(this.getTodoById(this.nextId)){
            this.nextId++
        }
        let newTodo = new TodoItem(this.nextId, task)  // creating a new todo Item 
        // this.todoItems.push(newTodo)
        this.itemMap.set(this.nextId, newTodo)
        return this.nextId
    }

    private getTodoById(todoId: number): TodoItem | undefined{
        return this.itemMap.get(todoId)
        // return this.todoItems.find(item => item.id === todoId);
    }

    markComplete(todoId: number){
        let todoItem: TodoItem | undefined = this.getTodoById(todoId)
        if(todoItem){
            todoItem.isCompleted = true;
        }
    }

    getTodoItems(includeCompleted: boolean = false): TodoItem[]{
        return [...this.itemMap.values()].filter(item => includeCompleted || !item.isCompleted)
    }

    printTasks(includeCompleted: boolean = true): void{
        console.log(" ")
        return this.itemMap.values().forEach(item => includeCompleted ? item.printDetails(): !item.isCompleted && item.printDetails())
    }

    // removing completed tasks from the list
    removeCompleted(): void{
        this.itemMap.values().forEach(item => item.isCompleted ? this.itemMap.delete(item.id) : null)
    }

    getitemsCount(): itemsCount{
        return {
            total: this.itemMap.size,
            inCompleted: this.getTodoItems().length
        }
    }
}
