let val = 5;
const str = "Hello my name is isaaccccc";
//typecast to str
val = String(6666);
val = (6666).toString();
val = (true).toString();
//date to string
val = String(new Date());


//typecast to number
val = Number('5');
val = Number(null);
val = Number(true);

val = parseInt('100');
val = parseFloat('100.30');
console.log(val);
console.log(typeof val);
//console.log(val.length);
console.log(val.toFixed());


//numbers
val = Math.round(3.4);
val = Math.ceil(3.2);
val = Math.floor(3.2);
val = Math.sqrt(3);
val = Math.abs(-2);
val = Math.pow(8,3);
val = Math.min(3, 4, 55, 2, 5, 666);
val = Math.max(3, 4, 55, 2, 5, 666);
val = Math.random(); //random number between 0 - 1. Random decimal
val = Math.floor(Math.random() * 20 + 1); //whole number between 1-20


//string methods
const firstName = "Isaac";
const lastName = "Reyes";


//concat
val = firstName + ' ' + lastName;

//append
val = firstName;
val += lastName;

//length
val = firstName.length;

//change cases
val = firstName.toUpperCase();
val = firstName.toLowerCase();

//indexOf()
val = firstName.indexOf('a');
val = firstName.lastIndexOf('a');

//charAt() val = firstName.charAt(1);
val = firstName.charAt(firstName.length - 1);

//substr
val = firstName.substring(0,4);

//slice -> similar to substring
val = firstName.slice(0,4);
val = firstName.slice(-3); //will start from the back of the string

//split(), splits string into an array based on a separator
val = str.split(' ');

//replace(), old, new
val = str.replace('isaac', "ISAAC");

//includes()
val = str.includes("ISAAC");

const name = "Isaac";
const age = 30;
const job = "None";
const city = "Houston";

//string template
html = `
<ul>
    <li>Name: ${name}</li>
    <li>Age: ${age}</li>
    <li>Job: ${job}</li>
    <li>City: ${city}</li>
</ul>
`;

document.body.innerHTML = html;
//arrays
const numbers = [1, 2, 3 ,4, 5, 6, 7, 9, 10];
const numbers2 = new Array(33, 4, 5, 6);
const fruit = ["apple", "banana", "orange"];
const mixed = [22, "hello", true, new Date(), {a:1, b:1}]


//get length
val = numbers.length;
//check if an array
val = Array.isArray(numbers);
//access elements
val = numbers[2];
//insert to arr
numbers[2] = "potato";
//find index of val
val = numbers.indexOf(44);
//add to end of array
numbers.push(99);
//add to front of array
numbers.unshift(0);
//remove from end of array
numbers.pop();
//remove from front of array
numbers.shift();
//splice values
numbers.splice(0,2)
//reverse
numbers.reverse();
//concat arrays
val = numbers.concat(numbers2);
//sort arrays
val = fruit.sort();
val = numbers.sort();  //doesnt work on numbers.
//sort numbers
val = numbers.sort(function(x,y){return x - y;});
//reverse sort
val = numbers.sort(function(x,y){return y - x;});
//find
function under50(num){return num < 50;}
val = numbers.find(under50);
console.log(numbers);
console.log(val);

//Objects
const person = {
    firstName: "Isaaaaac",
    lastName: "Reyesssss",
    age: 30,
    email: "Thegreatpotatoman@potatomail.com",
    hobbies:["computers", "videogames"], 
    address: {
        city: "houston",
        state: "TX"
    },
    getBirthYear: function(){return 1987;}
}

val = person;
val = person.firstName;  //preferred way
val = person['lastName']; //same as above
val = person.hobbies;
val = person.hobbies[1];
val = person.address.state;
val = person.address['city'];
val = person.getBirthYear();

//array of objects
const people = [
    {name: "John", age: 60},
    {name: "Teresa", age: 33}
];

for(let i = 0; i < people.length; i++)
    console.log(people[i].name);

//dates & times
const today = new Date();   //defaults to current date
let birthday = new Date('9/10/1981');
val = today;

//val = today.toString();

val = birthday;

val = today.getMonth();  //these are 0 based
val = today.getDate();
val = today.getDay();
val = today.getHours();
val = today.getFullYear();
val = today.getMinutes();
val = today.getSeconds();
val = today.getTime();

birthday.setMonth(2);
birthday.setDate(12);
birthday.setFullYear(1933);
birthday.setHours(3);

//switch
const color = "yellow";
switch(color){
    case "red":
        console.log("Color is red");
        break;
    case "blue":
        console.log("Color is blue");
        break;
    default:
        console.log("Color isn't listed chief");
        break;
}

//functions
function greet(firstName = "John", lastName = "Doe"){return "hello " + firstName + " " + lastName;}
console.log(greet("Isaac", "Reyes"));
console.log(greet());

//object functions ->methods
const todo = {
    add: function(){
        console.log("add todo..");
    },
    edit: function(id){
        console.log(`edit todo ${id}`);
    }
}
todo.add();  //calls add function of todo object
todo.edit(99);
//loops
for(let i= 0; i < 10; i++)
    console.log("Number " + i);

//while
let i = 0;
while(i < 5)
{
    console.log(i);
    i++;
}

i = 0;
do {
    console.log(i);
    i++
}
while(i < 5);

//loop array
const cars = ["car1", "car2", "car3","car4"];
for(let i = 0;i < cars.length; i++)
    console.log(cars[i]);

cars.forEach(function(car, index, array){
    console.log(`${index} : ${car}`);
    console.log(array);
});

//map
const users = [
    {id:1, name:"john"},
    {id:2, name: "keke"},
    {id:3, name: "eef"}
];

const ids = users.map(function(user){return user.id;});

const user = {
    firstName: "Jphn",
    lastName: "dooooe",
    age: 44
}

for(let x in user)
    console.log(`${x} : ${user[x]}`);

console.log(val);

























































