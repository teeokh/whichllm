/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme');
const plugin = require('tailwindcss/plugin');

module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    screens: {
      'sm': '480px',
      // => @media (min-width: 640px) { ... }
  
      'md': '547px',
      // => @media (min-width: 768px) { ... }
  
      'lg': '768px',
      // => @media (min-width: 1024px) { ... }
  
      'xl': '1024px',
      // => @media (min-width: 1280px) { ... }
  
      '2xl': '1680px',
      // => @media (min-width: 1536px) { ... }
    }, 
    extend: {
      
    }
  },
  plugins: [],
}