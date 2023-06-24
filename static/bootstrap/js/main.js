const counts = document.querySelectorAll('.count')
const speed = 300;
counts.forEach((counter) => {
    function upData() {
        const target = Number(counter.getAttribute('data-target'))
        const count = Number(counter.innerText)
        const inc = target / speed
        if (count < target) {
            counter.innerText = Math.floor(inc + count)
            setTimeout(upData, 1)
        } else {
            counter.innerText = target
        }
    }
    upData()
})


// START MULTI LANGUAGE
const translations = {
    en: {
        // START PAGE BASE
        blog: "Blog",
        top_videos: "Top Videos",
        pricing_plans: "pricing & Plans",
        calculator: "Calculator",
        calculator: "Calculator",
        calorie: "Calorie Calculator",
        bmr_calc: "BMR Calculator",
        tdee_calc: "Tdee Calculator",
        english: "English",
        arabic: "Arabic",
        // END PAGE BASE
        // START PAGE INDEX
        // SECTION LANDING
        coach_data: "I'm Ahmed tantawy, a registered dietitian and certified health coach.",
        // SCTION HEALTHY LIFE
        improve: "improve your health, improve your life",
        // SCTION SERVICES
        services: "services",
        // SCTION TESTIMONIALS
        testimonials: "testimonials",
        // END PAGE INDEX

    },
    ar: {
        // START PAGE BASE
        blog: "مدونة",
        top_videos: "أهم الفديوهات",
        pricing_plans: "التسعير و الخطط",
        calculator: "حاسبة",
        calorie: "حاسبة السعرات الحرارية",
        bmr_calc: "حاسبة BMR",
        tdee_calc: "حاسبة tdee",
        english: "الانجليزية",
        arabic: "العربية",
        // END PAGE BASE
        // START PAGE INDEX
        // SECTION LANDING
        coach_data: "أحمد طنطاوي أخصائي تغذية معتمد ومدرب صحي معتمد",
        // SCTION HEALTHY 
        improve: "حسن صحتك ، تحسن حياتك",
        // SCTION SERVICES
        services: "خدماتي",
        // SCTION TESTIMONIALS
        testimonials: "أراء عائلتنا",
        // END PAGE INDEX
    },
};
const languageSelector = document.querySelector("select");
languageSelector.addEventListener("change", (event) => {
    setLanguage(event.target.value);
    localStorage.setItem('lang', event.target.value)
});

const setLanguage = (language) => {
    const elements = document.querySelectorAll("[data-i18n]");
    elements.forEach((element) => {
        const translationKey = element.getAttribute("data-i18n");
        element.textContent = translations[language][translationKey];
    });
    document.dir = language === "ar" ? "rtl" : "ltr";
}


// END MULTI LANGUAGE