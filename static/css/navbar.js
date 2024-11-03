
  // Check dark mode preference before the page fully loads
  (function() {
    if (localStorage.getItem('darkMode') === 'enabled') {
      document.documentElement.classList.add('dark-mode');
    }
  })();

  function toggleDarkMode() {
    const body = document.documentElement;
    const isDarkMode = body.classList.toggle('dark-mode');

    // Save preference in localStorage
    if (isDarkMode) {
      localStorage.setItem('darkMode', 'enabled');
    } else {
      localStorage.setItem('darkMode', 'disabled');
    }
  }

  // Apply dark mode on page load if it was enabled
  window.onload = function() {
    if (localStorage.getItem('darkMode') === 'enabled') {
      document.getElementById('darkModeSwitch').checked = true;
    }
  };
