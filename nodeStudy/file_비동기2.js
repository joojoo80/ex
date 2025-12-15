import fs from 'fs'

//동기식 처리
// const a= fs.writeFileSync('my.txt',"안녕하세요\n 하하 hi");

// console.log('완료');

//비동기식 처리
// fs.writeFile('my2.txt','안녕하세요\n 하하 hi',()=>{
// console.log('완료1');
// });
// console.log('완료2');


//비동기는 항상 예외처리 해야함
// try {
//     fs.readFile('textfile.txt', (error,file)=>{
//         console.log(file);
//         console.log(file.toString());
//     })
// } catch (error) {
//     console.log(error);
    
// }

// try {
//     fs.readFile('textfile.txt2', (error,file)=>{
//         console.log(file);
//         console.log(file.toString());
//     })
// } catch (error) {
//     console.log(error);
// }
    
// 비동기 예외처리 
// 텍스트 파일 2 없음 >> 에러 출력
// fs.readFile('textfile2.txt', (error,file)=>{
//     if(error){
//         console.log('문제발생');
//     }else{
//         console.log('file.toString()');
//     }
// });

//예외시 조기 리턴
// 텍스트 파일 2 없음 >> 에러 출력

fs.readFile('textfile2.txt', (error,file)=>{
    if(error){
        console.log('문제발생');
        return;
    }
        console.log('file.toString()');

});

