document.addEventListener("DOMContentLoaded", () => {
	console.log("Script index cargado");

	// INFO: Get url from button attribute and redirect to notes page when click it
	const button = document.getElementById("btn-continue");
	if (button) {
		button.addEventListener("click", () => {
			const url = button.getAttribute("data-url");
			window.location.href = url;
		});
	}
});
