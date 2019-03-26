'use strict';

function randomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

(function(){
    if(process.argv.length!=3){
        console.log("usage:\n\tmkdate <interger>\n");
    }
    var wall = Number.parseInt(process.argv[2],10);    
    if(isNaN(wall) || wall<=0){
        console.log("error: input must be a positive integer\n");
    }
    wall*=10000;
    for(var cnt=0;cnt<wall;cnt++){
        var year = randomInt(20)+2000;
        var month = randomInt(12)+1;
        var day = randomInt(31)+1;
        var hour = randomInt(24)+1;
        var minute = randomInt(60)+1;
        var second = randomInt(60)+1;
        console.log(`${year}-${month}-${day} ${hour}:${minute}:${second}`);
    }
})();
