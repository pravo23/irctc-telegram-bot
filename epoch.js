// let epochDate = 268088400;

// var myDate = new Date( epochDate *1000);
// console.log(myDate.toGMTString()+"\n\n"+myDate.toLocaleString())

var myDate = new Date("July 1, 1978 02:30:00"); // Your timezone!
var myEpoch = myDate.getTime()/1000.0;
console.log(myEpoch)