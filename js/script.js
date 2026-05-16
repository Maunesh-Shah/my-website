document.addEventListener('DOMContentLoaded', function(){
  // Set initial theme from localStorage
  const savedTheme = localStorage.getItem('theme') || 'dark';
  if (savedTheme === 'light') {
    document.body.classList.add('light-theme');
    updateThemeToggle();
  }

  // Year
  document.getElementById('year').textContent = new Date().getFullYear();

  // Theme toggle
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      document.body.classList.toggle('light-theme');
      const isLight = document.body.classList.contains('light-theme');
      localStorage.setItem('theme', isLight ? 'light' : 'dark');
      updateThemeToggle();
    });
  }

  function updateThemeToggle() {
    const isLight = document.body.classList.contains('light-theme');
    themeToggle.textContent = isLight ? '☀️' : '🌙';
  }

  // Nav toggle for small screens
  const nav = document.getElementById('nav');
  const toggle = document.getElementById('nav-toggle');
  toggle.addEventListener('click', ()=> nav.classList.toggle('show'));

  // Modal behavior
  const modal = document.getElementById('modal');
  const modalTitle = document.getElementById('modal-title');
  const modalBody = document.getElementById('modal-body');
  const modalClose = document.getElementById('modal-close');
  modalClose.addEventListener('click', closeModal);
  modal.addEventListener('click', (e)=>{ if(e.target===modal) closeModal() });

  window.openProject = function(e, title){
    e.preventDefault();
    modalTitle.textContent = title;
    modalBody.textContent = title + ' — a short project description and links would go here.';
    modal.setAttribute('aria-hidden','false');
  }

  function closeModal(){ modal.setAttribute('aria-hidden','true'); }

  // Smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener('click', function(e){
      const href = this.getAttribute('href');
      if(href.length>1){
        e.preventDefault();
        document.querySelector(href).scrollIntoView({behavior:'smooth'});
      }
    })
  })
});
