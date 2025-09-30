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

// index page
document.addEventListener("DOMContentLoaded", function () {
    const radios = document.querySelectorAll('.slides input[name="radio-btn"]');
    let current = 0;

    const prevArrow = document.querySelector('.arrow-1.prev');
    const nextArrow = document.querySelector('.arrow-1.next');

    if(!prevArrow || !nextArrow) {
        return;
    }

    function showSlide(index) {
        radios[index].checked = true;
        current = index;
    }

    prevArrow.addEventListener('click', () => {
        let index = current - 1;
        if (index < 0) index = radios.length - 1;
        showSlide(index);
    });

    nextArrow.addEventListener('click', () => {
        let index = current + 1;
        if (index >= radios.length) index = 0;
        showSlide(index);
    });
    let intervalTime = 10000; // وقت البداية بين الانتقالات

    function startSlider() {
        let counter = 5; // التأكد من البدء من الصورة الأولى
        document.getElementById('radio' + counter).checked = true;

        setTimeout(function sliderTransition() {
            counter--;
            if (counter == 0) {
                counter = 5; // العودة إلى الصورة الأولى بعد الصورة الأخيرة
            }
            document.getElementById('radio' + counter).checked = true;

            // ضبط الانتقال التالي بنفس الوقت الثابت                
            setTimeout(sliderTransition, intervalTime);
        }, intervalTime);
    }

    startSlider(); // تشغيل السلايدر بمجرد أن الـ DOM جاهز


    // تعريف الـ Swiper لكن بدون autoplay
    var swiper = new Swiper('.swiper-container', {
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 'auto',
        initialSlide: 0,
        loop: true,
        speed: 2000,
        coverflowEffect: {
            rotate: 50,
            stretch: 0,
            depth: 100,
            modifier: 1,
            slideShadows: false
        },
        autoplay: false, // نوقف التشغيل التلقائي,
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
        },
        // 🔹 هنا نتحكم في القيم حسب حجم الشاشة
        breakpoints: {
            320: { // شاشات صغيرة (موبايل)
                coverflowEffect: {
                    stretch: 100
                }
            },
            768: { // شاشات متوسطة (تابلت)
                coverflowEffect: {
                    stretch: -30
                }
            },
            1024: { // شاشات كبيرة (لابتوب/ديسكتوب)
                coverflowEffect: {
                    stretch: -60
                }
            }
        }

    });
    // بدء التشغيل التلقائي بعد تحميل الصفحة
    window.addEventListener("load", function () {
        swiper.params.autoplay = { delay: 7000, disableOnInteraction: false }; // كل 7 ثواني
        swiper.autoplay.start();
    });
    document.addEventListener("visibilitychange", function () {
        if (document.hidden) {
            // إيقاف التشغيل لما تنتقل لتبويب ثاني
            swiper.autoplay.stop();
        } else {
            // إعادة التشغيل لما ترجع للتبويب
            swiper.autoplay.start();
        }
    });
});


//   infographic view
document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("infographContainer");

    // لو ما في بيانات infographs في الصفحة، نوقف
    if (!container) {
        return;
    }

    const loadMoreBtn = document.getElementById("loadMoreBtn");
    // console.log("Container and Button:", container, loadMoreBtn);
    // جلب البيانات من الـ script
    const data = JSON.parse(document.getElementById("infographs").textContent);
    // console.log("Data length:", data.length);
    
    let itemsPerPage = 6;   // كم عنصر نعرض كل مرة
    let currentIndex = 0;   // موقع البداية

    function renderItems() {
        // نتأكد أن فيه عناصر متبقية
        if (currentIndex >= data.length) {
            loadMoreBtn.style.display = "none";
            return;
        }

        // ناخذ الشرائح المتبقية فقط
        const slice = data.slice(currentIndex, currentIndex + itemsPerPage);

        slice.forEach(item => {
            const card = document.createElement("div");
            card.className = "studies-card infograph-card custom-studies-card fade-in"; // أضفنا fade-in
            card.innerHTML = `
                <a href="/Infographics/${item.slug}/">
                    <img src="/static/${item.image}" alt="إنفوجراف" class="infograph-img">
                    <div class="study-text-info">
                        <span>${item.date}</span>
                        <p>${item.title}</p>
                    </div>
                </a>
            `;
            container.appendChild(card);
        });

        // تحديث المؤشر
        currentIndex += slice.length;

        // إذا خلصت العناصر، أخفي الزر
        if (currentIndex >= data.length) {
            loadMoreBtn.style.display = "none";
            console.log("كل العناصر تم عرضها");
        }
    }

    // تحميل أول دفعة
    renderItems();

    // عند الضغط على عرض المزيد
    loadMoreBtn.addEventListener("click", renderItems);
});

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
                "legis": "160px"
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

// جميع العناصر المستهدفة لتغيير حجم النص
const elements = [
    ...document.querySelectorAll('.first-page .full-text p'),      // الفقرات
    ...document.querySelectorAll('.first-page .full-text ul'),     // القوائم غير المرتبة
    ...document.querySelectorAll('.first-page .full-text ol'),     // القوائم المرتبة
    ...document.querySelectorAll('.first-page .full-text h2'),     // العناوين
    ...document.querySelectorAll('.first-page .full-text h3'),     // العناوين
    ...document.querySelectorAll('.first-page .full-text h4'),     // العناوين
    ...document.querySelectorAll('.first-page .full-text h5'),     // العناوين
    ...document.querySelectorAll('.first-page .full-text figcaption'),  // عناوين الأشكال
    ...document.querySelectorAll('.first-page .full-text .source'), // المصادر 
    ...document.querySelectorAll('.first-page .table-caption'),    // عناوين الجداول
    ...document.querySelectorAll('.special-title'),                // العناوين الخاصة
    ...document.querySelectorAll('.special-title2'),
    ...document.querySelectorAll('.e_yemen tbody tr td')
];

// تحديد الأزرار
const increaseButton = document.getElementById('increaseFont');
const decreaseButton = document.getElementById('decreaseFont');

// الحجم الافتراضي للنص
let fontSize = 19;

// الحد الأقصى والأدنى للحجم
const maxFontSize = 30;
const minFontSize = 10;

if (increaseButton && decreaseButton) {
    // عند النقر على زر التكبير
    increaseButton.addEventListener('click', function () {
        if (fontSize < maxFontSize) { // تحقق أن الحجم أقل من الحد الأقصى
            fontSize += 1; // زيادة الحجم
            elements.forEach(function (el) {
                el.style.setProperty('font-size', `${fontSize}px`, 'important');
            });
        }
    });

    // عند النقر على زر التصغير
    decreaseButton.addEventListener('click', function () {
        if (fontSize > minFontSize) { // تحقق أن الحجم أكبر من الحد الأدنى
            fontSize -= 1; // تقليل الحجم
            elements.forEach(function (el) {
                el.style.setProperty('font-size', `${fontSize}px`, 'important');
            });
        }
    });
}


const studies = document.querySelectorAll(".study-item"); // جميع المواضيع
const itemsToShow = 4; // عدد المواضيع المعروضة
let startIndex = 0;

// دالة لتحديث العرض
function updateStudies() {
    // إذا ما في عناصر، نخرج
    if (!studies || studies.length === 0) {
        console.warn("⚠️ لا يوجد عناصر في studies");
        return;
    }

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

// عندما يقوم المستخدم بالتمرير
window.onscroll = function () {
    updateProgressBar();
};

function updateProgressBar() {
    const bar = document.getElementById('progress-bar');
    if (!bar) {
        return; // ما في progress bar → نخرج
    }
    // حساب الارتفاع الكلي للمحتوى
    const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
    const clientHeight = document.documentElement.clientHeight;

    // حساب نسبة التقدم
    const scrolled = (scrollTop / (scrollHeight - clientHeight)) * 100;

    // تحديث عرض progress bar
    document.getElementById('progress-bar').style.width = scrolled + "%";
}

