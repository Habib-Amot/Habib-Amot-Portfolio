let me = {
    name: 'habib',
    23: 'me'
}

for (let value in me) {
    console.log(value);
}
console.log(Array.isArray(me))
console.log(typeof me === 'object')