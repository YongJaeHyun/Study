const socket = io();

const myFace = document.querySelector("#myFace");
const muteBtn = document.querySelector("#mute");
const cameraBtn = document.querySelector("#camera");
const camerasSelect = document.querySelector("#cameras");
const call = document.querySelector("#call");
const chatBox = document.querySelector("#chatBox");
const chatForm = chatBox.querySelector("form");
const nicknameDiv = document.querySelector("#nicknameDiv");
const nicknameForm = nicknameDiv.querySelector("form");
const welcome = document.querySelector("#welcome");

call.hidden = true;
welcome.hidden = true;

let myStream;
let muted = false;
let cameraOff = false;
let roomName;
let myPeerConnection;
let myDataChannel;
let nickname;

async function getCameras() {
  try {
    const devices = await navigator.mediaDevices.enumerateDevices();
    const cameras = devices.filter((device) => device.kind === "videoinput");
    const currentCamera = myStream.getVideoTracks()[0];
    cameras.forEach((camera) => {
      const option = document.createElement("option");
      option.value = camera.deviceId;
      option.innerText = camera.label;
      if (currentCamera.label === camera.label) {
        option.selected = true;
      }
      camerasSelect.appendChild(option);
    });
  } catch (e) {
    console.log(e);
  }
}

async function getMedia(deviceId) {
  const initialConstrains = {
    audio: true,
    video: { facingMode: "user" },
  };
  const cameraConstraints = {
    audio: true,
    video: { deviceId: { exact: deviceId } },
  };
  try {
    myStream = await navigator.mediaDevices.getUserMedia(
      deviceId ? cameraConstraints : initialConstrains
    );
    myFace.srcObject = myStream;
    if (!deviceId) {
      await getCameras();
    }
  } catch (e) {
    console.log(e);
  }
}

function handleMuteClick() {
  myStream
    .getAudioTracks()
    .forEach((track) => (track.enabled = !track.enabled));
  if (!muted) {
    muteBtn.innerText = "Unmute";
    muted = true;
  } else {
    muteBtn.innerText = "mute";
    muted = false;
  }
}
function handleCameraClick() {
  myStream
    .getVideoTracks()
    .forEach((track) => (track.enabled = !track.enabled));
  if (cameraOff) {
    cameraBtn.innerText = "Camera Off";
    cameraOff = false;
  } else {
    cameraBtn.innerText = "Camera On";
    cameraOff = true;
  }
}

async function handleCameraChange() {
  await getMedia(camerasSelect.value);
  if (myPeerConnection) {
    const videoTrack = myStream.getVideoTracks()[0];
    const videoSender = myPeerConnection
      .getSenders()
      .find((sender) => sender.track.kind === "video");
    videoSender.replaceTrack(videoTrack);
  }
}

muteBtn.addEventListener("click", handleMuteClick);
cameraBtn.addEventListener("click", handleCameraClick);
camerasSelect.addEventListener("input", handleCameraChange);

// Welcome Form (Join a room)

const welcomeForm = welcome.querySelector("form");

async function initCall() {
  welcome.hidden = true;
  call.hidden = false;
  chatBox.hidden = true;
  await getMedia();
  makeConnection();
}

async function handleWelcomeSubmit(e) {
  e.preventDefault();
  const input = welcomeForm.querySelector("input");
  await initCall();
  socket.emit("join_room", input.value);
  roomName = input.value;
  input.value = "";
}

function handleNicknameSubmit(e) {
  e.preventDefault();
  const input = nicknameForm.querySelector("input");
  nickname = input.value;
  input.value = "";
  nicknameDiv.hidden = true;
  welcome.hidden = false;
}

welcomeForm.addEventListener("submit", handleWelcomeSubmit);
nicknameForm.addEventListener("submit", handleNicknameSubmit);

// Socket Code

function addMessage(e) {
  e.preventDefault();
  const input = chatForm.querySelector("input");
  const message = input.value;
  const ul = chatForm.querySelector("ul");
  const li = document.createElement("li");
  li.innerText = `You: ${message}`;
  ul.appendChild(li);
  ul.scrollTop = ul.scrollHeight; // scroll down to bottom automatically
  input.value = "";
  myDataChannel.send(`${myDataChannel.nickname} : ${message}`);
}

function receiveMessage(message) {
  const ul = chatForm.querySelector("ul");
  const li = document.createElement("li");
  li.innerText = message.data
    ? `${message.data}`
    : `${myDataChannel.nickname} : ${message}`;
  ul.appendChild(li);
  ul.scrollTop = ul.scrollHeight; // scroll down to bottom automatically
}

socket.on("welcome", async () => {
  myDataChannel = myPeerConnection.createDataChannel("chat");
  myDataChannel.nickname = nickname;
  myDataChannel.addEventListener("open", () => {
    chatBox.hidden = false;
    myDataChannel.send("chatroom connected!");
    myDataChannel.addEventListener("message", receiveMessage);
    chatForm.addEventListener("submit", addMessage);
  });
  const offer = await myPeerConnection.createOffer();
  myPeerConnection.setLocalDescription(offer);
  socket.emit("offer", offer, roomName);
});

socket.on("offer", async (offer) => {
  myPeerConnection.addEventListener("datachannel", (e) => {
    myDataChannel = e.channel;
    myDataChannel.nickname = nickname;
    chatBox.hidden = false;
    myDataChannel.send("chatroom connected!");
    myDataChannel.addEventListener("message", receiveMessage);
    chatForm.addEventListener("submit", addMessage);
  });
  myPeerConnection.setRemoteDescription(offer);
  const answer = await myPeerConnection.createAnswer();
  myPeerConnection.setLocalDescription(answer);
  socket.emit("answer", answer, roomName);
});

socket.on("answer", (answer) => {
  myPeerConnection.setRemoteDescription(answer);
});

socket.on("ice", (ice) => {
  myPeerConnection.addIceCandidate(ice);
});

socket.on("restriction", () => {
  location.reload();
  alert("max-people of room is 2");
});

// RTC Code

function makeConnection() {
  myPeerConnection = new RTCPeerConnection();
  myPeerConnection.addEventListener("icecandidate", handleIce);
  myPeerConnection.addEventListener("addstream", handleAddStream);
  myStream
    .getTracks()
    .forEach((track) => myPeerConnection.addTrack(track, myStream));
}

function handleIce(data) {
  socket.emit("ice", data.candidate, roomName);
}

function handleAddStream(data) {
  const peersFace = document.querySelector("#peersFace");
  peersFace.srcObject = data.stream;
}
