import { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import {
  Send,
  Paperclip,
  Image as ImageIcon,
  Mic,
  Menu,
  Sparkles,
  ChevronDown,
  Plus,
  X,
  LogOut,
} from 'lucide-react';
import { Message } from './ChatApp';
import { useAuth } from './AuthContext';
import { useRouter } from 'next/navigation';

interface ChatAreaProps {
  isSidebarOpen: boolean;
  onToggleSidebar: () => void;
  selectedModel: string;
  onModelChange: (model: string) => void;
}

const AI_MODELS = [
  'GPT-4',
  'GPT-4 Turbo',
  'GPT-3.5 Turbo',
  'Claude 3 Opus',
  'Claude 3 Sonnet',
  'Gemini Pro',
];

export function ChatArea({
  isSidebarOpen,
  onToggleSidebar,
  selectedModel,
  onModelChange,
}: ChatAreaProps) {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      text: "Hello! I'm your AI assistant. How can I help you today?",
      sender: 'bot',
      timestamp: new Date(),
    },
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [attachedFiles, setAttachedFiles] = useState<File[]>([]);
  const [showModelDropdown, setShowModelDropdown] = useState(false);
  const [showActions, setShowActions] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const imageInputRef = useRef<HTMLInputElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = () => {
    if (!inputValue.trim() && attachedFiles.length === 0) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      text: inputValue,
      sender: 'user',
      timestamp: new Date(),
      files: attachedFiles.map((f) => ({ name: f.name, type: f.type })),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInputValue('');
    setAttachedFiles([]);
    setIsTyping(true);

    // Simulate bot response
    setTimeout(() => {
      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: "I'm here to assist you! This is a demo response. In your production version, this would connect to your actual chatbot backend.",
        sender: 'bot',
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, botMessage]);
      setIsTyping(false);
    }, 1500);
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleFileSelect = (files: FileList | null) => {
    if (files) {
      setAttachedFiles((prev) => [...prev, ...Array.from(files)]);
    }
  };

  const removeFile = (index: number) => {
    setAttachedFiles((prev) => prev.filter((_, i) => i !== index));
  };

  const { logout } = useAuth();
  const router = useRouter();

  const handleLogout = () => {
    logout();
    router.push('/login');
  };

  return (
    <div className="flex-1 flex flex-col h-screen overflow-hidden">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-md border-b border-[#C9D4BE] px-4 py-3 flex items-center justify-between shadow-sm">
        <div className="flex items-center gap-3">
          <button
            onClick={onToggleSidebar}
            className="p-2 hover:bg-[#B8C9A8]/30 rounded-lg transition-colors"
          >
            <Menu className="w-5 h-5 text-[#6B7F5C]" />
          </button>
          <div className="flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-[#6B7F5C]" />
            <h1 className="font-semibold text-[#4A5D3F]">AI Assistant</h1>
          </div>
        </div>

        {/* Model Selector */}
        <div className="flex items-center gap-3">
        <div className="relative">
          <motion.button
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            onClick={() => setShowModelDropdown(!showModelDropdown)}
            className="flex items-center gap-2 px-4 py-2 bg-gradient-to-br from-[#B8C9A8] to-[#A8B89D] text-[#3A4A31] rounded-lg shadow-md hover:shadow-lg transition-all"
          >
            <span className="text-sm font-medium">{selectedModel}</span>
            <ChevronDown className="w-4 h-4" />
          </motion.button>

          <AnimatePresence>
            {showModelDropdown && (
              <>
                <div
                  className="fixed inset-0 z-10"
                  onClick={() => setShowModelDropdown(false)}
                />
                <motion.div
                  initial={{ opacity: 0, y: -10 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -10 }}
                  className="absolute right-0 mt-2 w-48 bg-white rounded-xl shadow-xl border border-[#C9D4BE] overflow-hidden z-20"
                >
                  {AI_MODELS.map((model) => (
                    <button
                      key={model}
                      onClick={() => {
                        onModelChange(model);
                        setShowModelDropdown(false);
                      }}
                      className={`w-full text-left px-4 py-3 text-sm transition-colors ${
                        selectedModel === model
                          ? 'bg-gradient-to-br from-[#B8C9A8]/40 to-[#A8B89D]/40 text-[#3A4A31] font-medium'
                          : 'text-[#5A5A50] hover:bg-[#F0F4ED]'
                      }`}
                    >
                      {model}
                    </button>
                  ))}
                </motion.div>
              </>
            )}
          </AnimatePresence>
        </div>

        {/* Logout Button */}
        <button
          onClick={handleLogout}
          className="p-2 hover:bg-[#B8C9A8]/30 rounded-lg transition-colors"
          title="Logout"
        >
          <LogOut className="w-5 h-5 text-[#6B7F5C]" />
        </button>
        </div>
      </header>

      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto px-4 py-6 space-y-4 [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none]">
        <div className="max-w-5xl mx-auto w-full space-y-4">
        <AnimatePresence initial={false}>
          {messages.map((message) => (
            <motion.div
              key={message.id}
              initial={{ opacity: 0, y: 10, scale: 0.95 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              transition={{ duration: 0.3 }}
              className={`flex ${
                message.sender === 'user' ? 'justify-end' : 'justify-start'
              }`}
            >
              <div
                className={`max-w-[85%] rounded-2xl px-5 py-3 ${
                  message.sender === 'user'
                    ? 'bg-gradient-to-br from-[#B8C9A8] to-[#A8B89D] text-[#3A4A31] shadow-md shadow-[#A8B89D]/30'
                    : 'bg-white/90 text-[#5A5A50] shadow-md shadow-[#E6E6E6]/50'
                }`}
              >
                {message.files && message.files.length > 0 && (
                  <div className="mb-2 space-y-1">
                    {message.files.map((file, index) => (
                      <div
                        key={index}
                        className="text-xs bg-white/30 px-2 py-1 rounded flex items-center gap-1"
                      >
                        <Paperclip className="w-3 h-3" />
                        <span className="truncate">{file.name}</span>
                      </div>
                    ))}
                  </div>
                )}
                <p className="leading-relaxed">{message.text}</p>
                <span className="text-xs opacity-60 mt-1 block">
                  {message.timestamp.toLocaleTimeString([], {
                    hour: '2-digit',
                    minute: '2-digit',
                  })}
                </span>
              </div>
            </motion.div>
          ))}
        </AnimatePresence>

        {isTyping && (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            className="flex justify-start"
          >
            <div className="bg-white/90 rounded-2xl px-5 py-3 shadow-md shadow-[#E6E6E6]/50">
              <div className="flex gap-1.5">
                <motion.div
                  animate={{ y: [0, -8, 0] }}
                  transition={{
                    duration: 0.6,
                    repeat: Infinity,
                    ease: 'easeInOut',
                  }}
                  className="w-2 h-2 bg-[#B8C9A8] rounded-full"
                />
                <motion.div
                  animate={{ y: [0, -8, 0] }}
                  transition={{
                    duration: 0.6,
                    repeat: Infinity,
                    ease: 'easeInOut',
                    delay: 0.2,
                  }}
                  className="w-2 h-2 bg-[#B8C9A8] rounded-full"
                />
                <motion.div
                  animate={{ y: [0, -8, 0] }}
                  transition={{
                    duration: 0.6,
                    repeat: Infinity,
                    ease: 'easeInOut',
                    delay: 0.4,
                  }}
                  className="w-2 h-2 bg-[#B8C9A8] rounded-full"
                />
              </div>
            </div>
          </motion.div>
        )}

        <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Input Area */}
      <div className="bg-white/80 backdrop-blur-md border-t border-[#C9D4BE] p-4">
        <div className="max-w-5xl mx-auto w-full">
        {/* Attached Files Preview */}
        {attachedFiles.length > 0 && (
          <div className="mb-3 flex flex-wrap gap-2">
            {attachedFiles.map((file, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                className="bg-[#F0F4ED] px-3 py-2 rounded-lg flex items-center gap-2 text-sm"
              >
                <Paperclip className="w-4 h-4 text-[#6B7F5C]" />
                <span className="text-[#4A5D3F] max-w-[150px] truncate">
                  {file.name}
                </span>
                <button
                  onClick={() => removeFile(index)}
                  className="text-red-600 hover:text-red-800 ml-1"
                >
                  ×
                </button>
              </motion.div>
            ))}
          </div>
        )}

        <div className="flex gap-3 items-end">
          {/* Action Buttons */}
          <div className="relative">
            {/* Plus Button */}
            <motion.button
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.9 }}
              onClick={() => setShowActions(!showActions)}
              className="p-3 bg-white hover:bg-[#F0F4ED] rounded-xl border border-[#C9D4BE] transition-colors"
              title="Options"
            >
              {showActions ? (
                <X className="w-5 h-5 text-[#6B7F5C]" />
              ) : (
                <Plus className="w-5 h-5 text-[#6B7F5C]" />
              )}
            </motion.button>

            {/* Hidden Action Buttons */}
            <AnimatePresence>
              {showActions && (
                <>
                  <div
                    className="fixed inset-0 z-10"
                    onClick={() => setShowActions(false)}
                  />
                  <motion.div
                    initial={{ opacity: 0, y: 10, scale: 0.9 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    exit={{ opacity: 0, y: 10, scale: 0.9 }}
                    className="absolute bottom-full mb-2 left-0 bg-white rounded-xl shadow-xl border border-[#C9D4BE] p-2 flex flex-col gap-2 z-20"
                  >
                    <input
                      ref={fileInputRef}
                      type="file"
                      multiple
                      className="hidden"
                      onChange={(e) => {
                        handleFileSelect(e.target.files);
                        setShowActions(false);
                      }}
                    />
                    <input
                      ref={imageInputRef}
                      type="file"
                      accept="image/*"
                      multiple
                      className="hidden"
                      onChange={(e) => {
                        handleFileSelect(e.target.files);
                        setShowActions(false);
                      }}
                    />

                    <motion.button
                      whileHover={{ scale: 1.05 }}
                      whileTap={{ scale: 0.95 }}
                      onClick={() => {
                        fileInputRef.current?.click();
                      }}
                      className="p-3 hover:bg-[#F0F4ED] rounded-lg transition-colors flex items-center gap-2 min-w-[140px]"
                      title="Attach file"
                    >
                      <Paperclip className="w-5 h-5 text-[#6B7F5C]" />
                      <span className="text-sm text-[#4A5D3F]">Attach File</span>
                    </motion.button>

                    <motion.button
                      whileHover={{ scale: 1.05 }}
                      whileTap={{ scale: 0.95 }}
                      onClick={() => {
                        imageInputRef.current?.click();
                      }}
                      className="p-3 hover:bg-[#F0F4ED] rounded-lg transition-colors flex items-center gap-2"
                      title="Attach image"
                    >
                      <ImageIcon className="w-5 h-5 text-[#6B7F5C]" />
                      <span className="text-sm text-[#4A5D3F]">Attach Image</span>
                    </motion.button>

                    <motion.button
                      whileHover={{ scale: 1.05 }}
                      whileTap={{ scale: 0.95 }}
                      onClick={() => setShowActions(false)}
                      className="p-3 hover:bg-[#F0F4ED] rounded-lg transition-colors flex items-center gap-2"
                      title="Voice input"
                    >
                      <Mic className="w-5 h-5 text-[#6B7F5C]" />
                      <span className="text-sm text-[#4A5D3F]">Voice Input</span>
                    </motion.button>
                  </motion.div>
                </>
              )}
            </AnimatePresence>
          </div>

          {/* Text Input */}
          <div className="flex-1 bg-white rounded-2xl shadow-md border border-[#C9D4BE] overflow-hidden">
            <textarea
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Type your message..."
              className="w-full px-5 py-3 resize-none outline-none bg-transparent text-[#5A5A50] placeholder-[#9AA88C] max-h-32"
              rows={1}
            />
          </div>

          {/* Send Button */}
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={handleSend}
            disabled={!inputValue.trim() && attachedFiles.length === 0}
            className="bg-gradient-to-br from-[#B8C9A8] to-[#A8B89D] p-4 rounded-2xl shadow-lg shadow-[#A8B89D]/40 disabled:opacity-50 disabled:cursor-not-allowed hover:shadow-xl transition-shadow"
          >
            <Send className="w-5 h-5 text-[#3A4A31]" />
          </motion.button>
        </div>
        </div>
      </div>
    </div>
  );
}