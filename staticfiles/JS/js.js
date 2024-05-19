// let spe_a = document.querySelector('.js-a');
// let ul_list = document.querySelector('.ul');
// window.onscroll = function () {
//     if (window.scrollX <= 794) {
//         ul_list.style.cssText = 'display: flex;flex-direction: row;'
//     }
// }
// // let nested_list = document.querySelector('.nested-list');
// spe_a.onclick = function (e) {
//     console.log("spe a");
//     e.preventDefault();
//     ul_list.style.display = 'block';
// }
let bar = document.querySelector(".toggle-menu");
let ul = document.querySelector(".js");
let arrow = document.querySelector(".left-arrow");
let arrow3 = document.querySelector(".left-arrow2");
let arrow4 = document.querySelector(".spe-arrow");
let arrow2 = document.querySelector(".arrow");
let lis = document.querySelectorAll(".js li");
let img_id = document.querySelector(".hidden-row");
window.onscroll = function () {
    if (window.scrollY >= 300) {
        img_id.style.display = 'block';
    }
    else {
        img_id.style.display = 'none';
    }
}
let aside_bar = document.querySelector('.aside');
let over = document.querySelector('.over');
console.log(aside_bar);
bar.onclick = function () {
    aside_bar.style.cssText = 'width: 50%;display:block';
    over.style.display = 'block';
}

document.body.addEventListener("click", function (e) {
    if (!e.target.classList.contains('toggle-menu')) {
        aside_bar.style.display='none';
        over.style.display='none';
    }
});
// bar.onclick = function () {
//     ul.style.cssText = "display: flex;flex-direction: column;position: absolute;left: -430%;width: 160px;top:10%;z-index: 1000;background-color:#333;color:white";
//     arrow.style.display = 'inline-block';
//     arrow3.style.display = 'inline-block';
//     arrow2.style.display = 'none';
//     arrow4.style.display = 'none';
// }

// document.body.addEventListener("click", function (e) {
//     if (!e.target.classList.contains('toggle-menu')) {
//         if (ul.style.display === 'flex') {
//             ul.style.display = 'none';
//         }
//     }
// });


let go_to_index = document.querySelector('.go-to-index');

setTimeout(function () {
    go_to_index.click();
}, 5000);

let go_to_index2 = document.querySelector('.go-to-index2');
setTimeout(function () {
    go_to_index2.click();
}, 5000);
// let bgImg = document.querySelector('.images-slider');
// let rightRow = document.querySelector('.right');
// let leftRow = document.querySelector('.left');
// let one = document.querySelector('.one');
// let two = document.querySelector('.two');
// let three = document.querySelector('.three');
// let ones = document.querySelector('.ones');
// let twos = document.querySelector('.twos');
// let threes = document.querySelector('.threes');

// console.log(bgImg);

// let imgsList = ['pexels-photo-206359.jpeg', 'aimen.jpeg', 'thir.jpeg'];

// let counter = 0;
// setInterval(function () {
//     let rand = Math.floor(Math.random() * imgsList.length);


//     console.log(rand);
//     if (rand === 0) {
//         bgImg.style.backgroundImage = 'url("static/imgs/' + imgsList[0] + '")';
//         two.style.display = 'none';
//         three.style.display = 'none';
//         one.style.display = 'block';
//         twos.style.display = 'none';
//         threes.style.display = 'none';
//         ones.style.display = 'block';
//     }
//     else if (rand === 1) {
//         bgImg.style.backgroundImage = 'url("static/imgs/' + imgsList[1] + '")';
//         one.style.display = 'none';
//         three.style.display = 'none';
//         two.style.display = 'block';
//         ones.style.display = 'none';
//         threes.style.display = 'none';
//         twos.style.display = 'block';
//     }
//     else if (rand === 2) {
//         bgImg.style.backgroundImage = 'url("static/imgs/' + imgsList[2] + '")';
//         two.style.display = 'none';
//         one.style.display = 'none';
//         three.style.display = 'block';
//         twos.style.display = 'none';
//         ones.style.display = 'none';
//         threes.style.display = 'block';
//     }
// }, 2000);

// rightRow.onclick = function () {
//     if (counter == 2) {
//         return;
//     }
//     else {
//         counter++;
//         bgImg.style.backgroundImage = 'url("static/imgs/' + imgsList[counter] + '")';
//     }
// }
// leftRow.onclick = function () {
//     if (counter == 0) {
//         return;
//     }
//     else {
//         counter--;
//         bgImg.style.backgroundImage = 'url("static/imgs/' + imgsList[counter] + '")';
//     }
// }

// let anchor = document.querySelector('.a-count');
// let count = document.querySelector('.count');

// anchor.onclick = function () {
//     console.log("dsadda");
//     count.innerHTML++;
// }
