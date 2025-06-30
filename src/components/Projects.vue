<template>
  <section id="projects" class="projects">
    <div class="container">
      <h2>Projects</h2>
      <p>Here are some of the things I've worked on recently:</p>
      <div class="grid">
        <div v-for="(project, index) in projects" :key="index" class="project-card">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
          <a :href="project.link" target="_blank" rel="noopener">View Demo</a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const projects = [
  {
    title: 'Rentaride',
    description: 'A Laravel-based car rental platform used by Jogja Volkswagen Tour.',
    link: 'https://frontend-rental.netlify.app/'
  },
  {
    title: 'LiteFit',
    description: 'UI/UX design for a sports progress tracker app.',
    link: 'https://www.figma.com/design/la9o8bP8LaR8ehpAjnyNdN/design-HCI?node-id=0-1&t=F6hFxaBFAB0pBNn7-1'
  }
]
</script>


<style scoped>
.projects {
  padding: 4rem 2rem;
}

h2 {
  text-align: center;
  color: #00ffd5;
  margin-bottom: 1rem;
}

.grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
}

.project-card {
  background: #1a1a1a;
  border: 1px solid #00ffd5;
  border-radius: 8px;
  padding: 1.5rem;
  width: 280px;
  transition: 0.3s;
}

.project-card:hover {
  background: #00ffd5;
  color: #000;
}
</style>
