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
let index_imgs = document.querySelectorAll(".show-studies-index .show-index-imgs .card img");
let index_imgs2 = document.querySelectorAll(".show-studies-index .show-index-imgs .card img.stud");
let show_ref = document.querySelector(".show-references");
let all_ref = document.querySelector(".refrences");
let social = document.querySelector(".social");
let socialSpan = document.querySelector(".social span");

socialSpan.onclick = function () {
    social.classList.toggle("social2");
    socialSpan.innerHTML = '-';
    res2 = getComputedStyle(social);
    dis2 = res2.right;
    if(dis2 == '10px'){
        socialSpan.innerHTML = '+';
    }
}

let counter = 1;
setInterval(function () {
    document.getElementById('radio' + counter).checked = true;
    counter++;
    if (counter > 4) {
        counter = 1;
    }
}, 5000);

window.onscroll = function () {
    if (window.scrollY >= 500) {
        index_imgs[0].style.width = '100%';
        index_imgs[1].style.width = '100%';
        index_imgs[2].style.width = '100%';
    }

    if (window.scrollY >= 800) {
        index_imgs2[0].style.width = '100%';
        index_imgs2[1].style.width = '100%';
        index_imgs2[2].style.width = '100%';
    }

    if (window.scrollY >= 50) {
        txt_information.style.cssText = 'visibility: visible; transform: translateX(0)';
    }


    else {
        head_page.style.cssText = "background-color: white;";
        img_id.style.display = 'none';
    }
}

let aside_bar = document.querySelector('.aside');
let over = document.querySelector('.over');
bar.onclick = function () {
    aside_bar.style.cssText = 'width: 100%;display:block';
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
}, 3000);

let go_to_index2 = document.querySelector('.go-to-index2');
setTimeout(function () {
    go_to_index2.click();
}, 3000);

show_ref.onclick = function () {
    // document.querySelector(".refrences").style.display = 'block';
    res = getComputedStyle(all_ref);
    dis = res.height;
    console.log(dis);
    if (all_ref.classList.contains("jordan")) {
        console.log("jordan");
        if (dis == '0px') {
            console.log("jordan");
            all_ref.style.height = '160px';
            show_ref.innerHTML = 'إخفاء المراجع'
        }
        else {
            all_ref.style.height = '0';
            show_ref.innerHTML = 'إظهار المراجع'
        }
    }
    else if (all_ref.classList.contains("eveloution")) {
        if (dis == '0px') {
            all_ref.style.height = '150px';
            show_ref.innerHTML = 'إخفاء المراجع'
        }
        else {
            all_ref.style.height = '0';
            show_ref.innerHTML = 'إظهار المراجع'
        }
    }

    else if (all_ref.classList.contains("legis")) {
        if (dis == '0px') {
            all_ref.style.height = '235px';
            show_ref.innerHTML = 'إخفاء المراجع'
        }
        else {
            all_ref.style.height = '0';
            show_ref.innerHTML = 'إظهار المراجع'
        }
    }
    else {
        if (dis == '0px') {
            all_ref.style.height = '310px';
            show_ref.innerHTML = 'إخفاء المراجع'
        }
        else {
            all_ref.style.height = '0';
            show_ref.innerHTML = 'إظهار المراجع'
        }
    }

}




