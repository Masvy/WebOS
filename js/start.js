document.addEventListener("DOMContentLoaded", function () {
  const themeToggle = document.getElementById("themeToggle");
  const body = document.body;
  const gif1 = document.getElementById("gif1");
  const gif2 = document.getElementById("gif2");
  const fire1 = document.getElementById("fire1");
  const fire2 = document.getElementById("fire2");

  themeToggle.addEventListener("click", function () {
    body.classList.toggle("dark");
    body.classList.toggle("light");
    const currentTheme = body.classList.contains("dark") ? "Light" : "Dark";
    themeToggle.textContent = `${currentTheme}`;

    if (currentTheme === "Dark") {
      gif1.src = "img/o_light.gif";
      gif2.src = "img/s_light.gif";
    } else {
      gif1.src = "img/o_dark.gif";
      gif2.src = "img/s_dark.gif";
    }

    if (currentTheme === "Dark") {
      fire1.src = "img/fire_light.gif";
      fire2.src = "img/fire_light.gif";
    } else {
      fire1.src = "img/fire_dark.gif";
      fire2.src = "img/fire_dark.gif";
    }
  });
});
