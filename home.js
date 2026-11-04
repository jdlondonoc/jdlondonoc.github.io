const navigationToggle = document.querySelector('.navbar-toggler');
const navigation = document.querySelector('#Navbar');

if (navigationToggle && navigation) {
	navigationToggle.addEventListener('click', () => {
		const isExpanded = navigationToggle.getAttribute('aria-expanded') === 'true';
		navigationToggle.setAttribute('aria-expanded', String(!isExpanded));
		navigation.classList.toggle('show', !isExpanded);
	});

	navigation.querySelectorAll('a').forEach((link) => {
		link.addEventListener('click', () => {
			navigationToggle.setAttribute('aria-expanded', 'false');
			navigation.classList.remove('show');
		});
	});
}
