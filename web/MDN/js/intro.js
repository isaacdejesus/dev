//3 ways to declare variables
var potato; //don't use
let potato1; //Only use if need to change value
const potato2 = "Must set value at time of declaration"; //Use whenver possible. Value can not be changed
//TypeOf 
console.log(typeof potato2);
//Data Types
//Number
const  threeDecimalPlaces = 1.28288287.toFixed(3);  //fixes decimal places to 3
//String
const a_String = "Hello, I am a string. What is your name: ";
//String concat
const another_String = "My name is the great potato man."
const a_Concat_String = a_String + another_String;
console.log(a_Concat_String);
//Template string  preferred way to concat strings
const template_String = `${a_String} My name is Isaac`;
console.log(template_String);
//casting to string and to number
const my_String = "123";
const my_Num = Number(my_String);  //casts string to number data type if possible
my_String2 = my_Num.toString();   //casts number to string data type
//length of a string
console.log(a_String.length);
//Checking for substring
a_String.includes("Hello");
//Check if a string starts with or ends with
const browserType = "mozilla";
if(browserType.startsWith("moz"))
    console.log("starts with Moz!");
else if(browserType.endsWith("lla"))
    console.log("Ends with illa");
//Extract substring from a string
console.log(browserType.slice(1,4));
//Changing case
console.log(browserType.toUpperCase());
console.log("HSKSJDKSJ".toLowerCase());
//updating parts of a string
const my_Name = "Hello, my name is Joe";
const my_New_Name = my_Name.replace("Joe", "Isaac");
console.log(`Old contents of string were: ${my_Name}`)
console.log(`New contents of string are: ${my_New_Name}`);

//arrays- Can contain different data types and be nested
const random = ["thre", 188,45, [33, 44, 55]];
//access second array
console.log(random[3][2]);
//get length of array
console.log(`Size of array is: ${random.length}`);
//finding items in array
console.log(`Location of 45 in array is: ${random.indexOf(45)}`); //doesn't seem to work on nested array?
//adding to back of array
random.push(9);
//adding to the front of the array
random.unshift(6);
//remove from end of array
random.pop(); //returns item deleted similar to stacks
//remove from head
random.shift();
//splice allows for removal of item(s) given the index/location
const arr = [1, 2, 3, 4, 5, 6, 7, 8];
console.log(`Original array is: ${arr}`);
const index = arr.indexOf(3);
arr.splice(index, 2); //will start at index and delete 2 items
console.log(`Newly spliced array is: ${arr}`);
//looping through array
for(const items of arr)
    console.log(items);
//standard for loop
for( let i = 0; i< arr.length; i++ ){
    console.log(`I am printing from standard for loop ${arr[i]}`);}
//while
const Cats = ['Pete', 'Biggles', 'Jasmine'];

let myFavoriteCats = 'My cats are called ';

let i = 0;

while (i < Cats.length) {
    if (i === Cats.length - 1) {
            myFavoriteCats += `and ${Cats[i]}.`;
    } else {
            myFavoriteCats += `${Cats[i]}, `;
    }
      i++;
}
console.log(myFavoriteCats);     // "My cats are called Pete, Biggles, and Jasmine."
//do while
MyFavoriteCats = "My cats are called ";
i = 0;
do {
    if (i === Cats.length - 1) {
            myFavoriteCats += `and ${Cats[i]}.`;
    } else {
            myFavoriteCats += `${Cats[i]}, `;
    }
      i++;
} while (i < Cats.length);
console.log(myFavoriteCats);     // "My cats are called Pete, Biggles, and Jasmine."
//
//map() and filter() takes as parameter a function
//Every element of the array if passed to the function.
//Operation is performed on each element and result is stored in a new array
//Map examples
function double (number){return number *2;}
const doubled_Numbers = arr.map(double);
console.log(`Double values of the array are: ${doubled_Numbers}`);
//Another map example
function toUpper(string){return string.toUpperCase();}
const cats = ['Leopard' , 'Serval', 'Jaguar', 'Tiger', 'Caracal' , 'Lion'];
let upperCats = cats.map(toUpper);
console.log(upperCats);
//function above can be rewritten with arrow function
upperCats = cats.map((cat) => cat.toUpperCase());  //allows to define function on call

//filter, filters stuff out
function isLong(city){return city.length > 8;}
const cities = ["London", "Not-London", "Houston", "Liverpool"];
const longer = cities.filter(isLong);
console.log(`Cities with more than 8 chars are: ${longer}`);
//Another filter example
function lcat(cat) {return cat.startsWith('L');}
let filtered = cats.filter(lcat);
//above filter can be compressed with arrow function
filtered = cats.filter((cat) => cat.startsWith('L'));
console.log(filtered);


//converting between strings and arrays
const myData = 'Manchester,London,Liverpool,Birmingham,Leeds,Carlisle';
//suppose we want to split string at ,
const my_arr = myData.split(','); //, is the separator
for( const item of my_arr )
    console.log(item);
//join() allows to revert to string by specifing separator
const dogs = ['rocket', 'Flash', 'Bella', 'Slugger'];
const dogs_string = dogs.join('-');
console.log(dogs_string);
//to_String uses , as separator by default
const dogs_to_string = dogs.toString();
console.log(dogs_to_string);
//split string into array example
const a_str = "Potatoes:6.99";
const a_arr = a_str.split(':');
console.log(`Access first element of new arr: ${a_arr[0]}`);
console.log(`Access second element of new arr: ${a_arr[1]}`);































































































//Functions
function logName(){console.log("my name is the great potato man");}
//invoked using
logName();
