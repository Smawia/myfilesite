let bar = document.querySelector(".toggle-menu");
let ul = document.querySelector(".js");
let arrow = document.querySelector(".left-arrow");
let arrow3 = document.querySelector(".left-arrow2");
let arrow4 = document.querySelector(".spe-arrow");
let arrow2 = document.querySelector(".arrow");
let lis = document.querySelectorAll(".js li");
let card = document.querySelectorAll(".card");
let head_page = document.querySelector(".head-page");
let nav_a = document.querySelectorAll(".nav-a");
let nav_i = document.querySelectorAll(".arrow");
let show_refs = document.querySelectorAll(".container > .show-references , .nested-ref > .show-references");
let all_refs = document.querySelectorAll(".container > .refrences , .nested-ref > .refrences");

// تأكد من أن هناك تساويًا بين عدد الأزرار والمراجع
if (show_refs.length !== all_refs.length) {
    console.error("عدد العناصر غير متساوٍ بين show_refs و all_refs!");
} else {
    show_refs.forEach((show_ref, index) => {
        const all_ref = all_refs[index]; // المرجع المرتبط بنفس الفهرس
        
        show_ref.onclick = function () {
            // الحصول على الأنماط الحالية للعنصر
            const res = getComputedStyle(all_ref);
            const dis = res.height;

            // تخزين ارتفاعات المراجع بناءً على الكلاس
            const heights = {
                "jordan": "160px",
                "eveloution": "150px",
                "legis": "235px"
            };

            // العثور على الكلاس المتطابق
            let matchedClass = null;
            for (const cls of all_ref.classList) {
                if (heights[cls]) {
                    matchedClass = cls;
                    break;
                }
            }

            // تحديد الارتفاع الجديد بناءً على الكلاس أو القيمة الافتراضية
            const newHeight = matchedClass ? heights[matchedClass] : "310px";

            // تبديل حالة العرض
            if (dis === "0px") {
                all_ref.style.height = newHeight;
                show_ref.innerHTML = "إخفاء المراجع";
            } else {
                all_ref.style.height = "0";
                show_ref.innerHTML = "إظهار المراجع";
            }
        };
    });
}

let social = document.querySelector(".social");
let socialSpan = document.querySelector(".social span");

socialSpan.onclick = function () {
    social.classList.toggle("social2");
    socialSpan.innerHTML = '-';
    res2 = getComputedStyle(social);
    dis2 = res2.right;
    if (dis2 == '-55px') {
        socialSpan.innerHTML = '+';
    }
}

let aside_bar = document.querySelector('.aside');
let over = document.querySelector('.over');
bar.onclick = function () {
    aside_bar.style.cssText = 'width: 100%;display:block';
    over.style.display = 'block';
}

document.body.addEventListener("click", function (e) {
    if (!e.target.classList.contains('toggle-menu') && !e.target.classList.contains('phone')) {
        aside_bar.style.display = 'none';
        over.style.display = 'none';
    }
});

// جميع العناصر المستهدفة لتغيير حجم النص
const elements = [
    ...document.querySelectorAll('.first-page .full-text p'),      // الفقرات
    ...document.querySelectorAll('.first-page .full-text ul'),     // القوائم غير المرتبة
    ...document.querySelectorAll('.first-page .full-text ol'),     // القوائم المرتبة
    ...document.querySelectorAll('.first-page .full-text h2'),     // العناوين
    ...document.querySelectorAll('.special-title'),                // العناوين الخاصة
    ...document.querySelectorAll('.special-title2'),
    ...document.querySelectorAll('.e_yemen tbody tr td')      
];

// تحديد الأزرار
const increaseButton = document.getElementById('increaseFont');
const decreaseButton = document.getElementById('decreaseFont');

// الحجم الافتراضي للنص
let fontSize = 16;

// الحد الأقصى والأدنى للحجم
const maxFontSize = 26;
const minFontSize = 10;

// عند النقر على زر التكبير
increaseButton.addEventListener('click', function () {
    if (fontSize < maxFontSize) { // تحقق أن الحجم أقل من الحد الأقصى
        fontSize += 2; // زيادة الحجم
        elements.forEach(function (el) {
            el.style.setProperty('font-size', `${fontSize}px`, 'important');
        });
    }
});

// عند النقر على زر التصغير
decreaseButton.addEventListener('click', function () {
    if (fontSize > minFontSize) { // تحقق أن الحجم أكبر من الحد الأدنى
        fontSize -= 2; // تقليل الحجم
        elements.forEach(function (el) {
            el.style.setProperty('font-size', `${fontSize}px`, 'important');
        });
    }
});


const studies = document.querySelectorAll(".study-item"); // جميع المواضيع
const itemsToShow = 4; // عدد المواضيع المعروضة
let startIndex = 0;

// دالة لتحديث العرض
function updateStudies() {
    // إخفاء جميع المواضيع
    studies.forEach((item) => item.classList.remove("active"));

    // عرض العناصر الثلاثة التالية
    for (let i = 0; i < itemsToShow; i++) {
        const index = (startIndex + i) % studies.length;
        studies[index].classList.add("active");
    }

    // تحديث البداية
    startIndex = (startIndex + itemsToShow) % studies.length;
}

// تحديث العرض عند التحميل
updateStudies();

// تبديل المواضيع كل 5 ثوانٍ
setInterval(updateStudies, 12000);

// تحديد العنصر باستخدام الكلاس
const hiddenRows = document.querySelectorAll('.hidden-row');

// إضافة مستمع للحدث scroll
window.addEventListener('scroll', () => {
    // الحصول على موضع التمرير العمودي
    const scrollPosition = window.scrollY;

    // تحديد الموضع الذي يظهر عنده العنصر
    const revealPosition = 300; // يمكن تعديله حسب احتياجك

    // إظهار جميع العناصر التي تحمل الكلاس إذا تجاوز التمرير الموضع المطلوب
    hiddenRows.forEach(row => {
        if (scrollPosition > revealPosition) {
            row.style.display = 'block';
        } else {
            row.style.display = 'none';
        }
    });
});


