import { useState, useEffect } from 'react'
import axios from 'axios'


function App() {
  const [events, setEvents] = useState([])

  useEffect(() => {
    axios
      .get('http://localhost:8000/data/events/')
      .then((response) => {
        setEvents(response.data)
      })
  }, [])

  return (
    <div>
      <h1>Kalenteri</h1>

      {events.map((event) => (
        <p key={event.id}>
          {event.title}
        </p>
      ))}
    </div>
  )
}

export default App
