/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",  // Asegura que Tailwind escanea estos archivos
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

