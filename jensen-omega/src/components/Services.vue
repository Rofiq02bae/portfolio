<template>
  <section class="services">
    <div class="container">
      <h2>Services</h2>
      <div class="cards">
        <div class="card" v-for="service in services" :key="service.title">
          <h3>{{ service.title }}</h3>
          <p>{{ service.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const services = [
  { title: 'Website Development', description: 'Custom and responsive websites.' },
  { title: 'App Development', description: 'Cross-platform and modern apps.' },
  { title: 'Website Hosting', description: 'Secure and fast hosting solutions.' }
]
</script>

<style scoped>
.services {
  padding: 4rem 2rem;
}

h2 {
  text-align: center;
  margin-bottom: 2rem;
  color: #00ffd5;
}

.cards {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  justify-content: center;
}

.card {
  background: #1f1f1f;
  padding: 2rem;
  border-radius: 10px;
  width: 280px;
  border: 1px solid #00ffd5;
  transition: 0.3s;
}

.card:hover {
  transform: translateY(-5px);
  background: #00ffd5;
  color: #000;
}
</style>
