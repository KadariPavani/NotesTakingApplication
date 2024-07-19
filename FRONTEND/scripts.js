document.getElementById('login-form-element').addEventListener('submit', async (event) => {
  event.preventDefault();
  const username = document.getElementById('login-username').value;
  const password = document.getElementById('login-password').value;
  const response = await fetch('/token', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: new URLSearchParams({
          username: username,
          password: password
      })
  });
  const data = await response.json();
  if (response.ok) {
      localStorage.setItem('access_token', data.access_token);
      document.getElementById('notes').style.display = 'block';
  } else {
      alert('Login failed');
  }
});
