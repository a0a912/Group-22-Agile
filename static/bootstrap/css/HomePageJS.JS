function toggleDarkmode() {
    var element = document.body;
    element.classList.toggle("dark-mode");

    localStorage.setItem('darkMode', element.classList.contains("dark-mode"));
  }
  window.onload = function() {
    var darkMode = localStorage.getItem('darkMode') === 'true';
    document.body.classList.toggle("dark-mode", darkMode);
}
  const darkModeToggle = document.getElementById('DarkModeToggle');
  darkModeToggle.addEventListener('click', toggleDarkmode);
