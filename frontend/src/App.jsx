import { useState, useEffect, useCallback } from 'react'
import { getItems, createItem, updateItem, deleteItem } from './api/items'
import ItemForm from './components/ItemForm'
import ItemList from './components/ItemList'
import './App.css'

export default function App() {
  const [items, setItems] = useState([])
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(true)

  const fetchItems = useCallback(async () => {
    try {
      setError(null)
      const data = await getItems()
      setItems(data)
    } catch (e) {
      setError(e.message)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => { fetchItems() }, [fetchItems])

  async function handleCreate(data) {
    try {
      const item = await createItem(data)
      setItems((prev) => [...prev, item])
    } catch (e) {
      setError(e.message)
    }
  }

  async function handleUpdate(id, data) {
    try {
      const item = await updateItem(id, data)
      setItems((prev) => prev.map((i) => (i.id === id ? item : i)))
    } catch (e) {
      setError(e.message)
    }
  }

  async function handleDelete(id) {
    try {
      await deleteItem(id)
      setItems((prev) => prev.filter((i) => i.id !== id))
    } catch (e) {
      setError(e.message)
    }
  }

  return (
    <div className="container">
      <h1>Items</h1>
      <ItemForm onSubmit={handleCreate} />
      {error && <p className="error">{error}</p>}
      {loading ? (
        <p className="hint">Loading...</p>
      ) : items.length === 0 ? (
        <p className="hint">No items yet. Add one above.</p>
      ) : (
        <ItemList items={items} onUpdate={handleUpdate} onDelete={handleDelete} />
      )}
    </div>
  )
}
