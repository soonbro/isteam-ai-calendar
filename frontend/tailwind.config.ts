import type { Config } from "tailwindcss"
import { fontFamily } from "tailwindcss/defaultTheme"

const config = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
	],
  prefix: "",
  theme: {
    extend: {
      colors: {
        main: 'var(--main)',
        mainAccent: 'var(--main-accent)',
        overlay: 'rgba(0,0,0,0.8)',

        // light mode
        bg: 'var(--bg)',
        text: 'black',
        border: 'var(--border)',

        // dark mode
        darkBg: 'var(--dark-bg)',
        darkText: '#eeefe9',
        darkBorder: 'var(--dark-border)',
      },
      translate: {
        boxShadowX: 'var(--horizontal-box-shadow)',
        boxShadowY: 'var(--vertical-box-shadow)',
        reverseBoxShadowX: 'calc(var(--horizontal-box-shadow) * -1)',
        reverseBoxShadowY: 'calc(var(--vertical-box-shadow) * -1)',
      },
      boxShadow: {
        light:
          'var(--horizontal-box-shadow) var(--vertical-box-shadow) 0px 0px var(--border)',
        dark: 'var(--horizontal-box-shadow) var(--vertical-box-shadow) 0px 0px var(--dark-border)',
        nav: '4px 4px 0px 0px var(--border)',
        navDark: '4px 4px 0px 0px var(--dark-border)',
      },
      fontFamily: {
        sans: ["var(--font-sans)", ...fontFamily.sans],
      },
      fontWeight: {
        base: 'var(--base-font-weight)',
        heading: 'var(--heading-font-weight)',
      },
      borderRadius: {
        base: 'var(--border-radius)',
      },
      keyframes: {
        marquee: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-100%)' },
        },
        marquee2: {
          '0%': { transform: 'translateX(100%)' },
          '100%': { transform: 'translateX(0%)' },
        },
        'accordion-down': {
          from: { height: '0' },
          to: { height: 'var(--radix-accordion-content-height)' },
        },
        'accordion-up': {
          from: { height: 'var(--radix-accordion-content-height)' },
          to: { height: '0' },
        },
        'caret-blink': {
          '0%,70%,100%': { opacity: '1' },
          '20%,50%': { opacity: '0' },
        },
      },
      animation: {
        marquee: 'marquee 5s linear infinite',
        marquee2: 'marquee2 5s linear infinite',
        'accordion-down': 'accordion-down 0.2s ease-out',
        'accordion-up': 'accordion-up 0.2s ease-out',
        'caret-blink': 'caret-blink 1.25s ease-out infinite',
      },
      screens: {
        m1500: { raw: '(max-width: 1500px)' },
        m1300: { raw: '(max-width: 1300px)' },
        m1100: { raw: '(max-width: 1100px)' },
        m1000: { raw: '(max-width: 1000px)' },
        m900: { raw: '(max-width: 900px)' },
        m850: { raw: '(max-width: 850px)' },
        m800: { raw: '(max-width: 800px)' },
        m750: { raw: '(max-width: 750px)' },
        m700: { raw: '(max-width: 700px)' },
        m650: { raw: '(max-width: 650px)' },
        m600: { raw: '(max-width: 600px)' },
        m550: { raw: '(max-width: 550px)' },
        m500: { raw: '(max-width: 500px)' },
        m450: { raw: '(max-width: 450px)' },
        m400: { raw: '(max-width: 400px)' },
        m350: { raw: '(max-width: 350px)' },
      },
      width: {
        container: '1300px',
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
} satisfies Config

export default config