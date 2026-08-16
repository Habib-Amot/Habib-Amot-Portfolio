"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.TodoCollection = void 0;
const TodoItem_1 = require("./TodoItem");
class TodoCollection {
    username;
    todoItems;
    nextId = 1;
    itemMap = new Map();
    constructor(username = "Unknown", todoItems = []) {
        this.username = username;
        this.todoItems = todoItems;
        todoItems.forEach(item => this.itemMap.set(item.id, item));
    }
    addTodo(task) {
        while (this.getTodoById(this.nextId)) {
            this.nextId++;
        }
        let newTodo = new TodoItem_1.TodoItem(this.nextId, task); // creating a new todo Item 
        // this.todoItems.push(newTodo)
        this.itemMap.set(this.nextId, newTodo);
        return this.nextId;
    }
    getTodoById(todoId) {
        return this.itemMap.get(todoId);
        // return this.todoItems.find(item => item.id === todoId);
    }
    markComplete(todoId) {
        let todoItem = this.getTodoById(todoId);
        if (todoItem) {
            todoItem.isCompleted = true;
        }
    }
    getTodoItems(includeCompleted = false) {
        return [...this.itemMap.values()].filter(item => includeCompleted || !item.isCompleted);
    }
    printTasks(includeCompleted = true) {
        console.log(" ");
        return this.itemMap.values().forEach(item => includeCompleted ? item.printDetails() : !item.isCompleted && item.printDetails());
    }
    // removing completed tasks from the list
    removeCompleted() {
        this.itemMap.values().forEach(item => item.isCompleted ? this.itemMap.delete(item.id) : null);
    }
    getitemsCount() {
        return {
            total: this.itemMap.size,
            inCompleted: this.getTodoItems().length
        };
    }
}
exports.TodoCollection = TodoCollection;
