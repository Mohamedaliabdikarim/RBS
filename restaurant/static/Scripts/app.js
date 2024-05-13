document.addEventListener('DOMContentLoaded', function() {
    var nextBtn = document.getElementById('next-btn');
    var prevBtn = document.getElementById('prev-btn'); 
    var reviewCards = document.querySelectorAll('.review-card');
    var nextIndex = 3;

   
    for (var i = 3; i < reviewCards.length; i++) {
        reviewCards[i].classList.add('d-none');
    }

    nextBtn.addEventListener('click', function() {
        showNextReviews();
    });

    prevBtn.addEventListener('click', function() { 
        if (nextIndex > 3) {
            showPreviousReviews();
        }
    });

    function showNextReviews() {
       
        for (var i = nextIndex - 3; i < nextIndex; i++) {
            reviewCards[i].classList.add('d-none');
        }
        
        for (var i = nextIndex; i < nextIndex + 3; i++) {
            if (reviewCards[i]) {
                reviewCards[i].classList.remove('d-none');
            }
        }
        
        nextIndex += 3;
        
        if (nextIndex >= reviewCards.length) {
            nextBtn.classList.add('d-none');
        } else {
            nextBtn.classList.remove('d-none');
        }
        prevBtn.classList.remove('d-none'); 
    }

    function showPreviousReviews() { /
        for (var i = nextIndex - 1; i >= nextIndex - 3; i--) {
            if (reviewCards[i]) {
                reviewCards[i].classList.add('d-none');
            }
        }
        
        for (var i = nextIndex - 4; i >= nextIndex - 6; i--) {
            if (reviewCards[i]) {
                reviewCards[i].classList.remove('d-none');
            }
        }
      
        nextIndex -= 3;
      
        if (nextIndex <= 3) {
            prevBtn.classList.add('d-none');
        } else {
            prevBtn.classList.remove('d-none');
        }
        nextBtn.classList.remove('d-none');
    }
});
