"use client";

import { useState } from 'react';
import { Sidebar } from './Sidebar';
import { ChatArea } from './ChatArea';

export interface Chat {
  id: string;
  title: string;
  lastMessage: string;
  timestamp: Date;
}

export interface Message {
  id: string;
  text: string;
  sender: 'user' | 'bot';
  timestamp: Date;
  files?: { name: string; type: string }[];
}

export function ChatApp() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [chats, setChats] = useState<Chat[]>([
    {
      id: '1',
      title: 'Project Planning Discussion',
      lastMessage: 'Can you help me with that?',
      timestamp: new Date(Date.now() - 1000 * 60 * 30),
    },
    {
      id: '2',
      title: 'Code Review Questions',
      lastMessage: 'Thanks for the explanation!',
      timestamp: new Date(Date.now() - 1000 * 60 * 60 * 2),
    },
    {
      id: '3',
      title: 'Documentation Help',
      lastMessage: 'How do I document this API?',
      timestamp: new Date(Date.now() - 1000 * 60 * 60 * 24),
    },
  ]);
  const [currentChatId, setCurrentChatId] = useState<string>('1');
  const [selectedModel, setSelectedModel] = useState('GPT-4');

  const handleNewChat = () => {
    const newChat: Chat = {
      id: Date.now().toString(),
      title: 'New Conversation',
      lastMessage: '',
      timestamp: new Date(),
    };
    setChats([newChat, ...chats]);
    setCurrentChatId(newChat.id);
  };

  const handleDeleteChat = (chatId: string) => {
    setChats(chats.filter((chat) => chat.id !== chatId));
    if (currentChatId === chatId && chats.length > 1) {
      setCurrentChatId(chats[0].id === chatId ? chats[1].id : chats[0].id);
    }
  };

  return (
    <div className="h-screen w-screen overflow-hidden bg-gradient-to-br from-[#F0F4ED] via-[#F5F8F2] to-[#E8F0E3] flex">
      <Sidebar
        isOpen={isSidebarOpen}
        onToggle={() => setIsSidebarOpen(!isSidebarOpen)}
        chats={chats}
        currentChatId={currentChatId}
        onSelectChat={setCurrentChatId}
        onNewChat={handleNewChat}
        onDeleteChat={handleDeleteChat}
      />
      <ChatArea
        isSidebarOpen={isSidebarOpen}
        onToggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)}
        selectedModel={selectedModel}
        onModelChange={setSelectedModel}
      />
    </div>
  );
}
