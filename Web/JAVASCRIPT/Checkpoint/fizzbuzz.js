const maxNum = 15;

for (let i = 1; i <= maxNum; i++){
    if (i%3==0){
        if (i%5==0){
            console.log("FizzBuzz");
        } else {
            console.log("Fizz");
        }
    } else if (i%5==0){
        console.log("Buzz");
    } else {
        console.log(i);
    }
}