const goToInfoButton = document.getElementById("go-to-more-info");
const goToDownloadButton = document.getElementById("go-to-download");
const goToUpButton = document.getElementById("go-to-up");

const infoSection = document.getElementById("info-section");
const downloadSection = document.getElementById("download-section");
const welcomeSection = document.getElementById("welcome-section");

goToInfoButton.addEventListener("click", () => {
  infoSection.scrollIntoView({ behavior: "smooth" });
});

goToDownloadButton.addEventListener("click", () => {
  downloadSection.scrollIntoView({ behavior: "smooth" });
});

goToUpButton.addEventListener("click", () => {
  welcomeSection.scrollIntoView({ behavior: "smooth" });
});
