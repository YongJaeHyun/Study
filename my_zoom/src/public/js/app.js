const socket = io();

const welcome = document.querySelector("#welcome");
const form = welcome.querySelector("form");
const room = document.querySelector("#room");

room.hidden = true;

let roomName;

function addMessage(message) {
  const ul = room.querySelector("ul");
  const li = document.createElement("li");
  li.innerText = message;
  ul.appendChild(li);
}

function handleMessageSubmit(e) {
  e.preventDefault();
  const input = room.querySelector("#message input");
  const value = input.value;
  socket.emit("new_message", value, roomName, () => {
    addMessage(`You: ${value}`);
  });
  input.value = "";
}

function handleNicknameSubmit(e) {
  e.preventDefault();
  const input = room.querySelector("#nickname input");
  const h3 = room.querySelector("#nickname h3");
  const value = input.value;
  socket.emit("nickname", value, roomName, () => {
    h3.innerText = `Your nickname: ${value}`;
  });
  input.value = "";
}

function handleQuitSubmit() {
  welcome.hidden = false;
  room.hidden = true;
  const ul = room.querySelector("ul");
  ul.innerHTML = "";
  socket.emit("quit_room", roomName);
}

function showRoom() {
  welcome.hidden = true;
  room.hidden = false;
  const h3 = room.querySelector("h3");
  h3.innerText = `Room ${roomName}`;
  const messageForm = room.querySelector("#message");
  const nicknameForm = room.querySelector("#nickname");
  const quitButton = room.querySelector("button");
  messageForm.addEventListener("submit", handleMessageSubmit);
  nicknameForm.addEventListener("submit", handleNicknameSubmit);
  quitButton.addEventListener("click", handleQuitSubmit);
}

function handleRoomSubmit(e) {
  e.preventDefault();
  const input = form.querySelector("input");
  socket.emit("enter_room", input.value, showRoom);
  roomName = input.value;
  input.value = "";
}

socket.on("connect", () => {
  socket.emit("init");
});

socket.on("enter_room", (roomName, id, nickname, newCount) => {
  const h3 = room.querySelector("h3");
  const h3_nickname = room.querySelector("#nickname h3");

  h3.innerText = `Room ${roomName} (Concurrent Users: ${newCount})`;
  if (id === socket.id) {
    h3_nickname.innerText = `Your nickname: ${nickname}`;
    addMessage("You Joined!");
  } else {
    addMessage(`${nickname} Joined!`);
  }
});

socket.on("bye", (nickname, newCount) => {
  const h3 = room.querySelector("h3");
  h3.innerText = `Room ${roomName} (Concurrent Users: ${newCount})`;
  addMessage(`${nickname} left ㅠㅠ`);
});

socket.on("new_message", (msg, nickname) => {
  addMessage(`${nickname}: ${msg}`);
});

socket.on("nickname_change", (prev_nickname, changed_nickname) => {
  addMessage(
    `nickname is changed! ✔ : (${prev_nickname} --> ${changed_nickname})`
  );
});

socket.on("room_change", (roomName, rooms) => {
  const roomList = welcome.querySelector("ul");
  roomList.innerHTML = "";
  if (rooms.length === 0) {
    return;
  }
  rooms.forEach((room) => {
    const li = document.createElement("li");
    const count = rooms[room];
    li.innerText = `Room ${roomName}  |  (Concurrent Users: ${count})`;
    roomList.appendChild(li);
  });
});

form.addEventListener("submit", handleRoomSubmit);
