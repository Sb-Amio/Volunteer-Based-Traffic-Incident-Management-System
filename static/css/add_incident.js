
function validateImage() {
    const fileInput = document.getElementById("id_image");
    const file = fileInput.files[0];
    const maxSize = 6 * 1024 * 1024;

    if (file) {
        const fileType = file.type;
        const validTypes = ["image/jpeg", "image/jpg", "image/png"];

        if (!validTypes.includes(fileType)) {
            alert("Please upload a valid image file (.jpg, .jpeg, .png).");
            return false;
        }

        if (file.size > maxSize) {
            alert("The file is too large. Maximum size is 6 MB.");
            return false;
        }
    }
    return true;
}
