AOS.init();
var owl = $('.my-carousel');

owl.owlCarousel({
    items: 4,
    loop: true,
    margin: 40,
    autoplay: true,
    autoplayTimeout: 4000,
    autoplayHoverPause: true,
    nav: false,
    responsive: {
        0: {
            items: 1,
        },
        600: {
            items: 2,
        },
        1000: {
            items:3,
        }
    }
});

// setTimeout(() => {
//     // Code to be executed after the timeout
//     // For example, you can hide the technology section
//     const technologySection = document.getElementById("technology");
//     technologySection.style.display = "non";
//   }, 1000); // 5000 milliseconds = 5 seconds


// setInterval(() => {
//     $('.nav-pills button.active').parents('li').next('li').children().addClass('active');
//     $('.nav-pills button.active').parents('li').prev('li').children().removeClass('active');
// }, 2000);

var currentIndex = 0;
var totalElements1 = $('.nav-pills li').length;
var totalElements2 = $('.tab-content>.tab-pane').length;
var sliderelement1 = $('.nav-pills li')
var sliderelement2 = $('.tab-content>.tab-pane')

$(sliderelement1).eq(currentIndex).addClass('active');
$(sliderelement2).eq(currentIndex).addClass('active show');

// auto sliding function



var intervalId;

function myFunction() {
    currentIndex++;
    $(sliderelement1).children().removeClass('active');
    $(sliderelement2).removeClass('active show');

    if (currentIndex >= totalElements1 && totalElements2) {
        currentIndex = 0;
    }

    $(sliderelement1).eq(currentIndex).children().addClass('active');
    $(sliderelement2).eq(currentIndex).addClass('active');
    if ($(sliderelement2).eq(currentIndex).hasClass('active')) {
        setTimeout(() => {
            $(sliderelement2).eq(currentIndex).addClass('show');
        }, 300);
    }
}

function startFunction() {
    intervalId = setInterval(myFunction, 2000);
}

function stopFunction() {
    clearInterval(intervalId);
}

$('#pills-tabContent').mouseenter(function () {
    stopFunction();
});

$('#pills-tabContent').mouseleave(function () {
    startFunction();
});

// Start the function initially
startFunction();


// second-carasol
$('.backer-carousel-1').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    autoplay:true,
    autoplayTimeout: 3000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 4
        }
    }
});

// blog-carousel
$('.blog-carousel').owlCarousel({
    loop: true,
    margin: 30,
    nav: false,
    autoplay:true,
    autoplayTimeout: 3000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 3
        }
    }
});