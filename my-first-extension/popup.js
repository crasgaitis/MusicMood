'use strict';
(function() {
  window.addEventListener('load', () => {
    document.querySelector('input').addEventListener('change', () => {
      chrome.tabs.query({currentWindow: true, active: true}, function (tabs){
        chrome.tabs.sendMessage(tabs[0].id, {"message": "toggle"});
       });
    });
  });
})();
