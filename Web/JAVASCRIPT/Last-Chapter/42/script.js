let stone = document.getElementById("stone");

let randNum = Math.floor(Math.random() * 9) + 1;

if (randNum == 1){
    stone.style.backgroundColor = "red";
} else if (randNum == 2){
    stone.style.backgroundColor = "orange";
} else if (randNum == 3){
    stone.style.backgroundColor = "yellow";
} else if (randNum == 4){
    stone.style.backgroundColor = "green";
} else if (randNum == 5){
    stone.style.backgroundColor = "blue";
} else if (randNum == 6){
    stone.style.backgroundColor = "#4169e1";
} else if (randNum == 7){
    stone.style.backgroundColor = "#00008b";
} else if (randNum == 8){
    stone.style.backgroundColor = "purple";
} else {
    stone.style.backgroundColor = "black";
}