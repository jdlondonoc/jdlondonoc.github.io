const typewriter = document.querySelector('#value-typewriter');

if (typewriter && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
	const phrases = [
		'practical digital solutions.',
		'connected Power Platform solutions.',
		'from process insight to production.'
	];
	let phraseIndex = 0;
	let characterIndex = 0;
	let deleting = false;

	const typeNextCharacter = () => {
		const phrase = phrases[phraseIndex];

		if (!deleting) {
			characterIndex += 1;
			typewriter.textContent = phrase.slice(0, characterIndex);

			if (characterIndex === phrase.length) {
				deleting = true;
				window.setTimeout(typeNextCharacter, 1500);
				return;
			}
		} else {
			characterIndex -= 1;
			typewriter.textContent = phrase.slice(0, characterIndex);

			if (characterIndex === 0) {
				deleting = false;
				phraseIndex = (phraseIndex + 1) % phrases.length;
			}
		}

		window.setTimeout(typeNextCharacter, deleting ? 24 : 47);
	};

	window.setTimeout(typeNextCharacter, 550);
}

const valueInsights = {
	operations: {
		label: 'OPERATIONS & PROCESS IMPROVEMENT',
		copy: 'More than a decade across process engineering, production management, and operations coordination—bringing a practical view of how work happens before deciding what to automate.',
		icon: 'fa-sitemap'
	},
	platform: {
		label: 'POWER PLATFORM DELIVERY',
		copy: 'Four years of Power Platform experience, spanning Canvas and model-driven apps, Cloud and Desktop flows, Power Pages, Copilot Studio, and connected solution architecture.',
		icon: 'fa-cubes'
	},
	projects: {
		label: 'PRODUCTION DELIVERY',
		copy: 'Delivered 15 production projects—from requirements and solution design through deployment and monitoring—including Canvas apps, Cloud and Desktop flows, and SAP GUI automation.',
		icon: 'fa-rocket'
	},
	leadership: {
		label: 'TECHNICAL LEADERSHIP & GOVERNANCE',
		copy: 'Led and mentored a team of three Power Platform developers, establishing development standards, governance frameworks, and practices for consistent solution delivery.',
		icon: 'fa-users'
	}
};

const insightPanel = document.querySelector('#value-insight');
const insightButtons = document.querySelectorAll('.value-metric[data-insight]');

if (insightPanel && insightButtons.length) {
	insightButtons.forEach((button, index) => {
		button.addEventListener('click', () => {
			const insight = valueInsights[button.dataset.insight];

			if (!insight) {
				return;
			}

			insightButtons.forEach((item) => {
				const selected = item === button;
				item.classList.toggle('is-selected', selected);
				item.setAttribute('aria-pressed', String(selected));
			});

			insightPanel.querySelector('.value-insight-icon i').className = `fa ${insight.icon}`;
			insightPanel.querySelector('.value-insight-label').textContent = insight.label;
			insightPanel.querySelector('.value-insight-copy').textContent = insight.copy;
			insightPanel.querySelector('.value-insight-index').textContent =
				`${String(index + 1).padStart(2, '0')} / ${String(insightButtons.length).padStart(2, '0')}`;
		});
	});
}
