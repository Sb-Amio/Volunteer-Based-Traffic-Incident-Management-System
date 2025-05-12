function validateImage() {
    // Get the file input field
    var fileInput = document.getElementById('id_image');
    var file = fileInput.files[0]; // Get the selected file

    // If no file is selected, allow the form to submit
    if (!file) {
        return true;
    }

    // Check if the file size exceeds 6 MB (6 * 1024 * 1024 bytes)
    var maxSize = 6 * 1024 * 1024; // 6 MB in bytes
    if (file.size > maxSize) {
        // Display error message
        var errorMessage = document.getElementById('image-error');
        errorMessage.style.display = 'block'; // Show the error message
        errorMessage.textContent = 'The image is too large. Maximum size is 6 MB.';

        // Prevent form submission
        return false;
    }

    // Hide the error message if file is valid
    var errorMessage = document.getElementById('image-error');
    errorMessage.style.display = 'none';
    return true;
}
