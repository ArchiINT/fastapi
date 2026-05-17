import { useState } from 'react'
import ItemForm from './ItemForm'

export default function ItemList({ items, onUpdate, onDelete }) {
  const [editingId, setEditingId] = useState(null)

  return (
    <ul className="item-list">
      {items.map((item) => (
        <li key={item.id}>
          {editingId === item.id ? (
            <ItemForm
              initial={item}
              onSubmit={(data) => {
                onUpdate(item.id, data)
                setEditingId(null)
              }}
              onCancel={() => setEditingId(null)}
            />
          ) : (
            <>
              <span className="item-title">
                <span className="item-id">#{item.id}</span>
                {item.title}
              </span>
              <div className="item-actions">
                <button onClick={() => setEditingId(item.id)}>Edit</button>
                <button onClick={() => onDelete(item.id)} className="btn-danger">
                  Delete
                </button>
              </div>
            </>
          )}
        </li>
      ))}
    </ul>
  )
}
