// Object creation in JS

const { useId } = require("react")

// this is literal way of creating objects in js. This involves using {} braces to denote the object and then pass it the properties that is needed
// for example, here is a car object
let Car = {
    brand: "Mercedes Benz",
    model:"ES 350",
    year: 2024,
    displayInfo: function (){
        // this keyword is a runtime bind argument that get resolved during runtime i.e its value is known when the object is being called
        return `${this.year | this.yearFounded} ${this.brand} ${this.model}` 
    } 
}

let Manufacturer = {
    name: "Benz",
    yearFounded: 1891,
    brand: "Mercedes Benz"

}
// in this case, the this keyword in the displayInfo method will resolve to the Car object
console.log(Car.displayInfo())

// but in this case, the this keyword in the displayInfo() function will resolve to another object
// despite the fact that the displayInfo method is defined inside the Car Object, the this keyword inside it is binded to Manufacturer
console.log(Car.displayInfo.call(Manufacturer))

/*                       METHOD 2                                         */
//Another way of creating objects is through the use of Object.create method
// this method allows for creating an object and passing the object the prototype that we want it to have. for example
let AuthorProto = {

    showInfo: function(){
        return `${this.authorName} is a Native of ${this.nationality} and has written ${this.numberOfBooks} books`
    },

    bookNumber: function() { 
        return this.numberOfBooks
    }
}
// and now I am going to create a new author and then pass it the AuthorProto prototype
let author1 = Object.create(AuthorProto)
author1.authorName = "Habib"
author1.nationality = "Nigeria"
author1.numberOfBooks = 44
console.log(author1.showInfo(), typeof author1.bookNumber())

/*                            METHOD 3                      */
// objects can also be created using function constructor method where a function is being used as a constructor to create objects by using the new keyword
let PersonProto = function(personName, personAge){
    this.name = personName;
    this.age = personAge;
    this.creationTime = new Date(Date.now());
    this.yearOfBirth = new Date(Date.now()).getFullYear() - this.age
}

// using the new keyword to initialize a new object
let person1 = new PersonProto('habib', 24)
console.log(`${person1.name} is ${person1.age} years old and is created at ${person1.creationTime.toUTCString()} ${person1.yearOfBirth}`)

// the way the new keyword works is that,
// 1. a new object is created by js
// 2. then the object prototype is created by passing the prototype of the constructor function 
// 3. the function is then called by passing the obj as it's argument which in turn instantiates the objects properties and methods

/*                        METHOD 4                              */
// the final way by which objects are created is through the use of Class Notation
class Human{
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
    speak(){
        console.log(`my name is ${this.name} and I am ${this.age} years old`)
    }
    /* toString(){
        return `${this.name} : ${this.age}`
    } */
}

let me = new Human('habib', 24)
console.log(me)
me.speak()
// similarly, class notations also work in the same way as using the function method 3 just with a different and more cleaner approach
// the same operations still happens under the hood

//  DEALING AND WORKING WITH MAPS
// maps are just a way to store only keys and values in an object-like form without having to worry about any extra properties that might not be 
// present during the definition of the object
let userInfo = new Map();
userInfo.set('Habib', 34);
userInfo.set('Hassan', 33);
userInfo.set('Hammed', 56);
userInfo.set('Hamza', 44);

console.log(userInfo.get('Habib'))

//                  POLYMORPHISM
// Polymorphism is a way in which an object or class has an interface or method that behaves differently under a particular function or method
// for example the String function when called with any object will look at the toString method of that function and then call it and also return 
// the string of the called function or method
// this behavior allows for creating objects that behaves differently under certain condition
// for example, we can add a toString method to Human class so that it can return a different data when called under the String function

Human.prototype.toString = function(){return `${this.name} : ${this.age}`}
newUser = new Human('Habib', 34);
console.log(String(newUser));
// polymorphism is a powerful concept that allows for a piece of code to work well with another type of code by exposing certain interfaces
// that other codes can plug into


/*                     SYMBOLS                   */
let sym = Symbol('habib')
Array.prototype[sym] = function(){
    return 'i am just a symbol'
}
console.log([1, 2][sym])

// the idea of symbols can be used to create interfaces in classes and this will be used to create a Matrix class for an example
// this matrix takes x and y and then uses this structure to build the matrix value
// this value is passed to the builder function which builds the value inside the content
class Matrix{
    constructor(width, height, builder = (x, y)=> undefined){
        this.matrixWidth = width;
        this.matrixHeight = height;
        this.content = []

        // building the actual content of the matrix
        for(let y = 0; y < this.matrixHeight; y++){  // looping through the height of the matrix
            for(let x = 0; x < this.matrixWidth; x++){  // looping through the actual content of the matrix
                this.content[y * this.matrixWidth + x] = builder(x, y);
            }
        }
    }

    get(x, y){
        return this.content[y * this.matrixWidth + 2];
    }
    set(x, y){
        this.content[y * this.matrixWidth + x] = value;
    }

}



// /*               GETTERS, SETTERS AND STATIC              */
// getters and setters are a way of getting and setting attributes of an object and making them seem like normal attribute value
// for example, using this Farenheit class
class Temperatures{
    constructor(celcius){
        this.celcius = celcius;
    }

    set fahrenheit(newValue){
        this.celcius = (newValue - 32) / 1.8;
    }
    get fahrenheit(){
        return this.celcius * 1.8 + 32
    }

    static fromFahrenheit(value){
        return new Temperatures((value- 32) / 1.8)
    }
}
let temp = new Temperatures(32);
console.log(temp.fahrenheit)
temp.fahrenheit = 43;
console.log(temp.fahrenheit);



/*               INHERITANCE             */
//this is the process in which certain methods or attributes are inherited from parent class
// for example
class LivingOrganism{
    constructor(type, organismClass, specie){
        this.type = type;
        this.organismClass = organismClass;
        this.specie = specie;
    }
}

class Mammal extends LivingOrganism{
    constructor(){
        super('mammal', 'Homo', 'Homo Sapient');
    }
}
let human1 = new Mammal();
console.log(human1.type)


//  Example Practice: Building a sample E-commerce project using classes and related terms
// first I am going to create a product class
class Product{
    constructor(name, price, manufacturer){
        this.name = name;
        this.price = price;
        this.manufacturer = manufacturer;
    }

    applyDiscount(discountPrice){  // in percentage
        this.price = this.price - (discountPrice/100 * this.price)
        console.log(`new price for ${this.name} is ${this.price}`)
    }

    showInfo(){
        console.log(this.name + " is manufactured by " + this.manufacturer + " and is available for "+ this.price)
    }
    toString(){
        return `${this.name} : $${this.price}`
    }
}

class Electronics extends Product{   // inheriting from the Product class
    constructor(name, price, brand, warrantyMonth){
        super(name, price, brand);
        this.warrantyMonth = warrantyMonth;
    }

    showInfo(){  // method overriding
        console.log(`${this.brand} ${this.name} costs $${this.price} with a ${this.warrantyMonth} months guarantee`)
    }
}

class Clothing extends Product{
    constructor(name, price, brand, gender, material, size){
        super(name, price, brand);
        this.gender = gender;
        this.material = material;
        this.size = size;
    }

    displayInfo(){
        console.log(`${this.name} is made from ${this.material} and manufactured by ${this.manufacturer} with a total cost of ${this.price}. Made for ${this.gender}`)
    }
}


// now I am going to create a user class to emulate a user that is shopping in our store
class User{
    constructor(name, age, userType){
        this.name = name;
        this.age = age;
        this.userType = userType;
        this.cart = []
    }

    showItem(){
        console.log(this.cart.map(p => String(p)))
    }
    addItem(item){
        this.cart.push(item)
    }
    getTotalItemPrice(){
        return `total price: $${this.cart.reduce((prevPrice, product) => product.price + prevPrice, 0)}`
    }
}
// now lets create an e-commerce store
class ECommerce{
    constructor(){
        this.products = [
            new Electronics('electric kettle', 30, 'philips', 12),
            new Electronics('refrigerator', 200, 'thermacool', 12),
            new Electronics('standing Fan', 100, 'Binatone', 12),
            new Clothing('Abaya', 290, 'Sariya fashion Store', 'female', 'cotton', 2),       
            new Clothing('Pant Trouser', 209, 'All fashion', 'male', 'cotton', 1),       
            new Clothing('Jean', 129, 'All fash', 'male', 'wool', 9)        
        ]
    }
}
let store = new ECommerce()
let user = new User('habib', 34, 'premium');
user.addItem(store.products[1])
user.addItem(store.products[4])
user.addItem(store.products[2])
user.showItem()
console.log(user.getTotalItemPrice())
