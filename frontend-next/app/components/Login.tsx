import { useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { motion } from 'framer-motion';
import { Mail, Lock, Sun, AlertCircle } from 'lucide-react';
import { useAuth } from './AuthContext';

export function Login() {
  const router = useRouter();
  const { login } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const success = await login(email, password);
      if (success) {
        router.replace('/');
      } else {
        setError('Invalid email or password');
      }
    } catch (err) {
      setError('An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex">
      {/* Left Side - Form */}
      <div className="flex-1 flex items-center justify-center p-8 bg-gradient-to-br from-[#F0F4ED] to-[#E8F0E0]">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="w-full max-w-md"
        >
          {/* Logo/Header */}
          <div className="text-center mb-8">
            <motion.div
              initial={{ scale: 0, rotate: -180 }}
              animate={{ scale: 1, rotate: 0 }}
              transition={{ type: 'spring', delay: 0.2, duration: 0.8 }}
              className="inline-flex items-center justify-center w-20 h-20 bg-gradient-to-br from-[#F4D03F] via-[#F5B041] to-[#EB984E] rounded-full mb-4 shadow-2xl relative"
            >
              <motion.div
                animate={{ rotate: 360 }}
                transition={{ duration: 20, repeat: Infinity, ease: 'linear' }}
                className="absolute inset-0 rounded-full"
              >
                <div className="absolute inset-0 rounded-full bg-gradient-to-br from-[#F4D03F]/20 to-transparent blur-xl" />
              </motion.div>
              <Sun className="w-10 h-10 text-white relative z-10 drop-shadow-lg" />
            </motion.div>
            <h1 className="text-3xl font-bold text-[#4A5D3F] mb-2">
              Welcome Back
            </h1>
            <p className="text-[#6B7F5C]">
              Sign in to continue to your AI Assistant
            </p>
          </div>

          {/* Form */}
          <motion.form
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.3 }}
            onSubmit={handleSubmit}
            className="bg-white/70 backdrop-blur-sm rounded-2xl shadow-xl p-8 border border-[#C9D4BE]"
          >
            {error && (
              <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg flex items-center gap-2 text-red-700 text-sm"
              >
                <AlertCircle className="w-4 h-4" />
                {error}
              </motion.div>
            )}

            {/* Email Field */}
            <div className="mb-4">
              <label className="block text-sm font-medium text-[#4A5D3F] mb-2">
                Email Address
              </label>
              <div className="relative">
                <Mail className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-[#6B7F5C]" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  className="w-full pl-10 pr-4 py-3 bg-white border border-[#C9D4BE] rounded-xl outline-none focus:ring-2 focus:ring-[#B8C9A8] focus:border-transparent transition-all text-[#4A5D3F] placeholder-[#9AA88C]"
                  placeholder="you@example.com"
                />
              </div>
            </div>

            {/* Password Field */}
            <div className="mb-6">
              <label className="block text-sm font-medium text-[#4A5D3F] mb-2">
                Password
              </label>
              <div className="relative">
                <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-[#6B7F5C]" />
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  className="w-full pl-10 pr-4 py-3 bg-white border border-[#C9D4BE] rounded-xl outline-none focus:ring-2 focus:ring-[#B8C9A8] focus:border-transparent transition-all text-[#4A5D3F] placeholder-[#9AA88C]"
                  placeholder="••••••••"
                />
              </div>
            </div>

            {/* Submit Button */}
            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              type="submit"
              disabled={loading}
              className="w-full bg-gradient-to-br from-[#B8C9A8] to-[#A8B89D] text-white py-3 rounded-xl font-medium shadow-lg hover:shadow-xl transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? 'Signing in...' : 'Sign In'}
            </motion.button>

            {/* Sign Up Link */}
            <p className="mt-6 text-center text-sm text-[#6B7F5C]">
              Don't have an account?{' '}
              <Link
                href="/signup"
                className="text-[#6B7F5C] font-medium hover:text-[#4A5D3F] transition-colors underline"
              >
                Sign up
              </Link>
            </p>
          </motion.form>
        </motion.div>
      </div>

      {/* Right Side - Image */}
      <div className="hidden lg:block flex-1 relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-[#B8C9A8]/30 to-[#A8B89D]/30 z-10" />
        <img
          src="https://images.unsplash.com/photo-1511497584788-876760111969?w=1200&q=80"
          alt="Nature background"
          className="w-full h-full object-cover"
        />
        <div className="absolute inset-0 flex items-center justify-center z-20">
          <div className="text-center text-white p-8">
            <h2 className="text-4xl font-bold mb-4 drop-shadow-lg">
              Your AI Assistant
            </h2>
            <p className="text-xl drop-shadow-lg">
              Powered by nature-inspired calm
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}