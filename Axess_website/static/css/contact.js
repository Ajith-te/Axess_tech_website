const rangeInput = document.getElementById("myRange");
const selectedValue = document.getElementById("selectedValue");

rangeInput.addEventListener("input", function() {
  const value = rangeInput.value;
  const formattedValue = formatValue(value);
  selectedValue.textContent = formattedValue;
});

function formatValue(value) {
  const minValue = 1500;
  const maxValue = 7500;
  const minDisplayValue = 1500;
  const maxDisplayValue = 7500;

  const range = maxValue - minValue;
  const displayRange = maxDisplayValue - minDisplayValue;
  const scaledValue = (value / range) * displayRange;
  const formattedValue = scaledValue + minDisplayValue;

  return formattedValue.toLocaleString("en-US", { style: "currency", currency: "USD" });
}
