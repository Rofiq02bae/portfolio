<template>
  <section class="skills">
    <div class="container">
      <h2>My Skills</h2>
      <ul class="skill-list">
        <li v-for="skill in skills" :key="skill">{{ skill }}</li>
      </ul>
    </div>
  </section>
</template>

<script setup>
const skills = [
  'HTML5', 'CSS', 'JavaScript', 'Node.js', 'Vue', 'GitHub', 'Docker', 'PHP'
]
</script>

<style scoped>
.skills {
  background: #181818;
  padding: 4rem 2rem;
  text-align: center;
}

h2 {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: #00ffd5;
}

.skill-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
  list-style: none;
  padding: 0;
}

.skill-list li {
  border: 1px solid #00ffd5;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: bold;
  color: #00ffd5;
  transition: 0.3s;
}

.skill-list li:hover {
  background: #00ffd5;
  color: #000;
}
</style>
