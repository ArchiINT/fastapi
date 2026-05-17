import { useState, useEffect } from 'react'

export default function ItemForm({ initial, onSubmit, onCancel }) {
  const [title, setTitle] = useState(initial?.title ?? '')

  useEffect(() => {
    setTitle(initial?.title ?? '')
  }, [initial])

  function handleSubmit(e) {
    e.preventDefault()
    if (!title.trim()) return
    onSubmit({ title: title.trim() })
    setTitle('')
  }

  return (
    <form onSubmit={handleSubmit} className="item-form">
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Item title..."
        autoFocus
      />
      <button type="submit">{initial ? 'Save' : 'Add'}</button>
      {onCancel && (
        <button type="button" onClick={onCancel} className="btn-secondary">
          Cancel
        </button>
      )}
    </form>
  )
}
