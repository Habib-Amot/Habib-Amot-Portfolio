export class TodoItem{
    constructor(public id: number, public task: string, public isCompleted: boolean = false){
        this.id = id;
        this.task = task;
        this.isCompleted = isCompleted;
    }

    printDetails(){
        console.log(`[${this.id}] \t ${this.task} => \t\t ${this.isCompleted ? "completed" : "not completed"}`)
    }
}
