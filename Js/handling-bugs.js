// this is a class about catching and handling bugs in JS
// first we are goint ot look at the strict mode of js

// even though the counter is not defined, Js is going to make this variable to be a local one and will not complain about the error
// in this case, it is as if the variable is using the var keyword
for(counter = 0; counter < 5; counter++){ 
    console.log(counter)
}

// also we notice that when function is called but not as a method, JS will happily bind the this inside that function to the global variable
// and then exit happily without logging an erro. For example,
function HumanProto(name){
    this.name = name;
}
let person = HumanProto('Habib Amot');  // will not complain even when we did not use the new keyword
console.log(name);  // will log Habib Amot even though it was not defined globally in our code

// to solve this problem, we need to activate the strict mode which we can place either at the top of the file or at the top of our function
function global(){
    'use strict'
    for(index = 0; index < 5; index++){ // will complain now
        console.log(index)
    }

    function HumanProto(name){
        this.name = name;
    }
    let person = HumanProto('Habib Amot');  // will complain without the new keyword
    console.log(name);
}

//          THROWING AND CATCHING OF EXCEPTION
// let's say for example we have a function that takes two numbers and then divide them, we have to catch the exception because we dont know if zero or any other thing aside a number might be passed into the function
// so in this case, we have to catch the exception and then log the problem to the user

function divNum(a, b){
    if(b === 0) throw new Error('ZeroDivision Error')
    return a/b;
}
// this is cause an errow if not wrapped in an exception block
try{
    console.log(divNum(2, 0))
}catch(e){
    console.log(e.message) // gtting the error message iteslf
    console.log(e.stack)  // getting the error and stack trace
}
