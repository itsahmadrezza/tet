// Home Swiper
var homeSwiper = new Swiper(".home-swiper", {
    spaceBetween: 30,
    loop: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });


document.getElementById('tt').onclick = main;

function main() {
  window.navigator.vibrate([300, 100, 200, 50, 300]);
  alert("اطلاعات دریافت شد")
  window.navigator.vibrate([300, 100, 200, 50, 300]);
  alert("به زودی با شما تماس خواهیم گرفت")
  window.navigator.vibrate([300, 100, 200, 50, 300,300, 100, 200, 50, 300]);
  alert("🤑🤑🤑قیمت دوره ۱۴ میلیون تومان")
}  