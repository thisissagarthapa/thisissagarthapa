<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sagar Thapa's GitHub Profile</title>
</head>
<body>
  <h1 align="center">Hi 👋, I'm Sagar Thapa</h1>
  <h3 align="center">A passionate Python developer from Nepal</h3>
  <img align='right' width='400' height='400' src='https://i.pinimg.com/564x/a2/e8/b6/a2e8b6f4092ba024fb41cdd9734e01e6.jpg' alt='Sagar Thapa'>

  <ul>
    <li>🌱 I’m currently learning Django Rest Framework</li>
    <li>📫 How to reach me: <a href="mailto:kingstonboysagar@gmail.com">kingstonboysagar@gmail.com</a></li>
    <li>🌐 My portfolio: <a href="http://jaimethegoat.pythonanywhere.com">jaimethegoat.pythonanywhere.com</a></li>
  </ul>

  <h3 align="left">Connect with me:</h3>
  <p align="left">
    <a href="https://www.facebook.com/profile.php?id=100078644620461" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/facebook/facebook-original.svg" alt="Facebook" width="40" height="40"/>
    </a>
    <a href="https://www.linkedin.com/in/sagar-thapa-a25657305" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linkedin/linkedin-original.svg" alt="LinkedIn" width="40" height="40"/>
    </a>
  </p>

  <h3 align="left">Languages and Tools:</h3>
  <p align="left">
    <a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="HTML5" width="40" height="40"/>
    </a>
    <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="CSS3" width="40" height="40"/>
    </a>
    <a href="https://getbootstrap.com" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="Bootstrap" width="40" height="40"/>
    </a>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="JavaScript" width="40" height="40"/>
    </a>
    <a href="https://www.python.org" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/>
    </a>
    <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer">
      <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="Django" width="40" height="40"/>
    </a>
    <a href="https://www.django-rest-framework.org/" target="_blank" rel="noreferrer">
      <img src="https://www.django-rest-framework.org/img/logo.png" alt="Django Rest Framework" width="40" height="40"/>
    </a>
    <a href="https://www.mysql.com/" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="MySQL" width="40" height="40"/>
    </a>
  </p>

  <h3 align="left">Most Used Languages (GitHub):</h3>
  <div id="languages"></div>

  <script>
    const username = 'thisissagarthapa';
    const apiUrl = `https://api.github.com/users/${username}/repos`;

    fetch(apiUrl)
      .then(response => response.json())
      .then(repos => {
        // Fetch languages used in each repository
        const languages = {};
        repos.forEach(repo => {
          fetch(repo.languages_url)
            .then(response => response.json())
            .then(data => {
              // Accumulate bytes of each language across all repositories
              Object.entries(data).forEach(([language, bytes]) => {
                if (languages[language]) {
                  languages[language] += bytes;
                } else {
                  languages[language] = bytes;
                }
              });

              // After accumulating all languages, calculate percentages
              const totalBytes = Object.values(languages).reduce((acc, val) => acc + val, 0);
              const languagePercentages = Object.entries(languages)
                .map(([language, bytes]) => ({
                  language,
                  percentage: ((bytes / totalBytes) * 100).toFixed(2)
                }))
                .sort((a, b) => b.percentage - a.percentage); // Sort by percentage descending

              // Display the top languages
              const languagesElement = document.getElementById('languages');
              languagePercentages.slice(0, 5).forEach(({ language, percentage }) => {
                const languageElement = document.createElement('p');
                languageElement.textContent = `${language}: ${percentage}%`;
                languagesElement.appendChild(languageElement);
              });
            })
            .catch(error => console.error('Error fetching languages:', error));
        });
      })
      .catch(error => console.error('Error fetching repositories:', error));
  </script>
</body>
</html>
