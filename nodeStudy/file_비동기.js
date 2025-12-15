
import fs from 'fs'
// import require from 'require'

// 동기

// const fs = require('fs');

// const a = fs.readFileSync('a.txt');
// const b = fs.readFileSync('b.txt');
// const c = fs.readFileSync('c.txt');

// console.log(a,b,c);
// console.log(a.toString(),b.toString(),c.toString());


//비동기 2
//모듈 설치 후 가능 : npm install async  
import async from 'async'

async.parallel([
    // 병렬
    (callback)=>{fs.readFile('a.txt',callback);},
    (callback)=>{fs.readFile('b.txt',callback);},
    (callback)=>{fs.readFile('c.txt',callback);},

],(error, results)=>{
    console.log(results.toString());
});


//비동기 2

// const a = fs.readFile('a.txt',(error, a)=>{
//     console.log(a.toString());
// });

// const b = fs.readFile('b.txt',(error, b)=>{
//     console.log(b.toString());
// });

// const c = fs.readFile('c.txt',(error, c)=>{
//     console.log(c.toString());
// });



