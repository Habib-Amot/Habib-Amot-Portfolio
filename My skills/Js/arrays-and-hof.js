// operation 1: finding the sum of all elements in an array
let array = [1, 2, 3, 4, 5];
let sum =  array.reduce((initial_value, current_value) => initial_value + current_value, 0);
console.log("Sum of all elements in the array: " + sum);

// operation 2: working with objects, finding all books that are published after a given year, extracting all author's name and counnting how many books the author has written
let books = [
    { title: "Book 1", author: "Author A", year: 2000 },
    { title: "Book 2", author: "Author B", year: 2005 },
    { title: "Book 3", author: "Author A", year: 2010 },
    { title: "Book 4", author: "Author C", year: 2015 },
    { title: "Book 5", author: "Author B", year: 2020 }
];
// finding all books that are published after a given year
function findBooksPublishedAfterYear(books, year) {
    let booksPublishedAfterYear = books.filter(book => book.year > year);
    return booksPublishedAfterYear.length > 0 ? booksPublishedAfterYear : [];
}
console.log(findBooksPublishedAfterYear(books, 2010));

// extracting all author's name and counting how many books the author has written
function getAuthorNames(book){
    let authorNames = []
    book.forEach(book => {
        if(!authorNames.includes(book.author)){
            authorNames.push(book.author);
        }
    })
    return authorNames
}
console.log(getAuthorNames(books));
// counting how many books the author has written
function countAuthorsBooks(books){
    let authorBooksCount = {};
    books.forEach(book => {
        if(authorBooksCount[book.author]){
            authorBooksCount[book.author]++;
        }else{
            authorBooksCount[book.author] = 1;
        }
    })
    return authorBooksCount;
}
console.log(countAuthorsBooks(books));

//operation 3: converting an array of temperatures in Celsius to Fahrenheit
let celsiusTemperatures = [0, 20, 37, 100];
function convertCelsiusToFahrenheit(celsiusTemperatures) {
    let FahrenheitTemperatures = celsiusTemperatures.map(temp => (temp * 9/5) + 32);
    return FahrenheitTemperatures;
}
console.log("Celsius Temperatures: ",  celsiusTemperatures);
console.log("Fahrenheit Temperatures: ", convertCelsiusToFahrenheit(celsiusTemperatures));

// operation 4: given an array of 10 people with name, age and salary
people = [
    { name: "John", age: 25, salary: 50000 },
    { name: "Jane", age: 30, salary: 60000 },
    { name: "Bob", age: 35, salary: 70000 },
    { name: "Alice", age: 28, salary: 80000 },
    { name: "Tom", age: 40, salary: 90000 },
    { name: "Jerry", age: 22, salary: 55000 },
    { name: "Sara", age: 27, salary: 65000 },
    { name: "Mike", age: 32, salary: 75000 },
    { name: "Emma", age: 29, salary: 85000 },
    { name: "Chris", age: 38, salary: 95000 }
]
// increasing each person's salary by 10%
function increaseSalaryBy10_Percent(people){
    if(!typeof people === 'object'){
        console.log('please pass in an array of people')
    }else{
        return people.map(person => {
            let personSalary = person.salary;
            person.salary += Math.floor((10/100)*personSalary)
            return person
        })
    }
}
console.log(increaseSalaryBy10_Percent(people))