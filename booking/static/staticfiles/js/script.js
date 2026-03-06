// Simple JS for your booking project

// Example: Alert on booking button click
document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll("button");
    
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            alert("Booking request submitted!");
        });
    });
});

// Example: Simple form validation
const bookingForm = document.querySelector("form");
if (bookingForm) {
    bookingForm.addEventListener("submit", function(e) {
        const name = bookingForm.querySelector("input[name='name']");
        if (name && name.value.trim() === "") {
            e.preventDefault();
            alert("Please enter your name!");
            name.focus();
        }
    });
}