var bindEvents = function() {
	var i;

	var elements = {
		mobileMenuButton: document.querySelector('.navigation__navicon'),
		mobileMenu: document.querySelector('.navigation'),
		mobileShowButtons: document.querySelectorAll('.item__toggle'),
		scrollToAnchors: document.querySelectorAll('.menu__item a'),
	};

	// mobile menu toggle
	elements.mobileMenuButton.addEventListener('click', function(e) {
		e.preventDefault();

		if (elements.mobileMenu.classList.contains('show')) {
			elements.mobileMenu.classList.remove('show');
		} else {
			elements.mobileMenu.classList.add('show');
		}
	});

	// scrolls
	// for (i = 0; i < elements.scrollToAnchors.length; i++) {
	// 	elements.scrollToAnchors[i].addEventListener('click', function(e) {
	// 		e.preventDefault();
	// 		elements.mobileMenu.classList.remove('show');

	// 		Velocity(
	// 			document.querySelector(this.getAttribute('href')),
	// 			'scroll',
	// 			{ duration: 300, offset: -40 }
	// 		);
	// 	});
	// }

	// mobile facilitator show more
	for (i = 0; i < elements.mobileShowButtons.length; i++) {
		elements.mobileShowButtons[i].addEventListener('click', function(e) {
			e.preventDefault();
			this.parentElement.classList.add('show');
		});
	}
};

var scrollToSlug = function() {
	var urlParts = window.location.href.split('/').filter(Boolean);

	if (urlParts.length > 2) {
		var slug = urlParts.pop();
		var offset = document.querySelector('#' + slug).getBoundingClientRect().top;
		setTimeout(function() {
			document.body.scrollTop = offset;
		}, 10);
	}
};

document.addEventListener('DOMContentLoaded', function() {
	bindEvents();
});

// scrollToSlug();
