const swiper = new Swiper(".swiper", {
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  slidesPerView: 4,
  spaceBetween: 20,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    300: {
      slidesPerView: 1
    },
    400: {
      slidesPerView: 1
    },
    807: {
      slidesPerView: 2
    },
    1000: {
      slidesPerView: 3
    }
  }
});

const burgerBtn = document.querySelector("header svg");
const burger = document.querySelector(".burger");

burgerBtn.addEventListener("click", () => {
  burgerBtn.classList.toggle("active");
  burger.classList.toggle("active");
  document.body.classList.toggle("active");
})

