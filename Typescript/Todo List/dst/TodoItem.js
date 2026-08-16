"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.TodoItem = void 0;
class TodoItem {
    id;
    task;
    isCompleted;
    constructor(id, task, isCompleted = false) {
        this.id = id;
        this.task = task;
        this.isCompleted = isCompleted;
        this.id = id;
        this.task = task;
        this.isCompleted = isCompleted;
    }
    printDetails() {
        console.log(`[${this.id}] \t ${this.task} => \t\t ${this.isCompleted ? "completed" : "not completed"}`);
    }
}
exports.TodoItem = TodoItem;
