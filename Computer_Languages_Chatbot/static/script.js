const form = document.getElementById("chatForm");
const input = document.getElementById("messageInput");
const messages = document.getElementById("chatMessages");
const sendButton = document.getElementById("sendButton");
const clearButton = document.getElementById("clearButton");
const welcomeMarkup = document.getElementById("welcome").outerHTML;

function scrollToBottom() {
  messages.scrollTop = messages.scrollHeight;
  window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
}

function addMessage(text, sender) {
  const bubble = document.createElement("div");
  bubble.className = `message ${sender}`;
  const label = document.createElement("span");
  label.className = "message-label";
  label.textContent = sender === "user" ? "YOU" : "CODEBUDDY";
  const content = document.createElement("span");
  content.textContent = text;
  bubble.append(label, content);
  messages.appendChild(bubble);
  scrollToBottom();
}

async function sendMessage(text) {
  const message = text.trim();
  if (!message || sendButton.disabled) return;

  const welcome = document.getElementById("welcome");
  if (welcome) welcome.remove();

  addMessage(message, "user");
  input.value = "";
  input.style.height = "auto";
  sendButton.disabled = true;

  const waiting = document.createElement("div");
  waiting.className = "message bot";
  waiting.textContent = "Thinking...";
  messages.appendChild(waiting);
  scrollToBottom();

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });
    const data = await response.json();
    waiting.remove();
    addMessage(data.reply || "Sorry, I couldn't find an answer.", "bot");
  } catch (error) {
    waiting.remove();
    addMessage("Could not connect to the server. Check that Flask is running, then try again.", "bot");
  } finally {
    sendButton.disabled = false;
    input.focus();
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  sendMessage(input.value);
});

input.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    form.requestSubmit();
  }
});

input.addEventListener("input", () => {
  input.style.height = "auto";
  input.style.height = Math.min(input.scrollHeight, 130) + "px";
});

document.querySelectorAll("[data-question]").forEach((button) => {
  button.addEventListener("click", () => sendMessage(button.dataset.question));
});

clearButton.addEventListener("click", () => {
  messages.innerHTML = welcomeMarkup;
  document.querySelectorAll("#welcome [data-question]").forEach((button) => {
    button.addEventListener("click", () => sendMessage(button.dataset.question));
  });
  input.value = "";
  input.focus();
});
