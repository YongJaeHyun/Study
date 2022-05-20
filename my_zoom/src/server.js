import http from "http";
import { Server } from "socket.io";
import { instrument } from "@socket.io/admin-ui";
import express from "express";

const app = express();

app.set("view engine", "pug");
app.set("views", __dirname + "/views");
app.use("/public", express.static(__dirname + "/public"));
app.get("/", (req, res) => res.render("home"));
app.get("/*", (req, res) => res.redirect("/"));

const handleListen = () => console.log(`listening on http://localhost:3000`);

const httpServer = http.createServer(app);
const wsServer = new Server(httpServer, {
  cors: {
    origin: ["https://admin.socket.io"],
    credentials: true,
  },
});
instrument(wsServer, {
  auth: false,
});

function publicRooms() {
  const {
    sockets: {
      adapter: { sids, rooms },
    },
  } = wsServer;
  const publicRooms = [];
  rooms.forEach((_, key) => {
    if (sids.get(key) === undefined) {
      publicRooms.push({ key: countRoom(key) });
    }
  });
  return publicRooms;
}

function showRoom(roomName) {
  wsServer.sockets.emit("room_change", roomName, publicRooms());
}

function countRoom(roomName) {
  return wsServer.sockets.adapter.rooms.get(roomName)?.size;
}

wsServer.on("connection", (socket) => {
  socket["nickname"] = `Anonymous${Math.ceil(Math.random() * 9999)}`;
  // socket.onAny((e) => {
  //   console.log(`Socket Event: ${e}`);
  // });

  socket.on("init", () => {
    publicRooms().forEach((roomName) => {
      showRoom(roomName);
    });
  });
  socket.on("enter_room", (roomName, done) => {
    socket.join(roomName);
    done();
    wsServer
      .to(roomName)
      .emit(
        "enter_room",
        roomName,
        socket.id,
        socket.nickname,
        countRoom(roomName)
      );
    showRoom(roomName);
  });
  socket.on("quit_room", (roomName) => {
    socket.rooms.forEach((room) => {
      if (room !== socket.id) {
        socket.to(room).emit("bye", socket.nickname, countRoom(room) - 1);
      }
    });
    socket.leave(roomName);
    showRoom(roomName);
  });
  socket.on("disconnecting", (e) => {
    socket.rooms.forEach((room) => {
      if (room !== socket.id) {
        socket.to(room).emit("bye", socket.nickname, countRoom(room) - 1);
      }
    });
    publicRooms().forEach((roomName) => {
      if (socket.rooms.has(roomName)) {
        socket.leave(roomName);
        showRoom(roomName);
      }
    });
  });
  socket.on("new_message", (msg, room, done) => {
    socket.to(room).emit("new_message", msg, socket.nickname);
    done();
  });
  socket.on("nickname", (nickname, roomName, done) => {
    const prev_nickname = socket.nickname;
    socket["nickname"] = nickname;
    wsServer
      .to(roomName)
      .emit("nickname_change", prev_nickname, socket.nickname);
    done();
  });
});

httpServer.listen(3000, handleListen);
