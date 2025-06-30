<template>
  <section id="projects" class="projects">
    <div class="container">
      <h2>Projects</h2>
      <p>Here are some of the things I've worked on recently:</p>
      <div class="grid">
        <div v-for="n in 3" :key="n" class="project-card">
          <h3>Project {{ n }}</h3>
          <p>Rentaride
              a laravel based car rental application platform used by Jogja Volkswagen Tour
            link to demo : https://frontend-rental.netlify.app/
          </p>
          <p>LiteFit
              ui/ux for sports progress tracker app 
            link to demo : https://www.figma.com/design/la9o8bP8LaR8ehpAjnyNdN/design-HCI?node-id=0-1&t=F6hFxaBFAB0pBNn7-1
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

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
