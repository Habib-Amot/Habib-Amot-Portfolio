/*
Our project is to build an automaton, a little program that performs a task in a virtual world. Our automaton will be a mail
delivery robot picking up and dropping off parcels. 
 */

// first I will create a list of road definition which shows how each road is connected to each other in the Village
let roads = [
    "Alice's House-Bob's House",   "Alice's House-Cabin",
    "Alice's House-Post Office",   "Bob's House-Town Hall",
    "Daria's House-Ernie's House", "Daria's House-Town Hall",
    "Ernie's House-Grete's House", "Grete's House-Farm",
    "Grete's House-Shop",          "Marketplace-Post Office",
    "Marketplace-Town Hall",       "Marketplace-Farm",
    "Marketplace-Shop",            "Shop-Town Hall"
]

// now I am going to create a graph from the list of roads, and what I am going to do is to create a map such that we define where
// we can get to from a particular place or road
function createMap(roads){
    // creating an object that has not prototype so that we don't mess things up later while accessing properties
    let map = Object.create(null);

    function addEdge(from, to){
        if(map[from] == null){
            map[from] = [to];
        }else{
            map[from].push(to);
        }
    }
    for([from, to] of roads.map(road => road.split('-'))){
        addEdge(from, to);
        addEdge(to, from)
    }
    return map;
}

const roadGraph = createMap(roads);  // returning the map of roads and how they are interconnected
console.log(Object.keys(roadGraph))
