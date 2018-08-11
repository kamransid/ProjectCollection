var express = require('express')
var bodyParser = require('body-parser')
var path = require('path')

var app = express()
app.set('view engine', 'ejs')
app.set('views', path.join(__dirname,'views'))
app.listen(3000, function(){
    console.log('Hello wolrd from express....')
    console.log('Port started at 3000')
})
var person = [
    {
        name : 'Karan',
        age : 30
    },
    {
        name : 'Kamran',
        age : 27
    },
    {
        name : 'Husain',
        age : 40 
    }
 ]

var logger = function(req,res,next){
    console.log('Hi Hello')
    next()
}

app.use(logger)

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended:false}))
app.use(express.static(path.join(__dirname,'public')))

var users = [
     {
         id: 1,
         first_name : 'jhon',
         last_name : 'Doe',
         email: 'jhon@gmail.com'
     },
     {
         id:2,
         first_name:'Steven',
         last_name:'Smith',
         email: 'smith@gmail.com'
     },
     {
        id:3,
        first_name:'Peter',
        last_name:'Smith',
        email: 'smith@gmail.com'
    },
    {
        id:3,
        first_name:'Brain',
        last_name:'Jordan',
        email: 'jordan@gmail.com'
    }
]




app.get('/hello', function(req,res){
      res.render('index', {
          title:'Kafka',
          users: users
      })    
})

app.post('/users/add', function(req,res,next){
    console.log('Form submitted')
    console.log(req.body.first_name)
    next()
})


