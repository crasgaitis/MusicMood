// background.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "sentimentAnalysis") {
    const text = message.text;
    const sentimentScore = analyzeSentiment(text);

    const imageUrl = sentimentScore > 0 ? "happy.png" : "sad.png";
    const imageElement = document.createElement("img");
    imageElement.src = chrome.runtime.getURL(imageUrl);
    document.body.appendChild(imageElement);
  }
});

chrome.action.onClicked.addListener((tab) => {
  chrome.tabs.sendMessage(tab.id, { type: "openPopup" });
});

function analyzeSentiment(text) {
  // perform sentiment analysis and return a score between -1 and 1
}

const button = document.getElementById("button");

// link to the website: https://crasgaitis-musicmood-main-xxcrlo.streamlit.app/
button.addEventListener("click", () => {
  chrome.tabs.create({ url: "https://crasgaitis-musicmood-main-xxcrlo.streamlit.app/" });
});