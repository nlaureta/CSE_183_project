// This will be the object that will contain the Vue attributes
// and be used to initialize it.
let app = {};

// Given an empty app object, initializes it filling its attributes,
// creates a Vue instance, and then initializes the Vue instance.

let init = (app) => {

    // This is the Vue data.
    app.data = {
        // Complete as you see fit.
        showWinnerScreen: false,
        showLoserScreen: false,
        guesses: 5,
        guessedWord: "",
        correctWord: "",
        urls: '',
        hasDrawing: false,
        audioElement: null,
        win: '',
        draw_id: '',
    };

    app.enumerate = (a) => {
        // This adds an _idx field to each element of the array.
        let k = 0;
        a.map((e) => { e._idx = k++; });
        return a;
    };

    // This contains all the methods.
    app.methods = {
        // Complete as you see fit.
        checkGuess() {
            console.log(this.correctWord);
            if (this.guessedWord.toLowerCase() === this.correctWord.toLowerCase()) {
                // logic when the guess is correct
                this.showWinnerScreen = true;
                this.playAudio('http://127.0.0.1:8000/QuickDraw/static/sounds/ApplauseSound.mp3');
            } 
            else if (this.guessedWord.toLowerCase() !== this.correctWord.toLowerCase() && this.guesses !== 0) {
                // logic when the guess is wrong but still have guesses
                this.guesses--;
            } 
            else {
                // logic when guess is wrong and no guesses left
                this.showLoserScreen = true;
                this.playAudio('http://127.0.0.1:8000/QuickDraw/static/sounds/SadTrumpet.mp3');
            }
        },
        
        playAudio(src) {
            if (!this.audioElement) {
                this.audioElement = new Audio(src);
            }
            this.audioElement.play();
        },

        handleGuessTheDrawing(event) {
            if (!this.hasDrawing) {
                event.preventDefault(); // prevent page from going to guess page
                alert("No drawings in the database to guess. Please proceed to draw first.");
            }
        },

        setWord(correctWord){ //set the correct word
            app.vue.correctWord = correctWord;
        },

        setResult(draw_id, win){
            app.vue.draw_id = draw_id;
            app.vue.win = win;
            this.saveResult();
        },

        saveResult(){
            axios.post('/saveResult', {
                draw_id: app.vue.draw_id,
                win: app.vue.win
            })
            .then(function(r) {
                console.log('Result saved with ID:', r.data.id);
            })
            .catch(error => {
                console.error(error);
            });
        }

    };

    // This creates the Vue instance.
    app.vue = new Vue({
        el: "#vue-target",
        data: app.data,
        methods: app.methods
    });

    app.init = () => {
        axios.get('/getImages')
        .then(function(r) {
            app.vue.urls = r.data.urls;
            app.vue.hasDrawing = r.data.urls.length > 0; //check if there is drawings in the database
            console.log(app.vue.urls)
        })
        .catch(error => {
            console.error(error);
        });
    };

    // Call to the initializer.
    app.init();
};

// This takes the (empty) app object, and initializes it,
// putting all the code in it. 
init(app);
