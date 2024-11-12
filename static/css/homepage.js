 document.addEventListener("DOMContentLoaded", function() {
        const seeMoreButtons = document.querySelectorAll(".see-more-btn");

        seeMoreButtons.forEach(button => {
            button.addEventListener("click", function() {
                const descriptionText = this.previousElementSibling;
                const fullText = descriptionText.getAttribute("data-full-text");

                if (descriptionText.textContent === fullText) {
                    descriptionText.textContent = fullText.slice(0, 200) + "...";
                    this.textContent = "See More";
                } else {
                    descriptionText.textContent = fullText;
                    this.textContent = "See Less";
                }
            });
        });
    });
