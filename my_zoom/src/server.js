import http from "http";
import SocketIO from "socket.io";
import express from "express";

const app = express();

app.set("view engine", "pug");
app.set("views", __dirname + "/views");
app.use("/public", express.static(__dirname + "/public"));
app.get("/", (req, res) => res.render("home"));
app.get("/*", (req, res) => res.redirect("/"));

const handleListen = () => console.log(`listening on http://localhost:3000`);

const httpServer = http.createServer(app);
const wsServer = SocketIO(httpServer);

wsServer.on("connection", (socket) => {
  socket["nickname"] = "Anonymous";
  socket.onAny((e) => console.log(`Socket Event: ${e}`));

  socket.on("enter_room", (roomName, done) => {
    socket.join(roomName);
    done();
    socket.to(roomName).emit("welcome", socket.nickname);
  });
  socket.on("disconnecting", () => {
    socket.rooms.forEach((room) => {
      socket.to(room).emit("bye", socket.nickname);
    });
  });
  socket.on("new_message", (msg, room, done) => {
    socket.to(room).emit("new_message", msg, socket.nickname);
    done();
  });
  socket.on("nickname", (nickname, done) => {
    socket["nickname"] = nickname;
    done();
  });
});

// const sockets = [];

// wss.on("connection", (backSocket) => {
//   sockets.push(backSocket);
//   backSocket["nickname"] = "Anonymous";
//   sockets.at(-1).send(`Your Nickname : ${backSocket.nickname}`);
//   console.log("Connected to the browser ✅");

//   sockets
//     .slice(0, sockets.at(-1))
//     .forEach((aSocket) =>
//       aSocket.send(`New ${backSocket.nickname} is entered.`)
//     );

//   backSocket.on("close", () => {
//     console.log("Disconnected from the browser ❌");
//   });

//   backSocket.on("message", (msg) => {
//     const message = JSON.parse(msg);
//     switch (message.type) {
//       case "new_message":
//         sockets.forEach((aSocket) =>
//           aSocket.send(`${backSocket.nickname}: ${message.payload}`)
//         );
//         break;
//       case "nickname":
//         const originNickname = backSocket.nickname;
//         backSocket["nickname"] = message.payload;
//         sockets.forEach((aSocket) =>
//           aSocket.send(
//             `${originNickname} changed nickname to ${backSocket.nickname}`
//           )
//         );
//         break;
//     }
//   });
// });

httpServer.listen(3000, handleListen);
