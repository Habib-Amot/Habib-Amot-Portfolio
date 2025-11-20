/*  In a synchronous programming model, things happen one at a time. When you call a function that performs a long-running action, it returns
 only when the action has finished and it can return the result. This stops your program for the time the action takes.An asynchronous model allows multiple things to happen at the same time. When you start an action, your program continues to run. When the action finishes, the program is informed and gets access to the result
 (for example, the data read from disk).
*/



let action = new Promise((resolve, reject )=>{
    var resolved = false;
    setTimeout(()=>{
        resolved = 55;
        resolve(resolved)
        console.log("hello world")
    }, 3000);


})

/* / the above operation can also be achieved with the use of async/await call, for example
async function apiCall(){
    console.log('this is just going to work regardless before we call await')
    let names = await XMLHttpRequest();
} */
action.then(value=>value * 5).then(value=>{console.log(value)})
console.log(" I will keep runnig even if the asynchronous activity is not yet done")
