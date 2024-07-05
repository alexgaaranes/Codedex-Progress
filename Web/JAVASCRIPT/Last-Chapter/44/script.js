const memeArray = [
    "https://i.imgur.com/bSi4xLb.png",
    "https://i.imgur.com/6y0G7N0.png",
    "https://i.imgur.com/LXnRao1.png",
    "https://i.imgur.com/Qqoxh1N.png"
  ];

const captionArray = [
    "Wut da hil",
    "Nailed it",
    "Sure brudda",
    "WTF"
];

function randNum(size){
    return Math.floor(Math.random() * size);
}

let randMeme = document.getElementById("random-meme");
let randCaption = document.getElementById("random-caption");
let genButton = document.getElementById("generator-button");

genButton.addEventListener("click", function(){
        let memeIndex = randNum(memeArray.length);
        let captionIndex = randNum(captionArray.length);

        randMeme.src = memeArray[memeIndex];
        randCaption.innerText = captionArray[captionIndex];
    }
  )