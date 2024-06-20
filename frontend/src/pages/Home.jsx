import { useEffect, useState } from "react"
import api from "../api"
import Note from "../components/Note"
import "../styles/Home.css"
export default function Home() {
    const [notes, setNotes] = useState([])
    const [content, setContent] = useState("")
    const [title, setTitle] = useState("")


    const getNote = async () => {
        try {
            const res = await api.get("/api/notes/")
            console.log(res)
            if (res.statusText !== "OK") throw new Error("fetch failed")
            console.log(res.data)
            setNotes(res.data)
        }
        catch (error) {
            alert(error)
        }

    }

    const deleteNote = (id) => {
        api.delete(`/api/notes/delete/${id}`).
            then((res) => {
                if (res.status === 204) alert("Note deleted!")
                else alert("Failed to delete note.")
                getNote() //put here so it fetches the update right away
            }).catch((err) => alert(err))
    }

    useEffect(() => {
        getNote()

    }, [])

    const createNote = (e) => {
        e.preventDefault()
        api.post("/api/notes/", { content, title }).then((res) => {
            if (res.status === 201) alert("Note created")
            else alert("Failed to make notes")
            getNote();
        }).catch((err) => alert(err));
    }



    return (
        <div>
            <h2 className="header">Notes</h2>
            {notes.map(note => <Note note={note} onDelete={deleteNote} key={note.id} />)}
            <form onSubmit={createNote}>
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)}
                    value={title}
                />

                <label htmlFor="content">Title:</label>
                <br />
                <textarea
                    id="content"
                    name="content"
                    required
                    onChange={(e) => setContent(e.target.value)}
                    value={content}
                />
                <br></br>
                <input type="submit" value="Submit" />
            </form>
        </div>
    )




}