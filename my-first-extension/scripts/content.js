console.log('hello! I am a content script');

const p = document.querySelectorAll('p');

// accepts user inputs from a text box.
const textbos = document.getElementById("textbox");

testbox.addEventListener("input", (event) => {
  const text = event.target.value;
  chrome.runtime.sendMessage({ type: "sentimentAnalysis", text})
});


for (els of p) {
  els.style.transition = '15s';
  els.style.transform = 'translateX(1000px)';

  // alternate to directly adding styles is adding a class. We need to let our manifest.json know 
  // which css file we're referring to/containes the runaway class
  els.classList.add("runaway");
}

chrome.runtime.onMessage.addListener(processMessage);

function processMessage(request, sender, senderResponse) {
  console.log(request);

  document.querySelector('body').classList.toggle('disco');
}