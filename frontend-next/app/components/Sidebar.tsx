import { motion, AnimatePresence } from 'motion/react';
import { MessageSquarePlus, Trash2, Menu, X } from 'lucide-react';
import { Chat } from './ChatApp';

interface SidebarProps {
  isOpen: boolean;
  onToggle: () => void;
  chats: Chat[];
  currentChatId: string;
  onSelectChat: (id: string) => void;
  onNewChat: () => void;
  onDeleteChat: (id: string) => void;
}

export function Sidebar({
  isOpen,
  onToggle,
  chats,
  currentChatId,
  onSelectChat,
  onNewChat,
  onDeleteChat,
}: SidebarProps) {
  return (
    <>
      {/* Mobile overlay */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onToggle}
            className="fixed inset-0 bg-black/30 z-40 lg:hidden"
          />
        )}
      </AnimatePresence>

      {/* Sidebar */}
      <motion.aside
        initial={false}
        animate={{ x: isOpen ? 0 : -320 }}
        transition={{ type: 'spring', damping: 25, stiffness: 200 }}
        className="fixed lg:relative z-50 h-full w-80 bg-white/80 backdrop-blur-md border-r border-[#C9D4BE] flex flex-col shadow-xl lg:shadow-none"
      >
        {/* Header */}
        <div className="p-4 border-b border-[#C9D4BE] bg-gradient-to-r from-[#B8C9A8]/30 to-[#C9D4BE]/30">
          <div className="flex items-center justify-between mb-4">
            <h2 className="font-semibold text-[#4A5D3F]">Chat History</h2>
            <button
              onClick={onToggle}
              className="lg:hidden p-2 hover:bg-[#B8C9A8]/30 rounded-lg transition-colors"
            >
              <X className="w-5 h-5 text-[#6B7F5C]" />
            </button>
          </div>
          <motion.button
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            onClick={onNewChat}
            className="w-full bg-gradient-to-br from-[#B8C9A8] to-[#A8B89D] text-[#3A4A31] px-4 py-3 rounded-xl font-medium shadow-md hover:shadow-lg transition-all flex items-center justify-center gap-2"
          >
            <MessageSquarePlus className="w-5 h-5" />
            New Chat
          </motion.button>
        </div>

        {/* Chat List */}
        <div className="flex-1 overflow-y-auto p-3 space-y-2 [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none]">
          {chats.map((chat) => (
            <motion.div
              key={chat.id}
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              className={`group relative p-3 rounded-xl cursor-pointer transition-all ${
                currentChatId === chat.id
                  ? 'bg-gradient-to-br from-[#B8C9A8]/40 to-[#A8B89D]/40 shadow-md'
                  : 'hover:bg-[#F0F4ED]'
              }`}
              onClick={() => onSelectChat(chat.id)}
            >
              <div className="flex items-start justify-between gap-2">
                <div className="flex-1 min-w-0">
                  <h3 className="font-medium text-[#4A5D3F] text-sm truncate">
                    {chat.title}
                  </h3>
                  <p className="text-xs text-[#6B7F5C] truncate mt-1">
                    {chat.lastMessage || 'No messages yet'}
                  </p>
                  <p className="text-xs text-[#9AA88C] mt-1">
                    {formatTimestamp(chat.timestamp)}
                  </p>
                </div>
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    onDeleteChat(chat.id);
                  }}
                  className="opacity-0 group-hover:opacity-100 p-1.5 hover:bg-red-100 rounded-lg transition-all"
                >
                  <Trash2 className="w-4 h-4 text-red-600" />
                </button>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-[#C9D4BE] bg-gradient-to-r from-[#F0F4ED] to-[#F5F8F2]">
          <p className="text-xs text-[#6B7F5C] text-center">
            AI Assistant • Nature Theme
          </p>
        </div>
      </motion.aside>
    </>
  );
}

function formatTimestamp(date: Date): string {
  const now = new Date();
  const diff = now.getTime() - date.getTime();
  const minutes = Math.floor(diff / 60000);
  const hours = Math.floor(diff / 3600000);
  const days = Math.floor(diff / 86400000);

  if (minutes < 1) return 'Just now';
  if (minutes < 60) return `${minutes}m ago`;
  if (hours < 24) return `${hours}h ago`;
  if (days < 7) return `${days}d ago`;
  return date.toLocaleDateString();
}