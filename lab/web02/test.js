// let firstName = "Shukai";
// let lastName = "Hsieh";
// let fullName = firstName + " " + lastName;
// console.log(fullName);
let user = {
  // ...
};

// first, declare
function sayHi() {
  alert("Hello!");
}

// then add as a method
user.sayHi = sayHi;

user.sayHi(); // Hello!
