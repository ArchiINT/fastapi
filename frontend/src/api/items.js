const BASE = '/api/v1/item'

async function request(url, options = {}) {
  const res = await fetch(url, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!res.ok) {
    const err = await res.json().catch(() => ({}))
    throw new Error(err.detail ?? `HTTP ${res.status}`)
  }
  if (res.status === 204) return null
  return res.json()
}

export const getItems = () => request(BASE)
export const getItem = (id) => request(`${BASE}/${id}`)
export const createItem = (data) => request(BASE, { method: 'POST', body: JSON.stringify(data) })
export const updateItem = (id, data) => request(`${BASE}/${id}`, { method: 'PATCH', body: JSON.stringify(data) })
export const deleteItem = (id) => request(`${BASE}/${id}`, { method: 'DELETE' })
