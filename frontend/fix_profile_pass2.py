import re

with open('src/pages/Profile.tsx', 'r', encoding='utf-8') as f:
    c = f.read()

# I already added states and imports in previous run. Just replace inputs.

c = re.sub(
    r'<input\s+type="password"\s+value=\{currentPassword\}.*?/>',
    r'''<div className="relative">
                  <input 
                    type={showCurrentPassword ? "text" : "password"}
                    value={currentPassword}
                    onChange={e => setCurrentPassword(e.target.value)}
                    className="w-full bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl px-4 py-2.5 pr-10 text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition" 
                    placeholder="••••••••"
                  />
                  <button 
                    type="button"
                    onClick={() => setShowCurrentPassword(!showCurrentPassword)}
                    className="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition"
                  >
                    {showCurrentPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                  </button>
                </div>''',
    c, flags=re.DOTALL
)

c = re.sub(
    r'<input\s+type="password"\s+value=\{newPassword\}.*?/>',
    r'''<div className="relative">
                  <input 
                    type={showNewPassword ? "text" : "password"}
                    value={newPassword}
                    onChange={e => setNewPassword(e.target.value)}
                    className="w-full bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl px-4 py-2.5 pr-10 text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition" 
                    placeholder="••••••••"
                  />
                  <button 
                    type="button"
                    onClick={() => setShowNewPassword(!showNewPassword)}
                    className="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition"
                  >
                    {showNewPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                  </button>
                </div>''',
    c, flags=re.DOTALL
)

with open('src/pages/Profile.tsx', 'w', encoding='utf-8') as f:
    f.write(c)

print('Profile updated via regex')
