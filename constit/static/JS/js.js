let bar = document.querySelector(".toggle-menu");
let ul = document.querySelector(".js");
let arrow = document.querySelector(".left-arrow");
let arrow3 = document.querySelector(".left-arrow2");
let arrow4 = document.querySelector(".spe-arrow");
let arrow2 = document.querySelector(".arrow");
let lis = document.querySelectorAll(".js li");
let img_id = document.querySelector(".hidden-row");
let card = document.querySelectorAll(".card");
let head_page = document.querySelector(".head-page");
let txt_information = document.querySelector(".text-info");
let nav_a = document.querySelectorAll(".nav-a");
let nav_i = document.querySelectorAll(".arrow");
window.onscroll = function () {
    if (window.scrollY >= 300) {
        head_page.style.cssText = "background-color: rgb(227 9 29 / 48%); border-radius: 12px;";
        nav_a[0].style.color = "white";
        nav_a[1].style.color = "white";
        nav_a[2].style.color = "white";
        nav_a[3].style.color = "white";
        nav_a[4].style.color = "white";
        nav_a[5].style.color = "white";
        nav_i[0].style.color = "white";
        nav_i[1].style.color = "white";
        img_id.style.display = 'block';
    }
    if (window.scrollY >= 50) {
        txt_information.style.transform = 'translateX(0)';
    }

    else {
        head_page.style.cssText = "background-color: white;";
        nav_a[0].style.color = "black";
        nav_a[1].style.color = "black";
        nav_a[2].style.color = "black";
        nav_a[3].style.color = "black";
        nav_a[4].style.color = "black";
        nav_a[5].style.color = "black";
        nav_i[0].style.color = "black";
        nav_i[1].style.color = "black";
        img_id.style.display = 'none';
    }
}

let aside_bar = document.querySelector('.aside');
let over = document.querySelector('.over');
bar.onclick = function () {
    aside_bar.style.cssText = 'width: 50%;display:block';
    over.style.display = 'block';
}

document.body.addEventListener("click", function (e) {
    if (!e.target.classList.contains('toggle-menu')) {
        aside_bar.style.display = 'none';
        over.style.display = 'none';
    }
});

let go_to_index = document.querySelector('.go-to-index');

setTimeout(function () {
    go_to_index.click();
}, 5000);

let go_to_index2 = document.querySelector('.go-to-index2');
setTimeout(function () {
    go_to_index2.click();
}, 5000);