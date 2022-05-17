const messageList = document.querySelector("ul");
const nicknameForm = document.querySelector("#nickname");
const messageForm = document.querySelector("#message");
const frontSocket = new WebSocket(`ws://${window.location.host}`);

function makeMessage(type, payload) {
  const msg = { type, payload };
  return JSON.stringify(msg);
}

frontSocket.addEventListener("open", () => {
  console.log("Connected to Server ✅");
});

frontSocket.addEventListener("message", (message) => {
  const li = document.createElement("li");
  li.innerText = message.data;
  messageList.append(li);
});

frontSocket.addEventListener("close", () => {
  console.log("Disconnected ❌");
});

function handleSubmit(e) {
  e.preventDefault();
  const input = messageForm.querySelector("input");
  frontSocket.send(makeMessage("new_message", input.value));
  input.value = "";
}

function handleNicknameSubmit(e) {
  e.preventDefault();
  const myNickname = nicknameForm.querySelector("h2");
  const input = nicknameForm.querySelector("input");
  myNickname.innerText = `You: ${input.value}`;
  frontSocket.send(makeMessage("nickname", input.value));
  input.value = "";
}

messageForm.addEventListener("submit", handleSubmit);
nicknameForm.addEventListener("submit", handleNicknameSubmit);
