console.log("ddd")
let bar = document.querySelector(".toggle-menu");
let ul = document.querySelector(".js");
let lis = document.querySelectorAll(".js li");
console.log(ul)
console.log(lis)

bar.onclick = function () {
    ul.style.cssText = "display: flex;flex-direction: column;position: absolute;left: -400%;width: 160px;top:10%;z-index: 1000;background-color:#333;color:white";
}

document.body.addEventListener("click", function (e) {
    if (!e.target.classList.contains('toggle-menu')) {
        if (ul.style.display === 'flex') {
            ul.style.display = 'none';
        }
    }
})