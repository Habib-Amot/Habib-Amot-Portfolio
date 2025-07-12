// Object creation in JS
let Car = {
    brand: "Mercedes Benz",
    model:"ES 350",
    year: 2024,
    displayInfo: function (){
        console.log(`${this.year} ${this.brand} ${this.model}`)
    } 
}
console.log(Car.displayInfo())

