// export default {
//   server: {
//     host: true, // penting untuk akses publik
//     allowedHosts: [
//       'fa427f25-6cd9-460a-9647-20872c509d44-00-2o6866w3e29ay.pike.replit.dev'
//     ]
//   }
// }

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: true,
    allowedHosts: ['.replit.dev'] // agar bisa dibuka dari preview Replit
  }
})
