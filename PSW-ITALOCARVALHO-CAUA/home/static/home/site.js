document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.querySelector(".menu-toggle");
    const nav = document.querySelector(".primary-nav");
    if (!toggle || !nav) return;
    toggle.addEventListener("click", function () {
        const isOpen = toggle.getAttribute("aria-expanded") === "true";
        toggle.setAttribute("aria-expanded", String(!isOpen));
        toggle.setAttribute("aria-label", isOpen ? "Abrir menu" : "Fechar menu");
        nav.classList.toggle("is-open", !isOpen);
    });
});
