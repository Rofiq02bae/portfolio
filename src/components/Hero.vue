<template>
  <section id="hero" class="hero">
    <div class="container">
      <div class="hero-content">
        <div class="text">
          <h2>Hello, I'm <span class="highlight">As'adurrofiq</span></h2>
          <h3>Software Developer</h3>
          <div class="buttons">
            <a href="https://wa.me/+6287863535272" target=blank class="btn primary">Got a project?</a>
            <a href="https://drive.google.com/file/d/1BF5Bx6_xi2wHDjgYtoyvRRXLiQSSdXiz/view?usp=drivesdk" target="_blank" class="btn">My Resume</a>
          </div>
        </div>
        <div class="profile-wrapper">
          <img src="/profile.jpg" alt="Profile" class="profile-img" />
          <div class="glow"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  padding: 4rem 2rem;
  background: #111;
}

.container {
  max-width: 1200px;
  margin: auto;
}

.hero-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 2rem;
}

.text h2 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.text h3 {
  font-size: 1.5rem;
  color: #aaa;
}

.highlight {
  color: #00ffd5;
}

.buttons {
  margin-top: 1.5rem;
  display: flex;
  gap: 1rem;
}

.btn {
  padding: 0.75rem 1.5rem;
  border: 1px solid #00ffd5;
  color: #00ffd5;
  background: transparent;
  border-radius: 5px;
  text-decoration: none;
  transition: 0.3s;
}

.btn:hover {
  background: #00ffd5;
  color: #000;
}

.btn.primary {
  background: #00ffd5;
  color: #000;
}

.btn.primary:hover {
  opacity: 0.85;
}

.profile-wrapper {
  position: relative;
  width: 220px;
  height: 220px;
}

.profile-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  border: 4px solid #00ffd5;
  z-index: 2;
  position: relative;
}

.glow {
  position: absolute;
  top: 0;
  left: 0;
  width: 220px;
  height: 220px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0,255,213,0.2), transparent);
  animation: pulse 2s infinite ease-in-out;
  z-index: 1;
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
    opacity: 0.5;
  }
  50% {
    transform: scale(1.1);
    opacity: 1;
  }
}
</style>
