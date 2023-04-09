'use strict';
(function() {
  window.addEventListener('load', () => {
    document.querySelector('input').addEventListener('change', () => {
      chrome.tabs.query({currentWindow: true, active: true}, function (tabs){
        chrome.tabs.sendMessage(tabs[0].id, {"message": "toggle"});
       });
    });
  });

  // Set the popup width to 1/6 of the user's screen width
  window.addEventListener('DOMContentLoaded', () => {
    const screenWidth = window.screen.width;
    const popupWidth = Math.floor(screenWidth / 3);
    document.body.style.width = `${popupWidth}px`;
  });

  // Enable user to submit a text.
  document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting
  
    // Get the value of the textbox
    var text = document.querySelector('#text-input').value;
  
    // Do something with the text (e.g., log it to the console)
    console.log(text);
  });

})();
