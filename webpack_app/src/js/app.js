//alert(require('./people.js'));


// let obj = require('./people.js');
// alert("Hi");
// console.log(obj[0]);



let people = require('./people.js')
let $ = require('jquery')
require('../css/style.css')

// $('body').append('<h1>'+people[0].name+'</h1>')



$.each(people, function(key,value){
	$('body').append('<h1>'+people[key].name+'</br>')
})

console.log(people[0].name)