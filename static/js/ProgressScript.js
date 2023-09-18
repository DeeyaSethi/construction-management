// Function to update the countdown timer
function updateCountdown() {
  const deadline = new Date("2023-12-31").getTime(); // Set your project completion date here
  const now = new Date().getTime();
  const timeDifference = deadline - now;

  const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
  const hours = Math.floor(
    (timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
  );
  const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

  document.getElementById("days").textContent = days
    .toString()
    .padStart(2, "0");
  document.getElementById("hours").textContent = hours
    .toString()
    .padStart(2, "0");
  document.getElementById("minutes").textContent = minutes
    .toString()
    .padStart(2, "0");
  document.getElementById("seconds").textContent = seconds
    .toString()
    .padStart(2, "0");

  // Check if the deadline has passed
  if (timeDifference < 0) {
    clearInterval(countdownInterval);
    document.getElementById("countdown-timer").textContent =
      "Project Completed!";
  }
}

// Initial call to update the countdown
updateCountdown();

// Update the countdown every second
const countdownInterval = setInterval(updateCountdown, 1000);
