import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: true,
    allowedHosts: ['.replit.dev'], // agar bisa dibuka dari preview Replit
    port: 5173,
  },
})

