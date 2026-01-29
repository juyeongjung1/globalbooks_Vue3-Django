
import type { Book } from '../types/Book' // Assumption: Interface might be needed here or declared inline. I'll declare inline to be self-contained for starter.

export interface Book {
    id?: number
    title: string
    author: string
    price: number
    publisher?: string | null
    image_path?: string | null
}

const BASE_URL = 'http://localhost:8001/api/books/'

export async function getAllBooks(): Promise<Book[]> {
    const response = await fetch(BASE_URL)
    if (!response.ok) {
        throw new Error('Failed to fetch books')
    }
    return response.json()
}

export async function getBook(id: number): Promise<Book> {
    const response = await fetch(`${BASE_URL}${id}/`)
    if (!response.ok) {
        throw new Error('Failed to fetch book')
    }
    return response.json()
}

export async function createBook(book: Book): Promise<Book> {
    const response = await fetch(BASE_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(book)
    })
    if (!response.ok) {
        throw new Error('Failed to create book')
    }
    return response.json()
}

export async function updateBook(id: number, book: Book): Promise<Book> {
    const response = await fetch(`${BASE_URL}${id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(book)
    })
    if (!response.ok) {
        throw new Error('Failed to update book')
    }
    return response.json()
}

export async function deleteBook(id: number): Promise<void> {
    const response = await fetch(`${BASE_URL}${id}/`, {
        method: 'DELETE'
    })
    if (!response.ok) {
        throw new Error('Failed to delete book')
    }
}
