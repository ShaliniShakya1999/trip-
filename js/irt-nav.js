(function () {
  function init() {
    var menuBtn = document.getElementById("irt-mobile-menu-btn");
    var mobileNav = document.getElementById("irt-mobile-nav");
    if (!menuBtn || !mobileNav) return;
    menuBtn.addEventListener("click", function () {
      mobileNav.classList.toggle("hidden");
      var open = !mobileNav.classList.contains("hidden");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    mobileNav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        mobileNav.classList.add("hidden");
        menuBtn.setAttribute("aria-expanded", "false");
      });
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
