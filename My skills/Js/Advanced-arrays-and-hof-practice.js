// given an array of transactions containing id, amount and category, each transaction has a date and amount
let transactions = [
    { id: 1, amount: 100, category: 'food', date: '2023-01-01' },
    { id: 2, amount: 50, category: 'transport', date: '2023-01-02' },
    { id: 3, amount: 200, category: 'entertainment', date: '2023-01-03' },
    { id: 4, amount: 150, category: 'food', date: '2023-01-04' },
    { id: 5, amount: 75, category: 'transport', date: '2023-01-05' },
    { id: 6, amount: 300, category: 'entertainment', date: '2023-01-06' },
    { id: 7, amount: 120, category: 'food', date: '2023-01-07' },
    { id: 8, amount: 80, category: 'transport', date: '2023-01-08' },
    { id: 9, amount: 250, category: 'entertainment', date: '2023-01-09' },
    { id: 10, amount: 90, category: 'food', date: '2023-01-10' }
]

// 1. calculating the amount spent in each category
function calculateCategorySpending(transactions){
    let categorySpending = {};
    // first we need to make sure that the transactions is an object
    if(!Array.isArray(transactions)){
        throw new Error("transactions should be an array");
    }else{
        transactions.forEach(transaction =>{
            if(!transaction.category || transaction.amount  === undefined){
                throw new Error("transaction should have a category and amount");
            }else{
                categorySpending[transaction.category] ? categorySpending[transaction.category] += transaction.amount : categorySpending[transaction.category] = transaction.amount;
            }
            
        })
    }
    return categorySpending;
}
console.log(calculateCategorySpending(transactions));

// finding the category with the highest spending
function highestSpendingCategory(transactions){
    let categorySpending = calculateCategorySpending(transactions);
    let highestSpendingCategory = Object.keys(categorySpending).reduce((a, b) => categorySpending[a] > categorySpending[b] ? a : b);
    return `${highestSpendingCategory} has the highest spending of $${categorySpending[highestSpendingCategory]}`;
}
console.log(highestSpendingCategory(transactions));

// building a function that flattens an array of arrays
let nestedArray = [0,[1, 2, 3], [4, 5], [6, [7, 8]], [9], [10, [11, 12, 13, 14, [15, 16]]]];
function flatten(array){
    let flatArray = [];
    for(value of array){
        if(Array.isArray(value)){
            flatArray = flatArray.concat(flatten(value));
        }else{
            flatArray.push(value);
        }
    }
    return flatArray;
}
console.log(flatten(nestedArray));

// building a function that traverse a nested object and finds all value for a given object
let data = {
    company: {
        name: "AmotTech",
        id: 1,
        building: {
            id: 1,
            name: "AmotTech Building",
            department1: {
                id: 1,
                name: "AmotTech Department",
                employees: [
                    { id: 1, name: "John", age: 25 },
                    { id: 2, name: "Jane", age: 35 }
                ]
            },
            department2: {
                id: 2,
                name: "AmotTech Department",
                employees: [
                    { id: 3, name: "Bob", age: 35 },
                    { id: 4, name: "Alice", age: 25 }
                ]
            }

        }
    }
}

function getIDs(array, id){

    let IDs = [];
    if((!Array.isArray(array)) && typeof array === 'object'){
        for(key in array){
            if(id === key){
                IDs.push(array[key])
            }else if(typeof array[key] === 'object'){
                IDs.push(getIDs(array[key], id))

            }else{
                continue;
            }
        }
    }
    else if(Array.isArray(array)){
        array.forEach(array => {
            if(getIDs(array, id) == undefined){
                return ''
            }else{
                IDs.push(getIDs(array[key], id))
            }
        })
    }else{
        return 
    }
    return(IDs.length > 0 ? IDs : '');
}
console.log(getIDs(data, 'id'))
 

