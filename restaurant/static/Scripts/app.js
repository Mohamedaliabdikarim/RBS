document.addEventListener('DOMContentLoaded', function() {
    var nextBtn = document.getElementById('next-btn');
    var prevBtn = document.getElementById('prev-btn'); 
    var reviewCards = document.querySelectorAll('.review-card');
    var nextIndex = 3;

    // Initialt skjul alle anmeldelser unntatt de første tre
    for (var i = 3; i < reviewCards.length; i++) {
        reviewCards[i].classList.add('d-none');
    }

    nextBtn.addEventListener('click', function() {
        showNextReviews();
    });

    prevBtn.addEventListener('click', function() { // Nytt: Lytter etter klikk på "previous" knappen
        if (nextIndex > 3) { // Sjekker om det er noe å gå tilbake til
            showPreviousReviews();
        }
    });

    function showNextReviews() {
        // Skjul de gjeldende synlige anmeldelsene
        for (var i = nextIndex - 3; i < nextIndex; i++) {
            reviewCards[i].classList.add('d-none');
        }
        // Vis de neste tre anmeldelsene
        for (var i = nextIndex; i < nextIndex + 3; i++) {
            if (reviewCards[i]) {
                reviewCards[i].classList.remove('d-none');
            }
        }
        // Oppdater nextIndex for neste gruppe anmeldelser
        nextIndex += 3;
        // Sjekk om det er flere anmeldelser å vise
        if (nextIndex >= reviewCards.length) {
            nextBtn.classList.add('d-none');
        } else {
            nextBtn.classList.remove('d-none'); // Sørg for at "next" knappen er synlig hvis det er flere anmeldelser
        }
        prevBtn.classList.remove('d-none'); // Sørg for at "previous" knappen alltid er synlig når man klikker på "next"
    }

    function showPreviousReviews() { // Nytt: Funksjon for å vise forrige gruppe anmeldelser
        // Skjul de gjeldende synlige anmeldelsene
        for (var i = nextIndex - 1; i >= nextIndex - 3; i--) {
            if (reviewCards[i]) {
                reviewCards[i].classList.add('d-none');
            }
        }
        // Vis de forrige tre anmeldelsene
        for (var i = nextIndex - 4; i >= nextIndex - 6; i--) {
            if (reviewCards[i]) {
                reviewCards[i].classList.remove('d-none');
            }
        }
        // Oppdater nextIndex for forrige gruppe anmeldelser
        nextIndex -= 3;
        // Sjekk om det er flere anmeldelser å vise
        if (nextIndex <= 3) {
            prevBtn.classList.add('d-none'); // Skjul "previous" knappen hvis vi er tilbake til de første anmeldelsene
        } else {
            prevBtn.classList.remove('d-none'); // Sørg for at "previous" knappen er synlig hvis det er flere anmeldelser å gå tilbake til
        }
        nextBtn.classList.remove('d-none'); // Sørg for at "next" knappen alltid er synlig når man klikker på "previous"
    }
});
