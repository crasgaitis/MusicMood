console.log('hello, I am a background script!!!!!!!');

chrome.browserAction.onClicked.addListener(() => {
  console.log('ouch, you clicked me!');
});

chrome.browserAction.onClicked.addListener((obj) => {
  console.log(obj);
});