const net = require("net")


const server = net.createServer(socket => {
    socket.write("Open")
    socket.on("data",data => {
        console.log(data.toString())
        socket.write("Received your data: " + data.toString());
    })
    socket.on("end", () => {
        console.log("Client disconnected");
    });
})

console.log('server running')
server.listen(8080)