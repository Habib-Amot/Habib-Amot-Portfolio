/* Event Handling in the browser is the process in which an element on our webpage responds to certain event that is either triggered by the user
or by the browser. This allows for certain operations to take place during the occurence of an event
 */

// for example, we can get the first heading of our webpage and then attach some events to it
let firstH1 = document.body.children[0];
// and now we can attach some events to it
firstH1.addEventListener('mousedown', (e)=>{ // listening for a click event on the element
    firstH1.style.color = "red";  // changing the color of the H1 tag once it is clicked
    e.preventDefault()
});

// each event handler is passed an event object which holds additional information about the event that is being triggered
// the event object contains different information depending on the event that is being triggered. for example, a mousedown event
firstH1.addEventListener('mousedown', (e)=>{
    if(e.button == 0){
        firstH1.style.fontSize = '40px';
    }else if(e.button == 2){
        console.log("you right clicked on the heading tag")
        e.stopPropagation();
    }
})
// we can use this to prevent users from accessing the context menu of our webpage
document.addEventListener('contextmenu', (e)=>{
    e.preventDefault();  // preventing users from right clicking the web page
})

// using the mousedown and mousemove event to pick an element and then move it around on the screen until it is being released
function handleH1MouseMove(e, removeEvent=false){
    if(!removeEvent){
        let colors = ['red', 'green', 'brown']
        firstH1.style.color = colors[Math.floor(Math.random() * 3) - 1]
    }else{
        firstH1.removeEventListener('mousemove', handleH1MouseMove)
    }
}
firstH1.addEventListener('mouseenter', (e)=>{
    firstH1.addEventListener('mousemove', handleH1MouseMove);
});
firstH1.addEventListener('mouseout', handleH1MouseMove)

// Making a dot on every click that happens in the document
document.addEventListener('click', (e)=>{
    let dot = document.createElement('div');
    dot.style.position = 'absolute';
    dot.style.top = e.clientY + 'px';
    dot.style.left = e.clientX + 'px';
    dot.classList.add('dot');
    document.body.appendChild(dot);
})

// listening for Key events
// we can also create key combinations to perform some powerful actions in our website
// changing the background of our document by pressing Ctrl + b
document.addEventListener('keydown', (e)=>{
    if(e.key == 'b' && e.ctrlKey){
        document.body.style.backgroundColor = "red";
    }
});
// also we can listen for several keys being pressed at the same time
document.addEventListener('keydown', (e)=>{
    if(e.key == 'r' && e.ctrlKey && e.shiftKey){
        console.log(e.code)
        document.body.style.backgroundColor = 'white';
    }
})

// there are also some form events that we can listen for and also handle
let form = document.forms[0];
form.addEventListener('submit', (e)=>{
    let usernameField = form.querySelector('input[name=username]');
    console.log(usernameField.value)
    e.preventDefault()
})

// handling scroll events
// lets create an element that is going to be long enough to make the window height to overflow
let longText = document.createElement('p');
longText.innerHTML = 'super long and gigantic text'.repeat(1000)
documentBody.appendChild(longText)

let scrollBar = document.createElement('div');
scrollBar.style.position = 'fixed';
scrollBar.style.top = '0px';
scrollBar.style.left = '0px';
scrollBar.style.backgroundColor = 'purple';
scrollBar.style.height = '4px';
documentBody.appendChild(scrollBar);
// now I am going to add a scroll event to our window
window.addEventListener('scroll', ()=>{
    let max = documentBody.scrollHeight - innerHeight;
    scrollBar.style.width = ((pageYOffset / max) * 100) + '%';
})