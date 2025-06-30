<template>
  <section id="about" class="about">
    <div class="container">
      <h2>About Me</h2>
      <p>I am a passionate web developer and aspiring DevOps engineer currently pursuing my degree, with hands-on experience in creating web and mobile solutions through academic and personal projects.</p>
      <div class="stats">
        <div class="stat"><strong>20+</strong><br />Projects</div>
        <div class="stat"><strong>95%</strong><br />Client Satisfaction</div>
        <div class="stat"><strong>2+</strong><br />Years Experience</div>
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
