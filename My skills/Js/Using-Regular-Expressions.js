/* In this class, we are going to be dealing with processing and handling of strings using regular expressions */
let text = `
Hello, my name is John Doe. You can reach me at john.doe@example.com or call +1-202-555-0147.
I placed an order on 2025-11-19 for items costing $49.99 and $120.50.
Visit our website at https://www.example-store.com/products?id=123&ref=chat.
Alternative email: support+help@my-site.org.
Usernames: esh_bee123, Ayo-Dev, test.user99.
deployment time: 01-30-2003 15:20
Postal codes: 90210, 10001-1234.
Random codes: AB-1234, XY_89_2025, #hashtag, @mention, #familyaffairs.
IP addresses: 192.168.0.1, 8.8.8.8.
Times: 12:45 PM, 23:59, 07:05.
Colors: #FF5733, #fff, rgb(255, 0, 153).
abcent
`

// testing a string for a value
let regex = /\d{2}-\d{2}-\d{4} \d{2}:\d{2}/.test(text);  // matching a UTC compliant datetime format
console.log(regex)

// mathcing prices in our text
let pricesRegex = /(\$\d+\.\d{1,2})/
let priceTest = pricesRegex.test(text);  // when + is added to an expression, it means the occurence can happen one or more times
console.log(priceTest)

// extracting part of a string that matches an expression
// while the test method just checks if the string is present or not, the exec method checks and returns information about the matched data
// for exmaple, we might want to get the cost of items in a string
prices = pricesRegex.exec(text);
console.log(prices[0])

// strings also have the match method which works similarly to the exec method
console.log(text.match(pricesRegex)[0]);

// dealing with word boundaries
// word boundries are what separated words: like a space between words or a character between two words
console.log(text.match(/usernames\b.+/i)[0])
// also I can match the ip addresses in the above string
ipAddresses =  text.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g)
console.log(ipAddresses)

// I can also extract every mention and hashtags from the text
console.log(text.match(/\s(?!#[a-fA-F\d]{3}([a-fA-F\d]{3})?)[@#]\w+/g))

// Replacing words using regular expressions
// let's say I want to replace every hyphen (-) with an underscore (_), here is how I can achieve that using regex
newText = text.replace(/-/g, "_")
console.log(newText)

// I can also replace each username in the text with an uppercase version
let updatedUsername = text.replace(/usernames: (\w+[_\-.]\w+\b,?(\s|\b))+/ig, (match, username)=>{
    match =  match.toLowerCase().substring('usernames:'.length, ).trim().split(',')
    match = "Usernames: " + match.map(username=>username.toUpperCase()).join(',')
    return match;
})
console.log(updatedUsername)

