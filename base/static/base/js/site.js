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


var bindPortfolio = function() {
	var i;

	var elements = {
		items: document.querySelectorAll('.section--portolio .portfolio-item'),
		next: document.querySelector('.section--portolio .next'),
		previous: document.querySelector('.section--portolio .previous')
	};

	var count = elements.items.length;
	var activeClassName = 'portfolio-item--show';

	var activeItemIndex = function() {
		for (i = 0; i < count; i++) {
			if (elements.items[i].classList.contains(activeClassName)) {
				return i;
			}
		}

		return -1;
	}

	var showItem = function(index) {
		for (i = 0; i < elements.items.length; i++) {
			const el = elements.items[i];
			el.classList.remove(activeClassName);

			if (i === index) {
				const imgEl = el.querySelector('img');
				if (!imgEl.getAttribute('src'))
					imgEl.setAttribute('src', imgEl.getAttribute('data-src'));
				el.classList.add(activeClassName);
			}
		}
	}

	// navigation
	elements.previous.addEventListener('click', function(e) {
		e.preventDefault();
		var index = activeItemIndex();
		index = index <= 0 ? count - 1 : index - 1;
		showItem(index);
	});

	elements.next.addEventListener('click', function(e) {
		e.preventDefault();
		var index = activeItemIndex();
		index = index >= count - 1 ? 0 : index + 1;
		showItem(index);
	});

	// hide all items but first
	showItem(0);
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
	if (document.querySelector('.section--portolio')) {
		bindPortfolio();
	}
});

// scrollToSlug();
