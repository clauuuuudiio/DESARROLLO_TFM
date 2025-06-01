import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'https://chatbot-langchain.azurewebsites.net', // La URL de la API
        changeOrigin: true,  // Cambiar el origen de la solicitud
        secure: false,  // Si el servidor de la API no tiene HTTPS válido, se puede poner en false
      },
    },
  },
})
