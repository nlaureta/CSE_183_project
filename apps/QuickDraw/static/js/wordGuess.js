
let app = {};


let init = (app) => {

    app.data = {
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
        let k = 0;
        a.map((e) => { e._idx = k++; });
        return a;
    };

    app.methods = {
        checkGuess() {
            console.log(this.correctWord);
            if (this.guessedWord.toLowerCase() === this.correctWord.toLowerCase()) {
                // logic when the guess is correct
                this.showWinnerScreen = true;
                this.playAudio('http://127.0.0.1:8000/QuickDraw/static/sounds/sweetvictory.mp3');
            }
            else if (this.guessedWord.toLowerCase() !== this.correctWord.toLowerCase() && this.guesses !== 1) {
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
                alert("No drawings are currently available in the database for guessing. Please wait for others to draw first");
            }
        },

        setWord(correctWord) { //set the correct word
            app.vue.correctWord = correctWord;
        },

        setResult(draw_id, win) {
            app.vue.draw_id = draw_id;
            app.vue.win = win;
            this.saveResult();
        },

        saveResult() {
            axios.post('/saveResult', {
                draw_id: app.vue.draw_id,
                win: app.vue.win
            })
                .then(function (r) {
                    console.log('Result saved with ID:', r.data.id);
                })
                .catch(error => {
                    console.error(error);
                });
        }

    };

    app.vue = new Vue({
        el: "#vue-target",
        data: app.data,
        methods: app.methods
    });

    app.init = () => {
        axios.get('/getImages')
            .then(function (r) {
                app.vue.urls = r.data.urls;
                app.vue.hasDrawing = r.data.urls.length > 0; //check if there is drawings in the database
                console.log(app.vue.urls)
            })
            .catch(error => {
                console.error(error);
            });
    };

    app.init();
};

init(app);
