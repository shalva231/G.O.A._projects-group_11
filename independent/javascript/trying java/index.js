// // console.log("i like watter!!")
// // console.log("its very good")

// // window.alert("i really like watter")



// //this is a comment

// /*

// this 
// is 
// a 
// multiline 
// comment

// */






// // VARIABLES


// // variable is a container for storing data
// // a variable behaves as if it was value that it contains

// // two steps
// // 1. declaration (var, lat, const)
// // 2. assignment  ( = assignment operator)


// let firstname
// firstname = "shalva"

// let age
// age = 20
// age += 1

// let student
// student = true

// console.log("hello" , firstname)
// console.log("you are" , age , "years old")
// console.log("enroled:" , student)


// document.getElementById("p1").innerHTML = "hello " + firstname
// document.getElementById("p2").innerHTML = "you are " + age + " years old"
// document.getElementById("p3").innerHTML = "enroled: " + student




// //  =======================================================
// // programming with mosh
// //  =======================================================


// console.log("hello world");


// let me = "shalva";

// console.log("hello " + me);

// let firstName =  "shalva";
// let lastName = "shubitidze";
// console.log(firstName , lastName)




// const interestRate = 0.3;
// interestRate = 0.4; // this will throw an error
// console.log(interestRate)

// let person = {
//     name: "shalva",
//     age: 20,
// };
// person.name = "john";
// console.log(person.age);

// window.alert("sorry you are only " + person.age + " years old")

// document.getElementById("h1").textContent = person.name;
// document.getElementById("p1").textContent = person.age

// let x;
// x = 20

// if (x > 10) {
//     console.log("x is greater than 10");
// } 
// else {
//     console.log("x is less than or equal to 10");
// }

// let a = 10;

// if (a == 10) {
//     console.log("a is equal to 10");
// }

// let b = "10";

// if (a == b) {
//     console.log("a is equal to b");
// }

// let c = "10";

// if (a === c) {
//     console.log("a is equal to c");
// }


// let price = 10;
// let discount = 2;

// price = price - (price * discount / 100);

// console.log(`you have to pay $${price}`);
// console.log(typeof price);

// if (typeof price == typeof 1) {
//     console.log("price is a number");
//     console.log(price);
// }

// document.getElementById("p1").textContent = person.age;
// document.getElementById("h1").textContent = person.name;



// let person = {
//     name1: "shalva",
//     age1: 20,
//     name2: "gio",
//     age2: 12 
// };
// person.name1 = "john";




// ==============================================================================


// let username;
// username = window.prompt("what is your username? ");
// console.log(username);

let username;
document.getElementById("submit").onclick = function(){
    username = document.getElementById("text").value; 
    console.log(username);
    document.getElementById("h1").textContent = "hello " + username;
}