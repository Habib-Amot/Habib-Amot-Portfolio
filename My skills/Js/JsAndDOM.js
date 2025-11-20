// using js with DOM, we have access to controlling the document i.e the HTML content of our webpage
// and the binding that gives our script that access and control is the document binding
// the documentElement represents the html tag which is the parent container for other element on the page

let html = document.documentElement
console.log(html);  // this is going to show the entire HTML page and now we have access to traverse the entire webpage

console.log(html.childNodes);  // this is going to show all its nodes elements
let documentBody = document.body;  // accessing the body of the document

// getting the first child of the body even though this is not an actual elemt
let firstChild = documentBody.firstChild;
// and now we can get the node type of the element and log it to the console
console.log(firstChild.nodeType == firstChild.TEXT_NODE);  // logs true since this is a text node

// so how can i get the first actual element node
firstELement = documentBody.children[0];  // children will return the actual element nodes without text or comment nodes
// and now we can log the content of the element to the console
console.log(firstELement.innerHTML);  // the innerHTML attribute will get the content of an element in a string way

//                       finding elements in the DOM
// there are lots of ways to find and query elements in the DOM and these are via:
// document.querySelector, document.querySelectorAll, document.getElementById, document.getElementsByClassName, document.getElementsByTagName
// or via an element itself
// documentBody.querySelector, documentBody.querySelectorAll, documentBody.getElementById, documentBody.getElementsByClassName, documentBody.getElementsByTagName

// for example I can get the first P tag and then query it for all a tag inside it
console.log(documentBody.getElementsByTagName('p')[0].getElementsByTagName('a')[0]);  // will return all p tags in the body then all a tags

// let's say I want to make a query using class names
let pTag = document.getElementsByClassName('first-p')[0]
console.log(pTag)
// and now we can use querySelector to get the 'a' tag inside the p tag
console.log(pTag.querySelector('a'));  // query selector actually allows for use of css style of accessing elements, which makes it very powerful

// we can get all element with the class name of parent and then get the p tag inside them
console.log(document.querySelectorAll('.parent p'))  // returns all p tags inside a parent class name

/*                       CHANGING THE DOM                             */
// let say we want want to remove the last 'p' tag in the DOM

documentBody.removeChild(document.querySelector('body > p:last-of-type'))
// document.querySelector('body > p:last-of-type').remove()
// or we can append to the end of an element
let newP = document.createElement('p')
newP.innerHTML = 'I was inserted by JS';
documentBody.appendChild(newP);

// we can also get the attribute(s) of an element
let passwordInput = documentBody.querySelector('[type=password]')
let passwordToggle = documentBody.querySelector('input[name=password-toggle]');
passwordToggle.addEventListener('click', ()=>{
    // changing the attribute of the input class when the checkbox is being clicked
    passwordInput.setAttribute('type', passwordInput.getAttribute("type") === 'password'?'text':"password");
    // we can also update the classname of an element using either toggle or remove and add method
    passwordInput.classList.toggle('warning')  // adds and remove this class name
});

/*                  LAYOUTS                            */
// there are several different ways in which we can compute the size and positions of an element
// to get the width and height of an element without the border width or height we use: clientHeight, clientWidth
// to get the space taken by an element we use: offsetWidth and offsetHeight properties of the element
// to get the position of an element relative to the viewport, we use getBoundingClientRect property which return an object that has top, bottom, left 
// and right
// to get the position of an element relative to the document, we use pageXOffset and pageYOffset properties of the element
// to get the height and width of the entire document, we can use innerHeight and innerWidth
// for example, to get the space taken without borders of our pTag, I can make use of clientHeight and clientWidth properties
console.log(pTag.clientWidth, pTag.clientHeight);
// to get it's full space
console.log(pTag.offsetWidth, pTag.offsetHeight);

// to get its position relative to the screen
console.log(pTag.getBoundingClientRect().top)
