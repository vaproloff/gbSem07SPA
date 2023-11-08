(async function f() {
    async function fetchAndRender() {
        const path = window.location.pathname.split("/");
        const page = path[path.length - 1] || "main";

        try {
            const response = await fetch(`/get-content/${page}`);
            if (response.ok) {
                document.getElementById("content").innerHTML = await response.text();
            } else {
                console.error("Ошибка при обработке запроса");
            }
        } catch (error) {
            console.error("Ошибка при обработке запроса:", error);
        }
    }

    document.querySelectorAll(".menu-item").forEach(function (element) {
        element.addEventListener("click", async function (event) {
            event.preventDefault();
            history.pushState(null, null, element.id !== "main" ? `/${element.id}`: "/");

            await fetchAndRender();
        });
    });

    window.onpopstate = fetchAndRender;

    await fetchAndRender();
})();

