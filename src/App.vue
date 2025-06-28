<script setup>
import Hero from './components/Hero.vue'
import About from './components/About.vue'
import Projects from './components/Projects.vue'
import Services from './components/Services.vue'
import Skills from './components/Skills.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <main>
    <Hero />
    <Skills />
    <Services />
    <About />
    <Projects />
    <Footer />
  </main>
</template>

<style scoped>
main {
  font-family: 'Segoe UI', sans-serif;
  background: #0e0e0e;
  color: #f0f0f0;
}
</style>
