/**
 * code directly taken from https://medium.com/free-code-camp/vanilla-javascript-tutorial-build-a-memory-game-in-30-minutes-e542c4447eae
 */
'use strict';
(function() {

  let flip = false;
  let lock = false;
  let first, second;

  const NUM_CARDS = 12;

  window.addEventListener('load', init);

  function init() {
    shuffleCards();
    const cards = document.querySelectorAll('.memory-card');
    cards.forEach(card => card.addEventListener('click', flipCard));
  }

  function shuffleCards() {
    document.querySelectorAll('.memory-card').forEach(card => {
      card.style.order = Math.ceil(Math.random() * NUM_CARDS);;
    });
  }

  function flipCard() {
    if (lock) return;
    if (this === first) return;
    this.classList.add('flip');
    if (!flip) {
      flip = true;
      first = this;
      return;
    }
    second = this;
    lock = true;
    checkForMatch();
  }

  function checkForMatch() {
    let isMatch = first.dataset.name === second.dataset.name;
    isMatch ? disable() : revert();
  }
  
  function disable() {
    first.removeEventListener('click', flipCard);
    second.removeEventListener('click', flipCard);
    reset();
  }
  
  function revert() {
    setTimeout(() => {
      first.classList.remove('flip');
      second.classList.remove('flip');
  
      reset();
    }, 1000);
  }
  
  function reset() {
    flip = false;
    lock = false;
    first = null;
    second = null;
  }

})();

