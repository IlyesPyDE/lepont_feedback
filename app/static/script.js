const value = document.querySelector("#ratingvalue");
const input = document.querySelector("#rating");
value.textContent = input.value;
input.addEventListener("input", (event) => {
  value.textContent = event.target.value;
});