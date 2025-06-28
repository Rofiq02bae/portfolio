<template>
  <section id="about" class="about">
    <div class="container">
      <h2>About Me</h2>
      <p>I am a passionate developer with years of experience in creating web and mobile solutions.</p>
      <div class="stats">
        <div class="stat"><strong>120+</strong><br />Projects</div>
        <div class="stat"><strong>95%</strong><br />Client Satisfaction</div>
        <div class="stat"><strong>10+</strong><br />Years Experience</div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.about {
  padding: 4rem 2rem;
  background: #111;
  text-align: center;
}

h2 {
  color: #00ffd5;
  margin-bottom: 1rem;
}

.stats {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
  flex-wrap: wrap;
}

.stat {
  font-size: 1.2rem;
  border: 1px solid #00ffd5;
  padding: 1rem 2rem;
  border-radius: 10px;
}
</style>
