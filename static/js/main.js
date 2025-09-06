(function ($) {
  "use strict";

  $(".site-menu-toggle").click(function () {
    var $this = $(this);
    if ($("body").hasClass("menu-open")) {
      $this.removeClass("open");
      $(".js-site-navbar").fadeOut(400);
      $("body").removeClass("menu-open");
    } else {
      $this.addClass("open");
      $(".js-site-navbar").fadeIn(400);
      $("body").addClass("menu-open");
    }
  });

  $("nav .dropdown").hover(
    function () {
      var $this = $(this);
      $this.addClass("show");
      $this.find("> a").attr("aria-expanded", true);
      $this.find(".dropdown-menu").addClass("show");
    },
    function () {
      var $this = $(this);
      $this.removeClass("show");
      $this.find("> a").attr("aria-expanded", false);
      $this.find(".dropdown-menu").removeClass("show");
    }
  );

  $("#dropdown04").on("show.bs.dropdown", function () {
    console.log("show");
  });

  // aos
  AOS.init({
    duration: 1000,
  });

  // home slider
  $(".home-slider").owlCarousel({
    loop: true,
    autoplay: true,
    margin: 10,
    animateOut: "fadeOut",
    animateIn: "fadeIn",
    nav: true,
    autoplayHoverPause: true,
    items: 1,
    autoheight: true,
    navText: [
      "<span class='ion-chevron-left'></span>",
      "<span class='ion-chevron-right'></span>",
    ],
    responsive: {
      0: {
        items: 1,
        nav: false,
      },
      600: {
        items: 1,
        nav: false,
      },
      1000: {
        items: 1,
        nav: true,
      },
    },
  });

  // owl carousel
  var majorCarousel = $(".js-carousel-1");
  majorCarousel.owlCarousel({
    loop: true,
    autoplay: true,
    stagePadding: 7,
    margin: 20,
    animateOut: "fadeOut",
    animateIn: "fadeIn",
    nav: true,
    autoplayHoverPause: true,
    items: 3,
    navText: [
      "<span class='ion-chevron-left'></span>",
      "<span class='ion-chevron-right'></span>",
    ],
    responsive: {
      0: {
        items: 1,
        nav: false,
      },
      600: {
        items: 2,
        nav: false,
      },
      1000: {
        items: 3,
        nav: true,
        loop: false,
      },
    },
  });

  // owl carousel
  var major2Carousel = $(".js-carousel-2");
  major2Carousel.owlCarousel({
    loop: true,
    autoplay: true,
    stagePadding: 7,
    margin: 20,
    // animateOut: 'fadeOut',
    // animateIn: 'fadeIn',
    nav: true,
    autoplayHoverPause: true,
    autoHeight: true,
    items: 3,
    navText: [
      "<span class='ion-chevron-left'></span>",
      "<span class='ion-chevron-right'></span>",
    ],
    responsive: {
      0: {
        items: 1,
        nav: false,
      },
      600: {
        items: 2,
        nav: false,
      },
      1000: {
        items: 3,
        dots: true,
        nav: true,
        loop: false,
      },
    },
  });

  var siteStellar = function () {
    $(window).stellar({
      responsive: false,
      parallaxBackgrounds: true,
      parallaxElements: true,
      horizontalScrolling: false,
      hideDistantElements: false,
      scrollProperty: "scroll",
    });
  };
  siteStellar();

  var smoothScroll = function () {
    var $root = $("html, body");

    $('a.smoothscroll[href^="#"]').click(function () {
      $root.animate(
        {
          scrollTop: $($.attr(this, "href")).offset().top,
        },
        500
      );
      return false;
    });
  };
  smoothScroll();

  var dateAndTime = function () {
    $("#m_date").datepicker({
      format: "m/d/yyyy",
      autoclose: true,
    });
    $("#checkin_date, #checkout_date").datepicker({
      format: "d MM, yyyy",
      autoclose: true,
    });
    $("#m_time").timepicker();
  };
  dateAndTime();

  var windowScroll = function () {
    $(window).scroll(function () {
      var $win = $(window);
      if ($win.scrollTop() > 200) {
        $(".js-site-header").addClass("scrolled");
      } else {
        $(".js-site-header").removeClass("scrolled");
      }
    });
  };
  windowScroll();

  var goToTop = function () {
    $(".js-gotop").on("click", function (event) {
      event.preventDefault();

      $("html, body").animate(
        {
          scrollTop: $("html").offset().top,
        },
        500,
        "easeInOutExpo"
      );

      return false;
    });

    $(window).scroll(function () {
      var $win = $(window);
      if ($win.scrollTop() > 200) {
        $(".js-top").addClass("active");
      } else {
        $(".js-top").removeClass("active");
      }
    });
  };
})(jQuery);

const mobileForm = document.getElementById("mobileForm");
const mobileInput = document.getElementById("mobile");
const errorElement = document.getElementById("error");

mobileForm.addEventListener("submit", function (event) {
  const mobileNumber = mobileInput.value;
  const regex = /^[6-9]\d{9}$/; // Regular expression for validation

  if (!regex.test(mobileNumber)) {
    errorElement.textContent =
      "Please enter a valid 10-digit number starting with 6, 7, 8, or 9.";
    event.preventDefault(); // Prevent form submission
  } else {
    errorElement.textContent = ""; // Clear any previous error message
  }
});

const checkboxes = document.querySelectorAll('input[type="checkbox"]');

// Add event listeners to each checkbox
const checkbox1 = document.getElementById("checkbox1");
const checkbox2 = document.getElementById("checkbox2");

// Add event listeners for checkbox change
checkbox1.addEventListener("change", function () {
  if (checkbox1.checked) {
    checkbox2.checked = false; // Uncheck the other checkbox
  }
});

checkbox2.addEventListener("change", function () {
  if (checkbox2.checked) {
    checkbox1.checked = false; // Uncheck the other checkbox
  }
});

function initAutocomplete() {
  const input = document.getElementById("location");
  const autocomplete = new google.maps.places.Autocomplete(input);

  autocomplete.addListener("place_changed", function () {
    const place = autocomplete.getPlace();
    if (place.geometry) {
      console.log("Selected place:", place);
    } else {
      console.log("No details available for input: '" + input.value + "'");
    }
  });
}

window.onload = initAutocomplete;


