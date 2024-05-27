function toggleDarkmode() {
  var element = document.body;
  element.classList.toggle("dark-mode");

  var darkMode = element.classList.contains("dark-mode");
  localStorage.setItem('darkMode', darkMode);

  var image_as_button = document.getElementById('duck_no_sunglasses_image_as_button');
    if (darkMode) {
        image_as_button.src = "static/assets/duck_win_sunglasses.png";
    } else {
        image_as_button.src = "static/assets/duck_win_no_sunglasses.png";
    }
}

window.onload = function() {
  var darkMode = localStorage.getItem('darkMode') === 'true';
  document.body.classList.toggle("dark-mode", darkMode);

  // Add event listener to the image button
  const darkModeToggle = document.getElementById('duck_no_sunglasses_image_as_button');
  darkModeToggle.addEventListener('click', toggleDarkmode);
}
