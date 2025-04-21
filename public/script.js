const form = document.getElementById('loginForm');
const msg = document.getElementById('message');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const username = document.getElementById('loginUser').value;
  const password = document.getElementById('loginPass').value;

  const response = await fetch('/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });

  const result = await response.json();

  if (response.status === 200) {
    msg.style.color = 'green';
  } else {
    msg.style.color = 'red';
  }

  msg.textContent = result.message;
});
