/* FINALLY FIXED IT */

console.log('IT\'S ROCK, PAPER, SCISSORS TIME!');

function getUserChoice (userInput) {
    userInput = userInput.toLowerCase();
    if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors') {
      return userInput;
    } else {
      return 'Invalid Input';
    }
  }

/* console.log(getUserChoice('rock'));
 */

function getComputerChoice() {
    let randomNumber = Math.floor(Math.random() * 3)
    if (randomNumber === 0) {
      return 'rock';
    } else {
      if (randomNumber === 1) {
        return 'paper';
      } else {
        if (randomNumber === 2) {
          return 'scissors';
        }
      } 
    } 
  }


  function determineWinner(userChoice, computerChoice) {
    if (userChoice === computerChoice) {
      return 'It\'s a tie!';
    } else if (userChoice === 'rock' && computerChoice === 'scissors') {
      return 'User wins!';
    } else if (userChoice === 'rock' && computerChoice === 'paper') {
        return 'The mighty computer wins!';
    } else if (userChoice === 'paper' && computerChoice === 'rock') {
      return 'User wins!';
    }  else if (userChoice === 'paper' && computerChoice === 'scissors') {
        return 'The mighty computer wins!';
    } else if (userChoice === 'scissors' && computerChoice === 'rock') {
      return 'The mighty computer wins!';
    } else if (userChoice === 'scissors' && computerChoice === 'paper') {
        return 'User wins!';
      }
    }
  

  function playGame() {
    let userChoice = getUserChoice('rock');
    let computerChoice = getComputerChoice()
    console.log('The user\'s fragile mortal coil has chosen', userChoice)
    console.log('The all-powerful computer has chosen', computerChoice)
    console.log(determineWinner(userChoice, computerChoice));
  }
  
  playGame()