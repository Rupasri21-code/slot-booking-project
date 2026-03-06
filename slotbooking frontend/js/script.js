function bookSlot(){

fetch("https://slot-booking-project.onrender.com")

.then(response => response.text())

.then(data => {
document.getElementById("result").innerHTML = "Connected to Backend!";
});

}