
import React, { useRef, useState, useEffect } from 'react'
import { Bot, Send, Sparkles, Trash2 } from 'lucide-react'
import ChatMessage from './components/ChatMessage.jsx'
import { sendChatMessage } from './services/chatApi.js'

const welcome = {
  role: 'assistant',
  content:
    'Hi! I’m your AI chatbot. Ask me a question and I’ll do my best to help.',
}

export default function App() {
  const [messages, setMessages] = useState([welcome])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const endRef = useRef(null)

  // Scroll to the latest message.
  useEffect(() => {
    endRef.current?.scrollIntoView({
      behavior: 'smooth',
      block: 'end',
    })
  }, [messages, loading])

  async function handleSubmit(event) {
    event.preventDefault()

    const text = input.trim()

    if (!text || loading) {
      return
    }

    // Exclude the initial welcome message from conversation history.
    const history = messages
      .slice(1)
      .map(({ role, content }) => ({ role, content }))

    setMessages((previous) => [
      ...previous,
      { role: 'user', content: text },
    ])

    setInput('')
    setError('')
    setLoading(true)

    try {
      const reply = await sendChatMessage(text, history)

      setMessages((previous) => [
        ...previous,
        {
          role: 'assistant',
          content: reply || 'I could not generate a response. Please try again.',
        },
      ])
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : 'Unable to connect to the chatbot server.'
      )
    } finally {
      setLoading(false)
    }
  }

  function clearChat() {
    setMessages([welcome])
    setError('')
    setInput('')
  }

  return (
    <main className="app-shell">
      <section className="chat-card">
        <header className="topbar">
          <div className="brand-mark">
            <Bot size={24} />
          </div>

          <div className="brand-copy">
            <h1>AI Chatbot</h1>
            <p>
              <span className="online-dot" />
              {loading ? 'Generating response...' : 'Ready to help'}
            </p>
          </div>

          <button
            type="button"
            className="clear-button"
            onClick={clearChat}
            title="Clear conversation"
            aria-label="Clear conversation"
          >
            <Trash2 size={18} />
          </button>
        </header>

        <div className="chat-body">
          <div className="intro">
            <div className="intro-icon">
              <Sparkles size={20} />
            </div>

            <h2>How can I help you today?</h2>
            <p>Ask a question to get started.</p>
          </div>

          <div className="messages" aria-live="polite">
            {messages.map((message, index) => (
              <ChatMessage
                key={`${index}-${message.role}`}
                role={message.role}
                content={message.content}
              />
            ))}

            {loading && (
              <div className="typing" role="status">
                <span />
                <span />
                <span />
                <small>Thinking...</small>
              </div>
            )}

            {error && (
              <div className="error-message" role="alert">
                {error}
              </div>
            )}

            <div ref={endRef} />
          </div>
        </div>

        <form className="composer" onSubmit={handleSubmit}>
          <textarea
            value={input}
            onChange={(event) => setInput(event.target.value)}
            onKeyDown={(event) => {
              if (
                event.key === 'Enter' &&
                !event.shiftKey &&
                !event.nativeEvent.isComposing
              ) {
                event.preventDefault()

                if (input.trim() && !loading) {
                  event.currentTarget.form?.requestSubmit()
                }
              }
            }}
            placeholder="Type your question here..."
            rows={1}
            maxLength={12000}
            aria-label="Your question"
            disabled={loading}
          />

          <button
            type="submit"
            disabled={!input.trim() || loading}
            aria-label="Send message"
          >
            <Send size={18} />
          </button>
        </form>

        <footer className="footnote">
          AI can make mistakes. Check important information.
        </footer>
      </section>
    </main>
  )
}
