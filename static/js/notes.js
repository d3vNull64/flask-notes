document.addEventListener("DOMContentLoaded", () => {
	console.log("Script notes loaded");

	// Disable submit when key enter is pressed
	document
		.getElementById("new-note-form")
		.addEventListener("submit", (event) => {
			event.preventDefault();
		});

	// this function submit de form for add new note
	const submitNewNote = () => {
		let note_title = document.getElementById("new-note-input").value;
		if (note_title != "") document.getElementById("new-note-form").submit();
	};

	// This code execute de submit function when key enter is pressed
	document
		.getElementById("new-note-form")
		.addEventListener("keypress", (event) => {
			let key = event.key;
			if (key === "Enter") {
				submitNewNote();
			}
		});

	// This code execute de submit function when add button is clicked
	document.getElementById("btn-new-note").addEventListener("click", () => {
		submitNewNote();
	});

	// Set focus to textarea when one a note is loaded
	let focused = document
		.getElementById("note-content")
		.getAttribute("data-focus");
	if (focused) {
		setTimeout(() => {
			document.getElementById("note-content").focus();
		}, 100);
	}

	// This code make submit when a note in list is clicked
	const clickedNote = document.querySelectorAll(".list-group-item");
	clickedNote.forEach((button) => {
		button.addEventListener("click", () => {
			document.getElementById("clicked-note").value = button.id.split("-")[1];
			document.getElementById("notes-list-form").submit();
			setTimeout(() => {
				document.getElementById("notes-list-form").reser();
			}, 100);
		});
	});

	// This code dismiss the alert after few seconds
	setTimeout(() => {
		const my_alert = document.getElementById("alert");
		if (my_alert) {
			bootstrap.Alert.getOrCreateInstance(my_alert).close();
		}
	}, 3000);

	// Prevent submit when press enter into input title in the right section
	const noteContentForm = document.getElementById("controls-note-form");
	noteContentForm.addEventListener("submit", (event) => {
		event.preventDefault();
	});

	// Set focus to text area when key ENTER is pressed into input title in the right section
	const newTitleInput = document.getElementById("new-title");
	newTitleInput.addEventListener("keypress", (event) => {
		if (event.key === "Enter") {
			setTimeout(() => {
				document.getElementById("note-content").focus();
			}, 100);
		}
	});

	// Get current displayed note id and submit for save change
	const noteToSave = document.querySelector(".btn-save");
	noteToSave.addEventListener("click", () => {
		document.getElementById("current-note").value = noteToSave.id.split("-")[2];
		document.getElementById("controls-note-form").submit();
	});

	//Get id when modal delete is confirmed
	const deleteConfirmation = document.querySelector(".btn-delete");
	deleteConfirmation.addEventListener("click", () => {
		document.getElementById("delete-confirm-id").value =
			deleteConfirmation.id.split("-")[2];
		document.getElementById("delete-confirmation-form").submit();
	});
});
