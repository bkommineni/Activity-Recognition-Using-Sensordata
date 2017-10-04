var httpserver =  require("http");

httpserver.createServer(function (request,response)
{
	let body = [];
	response.writeHead(200,{'Content-Type': 'text/plain'});
  	request.on('data', (chunk) => {
    	body.push(chunk);
  	}).on('end', () => {
    	body = Buffer.concat(body).toString();
    	response.end(body);
  	});
	response.end('THE RESPOSNE FROM THE SERVER!!!!!!!!!!!!!!');
}
).listen(3000);

console.log('server running at localhost: on port :3000');
