const http = require('http')
const fs = require('fs')



const hostName = '127.0.0.1'
const port = 3000


fs.readFile('index.html', (err,html)=>{
	
	if(!err){
const server = http.createServer(function (req,res){
	res.statusCode = 200
	res.setHeader('Content-type','text/html')
	res.end(html)
})

server.listen(port,hostName,()=>{
 
	console.log('Server started on port '+port)

})}	
})



