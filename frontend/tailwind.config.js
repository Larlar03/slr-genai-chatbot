/** @type {import('tailwindcss').Config} */
const plugin = require('tailwindcss/plugin');

export default {
    content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
    theme: {
        extend: {
            height: {
                'chat-height': '400px',
            },
        },
        screens: {
            sm: '320px',
            // => @media (min-width: 320px) { ... }

            md: '640px',
            // => @media (min-width: 640px) { ... }

            lg: '768px',
            // => @media (min-width: 768px) { ... }

            xl: '1024px',
            // => @media (min-width: 1024px) { ... }

            '2xl': '1280px',
            // => @media (min-width: 1280px) { ... }

            '3xl': '1536px',
            // => @media (min-width: 1536px) { ... }
        },
    },
    plugins: [],
};
