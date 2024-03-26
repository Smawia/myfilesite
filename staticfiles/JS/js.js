// console.log("ddd")
let bar = document.querySelector(".toggle-menu");
let ul = document.querySelector(".js");
let arrow = document.querySelector(".left-arrow");
let arrow3 = document.querySelector(".left-arrow2");
let arrow4 = document.querySelector(".spe-arrow");
let arrow2 = document.querySelector(".arrow");
let lis = document.querySelectorAll(".js li");


bar.onclick = function () {
    ul.style.cssText = "display: flex;flex-direction: column;position: absolute;left: -400%;width: 160px;top:10%;z-index: 1000;background-color:#333;color:white";
    arrow.style.display = 'inline-block';
    arrow3.style.display = 'inline-block';
    arrow2.style.display = 'none';
    arrow4.style.display = 'none';
}

document.body.addEventListener("click", function (e) {
    if (!e.target.classList.contains('toggle-menu')) {
        if (ul.style.display === 'flex') {
            ul.style.display = 'none';
        }
    }
})