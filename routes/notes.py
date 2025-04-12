from flask import Blueprint, flash, redirect, render_template, request, url_for
from models.notes import Notes

notes_bp = Blueprint("notes", __name__)


@notes_bp.route("/notes", methods=["GET", "POST"])
def notes():

    if len(Notes.get_all_notes()) < 1:
        Notes.reset_notes()

    if request.method == "POST":
        note_title = request.form.get("new-note-input")
        clicked_note = request.form.get("clicked-note")
        save_change_id = request.form.get("current-note")
        delete_note_id = request.form.get("delete-confirm-id")

        if note_title:
            Notes.add_note(note_title)
            flash(f'"{str(note_title)}" added!.', "success")

        if clicked_note:
            Notes.mark_as_selected(clicked_note)

        if save_change_id:
            new_title = request.form.get("new-title")
            note_content = request.form.get("note-content")
            Notes.update_note(save_change_id, new_title, note_content)
            flash(f'"{str(new_title)}" updated!', "success")

        if delete_note_id:
            note_to_delete = request.form.get("delete-confirm-title")
            Notes.delete_note(delete_note_id)
            flash(f'"{note_to_delete}" deleted!', "danger")

        return redirect(url_for("notes.notes"))

    try:
        loaded = Notes.get_selected_note()[0]
    except:
        loaded = {}

    return render_template("notes.djhtml", notes=Notes.get_all_notes(), loaded=loaded)
