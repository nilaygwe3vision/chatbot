import React from 'react'
import { Bot, User } from 'lucide-react'

export default function ChatMessage({ role, content }) {
  const isUser = role === 'user'
  return (
    <div className={`message-row ${isUser ? 'user-row' : 'assistant-row'}`}>
      <div className={`avatar ${isUser ? 'user-avatar' : 'bot-avatar'}`}>
        {isUser ? <User size={17} /> : <Bot size={18} />}
      </div>
      <div className={`message-bubble ${isUser ? 'user-bubble' : 'assistant-bubble'}`}>
        <div className="message-label">{isUser ? 'You' : 'Assistant'}</div>
        <div className="message-content">{content}</div>
      </div>
    </div>
  )
}
