document.addEventListener("DOMContentLoaded", () => {
  const burger = document.getElementById("burger");
  const mobileNav = document.getElementById("mobile-nav");

  burger.addEventListener("change", () => {
    mobileNav.classList.toggle("show");
  });
});
